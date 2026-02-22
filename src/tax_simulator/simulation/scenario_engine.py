from typing import Dict, Any
from omegaconf import DictConfig
from datetime import date

from tax_simulator.data_ingestion.repositories import ICMSRepository
from tax_simulator.domain.models import Operation, OriginMerchandise
from tax_simulator.domain.engines import ICMSPolicyEngine
from tax_simulator.simulation.models import SimulationSettings

def run_simulation(
    cfg: DictConfig,
    settings: SimulationSettings
) -> Dict[str, Any]:
    
    # Configurações Iniciais
    uf_origin = settings.uf_origin
    uf_destiny = settings.uf_destiny
    monthly_amount = settings.monthly_amount
    months = settings.months

    # Define dados e engine    
    repo = ICMSRepository(cfg)
    engine = ICMSPolicyEngine(repo)

    # Define operações normal x comparação
    origin_operation = Operation(
        uf_origin=uf_origin,
        uf_destiny=uf_destiny,
        operation_date=date.today(),
        merchandise_origin=OriginMerchandise.NATIONAL
    )

    extrema_operation = Operation(
        uf_origin="MG",
        uf_destiny=uf_origin,
        operation_date=date.today(),
        merchandise_origin=OriginMerchandise.NATIONAL
    )

    # Comparação dos cenários
    scenario_comparation = engine.scenario_comparation(
        origin_operation=origin_operation,
        extrema_operation=extrema_operation,
        monthly_amount=monthly_amount,
        months=months
    )

    normal_total = scenario_comparation.normal_scenario.total_value
    tts_total = scenario_comparation.tts_scenario.total_value
    total_savings = scenario_comparation.total_savings
    percentual_savings = (total_savings / normal_total) * 100

    return {
        "normal_total": normal_total,
        "tts_total": tts_total,
        "total_savings": total_savings,
        "percentual_savings": percentual_savings,
    }

    