#Tuple
t=(1,2,3,4,5)
print(t)
#accessing element of tuple
print(t[2:4])
#crate one element if tuple 
single_element=("hi",)
print(single_element)
tuple1=t+single_element
print(tuple1)
tuple2=t*3
print(tuple2)
#sets
e={1,2,3,4}
r={7,5,6,4}
print(e)
print(e&r)# Intersection
print(e|r)#  Union
print(e^r)# Symmetric Difference
print(e-r)# Difference
# converting list into tuple and sets
list2=[1,2,3,4,5,6,7]
print(set(list2))
print(tuple(list2))
