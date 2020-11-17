import pygame, sys, os
from pygame.locals import *
from random import randint
from bases import *
from rotations import *
from alignements import *

RED = (255,0,0)
DARKRED = (210,35,35)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (18,240,78)
DARKGREEN = (0,160,0)
fpsClock = pygame.time.Clock()
FPS = 2
surface = (900,750)
surface_de_jeu = pygame.display.set_mode(surface)
pygame.display.set_caption('Pentago')
surface_de_jeu.fill(BLACK)
pygame.font.init()
font = pygame.font.Font('28DaysLater.ttf',25)
font2 = pygame.font.Font('28DaysLater.ttf',50)

def Affichage_plateau(n, plateau, surface):
	m = n // 2
	quadrant = [[0]*m for i in range (m)]
	for num_quadrant in range(1,5):
		if num_quadrant ==1:
			x, y = 100, 100
			for i in range(m):
				for j in range(m):
					quadrant[i][j] = plateau[i][j]
			Affichage_quadrant(quadrant, surface, num_quadrant, x, y)
		elif num_quadrant == 2:
			x, y = 470, 100
			for i in range(m):
				for j in range(m,n):
					quadrant[i][j-m] = plateau[i][j]
			Affichage_quadrant(quadrant, surface, num_quadrant, x, y)		
		elif num_quadrant == 3:
			x, y = 100, 470
			for i in range(m,n):
				for j in range(m):
					quadrant[i-m][j] = plateau[i][j]
			Affichage_quadrant(quadrant, surface, num_quadrant, x, y)
		else:
			x, y = 470, 470
			for i in range(n//2,n):
				for j in range(n//2,n):
					quadrant[i-m][j-m] = plateau[i][j]
			Affichage_quadrant(quadrant, surface, num_quadrant, x, y)
		
def Affichage_quadrant(quadrant, surface, num_quadrant, x, y):	
	compteur_x, compteur_y = 0, 0
	for ligne in quadrant:
		for k in ligne:
			if k == 0:
				pygame.draw.circle(surface_de_jeu, DARKGREEN, (x+compteur_x*90, y+compteur_y*90), 20, 0)
				compteur_x += 1
			elif k == 1:
				pygame.draw.circle(surface_de_jeu, WHITE, (x+compteur_x*90, y+compteur_y*90), 30, 0)
				compteur_x += 1
			elif k == 2:
				pygame.draw.circle(surface_de_jeu, BLACK, (x+compteur_x*90, y+compteur_y*90), 30, 0)
				compteur_x += 1
		compteur_x, compteur_y = 0, compteur_y+1
		pygame.display.update()
	
def Affichage_fond():
	for x in range(10,730,370):
		for y in range(10,730,370):
			pygame.draw.rect(surface_de_jeu, GREEN, (x,y,360,360), 0)
	pygame.display.update()		

def Pose_pion(plateau, surface, joueur, clic_x, clic_y):	
	case_vide = False
	for origine_x_quadrant in range(100,820,370):
		for origine_y_quadrant in range(100,820,370):
			for x in range(origine_x_quadrant,origine_x_quadrant+270,90):
				for y in range(origine_y_quadrant,origine_y_quadrant+270,90):
					if clic_x >= x-20 and clic_x <= x+20 and clic_y >= y-20 and clic_y <= y+20:
						verif = Verification(plateau, x, y)
						if joueur == 1 and verif == True:
							pygame.draw.circle(surface_de_jeu, WHITE, (x, y), 30, 0)
							case_vide = True
							if x < 370 and y < 370:
								plateau[(y-100)//90][(x-100)//90] = 1
							elif x < 370 and y > 370:	
								plateau[(y-100)//100][(x-100)//90] = 1
							elif x >370 and y < 370:
								plateau[(y-100)//90][(x-100)//100] = 1	
							else:
								plateau[(y-100)//100][(x-100)//100] = 1
							
						elif joueur == 2 and verif == True:
							pygame.draw.circle(surface_de_jeu, BLACK, (x,y), 30, 0)
							case_vide = True
							if x < 370 and y < 370:
								plateau[(y-100)//90][(x-100)//90] = 2
							elif x < 370 and y > 370:	
								plateau[(y-100)//100][(x-100)//90] = 2
							elif x >370 and y < 370:
								plateau[(y-100)//90][(x-100)//100] = 2	
							else:
								plateau[(y-100)//100][(x-100)//100] = 2
	return plateau, case_vide
	
def Verification(plateau, x, y):
	if x < 370 and y < 370:
		if plateau[(y-100)//90][(x-100)//90] == 0:	
			return True
		return False
		
	elif x < 370 and y > 370:	
		if plateau[(y-100)//100][(x-100)//90] == 0:
			return True
		return False
		
	elif x >370 and y < 370:
		if plateau[(y-100)//90][(x-100)//100] == 0:	
			return True
		return False

	else:
		if plateau[(y-100)//100][(x-100)//100] == 0:
			return True
		return False

def Affichage_fleche(surface_de_jeu):
	fleche_gh = pygame.image.load('Images\\flechegauchehaut.png')	#100*50px
	fleche_dh = pygame.image.load('Images\\flechedroitehaut.png')
	fleche_gb = pygame.image.load('Images\\flechegauchebas.png')
	fleche_db = pygame.image.load('Images\\flechedroitebas.png')
	surface_de_jeu.blit(fleche_gh,(85,20))
	surface_de_jeu.blit(fleche_dh,(195,20))
	surface_de_jeu.blit(fleche_gh,(455,20))
	surface_de_jeu.blit(fleche_dh,(565,20))
	surface_de_jeu.blit(fleche_gh,(85,400))	
	surface_de_jeu.blit(fleche_dh,(195,400))
	surface_de_jeu.blit(fleche_gh,(455,400))
	surface_de_jeu.blit(fleche_dh,(565,400))
	
def Affichage_rotation(n, plateau, clic_x, clic_y):
	rot_ok = False
	for i in range(2):																			#Rotation horaire
		for j in range(2):	
			x, y = 85 + i * 370, 20 + j * 380													#Formules permettant de passer d'1 coordonnée tableau à coordonnée pixel
			if clic_x > x and clic_x < x + 100 and clic_y > y and clic_y < y + 50:				#Verification emplacement clic sur une fleche
				sens = False
				if i == 0 and j == 0:
					num = 1
					plateau = Rotation(n, plateau, num, sens)
				elif i == 1 and j == 0:
					num = 2
					plateau = Rotation(n, plateau, num, sens)
				elif i == 0 and j == 1:		
					num = 3
					plateau = Rotation(n, plateau, num, sens)
				else:
					num = 4
					plateau = Rotation(n, plateau, num, sens)
				rot_ok = True
				return plateau, rot_ok
	for i in range(2):			#Rotation antihoraire
		for j in range(2):
			x, y = 195 + i * 370, 20 + j * 380
			if clic_x > x and clic_x < x + 100 and clic_y > y and clic_y < y + 50:
				sens = True
				if i == 0 and j == 0:
					num = 1
					plateau = Rotation(n, plateau, num, sens)
				elif i == 1 and j == 0:
					num = 2
					plateau = Rotation(n, plateau, num, sens)
				elif i == 0 and j == 1:		
					num = 3
					plateau = Rotation(n, plateau, num, sens)
				else:
					num = 4
					plateau = Rotation(n, plateau, num, sens)
				rot_ok = True
				return plateau, rot_ok
	return plateau, rot_ok

def  Menu():
	un_joueur = '1 joueur'									#Affichage 1 joueur
	txt_1j = font.render(un_joueur, True, WHITE, BLACK)
	rect_1j = txt_1j.get_rect()
	rect_1j.topleft = (750,350)
	surface_de_jeu.blit(txt_1j, rect_1j)
	deux_joueur = '2 joueurs'								#Affichage 2 joueurs
	txt_2j = font.render(deux_joueur, True, WHITE, BLACK)
	rect_2j = txt_2j.get_rect()
	rect_2j.topleft = (750,380)
	surface_de_jeu.blit(txt_2j, rect_2j)
	pygame.display.update()

def Initialisation(x, y, init):
	type_de_jeu = 0		
	if x > 750 and x < 840 and y > 355 and y < 375:
		type_de_jeu, init = 1, True
	elif x > 750 and x < 855 and y > 380 and y < 400:
		type_de_jeu, init = 2, True	
	return type_de_jeu, init
	Affichage_fond()
	Affichage_plateau(n, plateau, surface)
	return type_de_jeu, init
	
def Jeu_pvp(n, plateau, joueur, x, y, case_vide, pose_de_pion, jouer, match_nul, tour, type_de_jeu, jouabilite):
	if jouabilite == True:
		if pose_de_pion == False:			#Clic et pose de pion non effectuée
				plateau, case_vide = Pose_pion(plateau, surface, joueur, x, y)					#Pose du pion
				if case_vide == True:
					Affichage_fleche(surface_de_jeu)
					pose_de_pion, case_vide = True, False
			
		else:								#Clic et pose de pion effectuée
			plateau, rot_ok = Affichage_rotation(n, plateau, x, y)
			Affichage_plateau(n, plateau, surface)

			if rot_ok == True:
				pose_de_pion = False
				victoire1 = Alignement(n, plateau, 5, 1)
				victoire2 = Alignement(n, plateau, 5, 2)
				Affichage_fond()
				Affichage_plateau(n, plateau, surface)
				rot_ok = False
					
				if joueur == 1 and victoire1 == False and victoire2 == False:
					joueur = 2
				elif joueur == 2 and victoire1 == False and victoire2 == False:
					joueur = 1
				tour = tour + 1
				if victoire1 == True or victoire2 == True:
					jouabilite = Victoire_pvp(36, True, victoire1, victoire2, jouabilite)
		if tour == 36	:
			jouabilite = Victoire_pvp(36, False, victoire1, victoire2, jouabilite)
	return case_vide, pose_de_pion, jouer, match_nul, tour, joueur, type_de_jeu, jouabilite
	
def Victoire_pvp(tour, jouer, victoire1, victoire2, jouabilite):
	if tour == 36 and jouer == False:	
		texte_nul = font2.render('MATCH NUL', True, WHITE, BLACK)
		texte_rect = texte_nul.get_rect()
		texte_rect.center = (375, 375)
		surface_de_jeu.blit(texte_nul, texte_rect)
		jouer == True
	elif tour == 36 and jouer == True:
		if victoire1 == True and victoire2 == False:
			vic = 'Victoire du joueur 1'
		elif victoire2 == True and victoire1 == False:
			vic = 'Victoire du joueur 2'
		elif victoire1 == True and victoire2 == True:
			vic = 'Egalite'
		txt_vic = font2.render(vic, True, WHITE, BLACK)
		vic_rect = txt_vic.get_rect()
		vic_rect.center = (375, 375)
		surface_de_jeu.blit(txt_vic, vic_rect)
	if tour == 36:
		txt_restart = font.render('Nouvelle Partie', True, WHITE, BLACK)
		restart_rect = txt_restart.get_rect()
		restart_rect.center = (375, 420)
		surface_de_jeu.blit(txt_restart, restart_rect)
		txt_quit = font.render('Quitter', True, WHITE, BLACK)
		quit_rect = txt_quit.get_rect()
		quit_rect.center = (375, 450)
		surface_de_jeu.blit(txt_quit, quit_rect)
	return False
	
def Jeu_pve(n, plateau, joueur, x, y, case_vide, pose_de_pion, jouer, match_nul, tour, type_de_jeu, jouabilite, cpt):
	victoire, victoireIA = False, False
	if cpt == True:
		jouabilite = True
		cpt = False
		
	if jouabilite == True:	
		if joueur == 1:
			if pose_de_pion == False:															#pose de pion non effectuée
				plateau, case_vide = Pose_pion(plateau, surface, joueur, x, y)					#Pose du pion
				if case_vide == True:
					Affichage_fleche(surface_de_jeu)
					pose_de_pion, case_vide = True, False
			else:																				#pose de pion effectuée
				plateau, rot_ok = Affichage_rotation(n, plateau, x, y)
				Affichage_plateau(n, plateau, surface)

				if rot_ok == True:
					pose_de_pion = False
					Affichage_fond()
					Affichage_plateau(n, plateau, surface)
					victoire = Alignement(n, plateau, 5, 1)
					rot_ok = False
					joueur = 2
					tour += 1
			
		elif joueur == 2:							#IA
			'''_____Pose du pion_____'''
			if case_vide == False:
				x = randint(1,2)			#'Choix' cadran gauche ou droite 
				if x == 1:
					x = randint(0,2)		#'Choix' coordonnée x pion
					x = x * 90 + 100
				else:
					x = randint(0,2)		#'Choix' coordonnée x pion
					x = x * 90 + 470
					
				y = randint(1,2)			#'Choix' cadran haut ou bas
				if y == 1:
					y = randint(0,2)		#'Choix' coordonnée y pion
					y = y * 90 + 100
				else:
					y = randint(0,2)		#'Choix' coordonnée y pion
					y = y * 90 + 470
				plateau, case_vide = Pose_pion(plateau, surface, joueur, x, y)
				Affichage_fond()
				Affichage_plateau(n, plateau, surface)
				'''_____Rotation quadrant_____'''
			else:
				sens = randint(0,1)
				num = randint(1,4)
				if sens == 0:
					plateau = Rotation(n, plateau, num, True)
				else:
					plateau = Rotation(n, plateau, num, False)
				
				Affichage_fond()
				Affichage_plateau(n, plateau, surface)
				victoireIA = Alignement(n, plateau, 5, 2)
				joueur = 1
				tour += 1
		
		if victoire == True or victoireIA == True:
			Victoire_pve(36, True, victoire, victoireIA)
			jouabilite = False
		elif tour == 36	:
			Victoire_pve(36, False, victoire, victoireIA)
			jouabilite = False
	return case_vide, pose_de_pion, jouer, match_nul, tour, joueur, type_de_jeu, jouabilite, cpt

def Victoire_pve(tour, jouer, victoire1, victoire2):
	if tour == 36 and jouer == False:	
		texte_nul = font2.render('MATCH NUL', True, WHITE, BLACK)
		texte_rect = texte_nul.get_rect()
		texte_rect.center = (375, 375)
		surface_de_jeu.blit(texte_nul, texte_rect)
		jouer == True
		# return False
	elif tour == 36 and jouer == True:
		if victoire1 == True and victoire2 == False:
			vic = 'Victoire du joueur'
		elif victoire2 == True and victoire1 == False:
			vic = 'Victoire de l\'ordinateur'
		elif victoire1 == True and victoire2 == True:
			vic = 'Egalite'
		txt_vic = font2.render(vic, True, WHITE, BLACK)
		vic_rect = txt_vic.get_rect()
		vic_rect.center = (375, 375)
		surface_de_jeu.blit(txt_vic, vic_rect)
		# return False
		
	if tour == 36:
		txt_restart = font.render('Nouvelle Partie', True, WHITE, BLACK)
		restart_rect = txt_restart.get_rect()
		restart_rect.center = (375, 420)
		surface_de_jeu.blit(txt_restart, restart_rect)
		txt_quit = font.render('Quitter', True, WHITE, BLACK)
		quit_rect = txt_quit.get_rect()
		quit_rect.center = (375, 450)
		surface_de_jeu.blit(txt_quit, quit_rect)
		# return False
	# return True

	
'''______________________________PROGRAMME PRINCIPAL__________________________________'''
n = 6
plateau = Plateau_de_jeu(n)
Affichage_fond()
Affichage_plateau(n, plateau, surface)
Menu()
	
init, case_vide, pose_de_pion, jouer, match_nul, jouabilite, cpt, tour, type_de_jeu \
= False, False, False, False, False, True, True, 0, 0
inProgress = True

while inProgress:
	if type_de_jeu == 1 and joueur == 2 and init == True and jouabilite == True:
		case_vide, pose_de_pion, jouer, match_nul, tour, joueur, type_de_jeu, jouabilite, cpt \
		= Jeu_pve(n, plateau, joueur, x, y, case_vide, pose_de_pion, jouer, match_nul, tour, type_de_jeu, jouabilite, cpt)
	for event in pygame.event.get():
		if event.type == QUIT:
			inProgress = False
		if event.type == MOUSEBUTTONUP and event.button == 1:
			x, y = event.pos[0], event.pos[1]
			print('clic x: ',x,'y: ',y)
			print('cpt : ', cpt)
			if init == False:
				type_de_jeu, init = Initialisation(x, y, init)
				if type_de_jeu == 1:
					joueur = 1
				else:
					joueur = randint(1,2)
				if init == True:
					pygame.draw.rect(surface_de_jeu, BLACK, (750,350,110,100), 0)
				
			if type_de_jeu == 1:
				case_vide, pose_de_pion, jouer, match_nul, tour, joueur, type_de_jeu, jouabilite, cpt \
				= Jeu_pve(n, plateau, joueur, x, y, case_vide, pose_de_pion, jouer, match_nul, tour, type_de_jeu, jouabilite, \
				cpt)
			elif type_de_jeu == 2:
				case_vide, pose_de_pion, jouer, match_nul, tour, joueur, type_de_jeu, jouabilite \
				= Jeu_pvp(n, plateau, joueur, x, y, case_vide, pose_de_pion, jouer, match_nul, tour, type_de_jeu, jouabilite)
			
			if jouabilite == False:
				if x > 290 and x < 460 and y > 408 and y < 431:
					init, case_vide, pose_de_pion, jouer, match_nul, jouabilite, tour, type_de_jeu, cpt \
					= False, False, False, False, False, True, 0, 0, True
					
					plateau = Plateau_de_jeu(n)
					surface_de_jeu.fill(BLACK)
					Menu()
					Affichage_fond()
					Affichage_plateau(n, plateau, surface)
				elif x > 335 and x < 415 and y > 435 and y < 465:
					inProgress = False
			
		if type_de_jeu == 2:
			pygame.draw.rect(surface_de_jeu, BLACK,(750, 30, 150, 200), 0)
			if joueur == 1:
				txt_j = font.render('Au joueur 1', True, WHITE, BLACK)
			elif joueur == 2:
				txt_j = font.render('Au joueur 2', True, WHITE, BLACK)	
			j_rect = txt_j.get_rect()
			j_rect.topleft = (750, 30)
			surface_de_jeu.blit(txt_j, j_rect)
	pygame.display.update()

# os.system("pause")	
		
pygame.quit()
sys.exit()