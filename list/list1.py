# if we make chages to one list it replicates in other list
list1 = [1,2,3,5]
list2 = list1           #list1 and list2 are pointing to the same values
list3 = list1[:]        #list 3 will not get modified because it is a new list
print("Before : ",list1," ",list2," ",list3)
list1[1] = 99
print("After : ",list1," ",list2," ",list3," <------ Look there are no change in list3 as list2")



print("================")
# Slicing the lsit

print(list1[1:3])
print(list1[:len(list1)])
print(list1[0:])
print(list1[:])