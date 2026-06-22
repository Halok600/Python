#lambda arguments : expressions
add10 = lambda x: x + 10
print(add10(5))
#same as below
def add_func(x):
    return x+10

mult = lambda x,y : x*y

print(mult(2,3))


points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)
points2D_new_sorted = sorted(points2D, key = lambda x : x[1]) #Also can use sorted(points2D, key = sorted_by_y)
print(points2D_new_sorted) 
def sort_by_y(x):
    return x[1]

points2D_sorted_sum = sorted(points2D,key = lambda x: x[0]+x[1])
print(points2D_sorted_sum)

#map(func,seq)
print("MAP FUNCTION")
a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))
#can also use list comprehension
c = [x*2 for x in a]
print(c)

#filter(func,seq)
print("Filter Function")
a = [1,2,3,4,5,6]

b = filter(lambda x: x%2 == 0, a)
print(list(b))

c = [x for x in a if x%2== 1]
print(c)

#reduce(func,seq)
from functools import reduce
print("REDUCE FUNC")
a = [1,2,3,4,5,6]
prod = reduce(lambda x,y: x*y,a)
print(prod)