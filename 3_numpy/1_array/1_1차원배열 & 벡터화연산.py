import numpy as np

# 1차원 배열 만들기
ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(ar))

# 여러 개의 데이터를 모두 2배 해야 하는 경우
# 1) for 문 사용
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = []
for di in data:
    answer.append(2 * di)

print(answer)

# 2) 벡터화 연산 : 계산 속도도 빠르고 코드도 짧음
x = np.array(data)
print(2 * x)


# 벡터화 연산 예시
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(2 * a + b)
print(a == 2)
print(b > 10)
print((a == 2) & (b > 10))
