def Alignement_ligne(n, plateau, p, j):
	compteur, trou = 0, 0
	for ligne in plateau:
		for i in ligne:
			if i == j:
				compteur += 1
			elif i != j and compteur != 0 :
				trou += 1
			if compteur >= p and trou == 0:
				return True
		compteur, trou = 0, 0
	return False
	
def Alignement_colonne(n, plateau, p, j):
	compteur, trou = 0, 0
	for c in range(n):
		for i in range(n):
			if plateau[i][c] == j:
				compteur += 1
			elif plateau[i][c] != j and compteur > 0:
				trou += 1
			if compteur >= p and trou == 0:
				return True
		compteur, trou = 0, 0
	return False

def Alignement_diagonale2(n, plateau, p, j):
	compteur, trou = 0, 0
	liste = []
	for l in range(n):
		liste.append(l)
	for c,i in zip (liste,liste[::-1]):
		if plateau[i][c] == j:
			compteur += 1
		elif plateau[i][c] != j and compteur > 0:
			trou += 1
		if compteur >= p and trou == 0:
			return True
	return False
	
def Alignement_diagonale1(n, plateau, p, j):
	compteur, trou = 0, 0
	for i in range(n):
		if plateau[i][i] == j:
			compteur += 1
		elif plateau[i][i] != j and compteur > 0:
			trou += 1
		if compteur >= p and trou == 0:
			return True
	return False
	
def Alignement(n, plateau, p, j):
	ligne = Alignement_ligne(n, plateau, p, j)
	colonne = Alignement_colonne(n, plateau, p, j)
	diagonale1 = Alignement_diagonale1(n, plateau, p, j)
	diagonale2 = Alignement_diagonale2(n, plateau, p, j)
	if ligne or colonne or diagonale1 or diagonale2:
		return True
	return False