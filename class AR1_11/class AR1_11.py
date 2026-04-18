import pandas as pd

class AR1_11:
    def __init__(self, T=100):
        self.T = T
    def build(self):
        df = pd.DataFrame(index=range(self.T))  # 📌 0..T-1
        print(df.head())
        return df
# RUN
model = AR1_11(100)
df = model.build()