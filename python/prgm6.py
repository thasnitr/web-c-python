list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
if len(list1)==len(list2):
    print("a.The list have the same length.")
else:
    print("a.The list have different lengths.")
print(f"b.Sum of list1:{sum(list1)} & Sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print("The lists sum to the same value.")
else:
    print("The lists do not sum to the same value")
com_values=set(list1)&set(list2)
if com_values:
    print(f"c.Common values in both lists:{com_values}")
else:
    print("c.There are no common values in both lists.")
