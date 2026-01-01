import matplotlib.pyplot as plt
import numpy as np

# Données avec les valeurs jusqu'à 16 coups
coups = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
temps = np.array([
    0.000036,
    0.135977,
    0.006157,
    0.031364,
    0.103015,
    0.262347,
    0.978786,
    2.910068,
    5.228931,
    11.239877,
    22.675233,
    23.179409,
    65.649300
])

plt.figure(figsize=(10, 6))
plt.scatter(coups, temps, color='blue')
plt.yscale("log")

# Grille à la fois pour les lignes majeures et mineures
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.xticks(coups)
plt.xlabel("Nombre de coups", fontsize=12)
plt.ylabel("Temps de résolution moyen (secondes)", fontsize=12)
plt.title("Temps de résolution moyen en fonction du nombre de coups", fontsize=14, weight='bold')

plt.tight_layout()
plt.show()
