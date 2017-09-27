from random import*
from math import*
from pygame import*
from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from pygame.locals import*

font.init()

root = Tk() 
root.withdraw()

init()

class paintProgram:
    def __init__(self):
        #image loading~~~
        background=image.load("zelda.png")
        eraser=image.load("eraser.png")
        pencil=image.load("pencil.png")
        line=image.load("line.png")
        spray=image.load("spray.png")
        rect=image.load("rect.png")
        clear=image.load("clear.png")
        fill=image.load("fill.png")
        ellipse=image.load("ellipse.png")
        poly=image.load("poly.png")
        cpalette=image.load("CP.png")
        Undo=image.load("Undo.png")
        Redo=image.load("Redo.png")
        Crop=image.load("Crop.png")
        cursor=image.load("Curs.gif")
        Zelda=image.load("SS Zelda.png")
        Link=image.load("SS Link.png")
        Ghira=image.load("Ghira.png")
        Fi=image.load("Fi.png")
        Impa=image.load("Impa.png")
        Groose=image.load("Groose.png")
        Eye=image.load("Eye.png")
        Edrop=image.load("eyedropper.png")
        Save=image.load("Save.jpg")
        Load=image.load("Load.jpg")
        Loadimage=image.load("Loadimage.jpg")
        #playing music
        mixer.music.load("Title Screen.wav")
        #the (-1) makes it repeat infinitly
        mixer.music.play(-1)
        #drawing the canvas
        screen=display.set_mode((1000,700))
        background=transform.scale(background,(1000,700))
        screen.blit(background,(0,0))
        RECT=((400,100,550,550))
        canvas=draw.rect(screen,(255,255,255),(400,100,550,550))
        display.set_caption("Legend of Zelda Paint")

        #transparent cover for eye tool
        cover=Surface((550,550))
        cover.set_alpha(187)
        #colourkey means that if there is ever this specific colour used, it will not be
        #covered by the transparent cover
        cover.set_colorkey((255,255,254))

        #text border
        textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
        draw.rect(screen,(0,0,0),(400,655,550,40),1)

        #loading different fonts from MS WORD for title font and description font
        titlestyle=font.SysFont("Franklin Gothic Heavy",15)
        descriptstyle=font.SysFont("Times New Roman",14)

        #tool border
        draw.rect(screen,(224,255,255),(252,13,716,73))
        draw.rect(screen,(0,255,255),(251,12,718,75),2)

        #sticker border
        draw.rect(screen,(152,251,152),(10,390,160,231))
        draw.rect(screen,(50,205,50),(10,388,160,234),2)

        #undo redo save and load border
        draw.rect(screen,(190,190,190),(92,630,286,63))
        draw.rect(screen,(0,0,0),(92,628,286,65),2)

        #loadimage border
        draw.rect(screen,(255,255,0),(6,628,76,67),2)
        #box icons
        self.pencilbox=draw.rect(screen,(255,255,255),(900,20,60,60))
        self.eraserbox=draw.rect(screen,(255,255,255),(820,20,60,60))
        self.linebox=draw.rect(screen,(255,255,255),(740,20,60,60))
        self.spraybox=draw.rect(screen,(255,255,255),(660,20,60,60))
        self.rectbox=draw.rect(screen,(255,255,255),(580,20,60,60))
        self.ellipsebox=draw.rect(screen,(255,255,255),(500,20,60,60))
        self.polybox=draw.rect(screen,(255,255,255),(420,20,60,60))
        self.fillbox=draw.rect(screen,(255,255,255),(340,20,60,60))
        self.clearbox=draw.rect(screen,(255,255,255),(260,20,60,60))
        self.imagebox=draw.rect(screen,(255,255,224),(6,630,75,65))
        self.undobox=draw.rect(screen,(0,0,0),(98,634,62,54))
        self.redobox=draw.rect(screen,(0,0,0),(168,634,62,54))
        self.savebox=draw.rect(screen,(0,0,0),(238,634,62,54))
        self.loadbox=draw.rect(screen,(0,0,0),(308,634,62,54))
        self.eyedrop=draw.rect(screen,(255,255,255),(135,240,63,63))
        self.eyebox=draw.rect(screen,(255,255,255),(110,330,50,50))
        self.cropbox=draw.rect(screen,(255,255,255),(30,330,50,50))

        #stamp icons
        self.linkicon=draw.rect(screen,(255,255,255),(20,400,65,65))
        self.zeldaicon=draw.rect(screen,(255,255,255),(20,475,65,65))
        self.ghiraicon=draw.rect(screen,(255,255,255),(20,550,65,65))
        self.fiicon=draw.rect(screen,(255,255,255),(95,400,65,65))
        self.impaicon=draw.rect(screen,(255,255,255),(95,475,65,65))
        self.grooseicon=draw.rect(screen,(255,255,255),(95,550,65,65))

        #bomb icon border
        draw.rect(screen,(0,0,0),(258,18,63,63),4)

        #icon image transforming
        pencil=transform.smoothscale(pencil,(58,58))
        eraser=transform.smoothscale(eraser,(55,55))
        line=transform.smoothscale(line,(54,54))
        spray=transform.smoothscale(spray,(58,58))
        clear=transform.smoothscale(clear,(45,55))
        rect=transform.smoothscale(rect,(50,35))
        poly=transform.smoothscale(poly,(55,55))
        ellipse=transform.smoothscale(ellipse,(90,80))
        fill=transform.scale(fill,(68,55))
        Eye=transform.smoothscale(Eye,(45,45))
        Edrop=transform.smoothscale(Edrop,(62,60))
        Crop=transform.smoothscale(Crop,(40,40))
        Undo=transform.smoothscale(Undo,(58,50))
        Redo=transform.smoothscale(Redo,(58,50))
        Save=transform.smoothscale(Save,(58,50))
        Load=transform.smoothscale(Load,(58,50))
        Loadimage=transform.smoothscale(Loadimage,(65,63))

        #sticker transforming
        TLink=transform.smoothscale(Link,(60,60))
        TZelda=transform.smoothscale(Zelda,(46,60))
        TGhira=transform.smoothscale(Ghira,(43,60))
        TFi=transform.smoothscale(Fi,(60,60))
        TImpa=transform.smoothscale(Impa,(32,60))
        TGroose=transform.smoothscale(Groose,(30,60))


        #pasting image to screen
        screen.blit(pencil,(900,21))
        screen.blit(eraser,(821,22))
        screen.blit(line,(742,22))
        screen.blit(spray,(660,21))
        screen.blit(rect,(585,32))
        screen.blit(poly,(421,22))
        screen.blit(ellipse,(484,12))
        screen.blit(fill,(335,23))
        screen.blit(clear,(266,21))
        screen.blit(cpalette,[-15,-9])
        screen.blit(TLink,(20,400))
        screen.blit(TZelda,(26,477))
        screen.blit(TGhira,(26,552))
        screen.blit(TFi,(97,402))
        screen.blit(TImpa,(106,477))
        screen.blit(TGroose,(105,550))
        screen.blit(Edrop,(136,243))
        screen.blit(Eye,(111,331))
        screen.blit(Crop,(34,335))
        screen.blit(Undo,(100,636))
        screen.blit(Redo,(170,636))
        screen.blit(Save,(240,636))
        screen.blit(Load,(310,636))
        screen.blit(Loadimage,(13,630))

        #finding colour
        colcollide=draw.circle(screen,(0,0,0),(100,102),100,4)
        C=((0,0,0))
        #black and white palette
        for i in range(2,34):
            draw.line(screen,(0,0,0),(i,207),(i,237))
        for i in range(1,40):
            draw.line(screen,(255,255,255),(159+i,207),(159+i,237))
        for i in range(1,127):
            draw.line(screen,((i*2),(i*2),(i*2)),(33+i,207),(33+i,237))
        draw.rect(screen,(0,0,0),(1,205,198,34),2)
        bwcollide=Rect(2,205,198,30)

        #different sizes
        self.small=draw.rect(screen,(255,255,255),(955,110,40,40))
        self.medium=draw.rect(screen,(255,255,255),(955,160,40,40))
        self.draw.rect(screen,(0,0,255),(955,160,40,40),3)
        self.big=draw.rect(screen,(255,255,255),(955,210,40,40))
        self.rbig=draw.rect(screen,(255,255,255),(955,260,40,40))
        self.rrbig=draw.rect(screen,(255,255,255),(955,310,40,40))
        self.filled=draw.rect(screen,(0,0,0),(955,360,40,40))
        self.rotr=draw.rect(screen,(0,0,0),(955,410,40,40))
        self.rotl=draw.rect(screen,(0,0,0),(955,460,40,40))
        #default size
        self.S=4
        #list for polygon coordinates
        self.pxy=[]

        #default size and tool starts as nothing (aka "")
        self.size=""
        self.tool=""

        #undo and redo list
        self.undo=[]
        self.redo=[]

        #list used later for crop tool
        self.lcrop=[]
        #flag used later for crop tool
        self.r=0

    def mainLoop(self):
        running=True
        while running:
            for evnt in event.get():
                if evnt.type == QUIT:
                    running = False
                mx,my=mouse.get_pos()#mouse position
                mb=mouse.get_pressed()#mouse getting pressed
        

        
        
