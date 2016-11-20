from Basics import *
from Display import *
from Menu import *
import random

def Play(player,dam,player1,player2,gamemode):
    affiche(player,dam)
    noplay = np(dam,player)
    print (player1,": ", noplay[1])
    print (player2,": ", noplay[2])
    if (noplay[0] == 1):
        print ("Desole, vous ne pouvez pas jouer.")
        return Play(3-player,dam,player1,player2,gamemode)
    elif noplay[0] == 2:
        return print('Gagnant: ' , player1)
    elif noplay[0] == 3:
        return print('Gagnant: ' , player2)
        
    if gamemode == 1:
        if (player == 1):
            coup = int(input("Noir, ou voulez vous jouer?"))
        else:
            coup = int(input("Blanc, ou voulez vous jouer?"))
    if gamemode == 4:
        plyy = []
        for i in range (10):
            for j in range(10):
                if estValide(i,j,player,dam) and dam[i][j] == 0:
                    plyy.append(10*i+j)
        coup = plyy[random.randint(0,len(plyy)-1)]
    
    x = int(coup//10) #Oui, la magie existe!
    y = int(coup%10)
    if coup not in range (0,100,1):
        print ("Impossible")
        return Play(player,dam,player1,player2,gamemode)
    if not estValide(x,y,player,dam):
        print ("Impossible")
        return Play(player,dam,player1,player2,gamemode)
    Poser(x,y,player,dam)
    noplay = np(dam,player)   
    if (noplay[0] !=4)and(noplay[1]+noplay[2] != 100):
        return Play(3-player,dam,player1,player2,gamemode)
    elif (noplay[1]>noplay[2]):
        return print('Gagnant: ' , player1)
    elif (noplay[2]>noplay[1]):
        return print('Gagnant: ' , player2)
    else:
        return print('Egalité.')
    









