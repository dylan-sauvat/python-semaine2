def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Demander à l'utilisateur de saisir un nombre entier
n = int(input("Entrez un nombre entier: "))

# Vérifier si le nombre est positif ou nul
if n < 0:
    print("Erreur: le nombre doit être positif ou nul.")
else:
    # Calculer la factorielle et afficher le résultat
    result = factorial(n)
    print("La factorielle de", n, "est", result)
