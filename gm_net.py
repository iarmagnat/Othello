from Basics import *
from tkinter import *  ## Res = 1366 * 768
from update import *
from competition import *
from Minimax import *
#from Display import *

def GM_net_start(window,images):
    w , h = window.winfo_screenwidth(), window.winfo_screenheight()
    board=Canvas(window, width=1000, height=1000,bg="green",highlightthickness=0)
    board.place(x=(w-700)/2, y = (h-700)/2, width=700, height=700)
    damier= initdamier()
    boardupdate(window,board,images,damier,-1)
    scoreboard = Canvas(window, width = 200, height = 50)
    scoreboard.place(x = w-150,y = h/2-150)
    score_noir = scoreboard.create_text( 70,10,text = "Joueur 1: %d" %(2))
    score_blanc = scoreboard.create_text( 70,40,text ="Joueur 2: %d" %(2))
    def leave():
        host.destroy()
        join.destroy()
        retour.destroy()
    host = Button(window, text = 'Heberger' , command=lambda:(host_start(window,images,board,damier,scoreboard,score_noir,score_blanc),leave()))
    join = Button(window, text = 'Rejoindre' , command=lambda:(join_start(window,images,board,damier,scoreboard,score_noir,score_blanc),leave()))
    retour = Button(window, text = 'retour' ,command = lambda:(window.destroy(),leave()))
    host.place(x = w/2-75,y = h/2-85 , width=150, height=30)
    join.place(x = w/2-75,y = h/2-15 , width=150, height=30)
    retour.place(x = w/2-75,y = h/2+55 , width=150, height=30)
    
    
def host_start(window,images,board,damier,scoreboard,score_noir,score_blanc):
    w , h = window.winfo_screenwidth(), window.winfo_screenheight()
    id = creerPartie()
    middle = Canvas(window, width =200, height = 200, highlightthickness=0)
    middle.place(x=w/2-100,y=h/2-100)
    middle.create_text( 100,80,text = "port = %d" % (id))
    Button(middle, text = 'Pret?' , command=lambda:(middle.destroy(),netplay(window,images,board,1,0,0,damier,scoreboard,score_noir,score_blanc))).place(x = 80,y = 100)
    
def join_start(window,images,board,damier,scoreboard,score_noir,score_blanc):
    def leave():
        chatte.destroy()
        e.destroy()
    e = Entry(window)
    e.place (x=500,y=350)
    chatte = Button(window, text = 'Pret?' , command=lambda:(rejoindrePartie(e.get()),leave(),netplay(window,images,board,2,0,0,damier,scoreboard,score_noir,score_blanc)))
    chatte.place(x = 700,y = 350)
    
    
    
def netplay(window,images,board,player,coupE,date,damier,scoreboard,score_noir,score_blanc):
    if (date == 0) and (player == 2):
        coupE = attentePremierCoup()
        return netplay(window,images,board,player,coupE,1,damier,scoreboard,score_noir,score_blanc) #OnlinePlay(player,dam,coupE,1)
    elif (date == 0) and (player == 1):
        coupE = jouer(65)
        print ('moi: 65')
        Poser(6,5,1,damier)
        boardupdate(window,board,images,damier,player)
        return netplay(window,images,board,player,coupE,1,damier,scoreboard,score_noir,score_blanc)
        
    if (coupE != -1):
        xe = int(coupE//10) 
        ye = int(coupE%10)
        print ('lui: ',coupE)
        Poser(xe,ye,3-player,damier)
    else:
        print("the enemy pass")
    boardupdate(window,board,images,damier,player)
    noplay =np (damier,player)
    if noplay[0] == 4:
        return fin(-1)
    coup = Minimax (damier,player)
    print ('moi: ',coup)
    x = int(coup//10)
    y = int(coup%10)
    Poser(x,y,player,damier)
    noplay = np(damier,player)
    if noplay[0] == 4:
        return fin(coup)
    boardupdate(window,board,images,damier,player)
    scoreboard.itemconfigure(score_noir,text ="Joueur 1 : %d" %(noplay[1]))
    scoreboard.itemconfigure(score_blanc,text ="Joueur 2 : %d" %(noplay[2]))
    return netplay(window,images,board,player,jouer(coup),1,damier,scoreboard,score_noir,score_blanc)
    
    
   
