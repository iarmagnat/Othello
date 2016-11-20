import random
from Basics import *
def valuate(father,son,taken,player,x,y):
    noplay = np(son,player)
    reached = noplay[1] + noplay[2]
    value = 2*taken
    c_dist = cornerdist(x,y)
    if (c_dist == 0):
        value = value + 500
    count = reached-1
    if (noplay[0] == 4) and (noplay[player]>noplay[3-player]):
        return 50000
    if count >80:
        value = value + 10*taken
    if count >84:
        value = value + 10*noplay[player]
    if c_dist == 1:
        value = value-300
    if c_dist == 2 and count < 80:
        value = value + 50
    
    if reached<75:
        plyyE = 0
        for i in range (10):
            for j in range(10):
                if estValide(i,j,3-player,son):
                    plyyE =plyyE+1
        value = value - 75*plyyE
    
    
    
    
    return value
    
def cornerdist(x,y):
    if (((x == 0)or(x==9))and((y==0)or(y==9))):
        return 0
    elif [x,y] in [[0,1],[1,0],[1,1],[0,8],[1,8],[1,9],[8,0],[9,1],[8,1],[8,9],[9,8],[8,8]]:
        return 1
    elif [x,y] in [[0,2],[0,7],[1,2],[1,7],[2,0],[2,1],[2,2],[2,7],[2,8],[2,9],[7,0],[7,1],[7,2],[7,7],[7,8],[7,9],[8,2],[8,7],[9,2],[9,7]]:
        return 2
    
    
    
    
    
    
    
    