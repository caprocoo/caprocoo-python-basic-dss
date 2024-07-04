import numpy as np

# 배열 생성
# 1. zeros : 모든 값이 0인 배열을 생성
a = np.zeros(5)  # 1차원 배열
print(a)

b = np.zeros((2, 3))  # 다차원 배열
print(b)

c = np.zeros((5, 2), dtype="i")  # dtype 인수 명시
print(c)

e = np.ones((2, 3, 4), dtype="i8")  # 모든 원소가 1인 배열
print(e)

print('---------------------')

# 2. zeros_like, ones_like
f = np.ones_like(b, dtype="f")
print(f)

# 3. empty
g = np.empty((4, 3))
print(g)

# 4. arange
print(np.arange(10))  # 0 .. n-1
print(np.arange(3, 21, 2))  # 시작, 끝(포함하지 않음), 단계

# 5. linspace, logspace
print(np.linspace(0, 100, 5))  # 시작, 끝(포함), 갯수
print(np.logspace(0.1, 1, 10))

print('---------------------')

# 전치 연산 : 행과 열을 바꾸는 작업
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.T)

# 배열의 크기 변형
a = np.arange(12)
print(a)

b = a.reshape(3, 4)  # 2차원 행렬로 변경하기
print(b)
print(a.reshape(3, -1))
print(a.reshape(2, 2, -1))
print(a.reshape(2, -1, 2))

print(a.flatten())  # 다차원 배열을 1차원으로 만들기
print(a.ravel())  # 다차원 배열을 1차원으로 만들기
