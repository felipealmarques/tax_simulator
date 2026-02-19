import hydra
from datetime import date

from tax_simulator.domain.models import Operation, OriginMerchandise
from tax_simulator.domain.engines import ICMSPolicyEngine
from tax_simulator.data_ingestion.repositories import ICMSRepository

from tax_simulator.config.config_schema import TaxSimulatorCfg
from tax_simulator.config.config_store import register

register()

@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: TaxSimulatorCfg):

    repo = ICMSRepository(cfg)
    engine = ICMSPolicyEngine(repo)

    operacao = Operation(
        uf_origin="SP",
        uf_destiny="MG",
        operation_date=date.today(),
        merchandise_origin=OriginMerchandise.NATIONAL
    )

    aliquot = engine.aliquot_calculate(operacao)

    print(f"Alíquota: {aliquot}%")


if __name__ == "__main__":
    main()
