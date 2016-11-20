import copy
from Basics import *
import random


def open_node(damier,artaken, player, oldkey,tree):
    for i in range(10):
        for j in range(10):
            if (damier[i][j] == 0 )and (estValide(i,j,player,damier)):
                print('coucou')
                dam_ij = copy.deepcopy(damier)
                taken = Poser(i,j,player,dam_ij)+artaken
                key_ij = oldkey+'_'+str(i)+str(j)
                print(key_ij)
                tree[key_ij] = [dam_ij , taken]
                
def create_tree(depth,damier,player,tree):
    open_node(damier,0,player,'',tree)
    for i in range (1,depth,1):
        player = 3-player
        a = tree.keys()
        b = []
        for r in a:
            b.append(str(r))
        print(b)
        for j in b:
            if len(j) == 3*i:
                open_node(tree[j][0],tree[j][1],player,j,tree)

    a = tree.keys()
    b = []
    for r in a:
        b.append(str(r))

    for r in b:
        if len(r) != 3*depth:
            del tree[r]


def DumbMontecarlo_open(damier,artaken, player, oldkey,tree):
    for i in range(10):
        for j in range(10):
            if (damier[i][j] == 0 )and (estValide(i,j,player,damier)) and random.randint(0,5) <= 4:
                print('coucou')
                dam_ij = copy.deepcopy(damier)
                taken = Poser(i,j,player,dam_ij)+artaken
                key_ij = oldkey+'_'+str(i)+str(j)
                print(key_ij)
                tree[key_ij] = [dam_ij , taken]