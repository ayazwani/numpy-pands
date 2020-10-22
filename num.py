import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
print("*************************") 
print(a.ndim)
print("*************************")

#making an matrix with dtype = int16
b = np.array([[1,2,3],[11,33,55],
	[88,99,66],[45,55,77]],dtype='int16')

#Dimensions of array
print(b,b.ndim)
print("*************************")
#getting shape of the array 
print (b.shape)
print("*************************")
#getting type 
print(b.dtype)
print("*************************")
#getting size of elements in numpy array
print(b.itemsize)
print(a.itemsize)
print("*************************")
#getting number of elements in (a,b) array
print(a.size,b.size)
#getting number of bytes
print("*************************")
print(a.nbytes,b.nbytes)
print("*************************")
c = np.array([1.0,2.0,3.0])
print(c.nbytes)

