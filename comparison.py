# write a numpy program to create an element-wise comparision(greate,greate equal,less,less equal) of two given array
import numpy as np

arr1=np.array([1,3,6,7,9,5])
arr2=np.array([5,9,6,86,6,8])

greater=np.greater(arr1,arr2)
greater_equals=np.greater_equal(arr1,arr2)
less=np.less(arr2,arr2)
Less_equals=np.less_equal(arr2,arr2)

print("greater  is ",greater)
print("greater equals is ",greater_equals)
print("less is ",less)
print("less equals is ",Less_equals)