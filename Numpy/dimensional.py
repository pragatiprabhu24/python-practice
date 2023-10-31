import numpy as np 
a = np.array(24) # 0 dimension
b = np.array([1,2,3,4,5]) # 1 dimension
c = np.array([[2,3,4], [2,3,4]]) # 2 dimension
d = np.array([[[2,3,4], [4,3,6]], [[2,4,3], [6,7,8]]]) # 3 dimension

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Points to remember

# Dimensions array also known as nested array

# nested array means array have arrays as their elements

# ndim attribute used to check number of Dimensions

