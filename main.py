import pygame
import sys

pygame.init()
SCREENSIZE = (300,300)
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('TicTacToe')
icon = pygame.image.load('icon.png').convert_alpha()
pygame.display.set_icon(icon)
l = ['×','○']
chance = '×'
clicked = bool()
p1, p2, p3, p4, p5, p6, p7, p8, p9 = 0,0,0,0,0,0,0,0,0
pos_list = ['','','','','','','','','']


def draw_lines():
    pygame.draw.line(screen,'#ffffff',(100,0),(100,300),10)
    pygame.draw.line(screen,'#ffffff',(200,0),(200,300),10)
    pygame.draw.line(screen,'#ffffff',(0,100),(300,100),10)
    pygame.draw.line(screen,'#ffffff',(0,200),(300,200),10)

def click_event():
    global clicked
    if pygame.mouse.get_pressed()[0]and clicked == False:
        clicked = True
        return True
        
    if pygame.mouse.get_pressed()[0] == 0:
        clicked = False
    return False

def cheq_pos():
    global p1,p2,p3,p4,p5,p6,p7,p8,p9
    mouse = pygame.mouse.get_pos()
    if (mouse[1] > 0) and (mouse[1] < 100):
        if (((mouse[0] >  -1) and (mouse[0] < 100)) and pygame.mouse.get_pressed()[0])and p1 == False:
            p1 = True
            
            return 1
        if (((mouse[0] >  100) and (mouse[0] < 200)) and pygame.mouse.get_pressed()[0])and p2 == False:
            
            p2 = True
            
            return 2
        if (((mouse[0] >  200) and (mouse[0] < 300)) and pygame.mouse.get_pressed()[0])and p3 == False:

            p3 = True
            
            return 3
            
    if (mouse[1] > 100) and (mouse[1] < 200):
        if (((mouse[0] >  -1) and (mouse[0] < 100)) and pygame.mouse.get_pressed()[0])and p4 == False:

            p4 = True
            
            return 4
        if (((mouse[0] >  100) and (mouse[0] < 200)) and pygame.mouse.get_pressed()[0])and p5 == False:

            p5 = True
            
            return 5
        if (((mouse[0] >  200) and (mouse[0] < 300)) and pygame.mouse.get_pressed()[0])and p6 == False:

            p6 = True
            
            return 6

    if (mouse[1] > 200) and (mouse[1] < 300):
        if (((mouse[0] >  -1) and (mouse[0] < 100)) and pygame.mouse.get_pressed()[0])and p7 == False:

            p7 = True
            return 7
        if (((mouse[0] >  100) and (mouse[0] < 200)) and pygame.mouse.get_pressed()[0])and p8 == False:

            p8 = True
            return 8
        if (((mouse[0] >  200) and (mouse[0] < 300)) and pygame.mouse.get_pressed()[0]) and p9 == False:
            
            p9 = True
            return 9

def add_symbol(cellno):
    global pos_list,chance
    if cellno != None:
       index = cellno - 1
       pos_list[index] = chance
       l.reverse()
       chance = l[0]
       

def render():
    global pos_list
    class CellClass():
        def __init__(self,pos,x,y):
            self.label = pygame.font.SysFont('Monospace',100).render(pos_list[pos],1,'#ffffff')
            self.xpos = x
            self.ypos = y

        def draw(self):
             screen.blit(self.label,(self.xpos ,self.ypos ))
    p = 20
    q = -3
    cell1 = CellClass(0,p,q)
    cell2 = CellClass(3,p,q+100)
    cell3 = CellClass(6,p,q+200)
    cell4 = CellClass(1,p+100,q)
    cell5 = CellClass(4,p+100,q+100)
    cell6 = CellClass(7,p+100,q+200)
    cell7 = CellClass(2,p+200,q)
    cell8 = CellClass(5,p+200,q+100)
    cell9 = CellClass(8,p+200,q+200)

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()
    cell6.draw()
    cell7.draw()
    cell8.draw()
    cell9.draw()

def win_check():
    if (pos_list[0]==pos_list[1]==pos_list[2]=='×')\
        or\
        (pos_list[0]==pos_list[1]==pos_list[2]=='○'):

        pygame.draw.line(screen,'#fcf803',(0,50),(300,50),8)
        return True

    
    elif (pos_list[3]==pos_list[4]==pos_list[5]=='×')\
        or\
        (pos_list[3]==pos_list[4]==pos_list[5]=='○'):

        pygame.draw.line(screen,'#fcf803',(0,150),(300,150),8)
        return True


    elif (pos_list[6]==pos_list[7]==pos_list[8]=='×')\
        or\
        (pos_list[6]==pos_list[7]==pos_list[8]=='○'):

        pygame.draw.line(screen,'#fcf803',(0,250),(300,250),8)
        return True


    elif (pos_list[0]==pos_list[3]==pos_list[6]=='×')\
        or\
        (pos_list[0]==pos_list[3]==pos_list[6]=='○'):

        pygame.draw.line(screen,'#fcf803',(50,0),(50,300),8)
        return True

    
    elif (pos_list[1]==pos_list[4]==pos_list[7]=='×')\
        or\
        (pos_list[1]==pos_list[4]==pos_list[7]=='○'):

        pygame.draw.line(screen,'#fcf803',(150,0),(150,300),8)
        return True

    
    elif (pos_list[2]==pos_list[5]==pos_list[8]=='×')\
        or\
        (pos_list[2]==pos_list[5]==pos_list[8]=='○'):

        pygame.draw.line(screen,'#fcf803',(250,0),(250,300),8)
        return True


    elif (pos_list[2]==pos_list[4]==pos_list[6]=='×')\
        or\
        (pos_list[2]==pos_list[4]==pos_list[6]=='○'):

        pygame.draw.line(screen,'#fcf803',(300,0),(0,300),8)
        return True


    elif (pos_list[0]==pos_list[4]==pos_list[8]=='×')\
        or\
        (pos_list[0]==pos_list[4]==pos_list[8]=='○'):

        pygame.draw.line(screen,'#fcf803',(300,300),(0,0),8)
        return True

    else:
        return False

def main():
    global p1,p2,p3,p4,p5,p6,p7,p8,p9
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('#000000')
        draw_lines()
        if click_event():
            add_symbol(cheq_pos())

        render()
        if win_check():
            p1,p2,p3,p4,p5,p6,p7,p8,p9 = 1,1,1,1,1,1,1,1,1

        pygame.display.flip()



main()

