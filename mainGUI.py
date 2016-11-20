from tkinter import *  ## Res = 1366 * 768
from sys import exit
from gm_pvp import *
from gm_pve import *
from gm_net import *
##import winsound      in to do list

def annihilation(event):
    window.destroy()
    print("annihilation exit")
    exit(0)


def menu2(window,images,background):
    background.create_image(w/2,192/2,image = images[3])
    def leavemenu():
        background.create_image(w/2,h/2,image = images[4])
        pvp.destroy()
        pve.destroy()
        net.destroy()
    ##boutons
    Button(window, text = 'Exit' , command = exit).place(x=w-100, y = h-30, width=100, height=30)
    pvp = Button(window, text = 'Joueur contre Joueur' , command=lambda:(GM_pvp_start(window,images),leavemenu()))
    pve = Button(window, text = 'Joueur contre Ordinateur' , command=lambda:(GM_pve_start(window,images),leavemenu()))
    net = Button(window, text = 'Competition en ligne' , command=lambda:(GM_net_start(window,images),leavemenu()))
    pvp.place(x = w/2-75,y = h/2-85 , width=150, height=30)
    pve.place(x = w/2-75,y = h/2-15 , width=150, height=30)
    net.place(x = w/2-75,y = h/2+55 , width=150, height=30)
    



while(1):
    window = Tk()
    
    w , h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.overrideredirect(1)
    window.geometry("%dx%d" % (w, h))
    window.focus_force()
    window.bind("<Escape>", annihilation)
    
    #Button(window, text="Exit",command = kill(0),bg="black",fg="#00ff00").place(x=1000, y =500, width=80, height=30)

    ##Images
    PawnB = PhotoImage(file='data/PawnB.png')
    PawnW = PhotoImage(file='data/PawnW.png')
    Empty = PhotoImage(file='data/Empty.png')
    BG = PhotoImage(file='data/BG.png')
    Banner=PhotoImage(file='data/banner.png')
    Hint = PhotoImage(file='data/Hint.png')
    images = [PawnB,PawnW,Empty,Banner,BG,Hint]
    
    background = Canvas(window, width=w, height=h,bg="black",highlightthickness=0)
    background.place(x = 0 ,y = 0)
    background.create_image(w/2,h/2,image = BG)
    """Board=Canvas(window, width=1000, height=1000,bg="black")
    Board.place(x=(w-700)/2, y = (h-700)/2, width=700, height=700)"""
    menu2(window,images,background)
    
    window.mainloop()
 