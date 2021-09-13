import matplotlib.pyplot as plt
import numpy as np

# X軸：時刻
x = np.arange(0, 100, 0.5)
# Y軸：sin関数
Hz = 5.0
y = np.sin(2.0 * np.pi * (x * Hz) / 100)

# グラフを描写
plt.plot(x, y)
plt.savefig('test.png')

# テスト