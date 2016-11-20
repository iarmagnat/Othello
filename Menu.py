from gamemode1 import*
from gamemode2 import*
def menu():
    
    
    dam = []
    for i in range (10):
        dam.append([])
        for j in range (10):
            dam[i].append(0)
    dam[4][4]=2
    dam[5][5]=2
    dam[4][5]=1
    dam[5][4]=1
    print('')
    print('Que voulez vous faire?')
    print('1: PvP')
    print('2: PvAI')
    print('3: AIvAI Online')
    print('4: AIvAI Local')
    print('5: AIvRandom')
    print('6: Quitter')
    select = str(input())
    if select not in ['1','2','3','4','5','6']:
        print('Choix invalide')
        return
    player1 = 'Noirs'
    player2 = 'Blancs'
    if select == '6':
        quit()
    elif select == '5':
        Play(1,dam,player1,player2,5)
    elif select == '4':
        Play(1,dam,player1,player2,4)
    elif select == '3':
        print('1: Host')
        print('2: Join')
        select=int(input())
        if select == 1:
            OnlineStart(-1,1,dam)
        else:
            id = int(input('Id?'))
            OnlineStart(id,2,dam)
            
    elif select == '2':
        Play(1,dam,player1,player2,2)
    elif select == '1':
        player1 = str(input('Pseudo joueur 1?'))
        player2 = str(input('Pseudo joueur 2?'))
        Play(1,dam,player1,player2,1)
        return
    else:
        print('Choix invalide.')
    

            
