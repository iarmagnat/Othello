from Basics import *
from Display import *
from competition import *
from Minimax import *
import random

def Play(player,dam,player1,player2,gamemode):
    affiche(player,dam)
    if (win (dam,player, player1, player2,gamemode) == 0):
        print('')
    else:
        return
    if gamemode == 1:
        if (player == 1):
            coup = int(input(player1))
        else:
            coup = int(input(player2))
    if gamemode == 4:
        coup = Minimax(dam,player)
    if gamemode == 5:
        if player == 1:
            coup = Minimax(dam,player)
        else:
            plyy = []
            for i in range (10):
                for j in range(10):
                    if estValide(i,j,player,dam) and dam[i][j] == 0:
                        plyy.append(10*i+j)
            if plyy != []:
                coup = plyy[random.randint(0,len(plyy)-1)]
    if gamemode == 2:
        if player == 1:
            coup = int(input(player1))
        else:
            coup = Minimax(dam,player)
    x = int(coup//10) #Oui, la magie existe!
    y = int(coup%10)
    if coup == -1:
        print('aha')
    else:
        if coup not in range (0,100,1):
            print ("Impossible")
            return Play(player,dam,player1,player2,gamemode)
        if not estValide(x,y,player,dam):
            print ("Impossible")
            return Play(player,dam,player1,player2,gamemode)
    Poser(x,y,player,dam)
    return Play(3-player,dam,player1,player2,gamemode)
    
def win(damier, player, player1, player2,gamemode):
    noplay = np(damier,player)
    print (player1,": ", noplay[1])
    print (player2,": ", noplay[2])
    if (noplay[0] == 1):
        print ("Desole, vous ne pouvez pas jouer.")
        return Play(3-player,damier,player1,player2,gamemode)
    elif noplay[0] == 2:
        print('Gagnant: ' , player1)
        return 1
    elif noplay[0] == 3:
        print('Gagnant: ' , player2)
        return 1
    elif (noplay[0] == 4)or(noplay[1]+noplay[2] == 100):
        if (noplay[1]>noplay[2]):
            print('Gagnant: ' , player1)
            return 1
        elif (noplay[2]>noplay[1]):
            print('Gagnant: ' , player2)
            return 1
        else:
            print('Egalité.')
            return 1
    return 0
    









