import matplotlib.pyplot as plt
import numpy as np

a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

x = np.linspace(-10, 10, 500)
y = a * x**2 + b * x + c

plt.plot(x, y)
plt.title(f'Parabole : {a}x^2 + {b}x + {c}')
plt.grid()
plt.show()
