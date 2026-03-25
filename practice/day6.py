# list 
list1=[1,2,3,4,5,6,7]
list2=["hi","hello","bey"]
list3=[1,"santhu",True]
print(list1)
print(list2)
print(list3)
#append used for adding the elements in the end of the list...
list1.append(8)
list2.append("bye")
list3.append(2)
#insert this used for insert the element in any where>>
list1.insert(2,"gp")
print(list1)
print(list2)
print(list3)#extend this used for adding two lists.
list1.extend(list2)
print(list1)#remove this used for removing the element >>.
list2.remove("hi")
print(list2)#pop > pop the element in list
list3.pop(2)
print(list3)
list4=[5,6,7,2,3,1,0,9,4]
print(len(list4))# this len function used for check the how many element in the list
print(max(list4))#max number in the list
print(min(list4))#min number in the list
print(sum(list4))#sum of the list
#Accessing List Elements
print(list4[0:5])
print(list4[5:])
print(list4[:6])
list4.sort()#sort the element in incersing oder 
print(list4)
list4.reverse()
print(list4)