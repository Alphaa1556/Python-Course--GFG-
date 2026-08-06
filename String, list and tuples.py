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

