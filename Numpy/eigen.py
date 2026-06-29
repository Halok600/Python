import numpy as np

a = np.array([[1,2],[3,4]])
eigenValues, eigenVectors = np.linalg.eig(a)
print(f"Eigen Values : {eigenValues}\n Eigen Vector : {eigenVectors}") # coulum vectro

#e_vec * e_val = A dot e_vec
print("New")
b = eigenVectors*eigenValues
c = a@eigenVectors
print(b)
print(c)
print(np.allclose(b,c)) # for comparison

print('`'*25)
print("SOLVING LINEAR EQUATION")
#Nit best way
A = np.array([[1,1],[1.5,4.0]])
b = np.array([2200,5050])
A_inv = np.linalg.inv(A)
print(A_inv@b)

x = np.linalg.solve(A,b)
print(x)