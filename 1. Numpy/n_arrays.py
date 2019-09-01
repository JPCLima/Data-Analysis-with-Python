# Importing numpy
import numpy as np
import matplotlib.pyplot as plt

# Creating array 1D
data1 = [1, 2, 3.5, 4, 0]
arr1 = np.array(data1)
shape_arr1 = np.shape(arr1)

# Array 2D
data2 = [6, 7, 8.5, 9, 0]
arr2 = [data1,data2]
shape_arr2 = np.shape(arr2)

# Arrays
# Array zeros
    zeros_arr = np.zeros(5)
# Array ones
ones_arr = np.ones(5)


# Higher dimensional Array- pass a tuple for the shape
# Zeros
zeros_matrix = np.zeros((5,5))
# Ones
ones_matrix = np.ones((5,5))


# Arange - (start, stop, step, dtype=None)
n_arange = np.arange(1,11, 2.5999, dtype=int)

# Numeric string - np.string_
# convert a string to int - astype(np.int)
n_arange = np.array(["1", "2", "3", "4", "5"])
conv_init = n_arange.astype((np.int))

# Operations between Arrays and Scalars
arr_a = np.array([1, 2 , 3, 4, 5])
Sum = arr_a + arr_a
dif = arr_a - arr_a
div = 1/arr_a
mult = arr_a * arr_a


# Index and Slicing
arr_b = np.arange(0, 10)
arr_b[0] = 99
arr_b[5::] = 9999
print(arr_b)
# Higher Dimensional arrays
#2D
arr_c = np.ones((5,5))
arr_c[0:5:2] = 99
arr_c[2][2] = 0
# 3D
arr_d = np.ones((5,5,5))
arr_d[0:5:2] = 99
arr_d[2][2] = 0
arr_d[0:5][2][2] = 77
arr_d[1][2][2] = 77
arr_d[2][2][2] = 77
arr_d[3][2][2] = 77
arr_d[4][2][2] = 77

# Boolean Indexing 
data = np.random.randn(7,4)
data[data <0] = 99


# Fancy Index
arr_e = np.empty((8,4))
for i in range(8):
    arr_e[i] = i
arr_e = arr_e[[4, 3, 0, 6]]

# Reshaping 
arr_e = np.arange(1,41).reshape((4,10))


# Transposing arrays and Swaping axes
arr_f = np.arange(10,101,10).reshape(5,2)
Tarr_f = np.transpose(arr_f)

# Inner matriz product
arr_g = np.random.randn(3)
dot_arr = np.dot(arr_g.T, arr_g)
print(arr_g)

# Mathematical and Statistical Methods
arr_h = np.random.randn(10).reshape(5,2)
# mean 
mean = np.mean(arr_h)
mean_axis1 = arr_h.mean() 
# Sum
Sum = arr_h.sum()












