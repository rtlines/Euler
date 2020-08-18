import numpy as np
arr=np.array([1,2,3,4])
print(arr)
brr=np.copy(arr)
print (brr)
arr[3]=5
print (brr)
