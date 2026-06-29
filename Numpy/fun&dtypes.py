import numpy as np
a = np.array([[7,8,9,10,11,12,13],[17,18,19,20,21,22,23]])
print(a)
print(a.sum(axis=0))
print(a.mean(axis=0))
print(a.var(axis=0))
print(a.mean(axis=1))
print(a.var(axis=1))
print(a.std(axis=1))
#also can use like this
print(np.std(a,axis = None))

print('>'*9)
print(f"Datatypes")

a = np.array([1,3,4],dtype = np.int64)
print(a.dtype)
a = np.array([1,3,4],dtype = np.int32)
print(a.dtype)
a = np.array([1,3,4],dtype = np.float16)
print(a.dtype)
a = np.array([1,3,4],dtype = np.float32)
print(a.dtype)


b = a
b[0] = 42
print(a,b)
b = a.copy()
b[0] = 32
print(a,b)

print('`'*20)
print("Generating arrays")
print('`'*20)
a = np.zeros((3,2))
print(a)
b = np.ones((4,2))
print(b)
print(np.arange(3,10))
print(np.eye(4))
c = np.full((3,3), 5)
print(c)
d = np.linspace(0,10,4)
print(d)


print('`'*20)
print("Random numbers")
print('`'*20)

a = np.random.random((3,2))#mean = 0, var = 1
print(a)
a = np.random.randn(10) #normal/gaussian
print(a)
a= np.random.randint(-100,100, size = (3,3))
print(a)
a = np.random.choice(10,size =(2,2))
print(a)
a = np.random.choice([4,2,3,9,6],size = 9)
print(a)