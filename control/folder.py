import logging
import webbrowser

from config.configshandler import GlobalConfigs as cfg_hnd

class Folder():
    def __init__(self, input):
        self.logger = logging.getLogger(__name__)
        try:
            url = cfg_hnd.configs['command']['folder'][input]
            self.logger.info("Opening {url}")
            
            webbrowser.open(url)
        except Exception as e:
            self.logger.error(f"Can not open, due to {e}")