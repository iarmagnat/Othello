import copy


def estValide(x,y,player,damier):
    if damier[x][y] != 0:
        return False
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            if not ((i==0)and(j==0)):
                if testdirection(x,y,i,j,player,damier):
                    return True
    return False

def testdirection(x,y,dx,dy,player,damier):
    enemy = 0
    while(1):
        x=x+dx
        y=y+dy
        if (x not in range (10))or(y not in range (10))or(damier[x][y] == 0)or((enemy == 0)and(damier[x][y]==player)):
            return False
        elif(damier[x][y]==player)and(enemy>0):
            return True
        else:
            enemy = enemy+1

def Poser(x,y,player,damier):
    count = 0
    damier[x][y] = player
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            if not ((i==0)and(j==0)):
                if testdirection(x,y,i,j,player,damier):
                   count = count + flip(x,y,i,j,player,damier)
    return count
    
def flip(x,y,dx,dy,player,damier):
    count = 0
    while(1):
        x=x+dx
        y=y+dy
        if (damier[x][y]!=player):
            damier[x][y] = player
            count = count+1
        else:
            return count
            
def np(damier,player):
    noir = 0
    blanc = 0
    playableNoir = 0
    playableBlanc = 0
    for i in range(10):
        for j in range(10):
            if damier[i][j]==1:
                noir = noir + 1
            elif damier[i][j]==2:
                blanc = blanc + 1
            elif estValide(i,j,1,damier):
                playableNoir = 1
            elif estValide(i,j,2,damier):
                playableBlanc = 1
    if noir == 0:
        return [3,noir,blanc]
    elif blanc == 0:
        return [2,noir,blanc]
    elif (playableNoir == 0)and(playableBlanc == 0):
        return [4,noir,blanc]
    elif ((playableNoir == 0)and(player == 1))or((playableBlanc == 0)and(player == 2)):
        return [1,noir,blanc]
    else:
        return [0,noir,blanc]
        
def initdamier():
    damier= []
    for i in range (10):
        damier.append([])
        for j in range (10):
            damier[i].append(0)
    damier[4][4]=2
    damier[5][5]=2
    damier[4][5]=1
    damier[5][4]=1
    return damier