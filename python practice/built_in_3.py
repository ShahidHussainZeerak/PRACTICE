#34...len()..The len() function takes an argument which can be either a sequence(string, list, tuple, etc) or a collection(dictionary, set, etc) and returns the number of elements present inside them.
print(len([1,2,3,4,5,6,7,8,9]))
print(len((1,2,3,4)))
print(len("Shahid Hussain"))
print(len({1,2,3,4,5,6,7,8,9}))
print(" 34 **********\n")
print(sum([78,75,73,76,76,42,45]))
#35...39. list() The list() function returns or creates a new list. It takes iterable like sets, tuples, etc. and converts them into the list.
t=list((1,2,3,4))
print(t)
s=list({1,2,3,4,5,6,7,6})
print(s)
d={'name':'shahid','age':21}
print(list(d))
print(" 35 **********\n")

#36.. locals() The locals() in-built method is similar to the globals() method which we saw earlier. It returns a dictionary of the current local symbol table.
print(locals())
print(" 36 **********\n")

#37..max(iterable)..The max() function is self-explanatory, it takes an iterable container or sequence as an argument and returns the maximum value from the list.
print(max([5,6,7,8,1,2,3,-100,-30]))
print(max({2,3,4,-5,2}))
print(" 37 **********\n")

#38...min(iterable) The min() function is also similar to the max() functions. It returns the minimum value from a group of items in an iterable.
print(min([5,6,7,8,1,2,3,-100,-30]))
print(min({2,3,4,-5,2}))
print(" 38 **********\n")
#39..next()The next() function is used to get the next item from the iterator object. Every time we call the next() method the iterator points to the next element.
lst=iter([2,3,5,6,7,8])
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
#print(next(lst))
print(" 39 **********\n")
#40..oct(x).. The oct() function converts or returns an octal representation of a number.
print(oct(15))
print(oct(-15))
print(oct(28))
print(oct(20))
print(" 40 **********\n")

#41. object().. The object() method does not take any arguments and it returns a featureless object.
obj=object()
print(type(obj))
#print(dir(obj))
print(" 41 **********\n")
#42. ord(c).. The ord() method takes a Unicode character as an argument and returns an integer representation of the character. It is the opposite of the chr() function.
print(ord('7'))
print(ord("S"))
print(ord("h"))
print(ord("z"))
print(" 42 **********\n")
#43..pow(base, exp) The pow() function is used for calculating the mathematical power of a number. This function returns the base to the power of exp.
print(pow(2,16))
print(pow(3,16))
print(pow(4,16))
print(pow(3.6,16))
print(" 43 **********\n")
#44..print()..The print() function prints the objects to the text stream file.
print("shahid hussain khan zeerak Al-satar")
print(" 44 **********\n")
#45.range(start, stop, step) The range() function is used to generate a sequence of numbers from a starting range to the stop number. It is useful to iterate over a range of elements.
for i in range(0,50,2):
    print(i,end=",")
print(" 45 **********\n")
#46..4. repr() The repr() function is used to return a printable version of the Python objects.
print(repr("hello"))
print(repr(123))
print(repr([1,2,3,4,5]))
print(" 46 **********\n")
#47.... reversed(seq) The reversed() function takes a sequence as an argument and returns a reverse iterator to the sequence. It is used when we want to iterate the elements backward.
lst=[1,2,3,4,5,6]
for i in reversed(lst):
    print(i)
l=["a",'b','c','d','e']
for i in reversed(l):
    print(i)
print(" 47 **********\n")
#48..round(number,[digits])The round() function round offs a number to specified n-digits. If the digits are not specified then it round offs to a natural number.
print(round(3.67))
print(round(4.1198))
print(round(0.999))
print(round(-1.3455))
print(" 48 **********\n")

#49...set[iterable]..The set() function takes an iterable as an argument and returns a set object of that iterable.
set={2,2,3,4,4,5}
print(set)
s1={1,66,7,8,9,9,8}
print(s1)
print(" 49 **********\n")
#50..setattr(object, name, value)..Now the setattr() function is used to set a value of an attribute. We can set a new attribute or update an attribute if the class allows us to modify.
class student:
    pass
s1=student()
setattr(s1,'name','Ali')
print(s1.name)
print(" 50 **********\n")
