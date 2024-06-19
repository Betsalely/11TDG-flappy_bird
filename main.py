import pygame
import numpy as np


#this is how many columns and rows there in our grid/screen
col_count = 25
row_count = 18

#we are declaring the RGB values for the colours before we use them.

#for the sky
blue = (45, 100, 245)

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
        color = floor_pattern[col]
        pygame.draw.rect(screen, color, (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        pygame.draw.rect(screen, black, (col * square_size, (row_count - 1) * square_size, square_size, square_size), 1)

def move_floor(floor_pattern, column_pos, gap_start):
    screen.fill(black)  
    draw_board(board)   # Redraw the board

    # restarts floor pattern
    floor_pattern = floor_pattern[1:] + floor_pattern[:1]
    column_pos = (column_pos - 1) % col_count

    draw_floor(floor_pattern)
    draw_pipes(column_pos, gap_start)
    pygame.display.update()
    return floor_pattern, column_pos

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
    draw_pipes(column_pos,gap_start)

    #actual player
    pygame.draw.rect(screen, yellow, (6 * square_size, current_pos * square_size, square_size, square_size))
    pygame.draw.rect(screen, black, (6 * square_size, current_pos * square_size, square_size, square_size), 1)
    pygame.display.update()

    return current_pos

def draw_pipes(column_pos,gap_start):
    for row in range(row_count):
        if row < gap_start or row >= gap_start + 4: 
            pygame.draw.rect(screen, red, (column_pos * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (column_pos * square_size, row * square_size, square_size, square_size),1)

gap_start=np.random.randint(0,row_count -5)
#randomly creates the gap
floor_pattern = [((col * 18) % 256, 0, 0) for col in range(col_count)]
column_pos = col_count - 1 
# Start column at the rightmost position

    

board = create_board()
draw_board(board)
draw_floor(floor_pattern)
draw_pipes(column_pos,gap_start)

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


    floor_pattern, column_pos = move_floor(floor_pattern, column_pos, gap_start)
    if column_pos == col_count - 1: 
        gap_start = np.random.randint(0, row_count - 5)

    
    #moves it down if spavce is not pressed
    if not upper:
        current_pos = draw_player(current_pos, "DOWN")

    clock.tick(5)

pygame.quit()




#please add some example code on how to draw a square in pygame. 
#maybe do like what each parameter 
#means and then do an example using some
# of our variables like square_size.



# PUT CODE HERE

#pygame.draw.rect(*1, *2, (*3,*4,*5,*6))

#*1 = where we draw the square (like screen)
# *2 = colour. ususlly a constant whose RGB is previsouly established
# *3 and *4 = the actually posotion of the square. in loops you can mutilpy it by the
# rows and cols
# *5 and *6 = height and width of square. IN our code we have a constant called 
# square_size so we use that. 



