#comparing list values and comparing lists using "==" and "is"
list1 = [1,2,3,4]
list2 = [1,2,3,4]
list3 = list2

print("List1== List2 ? -->", list1==list2 )
print("List1 is List2 ? -->", list1 is list2 )
print("List3== List2 ? -->", list3==list2 )
print("List3 is List2 ? -->", list3==list2 )

#concatination of the list

list4 = list1+list2+list3
print("list4 : ",list4)

list4 = list4 + [99]
print("New list4 : ",list4)
