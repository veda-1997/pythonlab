list1 = [7, 5, 9]
list2 = [7, 5, 9]
list3 = list1
print(list1 == list2) # same content
print(list1 is list2) # same object?
print(list1 is list3) # same object?
print(id(list1), id(list2), id(list3))
#output
#True
#False
#True
#1811523301248 1811523292224 1811523301248

