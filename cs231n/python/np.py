import numpy as np

a = np.array([1,2,3]) # rank 1 array
print(type(a))
print(a.shape)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[0,2])

a = np.zeros((2,3,4))
print(a)

b = np.ones((1,2))
print(b)

c = np.full((2,2),7)
print(c)

d = np.eye(2)
print(d)

e = np.random.random((2,2))
print(e)
