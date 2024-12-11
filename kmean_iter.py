import numpy as np


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

centers = np.array(
    [[2, 10], [5, 8], [1, 2]]  # Centre 1 (A1)  # Centre 2 (A4)  # Centre 3 (A7)
)


def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))


# Variable pour stocker les clusters
labels = np.zeros(len(data))  # Labels pour chaque point
convergence = False  # Convergence des centres
iteration = 0


while not convergence:
    iteration += 1
    print(f"\n--- Itération {iteration} ---")

    # todo -> Affecter chaque point à son centre le plus proche
    new_labels = []
    for i, point in enumerate(data):
        distances = [euclidean_distance(point, center) for center in centers]

        # print(distances)
        closest_center = np.argmin(distances)  # Trouver l'indice du centre le plus proche
        distances = [float(d) for d in distances]
        formatted_distances = [f"{d:.3f}" for d in distances]
        new_labels.append(closest_center)
        print(f"Point {i + 1} ({point}) -> Centre {closest_center + 1} (Distance : {formatted_distances})")

    labels = np.array(new_labels)

    # todo -> Recalculer les centres
    new_centers = []
    for j in range(len(centers)):
        cluster_points = data[labels == j]
        if len(cluster_points) > 0:
            new_center = np.mean(cluster_points, axis=0)
        else:
            new_center = centers[j]  # Aucun point, garder le centre actuel
        new_centers.append(new_center)

    new_centers = np.array(new_centers)
    print("Nouveaux centres :")
    print(new_centers)

    # todo -> Vérifier la convergence (les centres ne changent plus)
    if np.allclose(new_centers, centers):
        convergence = True
    centers = new_centers


print(f"\nL'algorithme a convergé après {iteration} itérations.")
print("Clusters finaux :")
for j in range(len(centers)):
    cluster_points = data[labels == j]
    print(f"Groupe {j + 1} : {cluster_points}")
print("Centres finaux :")
print(centers)
