# 4 ascii ()
print(ascii('89'))
print(ascii("hello"))
print(ascii("8.9"))

#5 bin() it will converty integer into its binary representaion in string format.
print(bin(8))
print(bin(-8))
print(" 5 ***************") 

#6 bool() it will return true or false to check weather the is  element true or false.
print(bool([1,2,3,4]))
print(bool(False)) 
print(bool([0,0,1]))
print(" 6 ***************")

# 7 breakpoints(args,kws)
# msg="hello"
# breakpoint()
print(" 7 ***************")
#8 bytesarray([source,[encoding[error]]])...It returns a mutable version of bytes array of integers between 0-256.
print(bytearray(4))
print(bytearray(8))
print(bytearray("hi","utf-8"))
print(bytearray([4,5,6]))
print(" 8 ***************")
# 9 bytes()...The byte() function is similar to the bytearray() function. The only difference is that bytes() returns an immutable object. 
print(bytes(5))
print(bytes("abc","utf-16"))
print(bytes((1,2,3,4)))
print(" 9 ***************")

# 10 callable(object)...The callable function tells us whether an object is callable or not. It returns True when the argument passed is callable otherwise it returns False.
print(callable(3))
print(callable(input)) # All user  define and built in function are callable..if funactin callable it will return true otherwise false.
print(callable([1,2,3,4]))
print(" 10 ***************")
#11 chr()..The function chr() is an inverse of ord() function. It takes unicode code point as an argument and returns the string representation of the character.
print(chr(120))
print(chr(60))
print(chr(30))
print(" 11 ***************")
#12..claasmethod()The @classmethod() is a decorator that is used to create class methods that will be passed on all the objects just like self is passed.
class person:
    def display_age(cls):
        print("person's age is 42")
person.display_age(42)
print(" 12 ***************")
# 13..compile(source,filename,mood)..The compile() functions compiles the source code into an executable object. The object can be executed by using exec() or eval() functions.
exec(compile('num1=20; num2=30;print(num1+num2);','', 'exec'))
print(" 13 ***************")

# 14..complex([real[, imag]])..it return or convert the  number into a complex number . The first argument is the real part of the complex number and the second argument(optional) is the imaginary part.
print(complex(3,2))
print(complex(6-3))
print(complex(3+2j))
print(" 14 ***************")
# 15 delattr(object, name)..this function will delete the of in object.It takes two arguments, the object from which you want to delete and the attribute name that you want to delete.
# class car:
#     color="blue"
# c= car()
# print(c.color)
# delattr(c,'color')
# print(c.color)
# print(" 15 ***************")

#16.. dict()..this function  will return or create a new dictionary.
numbers1=dict(a=1,b=2,c=3,d=4)
numbers2=dict([('x',10),('y',11),('z',12)])
print(numbers1)
print(numbers2)
print("16..++++++++++++++++++++++++")

# 17.. dir(object)...The dir() object returns a list of all the names of the current local scope if no argument is passed.
vars1=10
vars2='hello world' 
print(dir())
#When we pass an object as an argument then it will return a list of all the valid attribute names of that object.
# let see atrributes of str.
print(dir(str))
print("17..*******************************")
#18...divmod(a,b)..The function divmod() takes two integer or float numbers as arguments and then returns a tuple whose first element is the quotient and second element is remainder.
print(divmod(2,4))
print(divmod(6,8))
print(divmod(9,11.4))
print("18..*******************************")








