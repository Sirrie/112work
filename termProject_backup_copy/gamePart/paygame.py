import pygame,os
from pygame.locals import *
SCREENRECT = Rect(0,0,640,480)

class Spritesheet:
    def __init__(self,filename):
        self.sheet=pygame.image.load(os.path.join('data',filename)).convert()
    def imgat(self,rect,colorkey=None):
        rect =Rect(Rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet,(0,0),rect)
        if colokey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey,RLEACCEL)
        return image
    def imgsat(self,rects,colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect,colorkey))
        return imgs

class Arena:
    tileside = 31
    numxtiles =12
    numytiles =14
    topx = (SCREENRECT.width-SCREENRECT.width/tileside)/2
    topy = (SCREENRECT.height-SCREENRECT.height/tileside)/2
    rect = Rect(topx+tileside,topy+tileside,tileside*numxtiles,tileside*numytiles)
    def __init__(self):
        self.background = pygame.Surface(SCREENRECT.size).convert()


 

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size)

    Spritesheet = Spritesheet('1.jpg')

    background = pygame.Surface(SCREENRECT.size).convert()
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    pygame.display.update()

    all=pygame.sprite.RenderUpdates()

    clock = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            if (event.type == QUIT
                or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                return
        all.clear(screen,background)
        all.update()
        dirty=all.draw(screen)
        pygame.display.update(dirty)
        clock.tick(30)
if __name__ == '__main__':main()
