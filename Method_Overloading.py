from multipledispatch import dispatch
@dispatch(int, int)
def addIntegers(a, b):
    print("Adding integers:", a + b)
@dispatch(int, int, int)
def addIntegers(a, b, c):
    print("Adding three integers:", a + b + c)
    
addIntegers(5, 10)  # Calls the first function
addIntegers(5, 10, 15)  # Calls the second function