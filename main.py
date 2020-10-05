from upemtk import *
from time import sleep
from random import randint

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases


def case_vers_pixel(case):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul
	prend en compte la taille de chaque case, donnée par la variable
	globale taille_case.
    """
    x, y = case
    return (x + .5) * taille_case, (y + .5) * taille_case

def affiche_menu(taille_fenetre):
    
    x,y = taille_fenetre

    x1,y1 = taille_texte(texte(425,120,'Jouer',ancrage='center'))
    x2,y2 = taille_texte(texte(425,222,'Options',ancrage='center'))
    x3,y3 = taille_texte(texte(425,324,'Quitter',ancrage='center'))
        
    rectangle(317, 144, 533, 96)
    rectangle(317, 246, 533, 198)
    rectangle(317, 348, 533,300)

def sans_bordure(emplacement_s):
    x,y=emplacement_s
    if x <0:
        x=55

    if x>55:
        x=-1

    if y<0:
        y=35
    
    if y >35:
        y=-1
    emplacement_s=(x,y)
    return emplacement_s
    
def jeu_perdu(emplacement_s,lst_mod,direction):
    x,y=emplacement_s
    p,q=direction

    x=x+p
    y=y+q

    if lst_mod[2]=='actif':
        for p in range (score):
            if emplacement_s==mur[p]:
                return False,emplacement_s
       
    if lst_mod[0]=='inactif':
        
        if x <0 or y >= 35 :
            return False,emplacement_s
            
        if x >=55 or y <0 :
            return False,emplacement_s
    
    if lst_mod[0]=='actif':
        x,y=emplacement_s
        emplacement_s=sans_bordure(emplacement_s)           
    for d in range (len(serpent)):
                    
        if serpent[0]==serpent[d] and d!=0:
                return False,emplacement_s
    else:
        return True,emplacement_s

def change_direction(mouvement, touche):
    # à compléter !!!
    if touche == 'Up':
        # flèche haut pressée
        if mouvement ==(0,1):
            return mouvement
        return (0, -1)

    elif touche == 'Down':
        #flèche bas pressée
        if mouvement == (0, -1):
            return mouvement
        return (0,1)

    elif touche == 'Right':
        #flèche de droite pressée
        if mouvement ==(-1,0):
            return mouvement
        return (1,0)

    elif touche == 'Left' :
        #flèche de gauche pressée
        if mouvement ==(1,0):
            return mouvement
        return (-1,0)
    else:
        # pas de changement !
        return mouvement

def affiche_serpent(emplacement_s,serpent):
    x,y = emplacement_s
    i,j = case_vers_pixel((x,y))
    cercle(i, j, taille_case/2 + 1,
            couleur='darkgreen', remplissage='green')

def affiche_pommes(emplacement_p):
    x,y = emplacement_p
    i,j=case_vers_pixel((x,y))


    cercle(i, j, taille_case/2,
            couleur='darkred', remplissage='red')
    rectangle(i-2, j-taille_case*.4, i+2, j-taille_case*.7,
            couleur='darkgreen', remplissage='darkgreen')

def affiche_donut(donut):

    (x,y) = donut
    i,j=case_vers_pixel((x,y))

    cercle(i,j,10,remplissage='goldenrod',couleur='goldenrod')
    cercle(i,j,8,remplissage='saddlebrown',couleur='saddlebrown')
    cercle(i,j,2,remplissage='linen',couleur='linen')

    #Pailettes colorées
    cercle(i,j-5,1,couleur='hotpink',remplissage='hotpink')
    cercle(i,j+5,1,couleur='deepskyblue',remplissage='deepskyblue')
    cercle(i-5,j,1,couleur='gold',remplissage='gold')
    cercle(i+5,j,1,couleur='green3',remplissage='green3')

def affiche_score(score):
    rectangle(0,525,825,600,couleur='grey17',remplissage='grey17')
    texte(400,560,'Score : '+str(score),couleur='deepskyblue',ancrage='center')

def affiche_settings(lst_mod):
    
    
    affiche_mod(lst_mod)
    rectangle(292, 452, 508, 404 )

    texte(400,120,'Mode sans bord (facile)',couleur='black',ancrage='center')
    texte(400,222,'Mode donut (moyen)',couleur='black',ancrage='center')
    texte(400,324,'Mode obstacles (difficile)',couleur='black',ancrage='center')
    texte(400,428,'Retour',couleur='black',ancrage='center')

def affiche_mod(lst_mod):
    efface_tout()

    if lst_mod[0] == "inactif" :
        rectangle(112, 144, 688, 96 )
                        
    if lst_mod[0] == "actif":
        rectangle(112, 144, 688, 96 ,remplissage='grey20')
        
    if lst_mod[1] == "inactif" :
        rectangle(112, 246, 688, 198)
        
    if lst_mod[1] == "actif":
        rectangle(112, 246, 688, 198 ,remplissage='grey20')
        
    if lst_mod[2] == "inactif" :
        rectangle(112, 348, 688, 300)
        
    if lst_mod[2] == "actif" :
        rectangle(112, 348, 688, 300 ,remplissage='grey20')
    mise_a_jour()

def affiche_mur(mur):
    x,y=mur
    i,j=case_vers_pixel((x,y))
    rectangle(i-7,j-7,i+7,j+7,remplissage='grey')

def deplacement(emplacement_s,mouvement):

    if ty == 'Touche' :
        mouvement = change_direction(mouvement, touche(ev))
    a,b = emplacement_s
    c,d = mouvement

    x = a+c
    y = b+d
    emplacement_s = (x,y)
    for i in range (score,-1,-1):
        serpent[i]=serpent[i-1]                
        affiche_serpent(serpent[i],serpent)

    serpent[0]=emplacement_s

    for a in range (score):
        affiche_serpent(serpent[a],serpent)           
        
    affiche_score(score)
    
    return emplacement_s,mouvement

def manger_donut(tete,donut,score,serpent):
    
    if serpent[0] == donut and lst_mod[1]=="actif":
        point=4               
        score+=point
                
        for i in range (point):
            emplacement_c=serpent[len(serpent)-1]
            a,b=emplacement_c
            c,d=mouvement
            m=a-c
            n=b-d
            emplacement_c=m,n
            serpent.append(emplacement_c)
            if lst_mod[2]=='actif':
                mur.append(emplacement_c)
                
        donut=(-1,-1)
    
    return donut,score
        
def manger_pomme(tete,pomme,donut,score,serpent):
    if serpent[0] == pomme:                
        point=1    
        score+=point

        for i in range (point):
            emplacement_c=serpent[len(serpent)-1]
            a,b=emplacement_c
            c,d=mouvement
            m=a-c
            n=b-d
            emplacement_c=m,n
            serpent.append(emplacement_c)

        x=randint(3,52)
        y=randint(3,32)
        pomme=x,y
        
        if lst_mod[2]=='actif':
            mur.append(emplacement_c)
        donut=apparition_donut(donut,score)
    
    return pomme,donut,score
 
def apparition_donut(donut,score):
    if score%7==0 and score != 0 and lst_mod[1]=="actif":
            
        x=randint(3,52)
        y=randint(3,32)
        donut = (x,y)
        
        
        
        for i in range (score):
            
            if lst_mod[2]=='actif':
                while serpent[i]==donut or mur[i]==donut:
                    x=randint(3,52)
                    y=randint(3,32)
                    donut=x,y
            else:
                
                while serpent[i]==donut:
                    x=randint(3,52)
                    y=randint(3,32)
                    donut=x,y
        return donut
                  
def spawn_nourriture(score,aliment):
                
    for i in range (score):

        if lst_mod[2]=='actif':      
            while serpent[i]==aliment or mur[i]==aliment:
                x=randint(3,52)
                y=randint(3,32)
                aliment=x,y
        else:
            while serpent[i]==aliment:
                x=randint(3,52)
                y=randint(3,32)
                aliment=x,y
    
    return aliment

def affichage_menu(jouer,menu,on,parametre,jeu):
    ev = donne_ev()
    tev = type_ev(ev)
        
    if tev == "ClicGauche":
        if 317<=abscisse(ev)<=533 and 96<=ordonnee(ev)<=144 :
            #Case jouer 
            jouer = True
            menu = False
            on = False

        if 317<=abscisse(ev)<=533 and 198<=ordonnee(ev)<=246 :      
            #case option
            efface_tout()
            
            affiche_settings(lst_mod)

            menu = False
            parametre = True 

        if 317<=abscisse(ev)<=533 and 300<=ordonnee(ev)<=348 :
            jeu=jouer=menu=on=parametre=False
    mise_a_jour()
    return jouer,menu,on,parametre,jeu

def affichage_parametre(parametre,menu):
    ev = donne_ev()
    tev = type_ev(ev)
    if tev == "ClicGauche" or None :
        mod_1(ev)
        mod_2(ev)
        mod_3(ev)
        
        efface_tout()        
        affiche_settings(lst_mod)
        mise_a_jour()
        
        parametre,menu=retour(ev,parametre,menu)
    mise_a_jour()
    return parametre,menu
           
def mod_1(ev):
    if 112<=abscisse(ev)<=688 and 96<=ordonnee(ev)<=144:
        if lst_mod[0]=="actif":
            lst_mod[0]="inactif"
        else:
            lst_mod[0]="actif"

def mod_2(ev):
    if 112<=abscisse(ev)<=688 and 198<=ordonnee(ev)<=246:           
        if lst_mod[1]=="actif":
            lst_mod[1]="inactif"                       
        else:
            lst_mod[1]="actif"

def mod_3(ev):
    if 112<=abscisse(ev)<=688 and 300<=ordonnee(ev)<=348:             
        if lst_mod[2]=="actif":
            lst_mod[2]="inactif"
        else:
            lst_mod[2]="actif"

def retour(ev,parametre,menu):
    if 292<=abscisse(ev)<=508 and 404<=ordonnee(ev)<=452:
        efface_tout()
        parametre = False
        menu = True
    return parametre,menu

def rejouer (jeu):
    mise_a_jour()

    rectangle(112, 246, 688, 198)
    rectangle(112, 348, 688, 300)

    texte(400,222,'Menu',couleur='black',ancrage='center')
    texte(400,324,'Quitter',couleur='black',ancrage='center')
    ev = attend_ev()
    ty = type_ev(ev)
    if 112<=abscisse(ev)<=688 and 198<=ordonnee(ev)<=246:           
        jeu=True
    if 112<=abscisse(ev)<=688 and 300<=ordonnee(ev)<=348:             
        jeu=False
    
    return jeu

# programme principal
if __name__ == "__main__":

    #zone mod sans interface:
    lst_mod= ["inactif","inactif","inactif"] #mode de jeu 1 accélération 
    wait = 0.5
    cree_fenetre(825,600)

    # initialisation du jeu
    framerate = 10   # taux de rafraîchissement du jeu en images/s
    
    # boucle principale
    # boucle principale
    jeu=True
    while jeu:
        jouer = False
        
        #Menu 
        menu = True
        parametre = False
        on=True
        while on : 
            efface_tout()
            affiche_menu((800,600))
            while menu :
                jouer,menu,on,parametre,jeu=affichage_menu(jouer,menu,on,parametre,jeu)
                        
            while parametre : 
                parametre,menu=affichage_parametre(parametre,menu)
        
        mouvement = (0, 0)  # mouvement initiale du serpent
        emplacement_s = (30,20) #mouvement du serpent (coordonnées)
        emplacement_p = (10,10)
        emplacement_d = (-1,-1)
        serpent = [(30, 20)] # liste des coordonnées de cases adjacentes décrivant le serpent
        mur=[]

        score=0
        point=1
        
        while jouer:
            # affiche des objets
            efface_tout()
            affiche_score(score)
            affiche_pommes(emplacement_p)
            
            for a in range (score):
                affiche_serpent(serpent[a],serpent)
            if score%7==0 and score != 0 and lst_mod[1]=="actif":
                affiche_donut(emplacement_d)
            if lst_mod[2]=='actif':
                for i in range(score):
                    affiche_mur(mur[i]) 
                                    
            mise_a_jour()
            ev = donne_ev()
            ty = type_ev(ev)
            
            if ty == 'Quitte':
                jouer = False          

            elif ty == 'Touche' or ty == None :
                emplacement_s,mouvement=deplacement(emplacement_s,mouvement)
                

                jouer,emplacement_s= jeu_perdu(emplacement_s,lst_mod,mouvement)

                
                if lst_mod[2]=='actif':
                    for i in range(score):
                        affiche_mur(mur[i]) 

                emplacement_p,emplacement_d,score = manger_pomme(emplacement_s,
                                            emplacement_p,emplacement_d,score,serpent)
                emplacement_p = spawn_nourriture(score,emplacement_p)

                if lst_mod[1]=="actif":
                    emplacement_d,score = manger_donut(emplacement_s,
                                                        emplacement_d,score,serpent)
            mise_a_jour()
            # attente avant rafraîchissement
            sleep(wait/framerate)

        if jeu==True:
            efface_tout()
            mise_a_jour()
            jeu=rejouer(jeu)
    
    efface_tout()
    mise_a_jour()
    texte(412,300,'A Bientôt!',couleur='black',ancrage='center')
    attente(1)
    
    # fermeture et sortie
    ferme_fenetre()