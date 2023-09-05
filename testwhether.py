# write a numpy program to test whether none of the elements of a given array are zero
import numpy as np

arr= np.array([1,0,3,4,5,])

result=np.all(arr!=0)

print("none of the elements are zero : ",result)