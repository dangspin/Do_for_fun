## This is the script to illustrate Python decorator

## Example 1:

def my_decorator(func):
    def wrapper(x):
        print("Something is happening before the function is called.")
        res = func(x)
        print("Something is happening after the function is called.")
        return res
    return wrapper

@my_decorator
def ff(x_input):
    print("This is the function ff")
    return x_input**3

ff(4)

## Something is happening before the function is called.
## This is the function ff
## Something is happening after the function is called.
## 64


## Example 2: A very interesting example to show how to decorate a function with many recursive calls.
import time

def slowdown(func):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper

@slowdown
def countDown(num):
    if num < 1:
        return "Times up!"
    else:
        print(num)
        return countDown(num - 1)
    
countDown(4)

## 4
## 3
## 2
## 1
## Times up!


## Example 3: Using class as a decorator
class printFunction:
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args):
        print("We are running the function: " + self.func.__name__)
        return self.func(*args)
    
@printFunction
def dxf(x):
    return x**3 + 10

dxf(3)

## We are running the function: dxf
## 37


## Example 4: Using class as a decorator, which accept parameter
import time

class helper:
    
    def __init__(self, *args):
        self.coeff = args[0]
        self.x_input = args[1]
        
    def __call__(self, func):
        print("We are running the function: " + func.__name__)
        time.sleep(2)
        return self.coeff * func(self.x_input)

@helper(2, 1)
def exf(x):
    return (1 + x + (x**2)/2 + (x**3)/(1*2*3))

exf

## We are running the function: exf
## 5.333333333333333


## Example 5. Same result as previous one, but accept more inputs
import time

class helper:
    
    def __init__(self, time_gap, coeff):
        self.time = time_gap
        self.coeff = coeff
        
    def __call__(self, func):
        def wrapper(x_input):
            print("We are running the function: " + func.__name__)
            time.sleep(self.time)
            return self.coeff * func(x_input)
        return wrapper

@helper(2, 2)
def exf(x):
    return (1 + x + (x**2)/2 + (x**3)/(1*2*3))


exf(1)

## Example 6. Compare between with/without decorator
def other_2(func):
    print("Wrapper will be called")
    def wrapper(*args):
        print("This is another function")
        return 3*func(*args)
    print(hex(id(wrapper)))
    return wrapper


def ff(x_input):
    x = x_input**3 + 10
    return x

ff(4)  ## output 74

ff = other_2(ff)
ff(4)

## Wrapper will be called
## 0x7fe12c5e4950
## This is another function
## This is another function
## 333
