import functools
import time
import os
import logger

'''
1. console logging
2. logging file
3. all methods, automatically
'''


class Timer():
    def __init__(self,filelog=False,console=False,all_methods=False):
        self.filelog = filelog
        self.console = console
        self.all_methods = all_methods
        self.logtime_data = {}
    
    def timeit(self,method):
        @functools.wraps(method)
        def wrapper(*args,**kwargs):
            start_time = time.perf_counter()
            result = method(*args,**kwargs)
            end_time = time.perf_counter()
            total_time = end_time-start_time
            self.logtime_data[method.__name__]=total_time
            return result
        return wrapper

