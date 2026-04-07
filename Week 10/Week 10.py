import numpy as np

# 1. Параметрлер (50-100 нүкте)
a = 0.8
T = 100
x = np.zeros(T)

# 2. eps-ті векторлық генерациялау (Vectorized Computation)
eps = np.random.normal(0, 1, T)

# 3. AR(1) циклі (Loop)
x[0] = eps[0]
for t in range(1, T):
    x[t] = a * x[t-1] + eps[t]

# Нәтижені тексеру
print(x)