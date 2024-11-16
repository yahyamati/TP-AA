
import pandas as pd
import numpy as np


data = {
    'X1': [1.4, 1.6, 1.1, 1.9, 2.4],
    'X2': [0.7, 0.7, 0.4, 0.9, 1.5],
    'X3': [3.5, 3.1, 2.9, 4.2, 3.2],
    'X4': [1.62, 1.60, 1.74, 1.55, 1.95],
    'X5': [1.02, 1.06, 1.33, 1.67, 1.92]
}


df = pd.DataFrame(data)

cov_matrix = df.cov()

corr_matrix = df.corr()


print("Matrice de Covariance :\n")
for row in cov_matrix.values:
    print(" ".join(f"{value:10.5f}" for value in row))


print("\nMatrice de Corrélation :\n")
for row in corr_matrix.values:
    print(" ".join(f"{value:8.5f}" for value in row))


def mahalanobis_distance(point, df):
    """Calculer la distance de Mahalanobis d'un point par rapport à la distribution."""
    
    mean = df.mean()
    cov_matrix = df.cov()
    
    
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    
    
    diff = point - mean
    distance = np.sqrt(np.dot(np.dot(diff, inv_cov_matrix), diff.T))
    
    return distance



point_to_evaluate = df.iloc[1].values
mahalanobis_dist = mahalanobis_distance(point_to_evaluate, df)

print(f"\nDistance de Mahalanobis pour le point {point_to_evaluate}: {mahalanobis_dist:.4f}")




# def calculate_covariance_matrix(data):
#     n = len(data[0])  # Number of variables
#     m = len(data)     # Number of samples

   
#     means = [sum(column) / m for column in zip(*data)]

   
#     cov_matrix = [[0.0] * n for _ in range(n)]

    
#     for i in range(n):
#         for j in range(n):
#             cov_sum = sum((data[k][i] - means[i]) * (data[k][j] - means[j]) for k in range(m))
#             cov_matrix[i][j] = cov_sum / (m - 1) 

#     return cov_matrix

# def calculate_standard_deviation(data):
#     m = len(data)      # Number of samples
#     means = [sum(column) / m for column in zip(*data)]

#     std_devs = []
#     for i in range(len(data[0])):
#         variance = sum((data[j][i] - means[i]) ** 2 for j in range(m)) / (m - 1)
#         std_devs.append(variance ** 0.5)
#     return std_devs

# def calculate_correlation_matrix(data):
   
#     cov_matrix = calculate_covariance_matrix(data)
#     std_devs = calculate_standard_deviation(data)
#     n = len(cov_matrix)
    
    
#     corr_matrix = [[0.0] * n for _ in range(n)]

    
#     for i in range(n):
#         for j in range(n):
#             if std_devs[i] != 0 and std_devs[j] != 0:
#                 corr_matrix[i][j] = cov_matrix[i][j] / (std_devs[i] * std_devs[j])
#             else:
#                 corr_matrix[i][j] = 0 

#     return corr_matrix

# def print_matrix(matrix, title): 
#     print(f"\n{title}:")
#     for row in matrix:
#         formatted_row = " ".join(f"{value:8.5f}" for value in row)
#         print(formatted_row)


# data = [ 
#      [1.4, 0.7, 3.5, 1.62, 1.02], 
#      [1.6, 0.7, 3.1, 1.60, 1.06], 
#      [1.1, 0.4, 2.9, 1.74, 1.33], 
#      [1.9, 0.9, 4.2, 1.55, 1.67], 
#      [2.4, 1.5, 3.2, 1.95, 1.92]  
# ]


# cov_matrix = calculate_covariance_matrix(data)
# corr_matrix = calculate_correlation_matrix(data)


# print_matrix(cov_matrix, "Covariance Matrix")
# print_matrix(corr_matrix, "Correlation Matrix")
