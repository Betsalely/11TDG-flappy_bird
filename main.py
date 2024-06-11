import pygame
import numpy as np


#this is how many columns and rows there in our grid/screen
col_count = 13
row_count = 18

#we are declaring the RGB values for the colours before we use them.

#for the sky
blue = (0, 0, 200)

#for the floor amd maybe the columns
red = (200, 0, 0)

#also for the floor
black = (0, 0, 0)

#player
yellow = (200, 200, 0)

#this is how big our squares are. we could make them samller but i think bigger squares are great 
#for our end users. the rest if the code is just for the peremeters of the screen
square_size = 40
width = col_count * square_size
height = row_count * square_size
size = (width, height)


#player y position (x position doesnt change
current_pos = 7

#starts pygame, sets up the csreen and the name for out app/game.
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Board")

def create_board():
    board = np.zeros((row_count, col_count))
    return board

def draw_board(board):
    #thius is for the background of the boaard.
    for row in range(row_count):
        for col in range(col_count):
            pygame.draw.rect(screen, blue, (col * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (col * square_size, row * square_size, square_size, square_size), 1)
    pygame.display.update()
    

def draw_floor(floor_pattern):
    for col in range(col_count):
        pygame.draw.rect(screen, ((col*18),0,0), (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        color = floor_pattern[col]
        pygame.draw.rect(screen, color, (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        pygame.draw.rect(screen, black, (col * square_size, (row_count - 1) * square_size, square_size, square_size), 1)

def move_floor(floor_pattern):
    screen.fill(black)  
    draw_board(board)   # Redraw the board

    # restarts floor pattern
    floor_pattern = floor_pattern[1:] + floor_pattern[:1]

    draw_floor(floor_pattern)
    pygame.display.update()
    return floor_pattern

#checks if the player can go up
def possible_up():
    return current_pos > 0

#creates a player and moves it up or down. += means down and vice versa because of how the board is drawn
def draw_player(current_pos, direction):
    if direction == 'UP':
        if possible_up():
            current_pos -= 1

    else:
        if current_pos < row_count - 2: 
            current_pos += 1

    #empty screen
    screen.fill(black)
    draw_board(board)
    draw_floor(floor_pattern)

    #actual player
    pygame.draw.rect(screen, yellow, (6 * square_size, current_pos * square_size, square_size, square_size))
    pygame.draw.rect(screen, black,  (6 * square_size, current_pos * square_size, square_size, square_size), 1)
    pygame.display.update()

    return current_pos

#for floor gradient
floor_pattern = [((col * 18) % 256, 0, 0) for col in range(col_count)]
    

    

board = create_board()
draw_board(board)
draw_floor(floor_pattern)

#main game loop
while True:
    upper = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            #space bar pressed
            if event.key == pygame.K_SPACE:
                current_pos = draw_player(current_pos, "UP")
                upper = True


    floor_pattern = move_floor(floor_pattern)
    #moves it down if spavce is not pressed
    if not upper:
        current_pos = draw_player(current_pos, "DOWN")

    clock.tick(5)

pygame.quit()