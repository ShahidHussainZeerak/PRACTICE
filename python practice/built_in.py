#51..sorted(iterable) The sorted() function sorts the given iterable and returns a list of all the elements in ascending order by default.
print(sorted([1,4,3,5,9,8,2,6,0]))
print(sorted({2,9,8,7,1,6,6}))
print(sorted(['z','x','a','c','d']))
print(" 51 **********\n")
#52..str(object).. The str() function is used to convert an object into a string. str is the built-in class for strings.
print(str(13))
print(str(100))
print(str("hello"))
print(" 52 **********\n")
#53..sum(iterable).. The function sum() is also self-explanatory. It takes an iterable collection or sequence as an argument and returns the sum of all the elements.
print(sum((40,43,49,50)))
print(sum([89,90,96,80]))
print(" 53 **********\n")

#54..tuple([iterable]).. Tuple is an immutable sequence of elements. The tuple() function is used to create or convert other sequences like lists, strings, etc into tuples.
l=tuple([1,2,3,4,5,6,7])
s=tuple({1,2,3,4,5,6,7})
d=tuple({'name':'shahid hussain','age':21})
print(l)
print(s)
print(d)
print(" 54**********\n")
#55..type() The type() function returns the type of the Python objects or the class of the Python objects.
print(type("Shahid"))
print(type(13))
print(type(3.6))
print(" 55 **********\n")
#56..vars([object]) The vars() function returns the __dict__ attribute of a module, class, instance, or any Python object. If arguments are not passed then it is similar to the locals() function.
print(vars(tuple))
print("\n")
print(vars(str))
print(" 56 **********\n")



