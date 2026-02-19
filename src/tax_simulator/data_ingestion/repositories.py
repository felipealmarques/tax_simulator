from tax_simulator.config.config_schema import TaxSimulatorCfg

class ICMSRepository:
    def __init__(self, cfg: TaxSimulatorCfg):
        self.cfg = cfg

    def get_aliquota_interna(self, uf: str) -> float:
        return self.cfg.icms.icms.interna[uf]
    
    def get_aliquota_interestadual(self, origin: str, destiny: str) -> float:
        return (
            self.cfg
            .icms.icms
            .interestadual["excecoes_matriz_completa"][origin][destiny]
        )

    def get_aliquota_importada(self) -> float:
        return self.cfg.icms.icms.importado["aliquota_interestadual"]