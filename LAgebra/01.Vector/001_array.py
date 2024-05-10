import numpy as np

asList = [1,2,3]
asArray = np.array([1,2,3])
rowVec = np.array([[1,2,3]])
colVec = np.array([[1],[2],[3]])

print(f'asList = {np.shape(asList)}')
print(f'asArray = {np.shape(asArray)}')
print(f'rowVec = {np.shape(rowVec)}')
print(f'colVec = {np.shape(colVec)}')