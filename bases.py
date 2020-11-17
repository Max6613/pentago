def Plateau_de_jeu(n):
	plateau = [[0]*n for i in range(n)]
	return plateau
	Affichage(plateau)
	
def Affichage(plateau):
	for ligne in plateau:
		for i in ligne:
			print(i, ' ', end='')
		print('')

