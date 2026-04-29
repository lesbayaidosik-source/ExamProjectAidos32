import numpy as np
import pandas as pd
class AR1_11:
    def __init__(self, T):
        self.T = T

    def generate_ar1(self, a):
        eps = np.random.normal(0, 1, self.T)
        x = np.zeros(self.T)

        for t in range(1, self.T):
            x[t] = a * x[t-1] + eps[t]
        return x

    def build_dataframe(self):
        x1 = self.generate_ar1(0.5)
        x2 = self.generate_ar1(0.9)
        df = pd.DataFrame({
            'x_a_05': x1,
            'x_a_09': x2
        }, index=range(self.T))
        print(df)
        return df
task = AR1_11(T=100)
df = task.build_dataframe()