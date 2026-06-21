#Tuple : ordered, immutable, allows duplicate elements

myTuple = ("Max", 28, "Boston") #myTuple = "Max", 28, "Boston"
print(myTuple)
tuple2 = tuple(["Max", 28, "Boston"])
print(type(tuple2))

item = myTuple[1]
print(item)
item = myTuple[-3]
print(item)

#Cannot edit a tuple => myTuple[0] = "tim" wrong
for i in myTuple:
    print(i)

if "Max" in myTuple:
    print("yes")
else:
    print("No")


my_tuple = ('a','p','p','l','e')

print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('p'))

myList = list(my_tuple)
print(myList)

my_tuple2 = tuple(myList)
print(my_tuple2)


a = (1,2,3,4,5,6,7,8,9,10)

b = a[2:5] # similarly you can use it like list for step and start and stop index
print(b)


my_tuple = "Max",28,"Boston"
name,age,city = my_tuple
print(name)
print(age)

i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)

#Tuple is immutable we can make some internal optimization

import sys

List1 = [0,1,2,"hello",True]
tuple1 = (0,1,2,"hello",True)

print(sys.getsizeof(List1),"bytes")
print(sys.getsizeof(tuple1))

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number = 1000000))
print(timeit.timeit(stmt = "(0,1,2,3,4,5)", number = 1000000))