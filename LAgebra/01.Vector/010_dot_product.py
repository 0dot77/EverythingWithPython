import numpy as np;

v = np.array([1,2,3,4])
w = np.array([5,6,7,8])
print(np.dot(v,w)) # 벡터 내적

s = -1
print(np.dot(s*v, w))