import numpy as np

# 배열의 인덱싱
a = np.array([0, 1, 2, 3, 4])
print([2])
print(a[-1])
print('-------------')

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a[0, 0])  # 첫번째 행의 첫번째 열
print(a[0, 1])  # 첫번째 행의 두번째 열
print(a[-1, -1])  # 마지막 행의 마지막 열
print('-------------')

# 배열 슬라이싱
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

print(a[0, :])  # 첫번째 행 전체
print(a[:, 1])  # 두번째 열 전체
print(a[1, 1:])  # 두번째 행의 두번째 열부터 끝열까지
print(a[:2, :2])
print('-------------')

# 연습
m = np.array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9],
              [10, 11, 12, 13, 14]])

print(m[1, 2])  # 7
print(m[2, 4])  # 14
print(m[1, 1:3])  # [6 7]
print(m[1:3, 2])  # [7 12]
print(m[:2, 3:])  # [[3 4] [8 9]]
print('-------------')

# 팬시 인덱싱(배열 인덱싱)
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True,
                False, True, False, True, False])
print(a[idx])
print(a % 2)
print(a % 2 == 0)
print(a[a % 2 == 0])
print('-------------')

a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
print(a[idx])  # array([11, 33, 55, 77, 99])

a = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
print(a[idx])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[:, [True, False, False, True]])
print(a[[2, 0, 1], :])
