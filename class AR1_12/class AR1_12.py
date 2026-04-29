import numpy as np
import pandas as pd
class AR1_12:
    def __init__(self, T):
        self.T = T
        self.df = None
    def generate_ar1(self, a):
        eps = np.random.normal(0, 1, self.T)
        x = np.zeros(self.T)
        for t in range(1, self.T):
            x[t] = a * x[t-1] + eps[t]

        return x
    def build_dataframe(self):
        x1 = self.generate_ar1(0.5)
        x2 = self.generate_ar1(0.9)

        self.df = pd.DataFrame({
            'x_a_05': x1,
            'x_a_09': x2
        }, index=range(self.T))


    def compute_stats(self):
        stats = pd.DataFrame({
            'x_a_05': [
                self.df['x_a_05'].mean(),
                self.df['x_a_05'].std()
            ],
            'x_a_09': [
                self.df['x_a_09'].mean(),
                self.df['x_a_09'].std()
            ]
        }, index=['mean', 'std'])
        stats.to_csv('stats.csv')
project = AR1_12(T=80)

project.build_dataframe()
project.compute_stats()
