import numpy as np
from scipy.stats import chi2


def chi_square_test(observed, alpha=0.05):
    """
    Effectue un test du khi-deux pour l'indépendance entre deux variables catégorielles.

    Args:
        observed: Tableau de contingence des fréquences observées.
        alpha: Niveau de signification (par défaut : 0.05).

    Returns:
        None. Affiche les résultats du test.
    """

    # Calcul des fréquences attendues
    total_row, total_col = observed.sum(axis=1), observed.sum(axis=0)
    total = observed.sum()
    expected = np.outer(total_row, total_col) / total # valleur theorique

    # distance entre les varialbes pour chaque modalite
    chi2_stat = np.sum((observed - expected) ** 2 / expected)

    # Degrés de liberté
    df = (observed.shape[0] - 1) * (observed.shape[1] - 1)

    # Valeur critique
    critical_value = chi2.ppf(1 - alpha, df)

    # Affichage des résultats
    print("Tableau de contingence observé:")
    print(observed)
    print("\nTableau de contingence attendu:")
    print(expected)
    print("\nStatistique du khi-deux:", chi2_stat)
    print("Degrés de liberté:", df)
    print("Valeur critique:", critical_value)

    # Conclusion
    if chi2_stat > critical_value:
        print("La statistique du khi-deux est supérieure à la valeur critique.")
        print(
            "On rejette l'hypothèse nulle. Il existe un lien significatif entre les deux variables."
        )
    else:
        print("La statistique du khi-deux est inférieure à la valeur critique.")
        print(
            "On ne peut pas rejeter l'hypothèse nulle. Il n'y a pas de preuve d'un lien significatif."
        )


# Données
observed = np.array([[25, 7], [25, 23]])

# Exécution du test
chi_square_test(observed)
