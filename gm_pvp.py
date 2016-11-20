from Basics import *
from tkinter import *  ## Res = 1366 * 768
from update import *


def GM_pvp_start(window,images):
    global player
    player = 1
    w , h = window.winfo_screenwidth(), window.winfo_screenheight()
    board=Canvas(window, width=1000, height=1000,bg="green" , highlightthickness=0)
    board.place(x=(w-700)/2, y = (h-700)/2, width=700, height=700)
    print ("pvp mode start")
    damier= []
    for i in range (10):
        damier.append([])
        for j in range (10):
            damier[i].append(0)
    damier[4][4]=2
    damier[5][5]=2
    damier[4][5]=1
    damier[5][4]=1
    boardupdate(window,board,images,damier,1)
    scoreboard = Canvas(window, width = 200, height = 50)
    scoreboard.place(x = w-150,y = h/2-150)
    score_noir = scoreboard.create_text( 70,10,text = "Joueur 1 : %d" %(2))
    score_blanc = scoreboard.create_text( 70,40,text ="Joueur 2 : %d" %(2))
    board.bind('<Button-1>',lambda event: click(event,window,board,images,damier,scoreboard,score_noir,score_blanc))
    
def Play(window,board,images,damier,X,Y,scoreboard,score_noir,score_blanc):
    w , h = window.winfo_screenwidth(), window.winfo_screenheight()
    global player
    noplay = np(damier,player)
    x = Y//70
    y = X//70
    if estValide(x,y,player,damier):
        Poser(x,y,player,damier)
        player = 3-player
        noplay = np(damier,player)
        boardupdate(window,board,images,damier,player)
        scoreboard.itemconfigure(score_noir,text ="Joueur 1 : %d" %(noplay[1]))
        scoreboard.itemconfigure(score_blanc,text ="Joueur 2 : %d" %(noplay[2]))
    noplay = np(damier,player)
    if noplay[0] == 4:
        print("game ended")
        if noplay[1] == noplay[2]:
            Button(window, text = 'Egalite' , command = lambda:window.destroy()).place(x=w/2-50, y = h/2-25, width=100, height=30)
        elif noplay[1] > noplay[2]:
            Button(window, text = 'Victoire joueur 1' , command = lambda:window.destroy()).place(x=w/2-50, y = h/2-25, width=100, height=30)
        else:
            Button(window, text = 'Victoire joueur 2' , command = lambda:window.destroy()).place(x=w/2-50, y = h/2-25, width=100, height=30)
    elif noplay[0] == 1:
        print( "skipped turn player: ", player)
        boardupdate(window,board,images,damier,player)
        player = 3-player
    
    
def click(event,window,board,images,damier,scoreboard,score_noir,score_blanc):
    X = event.x
    Y = event.y
    Play(window,board,images,damier,X,Y,scoreboard,score_noir,score_blanc)
    

    
