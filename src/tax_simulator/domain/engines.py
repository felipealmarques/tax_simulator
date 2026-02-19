from tax_simulator.data_ingestion.repositories import ICMSRepository
from tax_simulator.domain.models import Operation

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