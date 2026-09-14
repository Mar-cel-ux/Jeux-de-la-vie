# CREATION OF GAME'S ENVIRONMENT

lignes = int(input("Entrer le nombre de lignes : "))
colonnes = int(input("Entrer le nombre de colonne : "))

tableau = [[int(input(f"Entrez tableau[{i}][{j}] : ")) for j in range(colonnes)] for i in range(lignes)]

print("\nTableau :")
for ligne in tableau:
    print(ligne)

# DETERMINATION OF CELLULE' S FATE

cptv = 0
cptm = 0

for i in range(lignes):
   for j in range(colonnes):
      if tableau[i][j] == 1 :
          continue
      if tableau[i-1][j-1] == 1:
          cptv += 1
      if tableau[i-1][j] == 1:
          cptv += 1
      if tableau[i-1][j+1] == 1:
          cptv += 1
      if tableau[i][j-1] == 1:
          cptv += 1
      if tableau[i][j+1] == 1:
          cptv += 1
      if tableau[i+1][j-1] == 1:
          cptv += 1
      if tableau[i+1][j] == 1:
          cptv += 1
      if tableau[i+1][j+1] == 1:
          cptv += 1
      if cptv == 2 or cptv == 3:
          tableau[i][j] = 1
      else :
          tableau[i][j] = 0

      if tableau[i][j] == 0 :
          continue
      if tableau[i - 1][j - 1] == 0:
              cptm += 1
      if tableau[i - 1][j] == 0:
              cptm += 1
      if tableau[i - 1][j + 1] == 0:
              cptm += 1
      if tableau[i][j - 1] == 0:
              cptm += 1
      if tableau[i][j + 1] == 0:
              cptm += 1
      if tableau[i + 1][j - 1] == 0:
              cptm += 1
      if tableau[i + 1][j] == 0:
              cptm += 1
      if tableau[i + 1][j + 1] == 0:
              cptm += 1
      if cptm == 5 :
              tableau[i][j] = 1
      else :
              tableau[i][j] = 0
