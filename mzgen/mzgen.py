import pygame
import random


mazewidth = int(input('Maze Width: '))
mazeheight = int(input('Maze Height: '))

#[visited, top, bottom, left, right]
mazeboard = [[[0, 0, 0, 0, 0] for i in range(mazewidth)] for j in range(mazeheight)]



def allvisited(mazeboard):
	flag = True
	for y in range(0, len(mazeboard)):
		for x in range(0, len(mazeboard[0])):
			if mazeboard[y][x][0] == 0:
				flag = False
				break;
	return flag

def aremoves(x, y):
	moveup = True
	movedown = True
	moveleft = True
	moveright = True


	#determine if cell is on the edge
	if x == 0:
		moveleft = False
	if y == 0:
		moveup = False
	if x == mazewidth - 1:
		moveright = False
	if y == mazeheight - 1:
		movedown = False


	if moveleft == True:
		if mazeboard[y][x - 1][0] == 1:
			moveleft = False
	if moveup == True:
		if mazeboard[y - 1][x][0] == 1:
			moveup = False
	if moveright == True:
		if mazeboard[y][x + 1][0] == 1:
			moveright = False
	if movedown == True:
		if mazeboard[y + 1][x][0] == 1:
			movedown = False

	possiblemoves = []
	if moveleft == True:
		possiblemoves.append("moveleft")
	if moveright == True:
		possiblemoves.append("moveright")
	if movedown == True:
		possiblemoves.append("movedown")
	if moveup == True:
		possiblemoves.append("moveup")

	if len(possiblemoves) == 0:
		return False
	else:
		return True

def selectpossiblemove(x, y):
	
	moveup = True
	movedown = True
	moveleft = True
	moveright = True


	#determine if cell is on the edge
	if x == 0:
		moveleft = False
	if y == 0:
		moveup = False
	if x == mazewidth - 1:
		moveright = False
	if y == mazeheight - 1:
		movedown = False


	if moveleft == True:
		if mazeboard[y][x - 1][0] == 1:
			moveleft = False
	if moveup == True:
		if mazeboard[y - 1][x][0] == 1:
			moveup = False
	if moveright == True:
		if mazeboard[y][x + 1][0] == 1:
			moveright = False
	if movedown == True:
		if mazeboard[y + 1][x][0] == 1:
			movedown = False

	possiblemoves = []
	if moveleft == True:
		possiblemoves.append("moveleft")
	if moveright == True:
		possiblemoves.append("moveright")
	if movedown == True:
		possiblemoves.append("movedown")
	if moveup == True:
		possiblemoves.append("moveup")

	if len(possiblemoves) == 0:
		return False


	rint = random.randint(0, len(possiblemoves) - 1)
	return possiblemoves[rint]



#[visited, top, bottom, left, right]
def movecell(x, y):
	mazeboard[y][x][0] = 1

	m = aremoves(x, y)
	if allvisited(mazeboard) == True:
		return False
	while m == True:
		move = selectpossiblemove(x, y)
		if move == "moveleft":
			mazeboard[y][x][3] = 1
			mazeboard[y][x - 1][4] = 1
			movecell(x - 1, y)
			m = aremoves(x, y)

		elif move == "moveright":
			mazeboard[y][x][4] = 1
			mazeboard[y][x + 1][3] = 1
			movecell(x + 1, y)
			m = aremoves(x, y)

		elif move == "movedown":
			mazeboard[y][x][2] = 1
			mazeboard[y + 1][x][1] = 1
			movecell(x, y + 1)
			m = aremoves(x, y)

		elif move == "moveup":
			mazeboard[y][x][1] = 1
			mazeboard[y - 1][x][2] = 1
			movecell(x, y - 1)
			m = aremoves(x, y)

	return False
		
		

pygamew = mazewidth * 100
pygameh = mazeheight * 100

pygame.init()
gameDisplay = pygame.display.set_mode((pygamew,pygameh))
pygame.display.set_caption('Maze Generator')



def generateMaze(mazeboard):
	startingy = 0
	startingx = 0

	movecell(startingx, startingy)



def updateboard(board):
	for y in range(0, len(board)):
		for x in range(0, len(board[0])):
			if mazeboard[y][x][1] == 0:
				pygame.draw.line(gameDisplay, (0,0,255), (x * 100, y * 100), (x * 100 + 100, y * 100))
			if mazeboard[y][x][2] == 0:
				pygame.draw.line(gameDisplay, (0,0,255), (x * 100, y * 100 + 100), (x * 100 + 100, y * 100 + 100))
			if mazeboard[y][x][3] == 0:
				pygame.draw.line(gameDisplay, (0,0,255), (x * 100, y * 100), (x * 100, y * 100 + 100))
			if mazeboard[y][x][4] == 0:
				pygame.draw.line(gameDisplay, (0,0,255), (x * 100 + 100, y * 100), (x * 100 + 100, y * 100 + 100))
			
generateMaze(mazeboard)	

crashed = False
clock = pygame.time.Clock()

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True



    updateboard(mazeboard)

    pygame.display.update()


    clock.tick(60)
