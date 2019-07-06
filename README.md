# Execution-Time

[![Build Status](https://travis-ci.org/siddhant-curious/Execution-Time.svg?branch=master)](https://travis-ci.org/siddhant-curious/Execution-Time)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/siddhant-curious/Execution-Time/blob/master/LICENSE)

This is a tiny python package which provides you with a decorator to measure execution time of functions. 

## Installation

You should be able to install using `pip` in the usual ways:

```sh
$ pip install execution-time
```

Or just clone this repository and run:

```sh
$ python3 setup.py install
```

Or place the `execution_time` folder that you downloaded somewhere where it can be accessed by your scripts.

## Basic Usage

Import the class `ExecutionTime`, instantiate it and `@obj.timeit` decorater becomes available. 

```python
from execution_time import ExecutionTime
e = ExecutionTime()

@e.timit
def foo(arg1):
  do_something(arg1) 
  return 

@e.timeit
def bar():
  hello_world()
  return

foo("dragons")
bar()
print(e.logdata_time)

## {'foo': 0.12000000000012001, 'bar': 0.11650000000007488}

```
`logdata_time` is a dictionary which contains the data in `methodname:time took in ms` format. 

## Additonal Features

1. Auto-Decorate all functions in a script. 

This is a shortcut if you want to auto-deocreate all function. To do so, pass the `__name__` attribute to the class instantiation as: 

```python
from execution_time import ExecutionTime

def foo():
  do_something()
  return 

def bar():
  hi()

e = ExecutionTime(module_name=__name__)

foo()
bar()

print(e.logdata_time)
```
Note: The class instantiation must be done after functions have been defined and before they are called. This does limit where this feature can be used and the decorator approach is recommeneded in those scenarios. 

2. Provide console logs. 

```python
e = ExecutionTime(console=True)
```

Output the log time in console as: `2019-07-06 22:07:55,157 [INFO ]  Time take by method : foo is 0.12000000000012001 ms`

## Issues

You can report the bugs at the [issue tracker](https://github.com/siddhant-curious/Execution-Time/issues)

## License

Built with ♥ by Siddhant Chhabra([@siddhant-curious](https://github.com/siddhant-curious)) under [MIT License](https://github.com/siddhant-curious/Execution-Time/blob/master/LICENSE)

You can find a copy of the License at <https://github.com/siddhant-curious/Execution-Time/blob/master/LICENSE>
