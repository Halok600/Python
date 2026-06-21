# LISTS : ordered, mutable  allows duplicate elements

myList = ["banana","cherry","Apple"]
print(myList)

mylist2 = [5,2,1,32]
item = myList[-1]
print(item)
print(mylist2)

for i in myList:
    print(i)

if "apple" in mylist2:
    print("ues")
else:
    print("no")
print(myList)
myList.append("Lemon")
print(myList)

myList.insert(1,"blueberry")
print(myList)
x  =myList.pop()
print(x)

item = myList.remove("cherry")
print(myList)


print(myList)

myList.sort() #Inplace
new_list = sorted(mylist2)
print(new_list)
print(myList)

newList = [0]*5
print(newList)

mylist2 = mylist2+new_list
print(mylist2)

latest = [1,2,3,4,5,6,7,8,9]
a = latest[::-1]
print(a)

list_org = ["banana","cherry","apple"]
list_cpy = list_org #both list refer to the same list in the memory
list_cpy.append("lemon")
print(list_cpy)
print(list_org)
list_cpy1 = list_org.copy() # list(list_org) and also list_org[:]
list_cpy1.append("lemon")
print(list_cpy1)
print(list_org)



#List comprehension

a = [1,2,3,4,5,6]
b = [i*i for i in a]
print(a)
print(b)