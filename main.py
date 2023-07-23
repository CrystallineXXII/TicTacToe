import pygame as pg
import pickle as p
import socket
pg.init()


clock = pg.time.Clock()
screen = pg.display.set_mode((300,300))
pg.display.set_caption('TicTacToe')

font = pg.font.Font('Comfortaa.ttf', 50)
smolfont = pg.font.Font('Comfortaa.ttf', 20)
class Cell():
	def __init__(self,x,y):

		self.x = x
		self.y = y

		self.state = 0
		self.surf = pg.Surface((100,100))

	def update(self,screen,font:pg.font.Font):
		l = ['','x','o']

		label = font.render(l[self.state],1,'white').convert_alpha()
		label_rect = label.get_rect(center=(50,50))
		self.surf.blit(label,label_rect)
		pg.draw.rect(self.surf,(255,255,255),(0,0,100,100),2)
		screen.blit(self.surf,(self.x,self.y))


	def click(self,player):

		if self.state == 0:
			self.state = int(player) + 1
			return True

		
class Board(): 
	def __init__(self):
		self.cells = []
		for i in range(3):
			for j in range(3):
				self.cells.append(Cell(i*100,j*100))

		self.player = True

	def update(self,screen):
		for cell in self.cells:
			cell.update(screen,font)

		if self.check():
			return self.check()

		return 0

	def check(self):
		for i in range(3):
			if self.cells[i*3].state == self.cells[i*3+1].state == self.cells[i*3+2].state != 0:
				return self.cells[i*3].state
			if self.cells[i].state == self.cells[i+3].state == self.cells[i+6].state != 0:
				return self.cells[i].state
		if self.cells[0].state == self.cells[4].state == self.cells[8].state != 0:
			return self.cells[0].state
		if self.cells[2].state == self.cells[4].state == self.cells[6].state != 0:
			return self.cells[2].state
		
		if all([cell.state != 0 for cell in self.cells]):
			return 3
		return 0
	

def main():
	def event_handler():
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				x,y = event.pos
				for cell in board.cells:
					if cell.x < x < cell.x + 100 and cell.y < y < cell.y + 100:
						if cell.click(board.player):
							board.player = not board.player



	board = Board()

	while True:
		clock.tick(60)
		event_handler()
		screen.fill((0,0,0))
		result = board.update(screen)
		if result:
			surf = pg.Surface((300,300))
			surf.set_alpha(128)
			surf.fill((0,0,0))
			screen.blit(surf,(0,0))
			label = font.render(f'{[0,"x wins","o wins","Draw"][result]}!',1,'white')
			label_rect = label.get_rect(center=(150,150))
			screen.blit(label,label_rect)
			label = smolfont.render('<SPACE> to continue!',1,'orange')
			label_rect = label.get_rect(center=(150,250))
			screen.blit(label,label_rect)

			if pg.key.get_pressed()[pg.K_SPACE]:
				return main
		pg.display.flip()

if __name__ == '__main__':
	active = main
	while True:
		active = active()