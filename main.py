import pygame
import numpy as np


#this is how many columns and rows there in our grid/screen
col_count = 10
row_count = 10

#we are declaring the RGB values for the colours before we use them.

#for the sky
blue = (0, 0, 200)

#for the floor amd maybe the columns
red = (200, 0, 0)

#also for the floor
black = (0, 0, 0)

#this is how big our squares are. we could make them samller but i think bigger squares are great 
#for our end users. the rest if the code is just for the peremeters of the screen
square_size = 40
width = col_count * square_size
height = row_count * square_size
size = (width, height)

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
    pass
    

def create_floor():
    #drawing floor
    pass
    

board = create_board()
draw_board(board)
create_floor() 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break



    clock.tick(30)

pygame.quit()