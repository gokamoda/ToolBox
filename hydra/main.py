import hydra
from omegaconf import DictConfig, OmegaConf, open_dict

import logging

logger = logging.getLogger(__name__)

@hydra.main(version_base='1.2', config_path="config", config_name="config")
def main(cfg: DictConfig) -> None:
    logger.info('\n' + OmegaConf.to_yaml(cfg))

    # output directory
    hydra_cfg = hydra.core.hydra_config.HydraConfig.get()
    output_dir = hydra_cfg['runtime']['output_dir']
    logger.info(output_dir)

    # adding new key
    with open_dict(cfg):
        cfg['new_key'] = 'new_value'

    logger.info('\n' + OmegaConf.to_yaml(cfg))
    


if __name__ == '__main__':
    main()