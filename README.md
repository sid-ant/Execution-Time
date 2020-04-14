# Execution-Time

[![Build Status](https://travis-ci.org/siddhant-curious/Execution-Time.svg?branch=master)](https://travis-ci.org/siddhant-curious/Execution-Time)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/siddhant-curious/Execution-Time/blob/master/LICENSE)

This is a tiny python package which provides you with a decorator to measure execution time (in ms) of functions. 


## Installation

You should be able to install using `pip` in the usual ways:

```sh
$ pip install Execution-Time
```

Or just clone this repository and run:

```sh
$ python3 setup.py install
```

Or place the `execution_time` folder that you downloaded somewhere where it can be accessed by your scripts.


## Basic Usage

Import the class `ExecutionTime`, instantiate it and `@obj.timeit` decorater becomes available. 

```python
import time
import random
from execution_time import ExecutionTime
e = ExecutionTime(console=False, module_name=None)


def do_something(arg1):
  time.sleep(arg1)


def hello_world():
  t1 = round(random.random(), 4)  # seconds
  print('Hello world, time = ' + str(t1*1000) + ' ms')
  time.sleep(t1)


@e.timeit
def foo(arg1):
  do_something(arg1) 
  return 


@e.timeit
def bar():
  hello_world()
  return


foo(2.4)
bar()
bar()
bar()
print(e.logtime_data)

# OUTPUT
# {'foo': {'times_called': 1, 'total_time': 2400.2058, 'average_time': 2400.2058}, 'bar': {'times_called': 3, 'total_time': 1776.2484, 'average_time': 592.0828}}
```
`logtime_data` is a dictionary which contains the data in `methodname:time took in ms` format. 


## Additonal Features

1. Auto-Decorate all functions in a script. 

    This is a shortcut if you want to auto-deocreate all function. To do so, pass the `__name__` attribute to the class instantiation as: 

    ```python
    import time
    import random
    from execution_time import ExecutionTime


    def foo():
      time.sleep(1.2)
      return 


    def bar():
      time.sleep(random.random())
      return


    e = ExecutionTime(console=False, module_name=__name__)

    foo()
    bar()

    print(e.logtime_data)
    ```
    Note: The class instantiation must be done after functions have been defined and before they are called. This does limit where this feature can be used and the decorator approach is recommeneded in those scenarios. 

2. Provide console logs. 

    ```python
    e = ExecutionTime(console=True)
    ```

    Output the log time in console as: `2020-04-14 15:14:34,354 [INFO ]  Time take by method : foo is 1201.2767 ms`

## Issues

You can report the bugs at the [issue tracker](https://github.com/siddhant-curious/Execution-Time/issues)


## License

Built with ♥ by Siddhant Chhabra([@siddhant-curious](https://github.com/siddhant-curious)) under [MIT License](https://github.com/siddhant-curious/Execution-Time/blob/master/LICENSE)

You can find a copy of the License at <https://github.com/siddhant-curious/Execution-Time/blob/master/LICENSE>
