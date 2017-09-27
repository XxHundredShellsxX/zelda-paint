# ▲     Legend of Zelda   ▲  #
#▲ ▲       ~Paint~       ▲ ▲ #
#By Sajid Rahman
from random import*
from math import*
from pygame import*
from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from pygame.locals import*

#needed for font
font.init()
#needed for save and load
root = Tk() 
root.withdraw()
#initiation for music
init()
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
pencilbox=draw.rect(screen,(255,255,255),(900,20,60,60))
eraserbox=draw.rect(screen,(255,255,255),(820,20,60,60))
linebox=draw.rect(screen,(255,255,255),(740,20,60,60))
spraybox=draw.rect(screen,(255,255,255),(660,20,60,60))
rectbox=draw.rect(screen,(255,255,255),(580,20,60,60))
ellipsebox=draw.rect(screen,(255,255,255),(500,20,60,60))
polybox=draw.rect(screen,(255,255,255),(420,20,60,60))
fillbox=draw.rect(screen,(255,255,255),(340,20,60,60))
clearbox=draw.rect(screen,(255,255,255),(260,20,60,60))
imagebox=draw.rect(screen,(255,255,224),(6,630,75,65))
undobox=draw.rect(screen,(0,0,0),(98,634,62,54))
redobox=draw.rect(screen,(0,0,0),(168,634,62,54))
savebox=draw.rect(screen,(0,0,0),(238,634,62,54))
loadbox=draw.rect(screen,(0,0,0),(308,634,62,54))
eyedrop=draw.rect(screen,(255,255,255),(135,240,63,63))
eyebox=draw.rect(screen,(255,255,255),(110,330,50,50))
cropbox=draw.rect(screen,(255,255,255),(30,330,50,50))

#stamp icons
linkicon=draw.rect(screen,(255,255,255),(20,400,65,65))
zeldaicon=draw.rect(screen,(255,255,255),(20,475,65,65))
ghiraicon=draw.rect(screen,(255,255,255),(20,550,65,65))
fiicon=draw.rect(screen,(255,255,255),(95,400,65,65))
impaicon=draw.rect(screen,(255,255,255),(95,475,65,65))
grooseicon=draw.rect(screen,(255,255,255),(95,550,65,65))

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

def dot(mx,my,mmx,mmy):
    c=max(mmx,mx)
    d=min(mx,mmx)
    e=max(mmy,my)
    f=min(my,mmy)
    g=int((c-d)/10)
    h=int((e-f)/10)
    for i in range(g):
        draw.line(screen,(255,255,255),(d+5+(i*10),mmy-n),(d+(i*10),mmy-n),1)
        draw.line(screen,(255,255,255),(d+5+(i*10),my-a),(d+(i*10),my-a),1)
    for i in range(h):
        draw.line(screen,(255,255,255),(mmx-m,f+5+(i*10)),(mmx-m,f+(i*10)),1)
        draw.line(screen,(255,255,255),(mx-b,f+5+(i*10)),(mx-b,f+(i*10)),1)

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
small=draw.rect(screen,(255,255,255),(955,110,40,40))
medium=draw.rect(screen,(255,255,255),(955,160,40,40))
draw.rect(screen,(0,0,255),(955,160,40,40),3)
big=draw.rect(screen,(255,255,255),(955,210,40,40))
rbig=draw.rect(screen,(255,255,255),(955,260,40,40))
rrbig=draw.rect(screen,(255,255,255),(955,310,40,40))
filled=draw.rect(screen,(0,0,0),(955,360,40,40))

#default size
S=4
#list for polygon coordinates
pxy=[]

#default size and tool starts as nothing (aka "")
size=""
tool=""

#undo and redo list
undo=[]
redo=[]

#list used later for crop tool
lcrop=[]
#flag used later for crop tool
r=0

#sets the cursor invisible
mouse.set_visible(False)

#screen used and blitted repeatedly throughout code
#screen copies the screen while there cursor is not showing
#coldscreen stands for cursorless old screen
coldscreen=screen.copy()

#flag for when to show cursor
showcurs=True

#when to run cursor
Run=False
selected=False
go=False
finale=False
Second=False
Third=False

running=True
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        mx,my=mouse.get_pos()#mouse position
        mb=mouse.get_pressed()#mouse getting pressed


        if Run==True:#code so the screen doesn't copy the mouse cursor for undo and redo
            if evnt.type==MOUSEBUTTONDOWN and canvas.collidepoint(mx,my):
                screen.blit(copy,(400,100))
                showcurs=False
                copy=screen.subsurface(RECT).copy()
                undo.append(copy)
                redo=[]
                showcurs=True
        Run=False#stopping run
        if evnt.type==MOUSEBUTTONUP and undobox.collidepoint(mx,my):#when undo is pressed
            if len(undo)>0:#if something has happened on the screen
                #paste the previous screen so cursor is not blitted
                screen.blit(coldscreen,(0,0))
                #copy the screen for the canvas right now and add unto a list for redo
                rcopy=screen.subsurface(RECT).copy()
                redo.append(rcopy)
                #paste the last undo screen and get rid of it on the list
                screen.blit(undo[-1],(400,100))
                undo.pop()
                coldscreen=screen.copy()
                #reset lists for other tools
                lcrop=[]
                r=0

        if evnt.type==MOUSEBUTTONUP and redobox.collidepoint(mx,my):
            if len(redo)>0:#if undo was pressed first
                #paste the previous screen so cursor is not blitted
                screen.blit(coldscreen, (0,0))
                #copy canvas and add to undo list
                copy=screen.subsurface(RECT).copy()
                undo.append(copy)
                #paste the last redo screen and get rid of it on the list
                screen.blit(redo[-1],(400,100))
                redo.pop()
                coldscreen=screen.copy()

        #crucial so cursor is not blitted over and over
        screen.blit(coldscreen, (0,0))

        #if save button is pressed then window appears asking to save file
        if savebox.collidepoint(mx,my) and evnt.type==MOUSEBUTTONUP:
            fileName = asksaveasfilename(parent=root,title="Save the image as...")
            #as there is a name and not ""(nothing), then it saves the screen on canvas
            if fileName != "":
                image.save(screen.subsurface(RECT),"%s.png"%(fileName))
                
        #if load button is pressed then window appears asking to open file
        if loadbox.collidepoint(mx,my) and evnt.type==MOUSEBUTTONUP:
            fileName = askopenfilename(parent=root,title="Open Image:")
            #as there is a name and not ""(nothing), then it loads the screen on canvas
            if fileName != "":
                picture = image.load(fileName)
                #scales the image to fit whole canvas and then blits it on
                picture=transform.scale(picture,(550,550))
                screen.set_clip(canvas)
                screen.blit(picture,(400,100))
                #adds this to undo list so this can be undone and redone
                undo.append(copy)
                screen.set_clip(None)

        #draw coloured squares within size squares in whatever colour chosen
        draw.rect(screen,(C),(975,130,2,2))
        draw.rect(screen,(C),(973,178,4,4))
        draw.rect(screen,(C),(972,227,6,6))
        draw.rect(screen,(C),(971,276,8,8))
        draw.rect(screen,(C),(971,276,8,8))
        draw.rect(screen,(C),(970,325,10,10))
        draw.rect(screen,(C),(957,362,36,36))

        
        #if statements for all the sizes
        #changes the numeric size depending on which size is clicked
        #blue square is drawn to indicate which size is chosen
#------------------------------------------------------------------------------#
        if small.collidepoint(mx,my) and mb[0]==1:
            S=2
            size="small"
            draw.rect(screen,(0,0,255),(955,110,40,40),3)
        elif size!="small":
            draw.rect(screen,(0,0,0),(955,110,40,40),3)
            
        if medium.collidepoint(mx,my) and mb[0]==1:
            S=4
            size="medium"
            draw.rect(screen,(0,0,255),(955,160,40,40),3)
        elif size!="medium" and size!="":
            draw.rect(screen,(0,0,0),(955,160,40,40),3)
            
        if big.collidepoint(mx,my) and mb[0]==1:
            S=6
            size="big"
            draw.rect(screen,(0,0,255),(955,210,40,40),3)
        elif size!="big":
            draw.rect(screen,(0,0,0),(955,210,40,40),3)
            
        if rbig.collidepoint(mx,my) and mb[0]==1:
            S=8
            size="really big"
            draw.rect(screen,(0,0,255),(955,260,40,40),3)
        elif size!="really big":
            draw.rect(screen,(0,0,0),(955,260,40,40),3)
            
        if rrbig.collidepoint(mx,my) and mb[0]==1:
            S=10
            size="really really big"
            draw.rect(screen,(0,0,255),(955,310,40,40),3)
        elif size!="really really big":
            draw.rect(screen,(0,0,0),(955,310,40,40),3)
#------------------------------------------------------------------------------#

        #filled button which makes filled ellipses,rectangles, and polygons
        #otherwise just changes size to 40 for other tools
        if filled.collidepoint(mx,my) and mb[0]==1:
            S=40
            size="filled"
            draw.rect(screen,(0,0,255),(955,360,40,40),3)
        elif size!="filled":
            draw.rect(screen,(0,0,0),(955,360,40,40),3)
#------------------------------------------------------------------------------#
            
        #if statements for all my tools when their respective icon is clicked
        #draws textbox to go over previouse text and description based
        #on which tool is selected
        #draws green/red rectangle for whichever tool selected
        #draws back black rectangle for all tools not selected
        if eyedrop.collidepoint(mx,my) and mb[0]==1:
            tool="eyedrop"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Eyedrop Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and choose the colour you want anywhere on the screen",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,0),(135,238,64,65),2)
        elif tool!="eyedrop":
            draw.rect(screen,(0,0,0),(135,238,64,65),2)

        if tool=="" or tool=="pencil":
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Pencil Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Draw lines, size is changeable",1,(0,0,0)),(415,675))
            
        if pencilbox.collidepoint(mx,my) and mb[0]==1:
            tool="pencil"
            draw.rect(screen,(0,255,0),(898,18,63,63),4)
        elif tool!="pencil" and tool!="":
            draw.rect(screen,(0,0,0),(898,18,63,63),4)
            
        if eraserbox.collidepoint(mx,my) and mb[0]==1:
            tool="eraser"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Eraser Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Erase anything - because everyone makes mistakes, size is changeable",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(818,18,63,63),4)
        elif tool!="eraser":
            draw.rect(screen,(0,0,0),(818,18,63,63),4)
            
        if linebox.collidepoint(mx,my) and mb[0]==1:
            tool="line"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Line Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Draw *straight* lines, size is changeable",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(738,18,63,63),4)
        elif tool!="line":
            draw.rect(screen,(0,0,0),(738,18,63,63),4)
            
        if spraybox.collidepoint(mx,my) and mb[0]==1:
            tool="spray"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Spray Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Spread fairy dust across the canvas by moving the mouse, size is changeable",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(658,18,63,63),4)
        elif tool!="spray":
            draw.rect(screen,(0,0,0),(658,18,63,63),4)

        if rectbox.collidepoint(mx,my) and mb[0]==1:
            tool="rect"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Rectangle Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to make Rectangles, largest size for filled, any other size for unfilled",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(578,18,63,63),4)
        elif tool!="rect":
            draw.rect(screen,(0,0,0),(578,18,63,63),4)

        if ellipsebox.collidepoint(mx,my) and mb[0]==1:
            tool="ellipse"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Ellipse Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to make ovals or circles, largest size for filled, any other size for unfilled",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(498,18,63,63),4)
        elif tool!="ellipse":
            draw.rect(screen,(0,0,0),(498,18,63,63),4)

        if polybox.collidepoint(mx,my) and mb[0]==1:
            tool="poly"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Polygon Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Draw polygon, left click to make a series of lines, right click to close shape",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(418,18,63,63),4)
        elif tool!="poly":
            draw.rect(screen,(0,0,0),(418,18,63,63),4)

        if fillbox.collidepoint(mx,my) and mb[0]==1:
            tool="fill"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Fill Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Fill any area you want",1,(0,0,0)),(415,675))
            draw.rect(screen,(0,255,0),(338,18,63,63),4)
        elif tool!="fill":
            draw.rect(screen,(0,0,0),(338,18,63,63),4)
            
        #clear is an exception where no rectangle is drawn since it isn't a tool
        #clears all lists for other tools so their functions reset
        if clearbox.collidepoint(mx,my) and mb[0]==1:
            draw.rect(screen,(255,255,255),(400,100,550,550))
            pxy=[]
            lcrop=[]
            r=0

        if eyebox.collidepoint(mx,my) and mb[0]==1:
            tool="Eye"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Lens of Truth Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("See the *Truth*",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,0),(109,329,50,50),2)
        elif tool!="Eye":
            draw.rect(screen,(0,0,0),(109,329,50,50),2)

        if cropbox.collidepoint(mx,my) and mb[0]==1:
            tool="crop"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Selection Tool:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to select area, click area and drag to move around",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,0),(29,329,50,50),2)
        elif tool!="crop":
            r=0
            Second=False
            Third=False
            draw.rect(screen,(0,0,0),(29,329,50,50),2)

        if linkicon.collidepoint(mx,my) and mb[0]==1:
            tool="SS Link"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Link Stamp:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to size and place the HERO OF TIME",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,255),(18,398,67,67),3)
        elif tool!="SS Link":
            draw.rect(screen,(0,0,0),(18,398,67,67),3)

        if zeldaicon.collidepoint(mx,my) and mb[0]==1:
            tool="SS Zelda"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Zelda Stamp:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to size and place The Goddess Hylia's Incarnation",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,255),(18,473,67,67),3)
        elif tool!="SS Zelda":
            draw.rect(screen,(0,0,0),(18,473,67,67),3)

        if ghiraicon.collidepoint(mx,my) and mb[0]==1:
            tool="Ghira"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Ghirahim Stamp:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to size and place the Demon Lord",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,255),(18,547,67,67),3)
        elif tool!="Ghira":
            draw.rect(screen,(0,0,0),(18,547,67,67),3)

        if fiicon.collidepoint(mx,my) and mb[0]==1:
            tool="Fi"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Fi Stamp:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to size and place the Master Sword's Spirit",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,255),(93,398,67,67),3)
        elif tool!="Fi":
            draw.rect(screen,(0,0,0),(93,398,67,67),3)

        if impaicon.collidepoint(mx,my) and mb[0]==1:
            tool="Impa"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Impa Stamp:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to size and place the Guardian Sheikah",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,255),(93,473,67,67),3)
        elif tool!="Impa":
            draw.rect(screen,(0,0,0),(93,473,67,67),3)

        if grooseicon.collidepoint(mx,my) and mb[0]==1:
            tool="Groose"
            textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
            draw.rect(screen,(0,0,0),(400,655,550,40),1)
            screen.blit(titlestyle.render("Groose Stamp:",1,(0,0,0)),(402,660))
            screen.blit(descriptstyle.render("Click and drag to size and place the GROOSE",1,(0,0,0)),(415,675))
            draw.rect(screen,(255,0,255),(93,547,67,67),3)
        elif tool!="Groose":
            draw.rect(screen,(0,0,0),(93,547,67,67),3)
#------------------------------------------------------------------------------#
        #loads image from file and draws respective textbox
        #the picture opened is later used and explained in 'loaded image' function
        if imagebox.collidepoint(mx,my) and evnt.type==MOUSEBUTTONUP:
            fileName = askopenfilename(parent=root,title="Open Image:")
            if fileName != "":
                picture = image.load(fileName)
                tool="loaded image"
                textbox=draw.rect(screen,(255,255,255),(400,655,550,40))
                draw.rect(screen,(0,0,0),(400,655,550,40),1)
                screen.blit(titlestyle.render("Load Image Stamp:",1,(0,0,0)),(402,660))
                screen.blit(descriptstyle.render("Click and drag to size and place any image you chose",1,(0,0,0)),(415,675))
                draw.rect(screen,(255,0,255),(6,628,76,67),2)
        elif tool!="loaded image":
            draw.rect(screen,(0,0,0),(6,628,76,67),2)

        #copies the screen when mouse is pressed
        #gets coordinates for when mouse is first pressed
        #mmx and mmy stand for 'mousebuttondown-mouse-x/y'
        if evnt.type==MOUSEBUTTONDOWN:
            oldscreen=screen.copy()
            mmx,mmy=mouse.get_pos()

        #rectangle border for pencil when there is no tool selected since pencil is
        #starting tool
        if tool=="":
            draw.rect(screen,(0,255,0),(898,18,63,63),4)
            
#------------------------------------------------------------------------------#
        #all tools only work when left-clicking with mouse
        #all of them clips the screen
        #pastes oldscreen in some tools such as line, rect, ellipse, etc.
        #this is so whatever I shape I want to blit is only blitted when mouse
        #is let go
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvas)
            if tool=="pencil" or tool=="":
                #find the absolute minimum position from where your mouse is
                #and where it used to be
                x=mx-omx
                y=my-omy
                distance=int(((x)**2+(y)**2)**0.5)
                #makes sure distance is always at least 1
                if distance==0:
                    distance=1
                #draws multiple circle ensuring there is no gap in between
                #this makes the drawing pencil really smooth
                for i in range(int(distance)):
                    distx=int(omx+i/distance*x)
                    disty=int(omy+i/distance*y)
                    draw.circle(screen,(C),(distx,disty),S)
            screen.set_clip(None)
            
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvas)
            if tool=="eraser":
                #same formula as pencil but the colour is always white
                x=mx-omx
                y=my-omy
                distance=int(((x)**2+(y)**2)**0.5)
                if distance==0:
                    distance=1
                for i in range(int(distance)):
                    distx=int(omx+i/distance*x)
                    disty=int(omy+i/distance*y)
                    draw.circle(screen,(255,255,255),(distx,disty),S)
            screen.set_clip(None)
            
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvas)
            if tool=="line":
                #draws line from where mouse is pressed to where its released
                screen.blit(oldscreen,(0,0))
                draw.line(screen,(C),(mmx,mmy),(mx,my),S)
            screen.set_clip(None)
            
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvas)
            if tool=="spray":
                #draws 20 lines that are 1 pixels long and wide in random position
                #position that is within the size range from where your mouse is clicked
                for i in range(20):
                    cx=mx-randint(-S,S)
                    cy=my-randint(-S,S)
                    #used distance formula to make sure it only draws within a circle
                    dist=int(sqrt((mx-cx)**2 +(my-cy)**2))
                    if dist<S:
                        draw.line(screen,(C),(cx,cy),(cx,cy),1)
            screen.set_clip(None)

        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="rect":
                screen.blit(oldscreen,(0,0))
                if size!="filled":
                    #set a to a value to make sure lines that cover rectangle
                    #corners are proper
                    if my>mmy:
                        a=1
                    else:
                        a=0
                    #while the size is greater than thickness, it draws a filled rectangle
                    if S> abs(mx-mmx) or S> abs(my-mmy):
                         draw.rect(screen,(C),(mmx,mmy,mx-mmx,my-mmy))
                    else:
                        #draws the rectangle according to the difference from where you clicked
                        #and where your current position is
                        draw.rect(screen,(C),(mmx,mmy,mx-mmx,my-mmy),S)
                        #draw 2 lines that cover rectangle corners
                        draw.line(screen,(C),(mmx,min(mmy,my)-S/2+a),(mmx,min(mmy,my)+(max(my,mmy)-min(my,mmy))+S/2-a),S)
                        draw.line(screen,(C),(mmx+(mx-mmx)-1,min(mmy,my)-S/2+a),(mmx+(mx-mmx)-1,min(mmy,my)+(max(my,mmy)-min(my,mmy))+S/2-a),S)
                #if size is filled, then draw filled rectangles
                else:
                    draw.rect(screen,(C),(mmx,mmy,mx-mmx,my-mmy))
            screen.set_clip(None)

        if canvas.collidepoint(mx,my) and mb[0]==1:
            if tool=="ellipse":
                screen.set_clip(canvas)
                screen.blit(oldscreen,(0,0))
                #rectangle for ellipse is the same as rectangle in rect tool
                ERect=(mmx,mmy,mx-mmx,my-mmy)
                ER2=Rect(ERect)
                #normalize the ellipse so ellipse can be drawn with negative
                #length and width
                ER2.normalize()
                if size!="filled":
                    #draws a filled ellipse when size is greater than radius
                    #then an unfilled ellipse when radius is greater than size
                    if abs((mx-mmx)/2)<S or abs((my-mmy)/2)<S:
                        draw.ellipse(screen,(C),(ER2))
                    elif abs((mx-mmx)/2)>S or abs((my-mmy)/2)>S:
                        draw.ellipse(screen,(C),(ER2),S)
                #if size is filled, then draw filled circle
                else:
                    draw.ellipse(screen,(C),(ER2))
                screen.set_clip(None)

        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            if tool=="poly":
                #add x and y coordinates to a list
                if mb[0]==1:
                    pxy.append((mmx,mmy))
                if size!="filled":
                    #keep drawing lines from previouse point to current position
                    #from last to 2nd last point on list
                    #right-clicking draws current point to the first point clicked
                    #list is reset to draw new polygon
                    if mb[2]==1 and len(pxy)>1:
                        draw.polygon(screen,(C),pxy,S)
                        pxy=[]
                    if len(pxy)>1 and mb[0]==1:
                        draw.line(screen,(C),(pxy[-1]),(pxy[-2]),S)
                #draws filled polygon
                else:
                    if mb[2]==1 and len(pxy)>1:
                        draw.polygon(screen,(C),pxy)
                        pxy=[]
                    if len(pxy)>1 and mb[0]==1:
                        draw.aaline(screen,(C),(pxy[-1]),(pxy[-2]),1)
            screen.set_clip(None)

        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvas)
            if tool=="fill":
                #the surface colour of whatever is clicked
                sc=screen.get_at((mx,my))
                #if the surface colour isnt the currect colour chosen, program will fil
                if sc!=C:
                    #made list for the edge of how much to fill, starting with the point that is first clicked
                    edge=[[mx,my]]
                    #for all the coordinates in edge, and 1 pixel above, below, to the right and left
                    #if those pixels are the same colour as whatever surface was clicked first, it will be coloured with the colour selected
                    for (mx,my) in edge:
                        for (mmx,mmy) in ((mx+1,my),(mx-1,my),(mx,my+1),(mx,my-1)):
                            if screen.get_at((mmx,mmy))==sc:
                                screen.set_at((mmx,mmy),C)
                                #adds those coordinates to the edge of how much to fill so the colour fills every pixel
                                edge.append((mmx,mmy))         
            screen.set_clip(None)
#------------------------------------------------------------------------------#            
        #for all stampes
        #transforms image size based on mx and my position
        #flips image according to which direction it is dragged
        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="SS Link":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Link,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Link,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Link,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Link,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
          
            screen.set_clip(None)

        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="SS Zelda":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Zelda,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Zelda,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Zelda,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Zelda,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
            screen.set_clip(None)

        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="Ghira":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Ghira,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Ghira,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Ghira,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Ghira,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
            screen.set_clip(None)

        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="Fi":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Fi,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Fi,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Fi,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Fi,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
            screen.set_clip(None)

        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="Impa":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Impa,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Impa,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Impa,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Impa,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
            screen.set_clip(None)

        if mb[0]==1:
            screen.set_clip(canvas)
            if tool=="Groose":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Groose,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Groose,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.smoothscale(Groose,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.smoothscale(Groose,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
            screen.set_clip(None)
            
        if mb[0]==1 and canvas.collidepoint(mmx,mmy):
            screen.set_clip(canvas)
            if tool=="loaded image":
                screen.blit(oldscreen,(0,0))
                if mx>mmx and my>mmy and mb[0]==1:
                    SLink=transform.scale(picture,(mx-mmx,my-mmy))
                    screen.blit(SLink,(mmx,mmy))
                if mx<mmx and my<mmy and mb[0]==1:
                    SLink=transform.scale(picture,(mmx-mx,mmy-my))
                    SLink=transform.flip(SLink,True,True)
                    screen.blit(SLink,(mx,my))
                if mx>mmx and my<mmy and mb[0]==1:
                    SLink=transform.scale(picture,(mx-mmx,mmy-my))
                    SLink=transform.flip(SLink,False,True)
                    screen.blit(SLink,(mmx,my))
                if mx<mmx and my>mmy and mb[0]==1:
                    SLink=transform.scale(picture,(mmx-mx,my-mmy))
                    SLink=transform.flip(SLink,True,False)
                    screen.blit(SLink,(mx,mmy))
            screen.set_clip(None)
#------------------------------------------------------------------------------#        
        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            if tool=="Eye": 
                screen.blit(oldscreen,(0,0))
                if mb[0]==1:
                    #filled transparent cover red
                    cover.fill((255,0,0))
                    #drew circle which is not affected by transparent cover
                    #this is by selecting the colourkey which isn't affected by
                    #transparancy(255,255,254)
                    draw.circle(cover,(255,255,254),(mx-400,my-100),50)
                    #for all the pixels within a range of 50 and used distance formula
                    #to make it circular
                    for i in range(-50,50):
                        for j in range(-50,50):
                            cx=mx-i
                            cy=my-j
                            dist=int(sqrt((mx-cx)**2 +(my-cy)**2))
                            if dist<50:
                                pixC=screen.get_at((cx,cy))
                                #set the inverse colour for each of these pixels
                                #this is by subtracting their value from 255
                                r=255-pixC[0]
                                g=255-pixC[1]
                                b=255-pixC[2]
                                screen.set_at((cx,cy),(r,g,b))
                    #add the cover to canvas
                    screen.blit(cover,(400,100))
                #if mouse is not clicked, then screen is normal
                elif mb[0]!=1:
                    screen.blit(oldscreen,(0,0))
            screen.set_clip(None)

#------------------------------------------------------------------------------#

        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)
            if tool=="crop":
                #while the length of list crop is 0, it draws a rectangle like the
                #rect tool and copies it
                #while dragging, a rectangular outline is drawn to indicate the area
                #you are able to drag
                #set the flag of r and increase it so only after do you do draw the rectangle
                #and you let go of left click that it adds something to the list
                if mb[0]==1 and len(lcrop)==0:
                    if my>mmy:
                        a=1
                        n=0
                    else:
                        a=0
                        n=1
                    if mx>mmx:
                        b=1
                        m=0
                    else:
                        b=0
                        m=1
                    c=max(mmx,mx)
                    d=min(mx,mmx)
                    e=max(mmy,my)
                    f=min(my,mmy)
                    screen.blit(oldscreen,(0,0))
                   
                    irect=Rect(d,f,c-d,e-f)
                    cimage=screen.subsurface(irect).copy()
                    draw.rect(screen,(0,0,0),(d,f,c-d,e-f),1)
                    dot(mx,my,mmx,mmy)
                    rimage=screen.subsurface(irect).copy()
                    r+=1
                if mb[0]==0 and len(lcrop)==0 and r>0:
                    lcrop.append(cimage)
                    #r=0 this makes the picture unable to lose outline without moving
                    go=False
                    selected=False
                    Second=False
                    Third=False
                #if after the length of lcrop is greater that 0 and the user presses down on the rectange
                #are they able to drag it
                if mb[0]==1 and irect.collidepoint(mx,my) and len(lcrop)>0:
                    if go==False:
    
                        screen.blit(oldscreen,(0,0))
                        #draws a white rectangle where the cropped image used to be
                        draw.rect(screen,(255,255,255),(d,f,c-d,e-f))
                        z=screen.copy()
                        u=mx-(mmx-d)
                        v=my-(mmy-f)
                        x=mmx-d
                        y=mmy-f
                        screen.blit(cimage,(mx-x,my-y))
                        
                        
                        Second=True
                    elif go:
                
                        finale=True
                        screen.blit(z,(0,0))
                        s=mx-(c-d)/2
                        t=my-(e-f)/2
                        screen.blit(cimage,(s,t))
                        Second=False
                        Third=True
                        
                    #blit it relative to where my mouse is holding on
                    #constantly change the position of the irect so it can be dragged anywhere
                    irect=Rect(400,100,550,550)
                    #used asa flag to indicate whether cropped image was dragged
                    r+=1
                    selected=True
                #if the mouse does not collide with the rectangle while the length of
                #lcrop is 0, then the list is reset to 0 and function is reset to making
                #the first step(making the rectangle and copying image of that rectangle)
                if len(lcrop)>0 and mb[0]==1 and irect.collidepoint(mx,my)==False:
                    #if cropped image is not dragged then the image cropped is blitted again
                    #to get rid of rectangular outline
                    if r==0:
                        screen.blit(cimage,(d,f))
                        oldscreen=screen.copy()
                    elif Second:
                        screen.blit(cimage,(u,v))
                        oldscreen=screen.copy()
                        
                    elif Third:
                        screen.blit(cimage,(s,t))
                        oldscreen=screen.copy()
                    lcrop=[]
                    
                if mb[0]==0 and selected==True:
                    if go==False:
                        irect=Rect(mx-(mmx-d),my-(mmy-f),c-d,e-f)
                        screen.blit(rimage,(u,v))
                        
                    if finale==True and go:
                        irect=Rect(mx-(c-d)/2,my-(e-f)/2,c-d,e-f)
                        screen.blit(rimage,(s,t))
                   
                    finale=False
                    go=True
                    selected==False
            screen.set_clip(None)

#------------------------------------------------------------------------------#
#stuff with colour
            
        if eyedrop.collidepoint(mx,my)==False and mb[0]==1:
            if tool=="eyedrop":
                #sets the colour as anything you click on that is not a button
                C=screen.get_at((mx,my))
                
        #getting the colour for colour palette                       
        if colcollide.collidepoint(mx,my) and mb[0]==1:
            C=screen.get_at((mx,my))
        #getting the colour for gradient palette
        if bwcollide.collidepoint(mx,my) and mb[0]==1:
            C=screen.get_at((mx,my))
            
        #shows what colour is currently selected      
        draw.rect(screen,(C),(1,238,133,66))
        #border for colour-shower
        draw.rect(screen,(0,0,0),(1,238,134,65),2)

#------------------------------------------------------------------------------#

        #makes the mouse position at the end of the code the old mouse position        
        omx,omy=mx,my

        #2 borders for canvas
        bord=draw.rect(screen,(0,0,0),(400,100,550,550),3)
        bord2=draw.rect(screen,(255,215,0),(400,100,550,550),1)
        #defines cold screen (cursorless old screen) before Run is true and cursor is blitted
        coldscreen=screen.copy()
        #the copy for just the canvas
        copy=screen.subsurface(RECT).copy()

        #when mouse is able to showcursor
        Run=True

        #if showing cursor is true, then blit the cursor to mouse position
        if showcurs:
            screen.blit(cursor,(mx-31,my-32))
#------------------------------------------------------------------------------#
    display.flip()
quit()

