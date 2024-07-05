import numpy as np

x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])

# 데이터의 개수(count)
print(len(x))
print('---------------------')

# 평균(mean, average)
print(np.mean(x))  # 평균
print('---------------------')

# 분산(variance)
print(np.var(x))  # 분산
print(np.var(x, ddof=1))  # 비편향 분산.
print('---------------------')

# 표준 편차(standard deviation)
print(np.std(x))  # 표준 편차
print('---------------------')

# 최댓값(maximum)
print(np.max(x))  # 최댓값
print('---------------------')

# 최솟값(minimum)
print(np.min(x))  # 최솟값
print('---------------------')

# 중앙값(median)
print(np.median(x))  # 중앙값
print('---------------------')

# 사분위수(quartile)
print(np.percentile(x, 0))  # 최소값
print(np.percentile(x, 25))  # 1사분위 수
print(np.percentile(x, 50))  # 2사분위 수
print(np.percentile(x, 75))  # 3사분위 수
print(np.percentile(x, 100))  # 최댓값
print('---------------------')
