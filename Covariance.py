# import numpy as np
# import pandas as pd

# # Données des caractéristiques des voitures
# data = {
#     'X1': [1.4, 1.6, 1.1, 1.9, 2.4],  # Puissance du moteur
#     'X2': [0.7, 0.7, 0.4, 0.9, 1.5],  # Poids
#     'X3': [3.5, 3.1, 2.9, 4.2, 3.2],  # Consommation de carburant
#     'X4': [1.62, 1.60, 1.74, 1.55, 1.95],  # Vitesse maximale
#     'X5': [1.02, 1.06, 1.33, 1.67, 1.92]  # Prix
# }

# # Création d'un DataFrame avec les données
# df = pd.DataFrame(data)

# # Calcul de la matrice de covariance
# cov_matrix = df.cov()

# print("Matrice de Covariance :\n", cov_matrix)


def calculate_covariance_matrix(data):
    n = len(data[0])  # nmbr of variable
    m = len(data)     # nmbre of sample (cars)

     # Calculate means of each variable
    means = [sum(column) / m for column in zip(*data)]

    # Initialize covariance matrix
    cov_matrix = [[0.0] * n for _ in range(n)]

   # Calculate covariance matrix
    for i in range(n):
        for j in range(n):
            cov_sum = sum((data[k][i] - means[i]) * (data[k][j] - means[j]) for k in range(m))
            cov_matrix[i][j] = cov_sum / (m - 1) 

    return cov_matrix


data = [ 
     [1.4, 0.7, 3.5, 1.62, 1.02], #1 sample
     [1.6, 0.7, 3.1, 1.60, 1.06], #2 sample
     [1.1, 0.4, 2.9, 1.74, 1.33], #3 sample
     [1.9, 0.9, 4.2, 1.55, 1.67], #4 sample
     [2.4, 1.5, 3.2, 1.95, 1.92]  #5 sample
  ]


cov_matrix = calculate_covariance_matrix(data)


for row in cov_matrix:
    print(row)



#*القانون 
#*Cov(X,Y)= 1/(m−1) i=1..m ∑(X𝑖-Xˉ)(Y𝑖− Yˉ)

#*   X𝑖 and 𝑌𝑖 are the individual sample points,
#*   Xˉ and Yˉ are the sample means ==>Xˉ= ∑ la valeur ta3 la column X1 kaml / nmbr de sample (nmbr de line)
#*   (X𝑖-Xˉ) = ∑ ( X1 كل خانة فال - Xˉ)
#*   m is the number of samples.

#*   matrice de covariance =>
#*   Diagonale principale :Les éléments diagonaux représentent la variance de chaque variable.
#*   Éléments hors diagonale : 
#                             Une valeur positive indique que les deux variables varient dans le même sens 
#                             valeur négative indique qu'elles varient en sens opposé.