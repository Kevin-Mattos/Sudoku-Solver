import sys, pygame, time, math, random
import classes 
RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 200,200,200
blockSize = 30
margin = 2
fullSize = blockSize + margin
width, height = 9*(fullSize), 9 * (fullSize)
compensation = 6
size = width + blockSize + compensation, height + blockSize + compensation

def imp(grid):
    for i in range(9):
        for j in range(9):
            print(str(grid[i][j].num) + " ", end = "")   
        print("")        

def fillBoard():
    marginY = 0
    marginX = 0
    a = []
    margemX = math.ceil(fullSize/2)
    for x in range(math.floor(width/(fullSize))): 
        a.append([])       
        marginY = math.ceil(fullSize/2)  
        if(x % 3 == 0 and x != 0):
            margemX += 3
        for y in range(math.floor(height/(fullSize))):     
            tamanhox =  x*(fullSize)            
            tamanhoy = y*(fullSize)

            if(y % 3 == 0 and y != 0):
                marginY+=3

            rect = pygame.Rect(tamanhox +  margemX, tamanhoy + marginY, blockSize, blockSize)
            but = classes.Button((tamanhox + margemX, tamanhoy + marginY), rect, fullSize)
            
            a[x].append(but)
            #print(str(but.vetpos) + "", end = "")
            screen.blit(but.image, but.pos)
    return a


def getBoard(grid):
    f=open("Grids.txt", "r")
    content = f.read()
    i = 0
    
    for linha in range(math.floor(width/(fullSize))): 
        for coluna in range(math.floor(height/(fullSize))): 
            if(content[i] == "\n"):
                i += 1
            grid[linha][coluna].displayNum(int(content[i]), screen)
            if(int(content[i]) != 0):
                grid[linha][coluna].fixed = True
            i += 1
            
    f.close()

def sudokuSolver(grid):
    num = [1,2,3,4,5,6,7,8,9,10]
   #y= linha
   #x = coluna
    linha = 0
    coluna = 0
    verificador = 0

    while( linha < math.floor(width/(fullSize))):         
        while(coluna < (math.floor(height/(fullSize)))): 
            if(not (grid[linha][coluna].fixed)):
                while(verificador != 10 and not grid[linha][coluna].fixed):                    
                
                    if(grid[linha][coluna].num == 0 and canItBeThere(grid, (linha, coluna), verificador)):
                    
                        if(grid[linha][coluna].displayNum(verificador, screen)):
                            pygame.display.flip()                        
                            time.sleep(.5)
                            break
                    else:
                        verificador += 1

                if(verificador == 10):                    
                    while(not grid[linha][coluna].removeNum(screen)):
                        linha, coluna = backtrack((linha,coluna))
                        verificador = grid[linha][coluna].num
                   
                    pygame.display.flip() 

            
        
                    
                
            print("aumentando coluna", coluna +1)
            coluna += 1  
        print("aumentando linha", linha +1)
        linha += 1
        coluna = 0  
            
    """
            if(verificador == 10):
                x, y = backtrack((x,y))
                print("retorne: ",x,y)
                verificador = 0
                grid[x][y].removeNum(screen)
            for num in nums:
                if(num == 10):
                    verificador = 10                    
                elif(grid[x][y].num == 0 and canItBeThere(grid,(x, y), num)):
                    grid[x][y].displayNum(num, screen)
                    pygame.display.flip()
                    time.sleep(2)
                    break
                
                    
            """

def recursive(grid):  
    pos = [0,0]
    
    pygame.display.flip() 

    time.sleep(.08)
    
    if(not emptyLocations(grid, pos)):
        return True

    linha = pos[0]
    coluna = pos[1]
    print("posicao:", (linha, coluna))
    for i in range(1,10):
        #if(button.fixed):            
        #    recursive(grid, grid[pos[0]][pos[1]])
        #    return True
        
        if(canItBeThere(grid,(linha, coluna), i)):   
           
            grid[linha][coluna].displayNum(i, screen)
            if(recursive(grid)):
                return True

            grid[linha][coluna].removeNum(screen)

    return False

def emptyLocations(grid, l):

    for i in range(9):        
        for j in range(9):
            if(grid[i][j].num == 0):
                l[0] = i
                l[1] = j
                return True
    return False
                 

def backtrack(pos):
    
    i = pos[0]
    j = pos[1]
    print("backtrack", i, j)
    if(j <= 0):
        return i - 1, 8
    else:
        return i, j - 1
            
def canItBeThere(grid, pos, num):
    
    for y in range(9):
        if (grid[pos[0]][y].num == num or grid[y][pos[1]].num == num):
            
            return False

    box = getBox(pos)
    
    for x in range(box[0], box[0] + 3):
        for y in range(box[1], box[1] + 3):            
            if( grid[x][y].num == num):
                return False
    
    
    return True

    

def getBox(pos):
    if(pos[0] < 3):
        x = 0
    elif(pos[0] < 6):
        x = 3
    else:
        x = 6
    if(pos[1] < 3):
        y = 0
    elif(pos[1] < 6):
        y = 3
    else:
        y = 6
    return x, y

        

pygame.init()

screen = pygame.display.set_mode(size)

screen.fill(GREY)
vet = fillBoard()

getBoard(vet)
print("________________________________")
#sudokuSolver(vet)
pygame.display.flip()
time.sleep(3)
recursive(vet)
print("acabou")
#imp(vet)
while(1):           
    # proceed events
    pygame.display.flip()
    ev = pygame.event.get()
    
    for event in ev: 

        #print(event)       
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                print("arrow pressed, exiting game")
                pygame.display.quit()
                pygame.quit()
                sys.exit()