from pathlib import Path
from omegaconf import OmegaConf, DictConfig

def load_config() -> DictConfig:
    config_path = Path(__file__).parents[3] / "configs"

    dashboard = OmegaConf.load(config_path / "dashboard" / "dashboard.yaml")
    icms = OmegaConf.load(config_path / "icms" / "icms_padrao.yaml")
    system = OmegaConf.load(config_path / "system.yaml")

    cfg = OmegaConf.create({
        "dashboard": dashboard,
        "icms": icms,
        "system": system,
    })

    return cfg