import functools
import time
import os
import logging
from inspect import getmembers,isfunction
import sys


class Timer:

    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    def __init__(self,filelog=False,console=False,module_name=None,decorate_methods=False):
         
        self.issue_url = "https://github.com/siddhant-curious/Python-Method-Execution-Time/issues"
        
        self.filelog = filelog        
        self.console = console
        self.module_name = module_name
        self.logtime_data = {}

        if self.filelog:
            self.enable_filelogs()

        if self.console:
            self.enable_console()

        if self.module_name is not None:
            self.auto_decorate()
    
    def timeit(self,method):
        @functools.wraps(method)
        def wrapper(*args,**kwargs):
            start_time = time.perf_counter()
            result = method(*args,**kwargs)
            end_time = time.perf_counter()
            total_time = end_time-start_time
            self.logtime_data[method.__name__]=total_time
            if self.console is True:
                Timer.rootLogger.info(f'Time take by method : {method.__name__}  of {self.module_name} is {total_time}')
            return result
        return wrapper
    
    def enable_console(self):
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(Timer.logFormatter)
        Timer.rootLogger.addHandler(consoleHandler)
    
    def enable_filelogs(self):
        fileHandler = logging.FileHandler("execution_times.log")
        fileHandler.setFormatter(Timer.logFormatter)
        Timer.rootLogger.addHandler(fileHandler)

    def auto_decorate(self):
        try:
            module = sys.modules[self.module_name]
            methods = getmembers(module,isfunction)
            for name,addr in methods:
                setattr(module,name,self.timeit(addr))
        except KeyError as e:
            raise f'Error Occured, No module by name {module_name}. If you think this was a mistake than raise issue at {self.issue_url}'
