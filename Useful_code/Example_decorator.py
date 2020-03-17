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
