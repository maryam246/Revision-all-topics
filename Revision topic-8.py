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
