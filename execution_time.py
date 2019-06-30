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

    def __init__(self,filelog=False,console=False,module_name=None):
         
        self.issue_url = "https://github.com/siddhant-curious/Python-Method-Execution-Time/issues"
        
        self.filelog = filelog
        if self.filelog is True:
            fileHandler = logging.FileHandler("execution_times1.log")
            fileHandler.setFormatter(Timer.logFormatter)
            Timer.rootLogger.addHandler(fileHandler)
        
        self.console = console
        if self.console is True: 
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setFormatter(Timer.logFormatter)
            Timer.rootLogger.addHandler(consoleHandler)
        
        self.module_name = module_name
        if self.module_name is not None:
            try:
                module = sys.modules[module_name]
                methods = getmembers(module,isfunction)
                for name,addr in methods:
                    setattr(module,name,self.timeit(addr))
            except KeyError as e:
                raise f'Error Occured, No module by name {module_name}. If you think this was a mistake than raise issue at {self.issue_url}'
        self.logtime_data = {}
        
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