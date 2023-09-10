# Example of help function in python:
print(help("str"))
print(help())


# importing numpy module
np = __import__('numpy',globals(),locals(),[],0)
a = np.array([1,2,3,4])
print(type(a))

#ANother example:
np = __import__('numpy',globals(),locals(),['complex','array'],0)
comp = np.copmplex(3,5)
arr = np.array([1,2,3,4])
print(comp)
print(arr)

#Another example
from math import sqrt,pow
a = sqrt(5)
b = pow(2,3)
print(a,b)

import math as m
i = m.pi
print(i)

n =m.gcd(8,12,16)
print(n)

# Example of range:
for i in range(0,11):
    print(i)
    #Another example
r = range(1,5)
print(list(r))
#slicing operation on range
a = range(1,6)
print(list(a[2:5]))

#Example of coroutine:
def number():
    import time
    #it takes 4 sec to consuming task
    time.sleep(4)
    lst_of_num = [1,2,3,4,5,6,7]
    while True:
        n = (yield)
        if n in lst_of_num:
            print("Yeah! we found number")
        else:
            print("sorry! we not fond the number")
search = number()
next(search)
search.send(1)
print(input('Press enter'))
search.send(6)

#Another example
def fruits():
    import time
    time.sleep(3)
    fruit = "mango,orange,bnana,kiwi,grapes,melon,water melon"
    while True:
        f = (yield)
        if f in fruit:
            print(f"yes! {f} is a fruit")

        else:
            print(f"No! {f} is not a fruit")

search = fruits()
next(search)

search.send("banana")
input("Enter any key")
search.send("ali")

search.close()
#A nother example of coroutine
def cosmetic():
    import time
    time.sleep(3)
    cosmetics = "lipstic,hair bursh, nail polish,eye shadow,eye liner"
    while True:
        c = (yield)
        if c in cosmetics:
            print(f"{c} is available.")
        else:
            print(f"{c} is not available.")

search = cosmetic()
next(search)

search.send("lipstic")
input("Enter any key")
search.send("Tint")

#Another example

def print_name(prefix):
    print("searching for prefix: {}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

search = print_name('Dear')
next(search)
search.send('Maryam')
search.send('Dear Maryam')

#Another example
def print_name(prefix):
    print("searchin for prefix: {}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("closing coroutine")

search = print_name("Dear")
next(search)
search.send("Amina")
search.send("Dear Amine")

#Another example
def producer(sentence, next_coroutine):
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filtter(pattern='ing', next_coroutine=None):
    print("searching for{}: ".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("i am done with filtiring")

def print_token():
    print("i am a sink,i'll be print token")
    try:
        while True:
            token =(yield)
            print(token)
    except GeneratorExit:
        print("i'm done with printing.")

pt = print_token()
next(pt)
pf = pattern_filtter(next_coroutine = pt)
next(pf)

sentence = "Hi! I am a student of Virtual university."
producer(sentence,pt)

# Example of Python bit function on int:
# int.bit_length():
i = 7
print(i.bit_length())

l = 1123
print(l.to_bytes(3,byteorder="little"))

w=234
print(w.to_bytes(3,byteorder='big'))

s = 323
print(s.to_bytes(4,byteorder="big"))
#int.from_bytes(bytes,byteorder=*signed=false)
print(int.from_bytes(b'\00x\04',byteorder='big'))

print(int.from_bytes(b'\x04\x00',byteorder="big"))

# Example of File handling (read,write,update):
#read():
f = open("hello",mode='r')
data = f.read(34)
print(data)
f.close()

fi =open("hello.txt.py",mode='r')
data = fi.read()
print(data)
fi.close()

fil = open("check.py",mode='w')
data =fil.write('i am a student')
print(data)
fil.close()


file = open("check.py",mode='a')
data = file.write('i am a student')
print(data)
file.close()

fl = open("hello.txt.py",mode='a')
data = fl.write("Hllo world!")
print(data)
fl.close()

#Example of User defined Exception:
class colour_exception(Exception):
    pass

def check_colour():
    a = input("Enter colour name1: ")
    b = input("Enter colour name2: ")
    try:
        if a in ("white","Red") and b in ("blue","green"):
            raise  colour_exception
        print(a,b)

    except  colour_exception:
        print("Enter colour is wrong")
s1=check_colour()
print(s1)

# Another example:
class check_valid_age(Exception):
    pass
age =18

try:
    get = int(input("Enter age: "))
    if get>age:
        raise check_valid_age
    print("You are not eligible for casting vote")
except check_valid_age:
    print("cast vote")


#Another Example
class name_exception(Exception):
    pass
try:
    name = input("enter name")
    if name=='ali':
        raise name_exception
    else:
        print(f"{name} is fouund")

except name_exception:
    print("Great name_exception is handle.")

#Example of built in exception in python
try:
    result =10/0

except ZeroDivisionError:
    print("Error occured due to denominator=0")

#Another example
try:
    f = open("check.py",mode='r')
    data =f.read(45)
    print(data)
    f.close()
except FileNotFoundError:
    print("file is not exist")
#another example

try:
    list = int('arya')
except (ValueError,TypeError):
    print("there two error occured")

#Example of try and except in python:
t = input("Enter the number: ")
print(f"Multiplcation of {t} is: ")
try:
    for i in range(1,11):
        print(f"{int(t)} X {i} = {int(t)*i}")
except:
    print("invalid input")

# example of global ,local scope
a =22
def num1():
   b =67
   print(a)
   print(b)
num1()
print(a)

#indentation.
x =100
if x>20:
   print("False")
else:
   print("TRUE")

#Assignment statements
i = 2
j = 4
x = i+j*j-i+7
print(x)

#Chek validity of string
import keyword
t = "True"
if keyword.iskeyword(t):
   print(f"Found {t}")
else:
   print("not found")

#Another example
import keyword
y = "list"
if keyword.iskeyword(y):
   print("yes we found")
else:
   print("no")

# Assigning value in python and other language
x = 100
y = "maryam"
#in c++,java
#int x = 100

#example print a new line
print("I",end=" ")
print("am",end=" ")
print("a",end=" ")
print("girl.")

# Example of basic calculator:
def sum():
   i = int(input("Enter 1st number: "))
   j = int(input("Enter 2st number: "))
   return i+j

def div():
   i = int(input("Enter 1st number: "))
   j = int(input("Enter 2st number: "))
   return i/j

def mul():
   i = int(input("Enter 1st number: "))
   j = int(input("Enter 2st number: "))
   return i*j

def sub():
   i = int(input("Enter 1st number: "))
   j = int(input("Enter 2st number: "))
   return i-j

print("Select--> 1(sum)/2(div)/3(mul)/4(sub)")
a = int(input("Select: "))
if a==1:
   print(sum())
elif a==2:
   print(div())
elif a==3:
   print(mul())
elif a==4:
   print(sub())
else:
   print("Invalid selection!")

# Example of taking multiple input from user:
name = input("Enter your name: ")
print(name)
age = int(input("Enter your age: "))
print(age)
CGPA = float(input("Enter your CGPA: "))
print(CGPA)

#Example of Python Input Methods for Competitive Programming:
# input method:
from sys import stdin,stdout
a = stdin.readline()
print(a)

arr = [int(x) for x in stdin.readline().split()]

print(arr)
# output by stdout
n = stdout.write(str(sum()))
print(n)

#Example of print() function
m = "ali"
n = 22
o = 33.33
print("Data of m,n,o is: ",m,n,o)

#Example of sep ()function:
print("I love","Pakistan","hy","ali",sep=" ")

#Example of OUTPUT formating
fruit = "Apple"
price = 200
#output using %
print("Fruit: %s price: %d" % (fruit,price)) # %s for str, %f for float,%d for int

sallary = 20000.0
name = "Qamar"
print("sallary: %d name: %s" % (sallary,name))

# using{} braces
print("name:{} sallary:{}".format(name,sallary))
print("fruit:{} price:{}".format(fruit,price))

#Another example
a =20
b ='a'
print("a:%d b:%s"%(a,b))
print("a:{} b:{} ".format(a,b))


#Example of dictonary
dic = {"ali":1,"maryam":2,"kiran":3}
print(dic)

##Example of  Name(A special variable)in python:
a= 2
b = 5
z = a*b
print(z)
print("i am a ",__name__)
if __name__=='__main__':
   print("hello")

#Example of private variable
class A():
   def __init__(self, a):
      self.__a = a

   def show(self):
      print(f"{self.__a}")


a = A("I am a vowel")
a.show()

#Another example
class Student():
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def display_info(self):
      print(f"My name is {self.__name}, and my age is {self.__age}")


s = Student("maryam", 20)
s.display_info()

#Another example
class Papers():
   def __init__(self, p1, p2):
      self.__p1 = p1
      self.__p2 = p2

   def print_papers(self):
      print(f"MY 1st paper is {self.__p1}, and 2nd paper is {self.__p2}")


p = Papers('math', 'computer')
p.print_papers()

#Another example
class City_names():
   def __init__(self, c1, c2):
      self.__c1 = c1
      self.__c2 = c2

   def prnt(self):
      print(f"The first country name is {self.__c1}, and another city name is {self.__c2}")


c = City_names('Islamabad', 'Karachi')
c.prnt()

#Example of check equality
def check_equality(a,b):
   if a>b:
      print("a is greater than b")
   elif a!=b:
      print("a is not equal to b")
   else:
      print("Condition falls")
check_equality(2,5)

#Example of maximum possible value of an integer on your system
import sys
m = sys.maxsize
print("m")

#Example of packing and unpacking:
#Unpacking:
def fun(a,b,c,d):
   print(a,b,c,d)

l = [1,2,3,4]
fun(*l)

#Another example
a = [2,8]
print(list(range(*a)))

#Packing
def num(*n):
    print(n)

num(2,3,45,5)

#Another example
def colour(*c):
    print(c)

colour('orange','green','blue')

def A(*d):
   print(d)
A(2,3,4,2)

#Example of Bytes object VS String in
a = "Great"
b = b"Great"
print(a)
print(b  )
print(type(a))
print(type(b))
