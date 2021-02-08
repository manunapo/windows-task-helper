import json
import logging

class GlobalConfigs():
    
    configs = {}
    
    def load(conf_file = './config/configs.json'):
        print('Starting to load config file')
        logger = logging.getLogger(__name__)
        try:
            with open(conf_file,'r') as json_file:
                GlobalConfigs.configs = json.load(json_file)
            logger.info('config file succefully loaded')
        except Exception as e:
            logger.error(e)