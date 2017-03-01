#!/usr/bin/env python3

# ========= TOUCHES ========= #
# ZQSD pour déplacer le curseur
# X pour valider
# =========================== #

import sys
import time
MIN = -10
MAX = 10
IA = 1
JOUEUR = 0
grille = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
tours = 0
pos = [1, 1]

# ======= PARAMETRABLE ======= #
joueurs = [JOUEUR, IA]
profondeur_par_defaut = 3
# ============================ #

def nbalignements(joueur_ia) :
	adverse = (joueur_ia + 1) % 2
	ret = 0
	for i in range(0, 8) :
		acc = 0
		if(i >= 0) and (i <= 2) :
			for j in range(0, 3) :
				if(grille[j][i] == adverse) :
					break
				acc += 1
		elif(i >= 3) and (i <= 5) :
			for j in range(0, 3) :
				if(grille[i - 3][j] == adverse) :
					break
				acc += 1
		elif(i == 6) :
			for j in range(0, 3) :
				if(grille[j][j] == adverse) :
					break
				acc += 1
		elif(i == 7) :
			for j in range(0, 3) :
				if(grille[j][2 - j] == adverse) :
					break
				acc += 1
		if(acc == 3) :
			ret += 1
	return ret

def play_ia(prof):
	max_ = MIN
	max_i = 0
	max_j = 0
	for i in range(0, 3) :
		for j in range(0, 3) :
			if(grille[i][j] == -1) :
				grille[i][j] = (tours % 2)
				valeur_ = min(prof - 1)
				if(valeur_ >= max_) :
					max_ = valeur_
					max_i = i
					max_j = j
				grille[i][j] = -1
	grille[max_i][max_j] = tours % 2

def min(prof) :
	etat = end()
	if(etat != 0) :
		if (etat - 1) == (tours % 2) :
			return MAX
		if(etat != -1) :
			return MIN
	if(prof == 0) :
		return eval()
	min_ = MAX
	for i in range(0, 3) :
		for j in range(0, 3) :
			if(grille[i][j] == -1) :
				grille[i][j] = ((tours + 1) % 2)
				valeur_ = max(prof - 1)
				if(valeur_ < min_) :
					min_ = valeur_
				grille[i][j] = -1
	return min_

def max(prof) :

	etat = end()
	if(etat != 0) :
		if (etat - 1) == (tours % 2) :
			return MAX
		if(etat != -1) :
			return MIN
	if(prof == 0) :
		return eval()
	max_ = MIN
	for i in range(0, 3) :
		for j in range(0, 3) :
			if(grille[i][j] == -1) :
				grille[i][j] = (tours % 2)
				valeur_ = min(prof - 1)
				if(valeur_ > max_) :
					max_ = valeur_
				grille[i][j] = -1
	return max_

def eval() :
	return nbalignements(tours % 2) - nbalignements((tours + 1) % 2)

def end() :
	j1 = 0
	j2 = 0
	for i in range(0, 8) :
		j1 = 0
		j2 = 0
		if(i >= 0 and i <= 2) :
			for j in range(0, 3) :
				if(grille[j][i] == 0) :
					j1 += 1
				elif(grille[j][i] == 1) :
					j2 += 1
		elif(i >= 3 and i <= 5) :
			for j in range(0, 3) :
				if(grille[i - 3][j] == 0) :
					j1 += 1
				elif(grille[i - 3][j] == 1) :
					j2 += 1
		elif(i == 6) :
			for j in range(0, 3) :
				if(grille[j][j] == 0) :
					j1 += 1
				elif(grille[j][j] == 1) :
					j2 += 1
		elif(i == 7) :
			for j in range(0, 3) :
				if(grille[j][2 - j] == 0) :
					j1 += 1
				elif(grille[j][2 - j] == 1) :
					j2 += 1
		if(j1 == 3) :
			return 1
		if(j2 == 3) :
			return 2
	for i in range(0, 3) :
		for j in range(0, 3) :
			if(grille[i][j] == -1) :
				return 0
	return -1

def play_real() :
	while(1) :
		affiche()
		str = sys.stdin.readline()
		if(str[0] == 'z') :
			pos[0] -= 1
			if(pos[0] == -1) :
				pos[0] = 2
		elif(str[0] == 's') :
			pos[0] += 1
			if(pos[0] == 3) :
				pos[0] =0
		elif(str[0] == 'q') :
			pos[1] -= 1
			if(pos[1] == -1) :
				pos[1] = 2
		elif(str[0] == 'd') :
			pos[1] += 1
			if(pos[1] == 3) :
				pos[1] = 0
		elif(str[0] == 'x') :
			if(grille[pos[0]][pos[1]] == -1) :
				grille[pos[0]][pos[1]] = tours % 2
				break

def affiche() :
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("TOURS : ", tours, "\nJOUEUR : ", tours % 2)
	for i in range(0, 3) :
		for j in range(0, 3) :
			if(i == pos[0] and j == pos[1]) :
				if(grille[i][j] == -1) :
					print("[.]", end = "")
				else :
					print("[{}]".format(grille[i][j]), end = "")
			else :
				if(grille[i][j] == -1) :
					print(" . ", end = '')
				else :
					print(" {} ".format(grille[i][j]), end = "")
		print()
	print()

def jeu() :
	global tours
	etat = end()
	while(etat == 0) :
		if(joueurs[tours % 2] == IA) :
			affiche()
			print("l'IA joue...")
			time.sleep(2)
			play_ia(profondeur_par_defaut)
		else :
			play_real()
		tours += 1
		etat = end()
	affiche()
	if(etat == -1) :
		print("Fin du jeu, égalité")
	elif(etat == 1) :
		print("Fin du jeu, joueur 0 gagne")
	elif(etat == 2) :
		print("Fin du jeu, joueur 1 gagne")

jeu()