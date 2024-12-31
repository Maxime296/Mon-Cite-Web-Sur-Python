import matplotlib.pyplot as plt
import numpy as np

n = int(input("Entrez le nombre de côtés du polygone : "))
theta = np.linspace(0, 2 * np.pi, n + 1)
x = np.cos(theta)
y = np.sin(theta)

plt.plot(x, y)
plt.title(f'Polygone à {n} côtés')
plt.axis('equal')
plt.show()
