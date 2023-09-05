# write a numpy program to create an array with the value 1,7,13,105 and determine the size of the memory occupied by the array

import numpy as np


arr = np.array([1, 7, 13, 105], dtype=np.int32)


memory_size = arr.nbytes

# Print the array and its memory size
print("Array:", arr)
print("Memory size:", memory_size, "bytes")
