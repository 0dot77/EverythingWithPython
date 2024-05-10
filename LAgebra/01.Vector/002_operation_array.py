import numpy as np

aList = np.array([4,5,6])
bList = np.array([10,20,30])

result = aList + bList
print(result)

print("#########")

v = np.array([[4,5,6]]) # 행벡터
w = np.array([[10,20,30]]).T #열벡터

print(v+w)