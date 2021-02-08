import logging
import webbrowser

from config.configshandler import GlobalConfigs as cfg_hnd


class Browser():
    def __init__(self, input):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Starting new browser action")
        try:
            url = cfg_hnd.configs['command']['browser'][input]
            webbrowser.open(url)
            self.logger.info("Opening {url}")
        except Exception as e:
            self.logger.error(f"Can not open, due to {e}")