def compare_strings(s1, s2):
    # Si les chaînes sont identiques, retourner 1
    if s1 == s2:
        return 1
    
    # Diviser la chaîne s2 en sous-chaînes séparées par '*'
    s2_parts = s2.split('*')
    
    # Vérifier que s1 commence par la première sous-chaîne de s2
    if not s1.startswith(s2_parts[0]):
        return 0
    
    # Vérifier que s1 se termine par la dernière sous-chaîne de s2
    if not s1.endswith(s2_parts[-1]):
        return 0
    
    # Vérifier que les sous-chaînes restantes de s2 sont toutes incluses dans s1
    s1_position = len(s2_parts[0])
    for part in s2_parts[1:-1]:
        part_position = s1.find(part, s1_position)
        if part_position == -1:
            return 0
        s1_position = part_position + len(part)
    
    # Si toutes les vérifications ont réussi, retourner 1
    return 1

# Demander à l'utilisateur de fournir les chaînes à comparer
s1 = input("Entrez la première chaîne: ").lower()
s2 = input("Entrez la deuxième chaîne: ").lower()

# Comparer les chaînes et afficher le résultat
resultat = compare_strings(s1, s2)
print(resultat)
