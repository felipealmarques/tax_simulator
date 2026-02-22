from tax_simulator.data_ingestion.repositories import ICMSRepository
from tax_simulator.domain.models import Operation, ICMSBreakdown, ScenarioComparation

class ICMSPolicyEngine:
    def __init__(self, repository: ICMSRepository):
        self.repository = repository

    def aliquot_calculate(self, operation: Operation):
        if operation.uf_origin == operation.uf_destiny:
            return self.repository.get_aliquota_interna(operation.uf_origin)
        
        if operation.merchandise_origin.value == "imported":
            return self.repository.get_aliquota_importada()
        
        return self.repository.get_aliquota_interestadual(
            origin=operation.uf_origin,
            destiny=operation.uf_destiny
        )
    
    def operation_calculate(
            self, 
            operation: Operation, 
            monthly_amount: float, 
            months: int, 
            tts_flag: bool = False
    ) -> ICMSBreakdown:
        
        if operation.uf_origin == operation.uf_destiny:
            raise ValueError("DIFAL não se aplica a operação interna")
        
        # Alíquota base
        interstate_normal = self.repository.get_aliquota_interestadual(
            operation.uf_origin,
            operation.uf_destiny
        )

        intenal_destiny = self.repository.get_aliquota_interna(
            operation.uf_destiny
        )

        # Regra TTS
        if tts_flag:
            interstate_applied = 1.3
        else:
            interstate_applied = interstate_normal

        # DIFAL sempre calculado com interestadual NORMAL
        difal = max(intenal_destiny - interstate_normal, 0)

        total_aliquot = interstate_applied + difal

        # Valores monetários
        total_sales = monthly_amount * months

        icms_value = total_sales * (interstate_applied / 100)
        difal_value = total_sales * (difal / 100)
        total_value = icms_value + difal_value

        return ICMSBreakdown(
            interstate=interstate_applied,
            difal=difal,
            total_aliquot=total_aliquot,
            icms_value=icms_value,
            difal_value=difal_value,
            total_value=total_value
        )
    
    def scenario_comparation(
            self,
            origin_operation: Operation,
            extrema_operation: Operation,
            monthly_amount: float,
            months: int
    ) -> ScenarioComparation:
        
        normal = self.operation_calculate(
            operation=origin_operation,
            monthly_amount=monthly_amount,
            months=months,
            tts_flag=False
        )

        tts = self.operation_calculate(
            operation=extrema_operation,
            monthly_amount=monthly_amount,
            months=months,
            tts_flag=True
        )

        savings = normal.total_value - tts.total_value

        return ScenarioComparation(
            normal_scenario=normal,
            tts_scenario=tts,
            total_savings=savings
        )