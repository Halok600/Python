import numpy as np
a = np.array([[1,2,6],[3,4,5]])
print(a)
print(a.shape)
print(a[0,2]) # also can use a[0][2]

print(a[:,0])
print(a[0,:])

print(f"Transpose of array : {a.T}")
b = np.array([[1,2],[3,4]])
print(f"Inverse of b {np.linalg.inv(b)}")

print(f"Determinant of b {np.linalg.det(b)}")
c = np.diag(b)
print(f"Diagnal matrix of b {np.diag(c)}") # overloaded diag
#Slicing
print("Slicing")
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
b = a[0,1]
print(b)
c = a[0,1:3]
print(f"this is the {c}")
d = a[:,1]
print(d)


a = np.array([[1,2],[3,4],[5,6]])
print(f"new array : {a}")
bool_idx = a>2
print(bool_idx)
print(a[bool_idx]) #One step print(a[a>2])
b = np.where(a>2,a,-1)
print(b)


a = np.array([10,19,30,41,50,61])
print(a)
b = [1,3,5]
print(a[b]) #fancy indexing


print(a)


even = np.argwhere(a%2==0).flatten()
print(a[even])


print("Reshaping Array")

a = np.arange(1,7)
print(a)
print(a.shape)
b = a.reshape((2,3))
print(b)
print(b.shape)
b = a.reshape((3,2))
print(b)


b = a[np.newaxis, : ]
print(b)
print(b.shape)
b = a[:,np.newaxis ]
print(b)
print(b.shape)