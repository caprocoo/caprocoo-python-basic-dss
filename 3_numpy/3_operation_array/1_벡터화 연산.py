import numpy as np

# 벡터화 연산
# 명시적으로 반복문을 사용하지 않고도 배열의 모든 원소에 대해 반복연산을 할 수 있다.

# 1. 사칙연산
x = np.arange(1, 10001)
y = np.arange(10001, 20001)

z = x + y
print(z[:10])
print('---------------------')

# 2. 논리연산
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])

print(a == b)
print(a >= b)
print('---------------------')

# 3. 각 원소가 아닌 모든 원소가 다 같은지 알고싶다면?
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])

print(np.all(a == b))
print(np.all(a == c))
print('---------------------')

# 4. 수학 함수
a = np.arange(5)

print(np.exp(a))
print(np.log(a + 1))
print(10 ** a)
print('---------------------')

# 스칼라와 벡터/행렬의 곱셈
x = np.arange(10)
print(100 * x)

x = np.arange(12).reshape(3, 4)
print(x)
print(100 * x)
print('---------------------')

# 브로드캐스팅 : 서로 다른 크기를 가진 두 배열의 사칙연산
#              크기가 작은 배열은 자동으로 반복 확장하여 크기가 큰 배열에 맞추는 방법

x = np.arange(5)
y = np.ones_like(x)
print(x + y)
print(x + 1)
print('---------------------')

x = np.vstack([range(7)[i:i + 3] for i in range(5)])
y = np.arange(5)[:, np.newaxis]
print(x)
print(y)
print(x + y)

y = np.arange(3)
print(y)
print(x + y)
print('---------------------')

# 차원 축소 연산 : min, max, sum, mean, median ...
x = np.array([1, 2, 3, 4])
print(np.sum(x))
print(x.sum())
print('---------------------')

x = np.array([1, 3, 2])
print(x.min())
print(x.max())
print(x.argmin()) # 최솟값의 위치
print(x.argmax())
print('---------------------')

x = np.array([1, 2, 3, 1])
print(x.mean())
print(np.median(x))
print(np.all([True, True, False]))
print(np.any([True, True, False]))
print('---------------------')

a = np.zeros((100, 100), dtype=np.int8)
print(np.any(a != 0))
print(np.all(a == a))
print('---------------------')

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
print(((a <= b) & (b <= c)).all())
print('---------------------')

x = np.array([[1, 1], [2, 2]])
print(x.sum())
print(x.sum(axis=0))    # 열 합계
print(x.sum(axis=1))   # 행 합계
print('---------------------')
