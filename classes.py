import pygame, math



class Button(pygame.sprite.Sprite):
    
    def __init__(self, pos, rect, fullSize, num = 0):
        super().__init__()
        self.BLUE = pygame.Color('dodgerblue1')
        self.FONT = pygame.font.Font(None, 42)
        self.fixed = False
        self.num = num
        self.rect = rect
        self.pos = (pos[1], pos[0])
        self.vetpos = self.getPosByPixel(self.pos, fullSize)
        self.image = pygame.image.load('Images/0.png').convert()

    def displayNum(self, num, screen):

        self.num = num
        if(not self.fixed):
            self.image =  pygame.image.load('Images/{}.png'.format(self.num)).convert()
        else:
            self.image =  pygame.image.load('Images/{}Fixed.png'.format(self.num)).convert()

        self.setNumber(screen)
        print("setting {} at {}".format(num, self.vetpos))
        return not self.fixed

    def setNumber(self, screen):        
        screen.blit(self.image, self.pos)
        print("setting {} at {}".format(self.num, self.vetpos))
        
    def removeNum(self, screen):
        if(not self.fixed):
            self.image = pygame.image.load('Images/0.png').convert()
            screen.blit(self.image, self.pos)
            print("removing {} at {}".format(self.num, self.vetpos))
            self.num = 0
            return True
        return False

    def getPosByPixel(self, pos, fullSize):
        linha = math.floor((pos[0] - fullSize/2)/fullSize)
        coluna = math.floor((pos[1] - fullSize/2)/fullSize)    
        return coluna, linha 

    def getNext(self):
        i = self.vetpos[0]
        j = self.vetpos[1]
        if( j >= 8):
            return i + 1, 0
        elif(i == 8 and j == 8):
            return None
        else:
             return i, j+1

        
        