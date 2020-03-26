## 1. Yield, which turns a function to a generator:

## Ex1: Square of a number of input
def square(x_input):
    while True:
        t = x_input**2
        x_input = x_input + 1
        yield t
        
for num in square(10):
    if num > 500:
        break
    print(num)
    
    
 ## Ex2: Generate a set of numbers given a step
 def square(start, end, step):
    i = start
    while i <= end:
        yield i
        i = i + step
        
        
for num in square(0, 100, 3):
    print(num)
