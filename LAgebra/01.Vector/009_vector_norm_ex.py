import numpy as np

aList = np.array([[10,20,30]])

norm = np.linalg.norm(aList)

print(f'norm = {norm}')

result = aList * (1/norm)

print(f'result = {result}')