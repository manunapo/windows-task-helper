import logging

from control.browser import Browser
from control.folder import Folder
from config.configshandler import GlobalConfigs as cfg_hnd

class Function():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting')
        
    def parse_command(self, raw_value):
        command = None
        input = None
        splitted = raw_value.split(' ')
        if len(splitted) == 1 and splitted[0] != '':
            command = splitted[0]
        elif len(splitted) == 2:
            command = splitted[0]
            input = splitted[1]
        return command,input
        
    def run(self, entered_value):
        command,input = self.parse_command(entered_value)
        self.logger.debug(f'Entered command: {command}')
        self.logger.debug(f'Entered parameter: {input}')
        try:
            if command == 'exit':
                return 0
            elif command == 'l':
                cfg_hnd.load()
            elif command == 'b':
                Browser(input)
            elif command == 'f':
                Folder(input)
            return 1
        except Exception as e:
            self.logger.warn(f'Could not execute the command {command} {input}, please check it')
            self.logger.error(e)
            return 1