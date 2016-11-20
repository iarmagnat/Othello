from Basics import *
from Display import *
from Menu import *
from competition import *
import random

def OnlineStart(id,player,dam):
    if(id == -1):
        id = creerPartie()
        input('Enter when ready')
    else:
        rejoindrePartie(id)
    OnlinePlay(player,dam,1,0)
    
def OnlinePlay(player,dam,coupE,date):
    if (date == 0) and (player == 2):
        coupE = attentePremierCoup()
        return OnlinePlay(player,dam,coupE,1)
    elif (date == 0) and (player == 1):
        coupE = jouer(65)
        print ('moi: 65')
        Poser(6,5,1,dam)
        affiche(player, dam)
        return OnlinePlay(player,dam,coupE,1)
    if coupE != -1:
        xe = int(coupE//10) 
        ye = int(coupE%10)
        print ('lui: ',coupE)
        Poser(xe,ye,3-player,dam)
        dam[xe][ye] = 3-player
    affiche(player, dam)
    ###Randomatron
    plyy = []
    for i in range (10):
        for j in range(10):
            if estValide(i,j,player,dam) and dam[i][j] == 0:
                plyy.append(10*i+j)
    print(plyy)
    if plyy != []:
        coup = plyy[random.randint(0,len(plyy)-1)]
    else:
        coup = -1
        
    plyyE =[]
    for i in range (10):
        for j in range(10):
            if estValide(i,j,3-player,dam) and dam[i][j] == 0:
                plyyE.append(10*i+j)
    if (plyy == [])  and (plyyE == []):
        return fin(0)
    print ('moi: ',coup)
    x = int(coup//10)
    y = int(coup%10)
    dam[x][y] = player
    Poser(x,y,player,dam)
    affiche(player, dam)
    return OnlinePlay(player,dam,jouer(coup),1)
    
    
    

    
    
    
    
    