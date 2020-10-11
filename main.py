import pygame
from math import inf
import numpy as np
import time

pygame.init()

SCREENX = 1000
SCREENY = 750
FONT = pygame.font.SysFont('Arial', 72)

screen = pygame.display.set_mode((SCREENX, SCREENY))
global grid, itera
grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]
itera = 0
PLAYER = "X"
AI = "O"
# print((SCREENX/3)*2)
# print(SCREENX/3)
# print(((SCREENX/3)*2)- (SCREENX/3))

def clear_grid():
    global grid
    del grid
    grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
    ]

def empty_in_grid(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == None:
                count += 1
    return count

def is_game_won(grid):

    if empty_in_grid(grid) == 0:
        #print("Draw")
        return True, None

    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        #print("X wins Htop")
        return True, "X"

    if grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        #print("O wins Htop")
        return True, "O"

    if grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        #print("X wins Hmiddle")
        return True, "X"

    if grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        #print("O wins Hmiddle")
        return True, "O"

    if grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        #print("X wins HBottom")
        return True, "X"

    if grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        #print("O wins HBottom")
        return True, "O"

    if grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        #print("X wins VLeft")
        return True, "X"

    if grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        #print("O wins VLeft")
        return True, "O"

    if grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        #print("X wins Vmiddle")
        return True, "X"

    if grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        #print("O wins Vmiddle")
        return True, "O"
        
    if grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        #print("X wins VRight")
        return True, "X"

    if grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        #print("O wins VRight")
        return True, "O"

    if grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        #print("X wins D1")
        return True, "X"

    if grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        #print("O wins D1")
        return True, "O"

    if grid[2][0] == "X" and grid[1][1] == "X" and grid[0][2] == "X":
        #print("X wins D2")
        return True, "X"

    if grid[2][0] == "O" and grid[1][1] == "O" and grid[0][2] == "O":
        #print("O wins D2")
        return True, "O"

    else:
        return None, None

def copy_grid(grid):
    new_grid = []
    for row in grid:
        pl = []
        for col in row:
            pl.append(col)
        new_grid.append(pl)
        del pl
    return new_grid

def child_play_move(g, i, curPlayer):
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            if col == None and i == 0:
                g[r][c] = curPlayer
                return g
            if col == None:
                i -= 1

def miniMax_Tic_tac_toe(grid, depth, player):
    global itera
    itera += 1
    print(itera, depth)
    gameover, winner = is_game_won(grid)
    if depth == 0:
        return 0
    if gameover and winner == AI:
        return 10
    elif gameover and winner == PLAYER:
        return -10
    elif gameover and winner == None:
        return 0

    possible_moves = []
    for i in range(empty_in_grid(grid)):
        move = {}
        move['id'] = i
        g = child_play_move(copy_grid(grid), i, player)
        
        if player == "O":            
            move['res'] = miniMax_Tic_tac_toe(g, depth-1, "X")
        elif player == "X":
            move['res'] = miniMax_Tic_tac_toe(g, depth-1, "O")

        possible_moves.append(move)

    best_move = None
    if player == AI:
        best = -inf
        for move in possible_moves:
            if move['res'] > best:
                best = move['res']
                best_move = move['id']

    elif player == PLAYER:
        best = inf
        for move in possible_moves:
            if move['res'] < best:
                best = move['res']
                best_move = move['id']

    return best_move   


    
    # if Maxing:
    #     maxEval = math.inf
    #     for i in range(empty_in_grid(grid)): 
    #         g = child_play_move(copy_grid(grid), i, "X")
    #         evalu = miniMax_Tic_tac_toe(g, depth - 1, False)
    #         maxEval = max(maxEval, evalu)
    #     return maxEval
    # else:
    #     minEval = math.inf
    #     for i in range(empty_in_grid(grid)):
    #         g = child_play_move(copy_grid(grid), i, "O")
    #         evalu = miniMax_Tic_tac_toe(g, depth - 1, True)
    #         minEval = min(minEval, evalu)
    #     return minEval

running = True
isXturn = False

while running:

    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (SCREENX/3, SCREENY), (SCREENX/3, 0), 5)
    pygame.draw.line(screen, (0,0,0), (((SCREENX/3)*2), SCREENY), (((SCREENX/3)*2), 0), 5)
    pygame.draw.line(screen, (0,0,0), (0, SCREENY/3), (SCREENX, SCREENY/3), 5)
    pygame.draw.line(screen, (0,0,0), (0, ((SCREENY/3)*2)), (SCREENX, ((SCREENY/3)*2)), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not isXturn:
            x, y = pygame.mouse.get_pos()
            if 0 <= y <= 250:
                row = 0
            elif 250 <= y <= 500:
                row = 1
            else:
                row = 2
            if 0 <= x <= 333:
                col = 0
            elif 334 <= x <= 666:
                col = 1
            else:
                col = 2
            if pygame.mouse.get_pressed()[0]:
                if grid[row][col] == None:
                    grid[row][col] = "X"
                    isXturn = True

            if pygame.mouse.get_pressed()[2]:
                if grid[row][col] == None:
                    grid[row][col] = "O"

    count = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == None:
                colour = (255,255,255)
            elif col == "X":
                colour = (255,0,0)
            else:
                colour = (0,0,255)
            text = FONT.render(str(col), 1, colour)
            screen.blit(text, ((x*333) + 10, (y*250)+10))
            if col == None: 
                count += 1

    if is_game_won(grid)[0] == True:
        clear_grid()
    if isXturn:
        pygame.display.flip()
        play = miniMax_Tic_tac_toe(grid, -1, AI)
        child_play_move(grid, play, AI)
        isXturn = False
    pygame.display.set_caption(str(empty_in_grid(grid)))
    time.sleep(0.5)

    pygame.display.flip()