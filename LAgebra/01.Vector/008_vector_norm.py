# norm

import numpy as np

v = np.array([1,2,3,4,5,6,7,8,9])
v_dim = len(v) # 수학의 차원
v_mag = np.linalg.norm(v) # 수학적 크기, 길이, 노름

print(v_dim, v_mag)