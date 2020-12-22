import numpy as np
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) #this will create a 2D array
print(arr1.ndim) #this will show the dimension of the array created
print(arr1)#this will print the array created
print(arr1[1, 2]) #this will print the 3rd element of 2nd dimension
arr3d = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]],[[21,22,23,24,25],[26,27,28,29,30]]]) #this will create a array
print(arr3d)
print(arr3d[2,1,4])#this will print the 5th element of 2nd array of 3rd array
#array slicing
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[1:3])
print(arr[3:])
print(arr[:5])
print(arr[2::2])
print(arr1[0:2,0:5:2])
print("this is from 3d array ", arr3d[1,1,1:4])
print(arr.dtype)
#data types
arrdatatype = np.array([1.2,3,4.4,56], dtype='i')
print(arrdatatype.dtype)
print(arrdatatype)
arrdatatype = np.array([1.2,3,4.4,56,0], dtype='f')
print(arrdatatype)
arrdatatype1 = arrdatatype.astype('bool')
print(arrdatatype1)
print(arrdatatype1.dtype)
print(arr3d.shape)
#array shape
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2_1 = arr2.reshape(6,2)
print(arr2_1)
arr2_2 = arr2.reshape(3,2,2)
print(arr2_2)
print(arr2_2.base)
print(arr1)
for x in arr1:
    print(x)
    for y in x:
        print(y)
for x in np.nditer(arr1):
    print(x**2)
for x,y in np.ndenumerate(arr):
    print(x,y)
print(np.array_split(arr,6))