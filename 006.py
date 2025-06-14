def add(a,b):
    return a+b

class Test():
    def __init__(self, add_function):
        self.add_function = add_function
        
test = Test(add_function=add)
 # we want to get the function itself and not call it
print(test.add_function(1,2))