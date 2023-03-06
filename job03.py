def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x*x, n/2)
    else:
        return x * power(x, n-1)

# Demander à l'utilisateur de saisir un nombre et une puissance
x = int(input("Entrez un nombre: "))
n = int(input("Entrez une puissance entière positive: "))

# Vérifier si la puissance est positive ou nulle
if n < 0:
    print("Erreur: la puissance doit être positive ou nulle.")
else:
    # Calculer la puissance et afficher le résultat
    result = power(x, n)
    print(x, "puissance", n, "est égal à", result)
