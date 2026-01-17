def fun():
    print("Welcome to GFG")

fun()

def evenOdd(x):
    if (x%2==0):
        return"Even"
    else:
        return"Odd"
    
print(evenOdd(16))
print(evenOdd(7))

def myFun(x ,y=50):
    print("x:",x)
    print("y:",y)

myFun(60)
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

def nameAge(name,age):
    print("HI i am",name)
    print("My age is",age)

print("CASE-1:")
nameAge("Yash",19)
print("\n CASE-2:")
nameAge(19,"Yash")

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments(*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}=={value}")

myFun('Hey', 'Welcome', first='Geeks', mid='For', last='Geeks')

def f1():
    s='I Love Neelaja'
    def f2():
        print(s)
    f2()
f1()

def cube(x): return x*x*x
cube_l= lambda x: x*x*x

print(cube(7))
print(cube_l(7))

def square_value(num):
    return num**2

print(square_value(2))
print(square_value(-4))

def myFun(x):
    x[0]=20

lst=[10,11,12,13]
myFun(lst)
print(lst)

def myFun2(x):
    x=20

a=10
myFun2(a)
print(a)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(4))
