import numpy as np
print(np.__version__)
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(type(arr))
arr1 = np.array((1,2,3,4,5,6))
print(arr1)
print(type(arr1))
#2D Array
arr1 = np.array([[1,2,3,4,5,6],[7,8,9,5,6,7]])
print(arr1)
#3D Array
arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
d = np.array(42)
#checking array dimension
print(d.ndim)
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
#higher dimensional arrays
e = np.array([1,2,3,4,5], ndmin = 9)
print(e)
print(e.ndim)
print(arr)
print(arr[2])

