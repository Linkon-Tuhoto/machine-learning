name = "Linkon"
age = 35
score = 95.5
print(f"My name is {name} and am {age} years old. i scored {score}")

#Spacing should be the same, else it will result to an error- identation
if 5 > 2:
    print("Five is greater than two!");
#Comments is commented using #

#Variables
x=5
y="Hello"
print(x)
#variable type
print(type(y))
#variables are case sensitive

#string slicing 
a = " Hello, world"
#front slicing
print(a[:3])
#back slicing
print(a[3:])
#uppercase
print(a.upper())
#lowecase
print(a.lower())
#removing white spaces
print(a.strip())
#string replacing
print(a.replace("H", "J"))
#string split
print(a.split(","))
#string concatenation
c="Hello"
d="World"
e= c + d
f=c + " " + d
print(e)
print(f)
#string format
age = 24
txt = f"My name is Linkon my age is {age}"
print(txt)
#escape characters
my= "Kenya is a \"good\" country"
print(my)