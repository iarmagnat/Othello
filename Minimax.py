import copy
from Basics import *
from Display import *
from Valuation import valuate
def Minimax (damier,player):
    print('computing for player ',player,' ...')
    counter = 0
    for i in range (10):
        for j in range (10):
            if damier [i][j]!=0:
                counter+=1
    if counter < 70:
        depth = 3
    elif counter < 84:
        depth = 8
    else:
        depth = 16
    Tree = bigtree(damier,player,depth)  #Tree[dico: depth-1][Coup][0 = value, 1 = damier fils, 2 = father]
    if (len(Tree[0]) == 1):
        for k in Tree[0]:
            return int(k)
    bestcoup = -2
    bestval = -999999999999999
    for i in Tree[0]:
        if (Tree[0][i][0] > bestval):
            bestval = Tree[0][i][0]
            bestcoup = i
    print ('bestcoup = ' , bestcoup)
    print ('bestval = ' , bestval)
    if bestcoup == -2:
        return -1
    else:
        return  int(bestcoup)

        
            
def minimax_tree (tree):
    for depth_index in range (len(tree)-1,0,-1):
        for coup_index in tree[depth_index-1]:
            value = -999999999999999
            for i in tree[depth_index]:
                if ((tree[depth_index][i][2] == coup_index) and (tree[depth_index][i][0] > value)):
                    value = tree[depth_index][i][0]
            if value == -999999999999999 :
                value = 0
            tree[depth_index-1][coup_index][0] = tree[depth_index-1][coup_index][0]-value
    return Tree
    
def bigtree(damier,player,depth):
    Tree = []
    Tree.append(Tree_open(damier,player,''))
    if (len(Tree[0]) != 1) :
        for i in range (1, depth):
            player = 3-player
            Tree.append({})
            for k in Tree[i-1]:
                next = Tree_open(Tree[i-1][k][1],player,k)
                Tree[i] = dict(Tree[i], **next)
    return Tree
    
def Tree_open(damier,player,father):
    nexdico = {}
    playable = 0
    for x in range (10):
        for y in range (10):
            if estValide(x,y,player,damier):
                damier_son = copy.deepcopy(damier)
                taken = Poser(x,y,player,damier_son)
                case = 10*x+y
                value = valuate(damier,damier_son,taken,player,x,y)
                nexdico[str(case)] = [value,damier_son,father]
                playable = 1
            if ((x==10) and (y == 10) and (playable == 0)):
                value = valuate(damier,damier,0,player,-1,-1)
                nexdico['-1'] = [value,damier,father]
    return nexdico
