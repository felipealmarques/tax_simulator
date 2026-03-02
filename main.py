from omegaconf import DictConfig
from datetime import date

from tax_simulator.domain.models import Operation, OriginMerchandise
from tax_simulator.domain.engines import ICMSPolicyEngine
from tax_simulator.data_ingestion.repositories import ICMSRepository

from tax_simulator.config.config_loader import load_config
from tax_simulator.utils.helpers import print_results

# Função principal
def main(cfg: DictConfig):

    repo = ICMSRepository(cfg)
    engine = ICMSPolicyEngine(repo)

    # configurações
    uf_origin = "SP"
    uf_destiny = "BA"
    monthly_amount = 500_000
    months = 12

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

    # Calculo da alíquota
    aliquot = engine.aliquot_calculate(origin_operation)
    print(f"Alíquota: {aliquot}%")

    # Comparação dos cenários
    scenario_comparation = engine.scenario_comparation(
        origin_operation=origin_operation,
        extrema_operation=extrema_operation,
        monthly_amount=monthly_amount,
        months=months
    )

    print_results(
        scenario_comparation=scenario_comparation, 
        uf_origin=uf_origin,
        monthly_amount=monthly_amount,
        months=months
    )


if __name__ == "__main__":
    cfg = load_config()
    main(cfg=cfg)
