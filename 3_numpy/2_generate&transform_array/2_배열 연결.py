import numpy as np

# 배열 연결
# 1. hstack : 행의 수가 같은 두 개 이상의 배열을 옆으로 연결
a1 = np.ones((2, 3))
print(a1)
a2 = np.zeros((2, 2))
print(a2)
print(np.hstack([a1, a2]))
print('---------------------')

# 2. vstack : 열의 수가 같은 두 개 이상의 배열을 위아래로 연결
b1 = np.ones((2, 3))
print(b1)
b2 = np.zeros((3, 3))
print(b2)
print(np.vstack([b1, b2]))
print('---------------------')

# 3. dstack : 행이나 열이 아닌 깊이(depth) 방향으로 배열을 합친다.
c1 = np.ones((3, 4))
print(c1)
c2 = np.zeros((3, 4))
print(c2)
print(np.dstack([c1, c2]))
print((np.dstack([c1, c2])).shape)
print('---------------------')

# 4. stack : dstack 의 기능을 확장한 것으로 dstack처럼 마지막 차원으로 연결하는 것이 아니라
#            사용자가 지정한 차원(축으로) 배열을 연결한다. axis 인수를 사용하여 연결후의 회전방향을 정한다.
c = np.stack([c1, c2])
print(c)
print(c.shape)
c = np.stack([c1, c2], axis=1)
print(c)
print(c.shape)
print('---------------------')

# 5. r_ : hstack 과 비슷하게 배열을 좌우로 연결한다. 소괄호를 사용하지 않고 대괄호를 사용한다.
print(np.r_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print('---------------------')

# 6. c_
print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print('---------------------')

# 7. tile
a = np.array([[0, 1, 2], [3, 4, 5]])
print(np.tile(a, 2))
print(np.tile(a, (3, 2)))
print('---------------------')

