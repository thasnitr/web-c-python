def modifyList(lst):
    lst.append(10)
    print("Inside function:",lst)
numbers=[1,2,3]
modifyList(numbers)
print("Outside function:",numbers)
