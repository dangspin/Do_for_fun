## In this example, I will illustrate some examples about class with __call__ magic method

## Example 1: Multiplication class

class Multiple:
    
    def __init__(self, input):
        self.input = input
        
    def __call__(self, num):
        return self.input * num
    
t = Multiple(4)(4)

## or

multiple_t = Multiple(4)
multiple_t(4)

print(t)


## Example 2: Inheritance of __call__ method

class my:
    
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
    def __call__(self, c):
        return self.call(c)
    
    def call(self, c):
        return (self.a + self.b) *c
    
class my2(my):
    
    def __init__(self,a, b, d):
        super(my2, self).__init__(a,b)
        self.d = d
        
    def call(self,  c):
        return self.a + c
    
ex = my2(1, 2, 3)
print(ex(100))   ## print out 101
print(my(1, 2)(3))   ## print out 9
