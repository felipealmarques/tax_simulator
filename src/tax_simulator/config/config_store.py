from hydra.core.config_store import ConfigStore
from tax_simulator.config.config_schema import TaxSimulatorCfg

def register():
    cs = ConfigStore().instance()
    cs.store(name="tax_simulator", node=TaxSimulatorCfg)
    