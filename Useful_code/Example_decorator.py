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


## Example 2:
