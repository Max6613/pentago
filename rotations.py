def Rotation_horaire(m, quadrant):
	tmp = [[0]*m for i in range(m)]
	for i in range(m):
		for j in range(m):
			tmp[i][j] = quadrant[j][i]	
	quadrant = tmp
	for ligne in quadrant:
		ligne = ligne.reverse()
	return quadrant
	
def Rotation_antihoraire(m, quadrant):
	tmp = [[0]*m for i in range(m)]
	for i in range(m):
		for j in range(m):
			tmp[i][j] = quadrant[j][i]	
	quadrant = tmp 																				
	for i in range(m-1):
		quadrant[i], quadrant[-i-1] = quadrant [-i-1], quadrant[i]
	return quadrant
	
def Rotation(n, plateau, num_quadrant, sens):
	quadrant = [[0]*(n//2) for i in range(n//2)]
	if num_quadrant == 1:								#définition de quadrant avec
		for i in range(n//2):							#une partie de plateau
			for j in range(n//2):
				quadrant[i][j] = plateau[i][j]
		if sens == True:
			quadrant = Rotation_horaire(n//2, quadrant)
		else:
			quadrant = Rotation_antihoraire(n//2, quadrant)
		for i in range(n//2):							#modification de plateau avec
			for j in range(n//2):						#le quadrant ayant tourné
				plateau[i][j] = quadrant[i][j]
	
	elif num_quadrant == 2:
		for i in range(n//2):
			for j in range(n//2,n):
				quadrant[i][j-(n//2)] = plateau[i][j]
		if sens == True:
			quadrant = Rotation_horaire(n//2, quadrant)
		else:
			quadrant = Rotation_antihoraire(n//2, quadrant)
		for i in range(n//2):
			for j in range(n//2,n):
				plateau[i][j] = quadrant[i][j-(n//2)]
	
	elif num_quadrant == 3:
		for i in range(n//2,n):
			for j in range(n//2):
				quadrant[i-(n//2)][j] = plateau[i][j]
		if sens:
			quadrant = Rotation_horaire(n//2, quadrant)
		else:
			quadrant = Rotation_antihoraire(n//2, quadrant)
		for i in range(n//2,n):
			for j in range(n//2):
				plateau[i][j] = quadrant[i-(n//2)][j]
		
	elif num_quadrant == 4:
		for i in range(n//2,n):
			for j in range(n//2,n):
				quadrant[i-(n//2)][j-(n//2)] = plateau[i][j]
		if sens:
			quadrant = Rotation_horaire(n//2, quadrant)
		else:
			quadrant = Rotation_antihoraire(n//2, quadrant)
		for i in range(n//2,n):
			for j in range(n//2,n):
				plateau[i][j] = quadrant[i-(n//2)][j-(n//2)]
		
	return plateau
	



