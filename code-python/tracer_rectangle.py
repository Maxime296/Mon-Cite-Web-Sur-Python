import matplotlib.pyplot as plt

largeur = float(input("Entrez la largeur du rectangle : "))
hauteur = float(input("Entrez la hauteur du rectangle : "))
x = [0, largeur, largeur, 0, 0]
y = [0, 0, hauteur, hauteur, 0]

plt.plot(x, y)
plt.title(f'Rectangle ({largeur} x {hauteur})')
plt.axis('equal')
plt.show()
