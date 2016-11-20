from Basics import estValide

def affiche(player,damier) :
    for i in range (10):
        print (i , "|",  end='')
        for j in range (10):
            if (estValide(i,j,player,damier)):
                print(".|",  end='')
            elif (damier[i][j] == 0 ):
                print(" |",  end='')
            elif damier[i][j] == 1 :
                print("X|",  end='')
            elif damier[i][j] == 2 :
                print("O|",  end='')
        print("")
    print("   0 1 2 3 4 5 6 7 8 9 ")
