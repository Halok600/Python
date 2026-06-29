import numpy as np
print(np.__version__)

a = np.array([1,2,3])
print(a)
print(a.shape)
print(a.dtype)

print(a.ndim)
print(a.size)
print(a.itemsize)
print("First Element")
print(a[0])

a[0]= 10
print(a[0])

b = a * np.array([2,0,2])
print(b)

#diff b/w ython list and array

print("Difference between python list and array")

l = [1,2,3]
a = np.array([1,2,3])
print(a)
print(l)
l.append(4) #appending an element or this also works l = l + [4]
a = a + np.array([4]) #broadcasting
print(a)

a = np.array([1,2,3])
l = l*2
print(l)

a = a *2
print(a)
a = np.array([1,2,3])

a = np.sqrt(a)

print(a)

# DOT Product 
print("DOT product")

l1 = [1,2,3]
l2 = [4,5,6]

dot = 0
for i in range(len(l1)):
    dot += l1[i]*l2[i]

print(f"List dot product {dot}")

a = np.array(l1)
b = np.array(l2)
dot = np.dot(a,b)
print(f"Dot product with array {dot}")

sum1 = a * b
dot = (a*b).sum()
print(dot)

dot = a@b # a@b is dot product
print(dot)

#Compare
print("Comparison b/w list and array")
from timeit import default_timer as timer
a = np.random.randn(1000)
b = np.random.randn(1000)
A = list(a)
B = list(b)

T = 1000
def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot

def dot2():
    return np.dot(a,b)


start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end-start

print(f"List timer is : {t1}")
print(f"Array timer is : {t2}")
print(f"Ratio is {t1/t2}")