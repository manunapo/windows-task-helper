from config.configshandler import GlobalConfigs as cfg_hnd
from app.applicationhandler import ApplicationHandler
import logging
import logging.config

if __name__ == '__main__':
    logging.config.fileConfig('./log/logging.conf')
    logger = logging.getLogger(__name__)
    cfg_hnd.load()
    logger.debug(f'Loaded config file: {cfg_hnd.configs}')
    app_hnd = ApplicationHandler()