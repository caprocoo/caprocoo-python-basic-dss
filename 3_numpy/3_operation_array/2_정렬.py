import numpy as np

# 정렬
a = np.array([[4, 3, 5, 7],
              [1, 12, 11, 9],
              [2, 15, 1, 14]])
print(np.sort(a))  # axis=-1 또는 axis=1 과 동일
print(np.sort(a, axis=0))
print(a.sort(axis=1))
print('---------------------')

a = np.array([42, 38, 12, 25])
j = np.argsort(a)  # 순서를 알고 싶을 때
print(j)
print(a[j])
