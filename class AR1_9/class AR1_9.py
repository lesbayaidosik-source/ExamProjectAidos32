import numpy as np

class AR19:
    def __init__(self, T=100, seed=42):
        self.T = T
        self.seed = seed
    def generate(self, a):
        # тұрақты нәтиже
        np.random.seed(self.seed)
        eps = np.random.normal(0, 1, self.T)
        x = np.zeros(self.T)
        for t in range(1, self.T):
            x[t] = a * x[t-1] + eps[t]
        # нәтижені шығарады
        print(x)
        return x
# RUN
gen = AR19(T=100)
gen.generate(0.5)