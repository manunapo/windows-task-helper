import tkinter as tk
from pynput import keyboard
import ctypes
import pywinauto
import pygetwindow as gw
import logging

from app.function import Function
from config.configshandler import GlobalConfigs as cfg_hnd

class ApplicationHandler():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        root = tk.Tk()
        self.logger.info('Starting')
        app = Application(master=root)
        listener = keyboard.GlobalHotKeys({
                cfg_hnd.configs['hotkey']: lambda: app.bring_to_front()})
        listener.start()
        hk = cfg_hnd.configs['hotkey']
        self.logger.info(f'Global hot key {hk} added')
        app.mainloop()
        self.logger.info('Started')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        
        self.locate_window()

        self.entry = self.create_entry_box()
 
    def locate_window(self):
    	self.master.overrideredirect(True)
    	w = 350
    	h = 25
    	ws = self.master.winfo_screenwidth()
    	hs = self.master.winfo_screenheight()
    	x = (ws/2) - (w/2)
    	y = 0
    	self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def create_entry_box(self):
        entry = tk.Entry(self.master, width=40)
        def entry_callback(self,logger = self.logger, master = self.master):
        	entered_value = entry.get()
        	logger.debug(f'Entered value: {entered_value}')
        	entry.delete(0, 'end')
        	ret_code = Function().run(entered_value)
        	if ret_code == 0:
        		logger.info(f'Ending application, ret code: {ret_code}')
        		master.destroy()
        	else:
        		logger.info(f'Function returned {ret_code}')
                
        
        entry.bind('<Return>', entry_callback)
        entry.focus()
        entry.pack()
        return entry

    def bring_to_front(self):
    	tk_win = gw.getWindowsWithTitle('tk')[0]
    	tk_win.minimize()
    	tk_win.restore()
        
