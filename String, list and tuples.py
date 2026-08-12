a ='GFG'
b ='GeeksForGeeks'
print(a)
print(b)

s = """ I am Learning Python String on GeeksforGeeks"""
print(s)
s = '''Geek'''
print(s)

s="ABCDEF"
print(s[0])
print(s[4])

s="ABCDEF"
print(s[-3])
print(s[-5])

s="ABCEDEF"
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])

s="ABCDEF"
for char in s:
    print(char)

s="aBCDEF"
s="A"+s[1:]
print(s)

#Updating a String
s = " ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")
print(s1)
print(s2)

#Common String Methods
s = "GeeksforGeeks"
print(len(s))
s = "Hello World"
print(s.lower())
print(s.upper())
s = "   ABC  "
print(s.strip())
s = "Python is fun"
print(s.replace("fun", "Awesome"))

#Concatenating and Repeating Strings
s1 = "Hello"
s2 = "world"
print(s1 + " " + s2)
s = "Hello"
print(s *3)

#Formatting Strings
name ="Yash Khanavkar"
age = 20
print(f"Name: {name}, Age: {age}")
s = "My name is {} and I am {} years old.".format("YYash Khanavkar",22)
print(s)
s = "GeeksforGeeks"
print("geeks" in s)
print("GFG" in s)

#Creating a list
a=[1, 2, 3]
print(a)
b=["apple", "banana"]
print(b)

#Using list() constructor
a = list((1,2,3,'apple',4.5))
print(a)
b = list("GFG")
print(b)

a=[2]*5
print(a)
b=[0]*6
print(b)

a = [1,2,2, "Python"]
print(a[0])
print(a)

a=[10,20,30]
print(a[0])
print(a[-1])

a = [1,2]
a.append(3)
print(a)

a = [1,3]
a.insert(1,2)
print(a)

a = [1,2]
a.extend([3,4])
print(a)

#Updating Elements
a = [10,20,30,40,50]
a[1] = 25
print(a)

#Removing Elements
a = [1, 2, 3]
a.remove(2)
print(a)

a = [1, 2, 3]
a.pop()
print(a)

a = [1,2,3]
del a[1]
print(a)

a = [1, 2, 3]
a.clear()
print(a)

a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

a = [[1,2],[3,4]]
print(a[0])
print(a[1][0])
