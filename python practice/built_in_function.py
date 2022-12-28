# 1 Abs() will make negative number to positive and positive remain unchange.
print(abs(10)) #  ouput would be 10
print(abs(-10))# output would be 10 b/c it change the negative number to positive .
print(abs(-10)-10) # output will be 0 because abs(-10) =+10-10=0
print(abs(-7.9))# out put would be 7.9
print("1 ******************")
#2 : all() will check weather the number or element is true or false.it take the iterable(list,tuple,dict,set) container and return true or false
print(all([1,2,3,4,'shahid']))
print(all((0,0,False)))
print(all({"name":"shahid"}))
print(all([1,2,2,3,4]))
print(all([])) # result will be true .
print(" 2 ***************")

#3 any() it will return true if any of the elements of a given  iterable (list,dict,tuple,set) are true else it will return false
print(any([1,2,3,4,'shahid']))
print(any((0,0,False,1)))
print(any({"name":"shahid"}))
print(any([1,2,2,3,4]))
#print(any([])) #output will be false b/c the iterable is empty.
print(" 3 ***************")
# 4 Ascii()..

print(ascii(2020))
print(" 4 ***************")

#5 bin() it will converty integer into its binary representaion in string format.
print(bin(8))
print(bin(-8))
print(" 5 ***************")

#6 bool() it will return true or false to check weather the is  element true or false.
print(bool([1,2,3,4]))
print(bool('false')) 
print([0,0,1])
print(" 6 ***************")

#7 breakpoints(args,kws)
msg="hello"
print(breakpoint(msg))
print(" 7 ***************")

