#57...enumerate(iterable, start=0)..The function returns us an enumerate object which is used in loops to iterate over iterable objects. It is useful when we want to have a counter to calculate something.
# names=['shahid','hussain','khan','zeerak']
# for pos,name in names:
#     print(f"{pos} is....{name} ")
#     pos+=1

print(" 57 **********\n")
#58...eval()...The eval() function evaluates a Python expression that is passed in a string. It parses into a Python expression and then the function evaluates it.
var=eval(input("enter your number:"))
print(var,type(var))

print(eval('10<20'))
print(" 58 **********\n")
#59..filter()..The filter function is used to filter out the data. It does that by iterating on the second iterable argument and the first argument is a function that decides how we will filter the elements. This is mostly used with lambda expressions.
num=[1,2,3,6,4,5,7,9,8]
# list=filter(lambda num%2==0,num)
# print(list)

print(list(filter(lambda num:num%2==0,num))) # useing lambda function.

# filter function with out argument..and to get only valid names not a spacce.
name=['shahid','hussain','','khan', '','zeerak']
print(list(filter(name)))
print(" 59 **********\n")