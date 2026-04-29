import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AR1_13:
    def __init__(self, T):
        self.T = T
    def generate(self, a):
        eps = np.random.normal(0, 1, self.T)
        x = np.zeros(self.T)
        for t in range(1, self.T):
            x[t] = a * x[t-1] + eps[t]
        return x
    def build(self, x1, x2):
        df = pd.DataFrame({
            "a_0.5": x1,
            "a_0.9": x2
        }, index=range(self.T))
        return df
    def draw(self, df):
        plt.plot(df.index, df["a_0.5"], label="a=0.5")
        plt.plot(df.index, df["a_0.9"], label="a=0.9")

        plt.legend()
        plt.title("AR(1)")

        plt.savefig("plot.png")
        plt.close()

        print("TASK 13 DONE")

t13 = AR1_13(100)
x1 = t13.generate(0.5)
x2 = t13.generate(0.9)
df = t13.build(x1, x2)
t13.draw(df)