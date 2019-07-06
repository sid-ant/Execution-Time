import unittest
from code_time import ExecutionTime
import time
from unittest.mock import Mock

class TestExecutionTime(unittest.TestCase):

    def test_default_decorator(self):
        """
        Test ExecutionTime with default arguments
        """
        func = Mock()
        func.__name__ = 'foo'
        ex = ExecutionTime()
        decorated = ex.timeit(func)
        decorated()
        print(ex.logtime_data)
        self.assertTrue(ex.logtime_data,msg="logtime_data dict should not be empty")
        
    def test_console(self):
        """
        Test to check if log got written to console
        """
        func = Mock()
        func.__name__='bar'
        ex = ExecutionTime(console=True)
        decorated = ex.timeit(func)
        decorated()
        self.assertTrue(ex.logtime_data,msg="logtime_data dict should not be empty")

    
    # def test_auto_decorate(self):
    #     """
    #     Test to check if all functions were auto decorated in a given module
    #     """
    #     pass
    
    # def test_failure_auto_decoreate(self):
    #     pass 


if __name__ == '__main__':
    unittest.main()