import matplotlib.pyplot as plt
import numpy as np

rayon = float(input("Entrez le rayon du cercle : "))
theta = np.linspace(0, 2 * np.pi, 100)
x = rayon * np.cos(theta)
y = rayon * np.sin(theta)

plt.plot(x, y)
plt.title(f'Cercle de rayon {rayon}')
plt.axis('equal')
plt.show()
