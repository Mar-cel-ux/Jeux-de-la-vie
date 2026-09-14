# CREATION DE L'ENVIRONNEMENT DU JEU

lignes = int(input("Entrer le nombre de lignes : "))
colonnes = int(input("Entrer le nombre de colonnes : "))

tableau = [[int(input(f"Entrez tableau[{i}][{j}] : ")) for j in range(colonnes)] for i in range(lignes)]

print("\nTableau initial :")
for ligne in tableau:
    print(ligne)


def compter_voisins_vivants(grille, i, j, lignes, colonnes):
    """Compte les voisins vivants de la cellule (i, j) sans déborder de la grille."""
    total = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < lignes and 0 <= nj < colonnes:
                total += grille[ni][nj]
    return total


def evoluer(grille, lignes, colonnes):
    """Calcule la génération suivante à partir de l'état actuel (sans le modifier)."""
    nouvelle_grille = [[0] * colonnes for _ in range(lignes)]
    for i in range(lignes):
        for j in range(colonnes):
            voisins_vivants = compter_voisins_vivants(grille, i, j, lignes, colonnes)
            if grille[i][j] == 1:
                # Une cellule vivante survit avec 2 ou 3 voisins vivants
                nouvelle_grille[i][j] = 1 if voisins_vivants in (2, 3) else 0
            else:
                # Une cellule morte naît avec exactement 3 voisins vivants
                nouvelle_grille[i][j] = 1 if voisins_vivants == 3 else 0
    return nouvelle_grille


# DETERMINATION DU DESTIN DES CELLULES (une génération)

tableau = evoluer(tableau, lignes, colonnes)

print("\nTableau après une génération :")
for ligne in tableau:
    print(ligne)
