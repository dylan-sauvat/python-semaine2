def solve_n_queens(n):
    # Initialiser le plateau de jeu
    board = [['O' for x in range(n)] for y in range(n)]
    
    # Vérifier s'il est possible de placer une reine sur chaque colonne
    if solve_n_queens_helper(board, 0, n) == False:
        print("Aucune solution n'a été trouvée.")
        return False
    
    # Afficher le plateau de jeu résultant
    for row in board:
        print(' '.join(row))
    
    return True

def solve_n_queens_helper(board, col, n):
    # Cas de base : toutes les reines ont été placées
    if col == n:
        return True
    
    # Essayer de placer une reine dans chaque ligne de la colonne actuelle
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'X'
            
            # Récursivement essayer de placer les reines restantes
            if solve_n_queens_helper(board, col+1, n) == True:
                return True
            
            # Si cela ne fonctionne pas, retirer la reine placée précédemment
            board[row][col] = 'O'
    
    # Si aucune reine ne peut être placée dans cette colonne, retourner False
    return False

def is_safe(board, row, col, n):
    # Vérifier la ligne à gauche de la position actuelle
    for i in range(col):
        if board[row][i] == 'X':
            return False
    
    # Vérifier la diagonale supérieure gauche
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'X':
            return False
        i -= 1
        j -= 1
    
    # Vérifier la diagonale inférieure gauche
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 'X':
            return False
        i += 1
        j -= 1
    
    # Si toutes les vérifications ont été passées, retourner True
    return True
n = int(input("Entrez la taille du plateau de jeu : "))
solve_n_queens(n)
