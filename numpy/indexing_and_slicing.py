import numpy as np

list1 = [10,20,30,40,50]
arr = np.array(list1) 
print(arr) 

print(arr[0])

print(arr[1:5])

list2 = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(list2)
print(arr)
print(arr[2,0])

print(arr[:1,:1])
print(arr[:2,:3])

