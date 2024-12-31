import matplotlib.pyplot as plt

base = float(input("Entrez la base du triangle : "))
hauteur = float(input("Entrez la hauteur du triangle : "))

x = [0, base, base / 2, 0]
y = [0, 0, hauteur, 0]

plt.plot(x, y)
plt.title(f'Triangle de base {base} et hauteur {hauteur}')
plt.axis('equal')
plt.show()
