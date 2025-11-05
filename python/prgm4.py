n=int(input("Total number of integers:"))
list1=[]
for i in range(n):
    a=int(input("Enter an integer:"))
    if a<100:
        list1.append(a)
    else:
        list1.append("Over")
print(list1)
