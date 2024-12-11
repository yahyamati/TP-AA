import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = np.array(
    [
        [2, 10],  # A1
        [2, 5],  # A2
        [8, 4],  # A3
        [5, 8],  # A4
        [7, 5],  # A5
        [6, 4],  # A6
        [1, 2],  # A7
        [4, 9],  # A8
    ]
)


initial_centers = np.array(
    [[2, 10], [5, 8], [1, 2]]  # A1 (groupe 1)  # A4 (groupe 2)  # A7 (groupe 3)
)

# Étape 3 : Configurer k-means avec les centres initiaux
kmeans = KMeans(n_clusters=3, init=initial_centers, n_init=1, random_state=42)

# Variables pour stocker les états et vérifier la convergence
convergence = False
iteration_count = 0
prev_centers = initial_centers

# Étape 4 : Boucle pour les itérations
while not convergence:
    iteration_count += 1
    print(f"--- Itération {iteration_count} ---")

    # Exécuter k-means pour une seule itération
    kmeans.fit(data)

    # Récupérer les groupes (labels) et les nouveaux centres
    labels = kmeans.labels_
    new_centers = kmeans.cluster_centers_

    # Afficher les groupes
    for i in range(3):
        group_points = data[labels == i]
        print(f"Groupe {i + 1} : {group_points}")

    # Afficher les nouveaux centres
    print("Nouveaux centres :")
    print(new_centers)

    # Calculer les distances des objets à leurs centres
    distances = [np.linalg.norm(data[i] - new_centers[labels[i]]) for i in range(len(data))]
    print("Distances des points à leurs centres :")
    # print(distances)
    distances = [float(d) for d in distances]
    formatted_distances = [f"{d:.3f}" for d in distances]
    print(formatted_distances)

    # Vérifier si les centres convergent
    convergence = np.allclose(new_centers, prev_centers)
    prev_centers = new_centers

# Étape 5 : Afficher le nombre total d'itérations
print(f"L'algorithme a convergé en {iteration_count} itérations.")

# Étape 6 : Visualisation des résultats finaux
plt.figure(figsize=(8, 8))
colors = ["r", "g", "b"]
for i in range(3):
    group_points = data[labels == i]
    plt.scatter(
        group_points[:, 0], group_points[:, 1], label=f"Groupe {i + 1}", color=colors[i]
    )

# Afficher les centres finaux
# plt.scatter(
#     new_centers[:, 0],
#     new_centers[:, 1],
#     c="black",
#     marker="x",
#     s=100,
#     label="Centres finaux",
# )
# plt.legend()
# plt.grid()
# plt.title("Résultats finaux du k-means")
# plt.show()
