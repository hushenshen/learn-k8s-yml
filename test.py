import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-50, 150, 400)
y = 10**(-(x - 1) / 55)


plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y=10^{-\frac{x-1}{55}}$', color='b')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(' $y=10^{-\\frac{x-1}{55}}$')
plt.legend()
plt.show()
