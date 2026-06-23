#Factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#Fibonnaci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))

def fun(*args):
    return sum(args)
print(fun(10,15,20))
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k,val)
fun(a=1,b=2,c=3)

def student_info(*args,**kwargs):
    print("Subjects:",args)
    print("Details:",kwargs)
student_info("math","science","english",name="Alice",age=20,city="New york")

a='Geeks For Geeks'
Upper=lambda X: X.upper()
print(Upper(a))

s=['1','2','3','4']
res=map(int,s)
print(list(res))

def double (val):
    return val*2
a=[1,2,3,4]
res=list(map(double,a))
print (res)

a=[1,2,3,4]
res=list(map(lambda X:X**2,a))
print(res)

#FILTER() IN PYTHON

def starts_a(w):
    return w.startswith("a")

li=["apple","banana","avacado","grape","apricot"]
res=list(filter(starts_a,li))
print (list(res))

def even(n):
    return n%2==0
a=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(even,a))
print(res)

# REDUCE() IN PYTHON

from curses import wrapper
from functools import reduce
a=[ "GEEKS", "FOR",  "GEEKS"]
r=reduce(lambda x,y:x+""+y,a)
print(r)

from functools import reduce
a=[2,4,6,8]
r=reduce(lambda x,y:x+y,a)
print(r)

#ACCUMULATE() IN PYTHON

from itertools import accumulate
from operator import add
a=[1,2,3,4,5]
res=accumulate(a,add)
print(list(res))

#DECORATORS IN PYTHON
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def greet():
    print("Hello, world")
greet()

def simple_decorator(func):
    def wrapper():
        print(">>> Starting function")
        func()
        print(">>> Function finished")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
greet()

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result= func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))
