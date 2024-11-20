# BROUILLON Fusion sujet et projet


import pygame
from pygame.constants import K_0, K_9, K_1, K_LEFT, K_RIGHT, K_UP, K_DOWN 
import random 


horloge = pygame.time.Clock()


obstacles_lignes = [ [0, 4, 10, 16], [0, 14, 16], [0, 6, 16], [0, 9, 16], [0, 3, 15, 16], [0, 7, 16], [0, 1, 12, 16], [0, 7, 9, 16], [0, 7, 9, 16], [0, 4, 13, 16], [0, 6, 16], [0, 10, 16], [0, 8, 16], [0, 2, 15, 16], [0, 4, 10, 16], [0, 5, 12, 16] ]

obstacles_colonnes = [ [0, 5, 11, 16], [0, 6, 13, 16], [0, 4, 16], [0, 15, 16], [0, 10, 16], [0, 3, 16], [0, 10, 16], [0, 6, 7, 9, 12, 16], [0, 7, 9, 16], [0, 3, 12, 16], [0, 14, 16], [0, 16], [0, 7, 16], [0, 2, 10, 16], [0, 4, 13, 16], [0, 2, 12, 16] ]



x = 350
y = 125

Flag_mvmt = False
Flag_left = False
Flag_right = False
Flag_up = False
Flag_down = False

# Initialiser Pygame

pygame.init()

# Définir les dimensions de la fenêtre

screen = pygame.display.set_mode((800, 800))
#image = pygame.image.load("/Users/ehretaugustin/Desktop/info/Python/TD ipesup mpsi/paysage.jpg")
# Définir une couleur de fond

background_color = (255, 255, 255)
t = 0

# obstacle pygame crée a partir des coordonnées a et b 
def crée_obstacle_ligne(a,b):
    pygame.draw.rect(screen, (0,0,0), (50*a, 50*b, 5, 50))


def crée_obstacle_col(a,b):
    pygame.draw.rect(screen, (0,0,0), (50*a, 50*b, 50, 5))












# Démarrage de la boucle pp 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background_color)
    
    keys = pygame.key.get_pressed()
    
    # pour arreter si ca tourne mal :
    if keys[K_0]:
        print("TRUC")
        running = False
        
        
        
    # création du background 
    
    for i in range(0,800,50):
        for j in range(0,800,50):
            pygame.draw.rect(screen, (210,210,210), (i,j,50,50),10)
            pygame.draw.rect(screen, (51,50,55), (i,j,50,50), 1)
            pygame.draw.rect(screen, (191,191,191), (10+i,10+j,30,30),2) 

        
    pygame.draw.rect(screen,(197,183,174),(300,300,150,150))
    pygame.draw.rect(screen,(0,0,0),(300,300,150,150),10)


    
    
    # GENERATION D'UN BOARD      CA ON VERRA PLUS TARD
    







   
    
    
    
    # affichage des obstacles :    # PAS opti la boucle, en soit faudrait prendre le min de la taille des deux listes et compléter.
            
    if l == []:
        pass 
    else:
        for i in range(len(obstacles_lignes)):
            crée_obstacle_ligne(obstacles_lignes[i][0], obstacles_lignes[i][1])
        for i in range(len(obstacles_colonnes)):
            crée_obstacle_col(obstacles_colonnes[i][0], obstacles_colonnes[i][1])

    
   



    
    
    # MVMT ROBOTS
    
    mouvement_x = 5
    mouvement_y= 5
    










    
    # COLLISION GÉNÉRALE #Ici on implémente le sujet 
    
    N = len(obstacles_lignes)    #donc N-1 cases 


    def dichotomie(a,t):
        n = len(t)
        b = 0 
        c = n
        i  = (b+c)//2
        while t[i] > a or a >= t[i+1] :
            if t[i] <= a :
                b = i
                i = (i + c) // 2
            else : 
                c = i 
                i = (b + i)//2 
        return i 


    def deplacements_grille(a,b):
        ouest = (a, obstacles_lignes[a][dichotomie(b, obstacles_lignes[a])])
        est = (a, obstacles_lignes[a][dichotomie(b, obstacles_lignes[a]) + 1])
        nord = (obstacles_colonnes[b][dichotomie(a, obstacles_colonnes[b])], b)
        sud = (obstacles_colonnes[b][dichotomie(a, obstacles_colonnes[b]) + 1], b)
        return (ouest, est, nord, sud)



    def matrice_deplacements():
        res = [[(0,0,0,0) for i in range(N-1)] for j in range(N-1)]
        for i in range(N-1):
            for j in range(N-1):
                res[i][j] = deplacements_grille(i,j)
        return res 

    # ici t est le tableau des déplacements du robot principal en position a,b et c,d est la position d'un autre robot.

    def modif(t,a,b,c,d):    # t doit etre en fait un tuple sinon problemes apres dans deplacement robot ou ou applique ca a deplacmeent grille qui est un tuple 
        liste_tuple_t = []
        l = list(t)
        for i in range(len(l)):
            liste_tuple_t.append(list(l[i]))     # en fait on avait un un tuple de tuple et on le met en liste de liste (de nos déplacements)
        if b == d :                                # si les deux robots sont sur la meme colonne et apres on regarde si ils sont sur la meme ligne 
            if liste_tuple_t[2][0] <= c <= a :      # Nord devient la postion du robot (c)
                liste_tuple_t[2][0] = c
            if liste_tuple_t[3][0] >= c >= a :
                liste_tuple_t[3][0] = c
            
        if a == c :
            if liste_tuple_t[0][1] <= d <= b :      #on voit ce qu'il passe si meme ligne
                liste_tuple_t[0][1] = d
            if liste_tuple_t[1][1] >= d >= b :
                liste_tuple_t[1][1] = d
        t = tuple(liste_tuple_t)
        return t 


    def deplacement_robot(a,b,q):
        copy_deplacements_grille = deplacements_grille(a,b)
        for i in range(len(q)):
            copy_deplacements_grille = modif(copy_deplacements_grille,a,b,q[i][0],q[i][1])
        return copy_deplacements_grille
        

    
    













    
   
                
    
    
    
    
    # BOARD DE TRAVAIL POUR LES ROBOTS :
    
    
    objectif = deplacement_robot(x,y, [])         #On verra plus tard pour les robots 

    
    for i in range(4):    #pour que ca aille plus vite
        if keys[K_RIGHT] :
            if x < 50*objectif[1][1] +25 :
                x += mouvement_x
            
        if keys[K_LEFT]:
            if x > 50*objectif[0][1] +25 :
                x += - mouvement_x

          
            
        if keys[K_DOWN]:
            if y < 50*objectif[3][0] +25 :
                y += mouvement_y
            
            
        if keys[K_UP]:
            if y > 50*objectif[2][0] +25 :
                y += - mouvement_y
           
        
        
        
        
        # collision cotés : toujours ramener le robot sur le bord si il est hors du board.
        
        if x > 775 :     
            x = 775 
        if x < 25 :
            x = 25
        if y > 776 :
            y = 775
        if y < 24 :
            y = 25 
        if (x > 275 and x < 475) and (y > 275 and y < 475) :
            if previous_x < x :
                x = 275
            if previous_x > x :
                x = 475
            if previous_y < y :
                y = 275
            if previous_y > y :
                y = 475
                
        print (x,y)
        
        robots1 = pygame.draw.circle(screen, (255,0,0), (x,y),20)
        
        
        
        
        
    # Mettre à jour l'affichage
    pygame.display.flip()
    pygame.time.delay(20)
