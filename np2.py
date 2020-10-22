"""acessing elements/changing/specific elements/columns
"""
import numpy as np
a = np.array([[1,2,3,4,59,78],[4,5,6,7,89,90]],dtype='int')
print(a)
print("^^^^^^^^^^^^^^^^^^^^")
#get shape
print(a.shape)

print("^^^^^^^^^^^^^^^^^^^^")
#get specific elements  [ri , ci]
print(a[0,5])
print("^^^^^^^^^^^^^^^^^^^^")
#using negative notation for getting second last element from the ap array
print(a[1,-2])
print("^^^^^^^^^^^^^^^^^^^^")
#getting specfic row and all columns
print(a[1,:])
print("^^^^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^^^^^^^^")
#getting specific column and all rows
print(a[:,4])
print("^^^^^^^^^^^^^^^^^^^^")
#using indexing [start_index : end_index : step ]
print(a[0,1:6:2])
#using negative indexing 
print("^^^^^^^^^^^^^^^^^^^^")
print(a[1,1:-1:2])
print("^^^^^^^^^^^^^^^^^^^^")
#changing elements
a[1,3]=100
print(a)
print("^^^^^^^^^^^^^^^^^^^^")
a[:,3]=[555,77]
print(a)
print("^^^^^^^^^^^^^^^^^^^^")
#numpy 3d example 
threeD = np.array([[[1,2,3],[4,5,6]],[[66,77,88],[99,88,55]]],dtype='int16')
print(threeD)
print("^^^^^^^^^^^^^^^^^^^^")
#accessing 3d array elements [matrix_number,row,column]	matrix1=[[1,2,3][4,5,6]] likewise [[66,77,88],[99,88,55]] is second 
print(threeD[0,0])
print("===============")
print(threeD[0,1])
print("===============")
print(threeD[1,0,0])
print("===============")
print(threeD[1,1,2])
print("===============")
print(threeD[:,0,:])
print("===============")
#replacing elements 
threeD[:,1,:]=[[7,8,6],[6,33,22]]
print(threeD)