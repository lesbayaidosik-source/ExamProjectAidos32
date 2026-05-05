import numpy as np
class AR1_9:
    def __init__(self,T):
        self.T = T
    def generate(self):
        eps = np.random.normal(2 ,1, self.T)
        return eps
print(AR1_9(80).generate())