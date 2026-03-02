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
