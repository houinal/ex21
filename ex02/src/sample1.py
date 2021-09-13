import matplotlib.pyplot as plt
import numpy as np

# X軸
x = np.arange(0, 100, 0.5)

# y軸
Hz = 5.
y = np.sin(2.0 * np.pi * (x * Hz) / 100)

# グラフを描写
plt.plot(x, y)
plt.savefig('test.png')
