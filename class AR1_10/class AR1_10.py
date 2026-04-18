import numpy as np
import pandas as pd
class AR1_10:
    def __init__(self, T=100):
        self.T = T
    def gen(self, a):
        x = np.zeros(self.T)
        eps = np.random.normal(0, 1, self.T)
        for t in range(1, self.T):
            x[t] = a * x[t-1] + eps[t]
        return x
    def run(self):
        x1 = self.gen(0.5)
        x2 = self.gen(0.9)
        df = pd.DataFrame({"a0.5": x1, "a0.9": x2})
        print(df.head())
        df.to_csv("ar1.csv")
# RUN
AR1_10(100).run()