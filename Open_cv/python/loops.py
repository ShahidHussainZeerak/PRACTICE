list=[[1,2,3,4],[5,6,7,8],"a","b",['c','d','e']]
for item in list:
    for i in item:
        print(i)

# While loop.
print("enter a number :")
num=int(input())
while num>4:
    print("number is greater than 4")
    num=int(input())
    if num==10:
        break
    elif num==9:
        continue
    

