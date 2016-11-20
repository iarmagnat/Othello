from Basics import*
from tkinter import *  ## Res = 1366 * 768

def boardupdate(window,board,images,damier,player):
    for i in range (10):
        for j in range (10):
            if damier[i][j] == 1 :
                board.create_image(70*j+35 ,70*i+35,image = images[0])
            elif damier[i][j] == 2 :
                board.create_image(70*j+35 ,70*i+35,image = images[1])
            elif damier[i][j] == 0 :
                if estValide(i,j,player,damier):
                    board.create_image(70*j+35 ,70*i+35,image = images[5])
                else:
                    board.create_image(70*j+35 ,70*i+35,image = images[2])
                    
                    
