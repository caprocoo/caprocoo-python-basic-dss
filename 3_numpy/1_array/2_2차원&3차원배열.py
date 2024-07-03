import numpy as np

# 2차원 배열 만들기
c = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array
print(c)

# 행의 갯수
print(len(c))

# 열의 갯수
print(len(c[0]))


# 3차원 배열 만들기
d = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[11, 12, 13, 14],
               [15, 16, 17, 18],
               [19, 20, 21, 22]]])   # 2 x 3 x 4 array

# 3차원 배열의 깊이, 행, 열
len(d), len(d[0]), len(d[0][0])

print('------------')

# 배열의 차원과 크기 알아내기
a = np.array([1, 2, 3])
print(a.ndim)
print(a.shape)

c = np.array([[0, 1, 2], [3, 4, 5]])
print(c.ndim)
print(c.shape)

print(d.ndim)
print(d.shape)


# 배열의 인덱싱
a = np.array([0, 1, 2, 3, 4])
print([2])
print(a[-1])