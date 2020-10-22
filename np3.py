'''initialization of different types of arrays
'''
import numpy as np
#all zero matrix 
#zeros(3)3x3 / zeros((2matrix,3row,2col))
print(np.zeros((1,2,3))) 
print("################")
print(np.zeros((1,2,2,1,1)))
print("################")
#all ones array
print(np.ones((2,3,1,2),dtype='int16'))
#using full shape of array and then value for array
print("################")
print(np.full((3,2),55))
print("################")
a = np.array([[1,2,355,66],[65,43,76,55]])
#when yoy wnat an array to be of certain shape of array
print(np.full_like(a,77))
print("################")

#array of random decimal numbers 
print(np.random.rand(3,2,1))
print("################")
#random araays of certain array shape
print(np.random.random_sample(a.shape))
print("################")

#random Integer values
## randint(startval, endval , size(shape of array))
print(np.random.randint(7,size=3))