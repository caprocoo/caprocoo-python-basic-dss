import numpy as np

# 시드 설정하기
np.random.seed(0)
print(np.random.rand(5))
print('---------------------')

# 데이터의 순서 바꾸기
x = np.arange(10)
np.random.shuffle(x)
print(x)
print('---------------------')

# 데이터 샘플링 : 이미 있는 데이터 집합에서 일부를 무작위로 선택하는 것
print(np.random.choice(5, 5, replace=False))  # shuffle 명령과 같다.
print(np.random.choice(5, 10))  # 반복해서 10개 선택
print(np.random.choice(5, 10, p=[0.1, 0, 0.3, 0.6, 0]))  # 선택 확률을 다르게 해서 10개 선택
print('---------------------')

# 난수 생성
# 1. rand : 0부터 1사이의 균일 분포
print(np.random.rand(10))
print(np.random.rand(3, 5))
print('---------------------')

# 2. randn : 표준 정규 분포
print(np.random.randn(10))
print(np.random.randn(3, 5))
print('---------------------')

# 3. randint : 균일 분포의 정수 난수
print(np.random.randint(10, size=10))
print(np.random.randint(10, 20, size=10))
print(np.random.randint(10, 20, size=(3, 5)))
print('---------------------')


# 정수 데이터 카운팅
print(np.unique([11, 11, 2, 2, 34, 34]))

a = np.array(['a', 'b', 'b', 'c', 'a'])
index, count = np.unique(a, return_counts=True)
print(index)
print(count)

print(np.bincount([1, 1, 2, 2, 2, 3], minlength=6))