import pandas as pd
import matplotlib
matplotlib.use("MacOSX")  # ← Tkが入ってないのでMacOSXで表示する！

import matplotlib.pyplot as plt

# フォントを日本語に設定する（文字化け防止）
matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['axes.unicode_minus'] = False


df = pd.read_csv("eda_sample.csv")

# （あとは同じ）


# 職業ごとの人数（棒グラフ）
df["職業"].value_counts().plot(kind="bar", title="職業ごとの人数")
plt.ylabel("人数")
plt.xlabel("職業")
plt.tight_layout()
plt.show()

# 職業ごとの平均年収（棒グラフ）
df.groupby("職業")["年収"].mean().plot(kind="bar", title="職業別 平均年収")
plt.ylabel("平均年収（万円）")
plt.xlabel("職業")
plt.tight_layout()
plt.show()
