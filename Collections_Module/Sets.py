#Sets : unordered, mutable, no duplicates
mySet = {1, 2, 3, 4, 4}
print(mySet)
myset1 = set("hello")
print(myset1)

setx = set() # empty set because setx = {} -> will be an empty dictonary

setx.add(1)
setx.add(2)
setx.add(3)
setx.add(4)

setx.remove(3)
print(setx)

setx.discard(5)

setx.clear()

print(mySet.pop())
print(mySet)
for i in mySet:
    print(i)

if 2 in mySet:
    print("Yes")
else:
    print("No")


#Union And Intersection

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens)
print(u)

inter = odds.intersection(primes)
print(inter)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setB.difference(setA) #Alwyas return a new Set
print(diff)

diff2 = setB.symmetric_difference(setA) #REturn new sets
print(diff2)

setA.update(setB)
print(setA)
setA.intersection_update(setB)
print(setA)
setB.difference_update(setA)
print(setB)
#Subset and SuperSet
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8, 9}
print(setA.issubset(setB)) #False
print(setB.issubset(setA)) # True

print(setA.issuperset(setB)) #True
print(setB.issuperset(setA))

print(setA.isdisjoint(setC))


#Copying

setB = setA
print(setB) #only copy reference

setB.add(7)
print(setB)
print(setA)

setB = setA.copy() #setB = set(setA)
setB.add(8)
print(setB)
print(setA)

#FrozenSet -> imutable version of Set

a = frozenset([1, 2, 3, 4])
print(a)
# a.add(2) -> error
