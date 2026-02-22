from hydra import initialize, compose
from omegaconf import DictConfig

def load_config() -> DictConfig:
    with initialize(version_base=None, config_path="../../../configs"):
        cfg = compose(config_name="config")
    return cfg