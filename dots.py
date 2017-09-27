from math import *
from random import*
from pygame import*
x=800
y=600
size= width, height = x, y
screen = display.set_mode(size)
screen.fill((255,255,255))
running=True
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        mx,my=mouse.get_pos()#mouse position
        mb=mouse.get_pressed()#mouse getting pressed
        if evnt.type==MOUSEBUTTONDOWN:
            oldscreen=screen.copy()
            mmx,mmy=mouse.get_pos()
        if mb[0]==1:
            screen.blit(oldscreen,(0,0))
            draw.rect(screen,(0,0,0),(mmx,mmy,mx-mmx,my-mmy),1)
            f=int((max(mx,mmx)-min(mmx,mx))/10)
            e=int((max(my,mmy)-min(mmy,my))/10)
            for i in range(f):
                draw.line(screen,(255,255,255),(min(mmx,mx)+5+(i*10),mmy),(min(mmx,mx)+(i*10),mmy),1)
                draw.line(screen,(255,255,255),(min(mmx,mx)+5+(i*10),my-1),(min(mmx,mx)+(i*10),my-1),1)
            for i in range(e):
                draw.line(screen,(255,255,255),(mmx,min(mmy,my)+5+(i*10)),(mmx,min(mmy,my)+(i*10)),1)
                draw.line(screen,(255,255,255),(mx-1,min(mmy,my)+5+(i*10)),(mx-1,min(mmy,my)+(i*10)),1)

        display.flip()
quit()
