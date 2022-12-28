# 19 exec()..The exec() function is used to execute or run a Python code dynamically.We can write Python code in a string and pass it as an argument to the exec() function. It will parse the string and execute the Python code inside it.
exec("print('hello')")
exec("a=10;b=10;print(a+b)")
print(" 19 **********\n")
# 20..The float functions returns or convert the argument into a floating-point value if it is compatible. We can convert integers and strings that only contain digits.
print(float( 18))
print(float(10))
print(float('15'))
print(" 20 **********\n")
#21..frozenset()..The frozenset() function takes an iterable as an argument and converts it into an immutable
print(frozenset([1,2,3,4,5]))
print(frozenset({5,6,7,8,9}))
print(frozenset((1,2,3,4,5)))
print(" 21 **********\n")
#22..id()..The id() function takes an object as an argument and returns the identity of the object. The id is unique and constant for each object.
print(id(31))
print(id(3.1))
print(id("hello"))
print(" 22 **********\n")
#23..getattr(object, name)   The getattr() function is used to get the value of an object‟s attribute.
class car:
    color='black'
c=car()
print(getattr(c,'color'))
print(" 23 **********\n")

#24/..globals()...The function returns a dictionary in which all the global objects are accessible in the current scope or module.
l=[1,2,3,4,'a','b','c']
print(globals())
print(" 24 **********\n")
#25...hasattr(object, name)...This function is also similar to the getattr() function instead it checks if the object contains the specified attribute or not. It returns a boolean value.
class car:
    color='white'
    capacity="30ltr"
c="car"
print(hasattr(c,'color'))
print(hasattr(c,'price'))
print(hasattr(c,'capacity'))
print(" 25 **********\n")

#26..hash(object)...hash(object)..In Python, everything is an object, numbers, strings, etc. all are object. The hashable objects are mapped with an integer value in Python. The function hash() returns us the hash of the specified object.
print(hash(12345))
print(hash("abc"))
print((3.6))
print((True))
print(" 26 **********\n")

#27...help()..Python has an inbuilt help system which you can use to see details about any module, method, object, keyword, symbol, etc.
# print(help(print))
#help(str)

# print(help(type))
# print(5)

print(" 27 **********\n")

#28..input()..
x=input("enter your number:")
print(type(x))
print(" 28 **********\n")
#29...hex()..The hex() function converts or returns the string representation of the hexadecimal value of the number. It takes only integer number as an argument.
print(hex(128))
print(hex(139))
print(hex(70))
print(hex(12))
print(" 29 **********\n")

#30...int()..returns or converts a compatible number or string into an integers.
print(int(12.3))
print(int("1145"))
print(" 30 **********\n")

#31..isinstance(object, classinfo).The function isinstance() checks whether the object argument is an instance of the class given in the second argument, it returns a boolean value.
isinstance("shahid Hussain Khan Zeerak",str)
isinstance(23,int)
isinstance(3.7,float)

class car():
    color='black'
color=car
print(isinstance(color,car))
print(" 31 **********\n")

#32..issubclass(class, classinfo)...This function checks whether a class (first argument) is a subclass of the class in second argument.
class A:
    pass
class B(A):
    pass
print(issubclass(A,B))
print(issubclass(B,A))
print(" 32 **********\n")
#33..iter(object)...The inbuilt function iter() is used to return an iterator object that we can use to iterate over the elements in the object. This is mostly used in a for loop.
num=[1,2,3,4,5]
for num in iter(num):
    print(num,end=",")

print(" 33 **********\n")



