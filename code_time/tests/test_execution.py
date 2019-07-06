import unittest
from code_time import ExecutionTime
import time
from unittest.mock import Mock
import logging

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
        self.assertTrue(ex.logtime_data,msg="logtime_data dict should not be empty")

if __name__ == '__main__':
    unittest.main()