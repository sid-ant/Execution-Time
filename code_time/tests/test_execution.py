import unittest
from code_time import ExecutionTime
import time

class TestExecutionTime(unittest.TestCase):

    #fixture fucntion 
    sleep = lambda a : time.sleep(a)

    def test_default_decorator(self):
        ex = ExecutionTime()
        decorator = ex.timeit(TestExecutionTime.sleep(2))
        print(ex.logtime_data)
        self.assertIsNotNone(ex.logtime_data,msg="logtime_data dict should not be empty")
    
    def test_filelog(self):
        pass
    
    def test_console(self):
        pass
    
    def test_auto_decorate(self):
        pass


if __name__ == 'main':
    unittest.main()