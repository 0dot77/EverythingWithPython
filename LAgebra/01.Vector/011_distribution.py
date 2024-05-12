import numpy as np;

a = np.array([0,1,2])
b = np.array([3,5,8])
c = np.array([13,21,34])

# 내적 분배 법칙
res1 = np.dot(a, b+c)
res2 = np.dot(a,b) + np.dot(a,c)

print(res1, res2)