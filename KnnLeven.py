import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Ensemble d'apprentissage
words = ["lune","mer","maladie","obscurité","tempête","épidémie","soleil","ciel","bateau","avion","parfum","sable",]
labels = ["Féminin","Féminin","Féminin","Féminin","Féminin","Féminin","Masculin","Masculin","Masculin","Masculin","Masculin","Masculin",]

# Mots à classer
new_words = ["orage", "odeur", "train", "voiture"]


# todo -> Calcul de la distance de Levenshtein
def levenshtein_distance(s1, s2):
   len_s1, len_s2 = len(s1), len(s2)
   dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

   for i in range(len_s1 + 1):
      dp[i][0] = i
   for j in range(len_s2 + 1):
      dp[0][j] = j
   for i in range(1, len_s1 + 1):
      for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
               dp[i][j] = dp[i - 1][j - 1]
            else:
               dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
   return dp[len_s1][len_s2]


#todo ->  Méthode manuelle pour k-NN
def knn_classify(word, data, labels, k):
   distances = [
      (levenshtein_distance(word, sample), label)
      for sample, label in zip(data, labels)
   ]
   distances.sort(key=lambda x: (x[0], labels.index(x[1])))  # Gérer les égalités
   k_nearest = distances[:k]  # Prendre les k plus proches
   classes = [label for _, label in k_nearest]
   return max(set(classes), key=classes.count)  # Classe majoritaire


#todo Calcul manuel
print("\n*** Classification manuelle ***")
k = 3
for new_word in new_words:
   result = knn_classify(new_word, words, labels, k)
   print(f"Mot '{new_word}' classé comme : {result}")


# todo -> Transformation des données pour `scikit-learn`
def transform_to_features(data, reference_data):
   return np.array([[levenshtein_distance(word, ref) for ref in reference_data] for word in data])


# Création des ensembles d'entraînement et de test pour `scikit-learn`
X_train = transform_to_features(words, words)  # Matrice des distances entre les mots de l'ensemble d'apprentissage
y_train = labels
X_test = transform_to_features(new_words, words)

# todo -> k-NN avec `scikit-learn`
knn = KNeighborsClassifier(n_neighbors=k, metric="precomputed")  # k-NN avec une distance pré-calculée
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("\n*** Classification avec scikit-learn ***")
for new_word, pred in zip(new_words, y_pred):
   print(f"Mot '{new_word}' classé comme : {pred}")

# Comparaison des résultats
print("\n*** Comparaison des résultats ***")
for i, new_word in enumerate(new_words):
   manual_result = knn_classify(new_word, words, labels, k)
   sklearn_result = y_pred[i]
   print(f"Mot '{new_word}' : Manuel = {manual_result}, scikit-learn = {sklearn_result}")
