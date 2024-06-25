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
orange = (255, 150,0)

#score
white = (255,255,255)



#this is how big our squares are. we could make them samller but i think bigger squares are great 
#for our end users. the rest if the code is just for the peremeters of the screen
square_size = 40
width = col_count * square_size
height = row_count * square_size
size = (width, height)


#player y position (x position doesnt change
current_pos = 7
score = 0
highscore = 0

#starts pygame, sets up the csreen and the name for out app/game.
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Board")
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

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
    global score
    screen.fill(black)  
    draw_board(board)   # Redraw the board

    # restarts floor pattern
    floor_pattern = floor_pattern[1:] + floor_pattern[:1]
    column_pos = (column_pos - 1) % col_count

    if column_pos == 6:  # Hwen  the player go through collumn
        score += 1

    draw_floor(floor_pattern)
    draw_pipes(column_pos, gap_start)
    draw_score(score)

    pygame.display.update()
    return floor_pattern, column_pos

#checks uf the player can go up
def possible_up():
    return current_pos > 0

#creates a player and moves it up or down. += means down and vice versa because of how the board is drawn
def draw_player(current_pos, direction): 
    if direction == 'UP': 
        if possible_up(): current_pos -= 1 

    else: 
        if current_pos < row_count - 2: 
            current_pos += 1 
    # empty screen 
    screen.fill(black) 
    draw_board(board) 
    draw_floor(floor_pattern) 
    draw_pipes(column_pos, gap_start) 
    
    #ACTUAL PLAYER
    #yellow body
    player_x = 6 * square_size 
    player_y = current_pos * square_size 
    pygame.draw.rect(screen, yellow, (player_x, player_y, square_size, square_size)) 
    pygame.draw.rect(screen, black, (player_x, player_y, square_size, square_size), 1) 

    # Draw the orange beak 
    beak_width = square_size // 4 
    beak_height = square_size // 2 
    beak_x = player_x + square_size-(square_size/10) 
    beak_y = player_y + (square_size // 4) 
    pygame.draw.polygon(screen, orange, [(beak_x, beak_y), (beak_x + beak_width, beak_y + beak_height // 2), (beak_x, beak_y + beak_height)]) 

    #eye black
    radius = square_size//5
    eye_center_x = player_x+square_size//2
    eye_center_y = player_y+square_size//2 - 5
    pygame.draw.circle(screen, black, (eye_center_x, eye_center_y), radius)

    #eye white
    radius = square_size//10
    eye_center_x = player_x+square_size//2 + 2
    eye_center_y = player_y+square_size//2 - 5
    pygame.draw.circle(screen, white, (eye_center_x, eye_center_y), radius)


    draw_score(score) 
    pygame.display.update() 
    return current_pos

def draw_pipes(column_pos,gap_start):
    for row in range(row_count):
        if row < gap_start or row >= gap_start + 4: 
            pygame.draw.rect(screen, red, (column_pos * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (column_pos * square_size, row * square_size, square_size, square_size),1)

def check_collision(current_pos, column_pos, gap_start):
    if column_pos == 6:
        if current_pos < gap_start or current_pos >= gap_start + 4:
            return True
    if current_pos >= 16:
        return True    
    return False

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

def draw_start_screen():
    screen.fill(black)
    title_text = font.render("Pygame Board", True, white)
    start_text = small_font.render("Press Enter to Start", True, white)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height() // 2 - 20))
    screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2 - start_text.get_height() // 2 + 20))
    pygame.display.update()

def draw_game_over_screen(score, highscore):
    screen.fill(black)
    game_over_text = font.render("Game Over", True, white)
    score_text = small_font.render(f"Score: {score}", True, white)
    highscore_text = small_font.render(f"Highscore: {highscore}", True, white)
    retry_text = small_font.render("Press Enter to Retry", True, white)
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2 - 40))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 - score_text.get_height() // 2 - 10))
    screen.blit(highscore_text, (width // 2 - highscore_text.get_width() // 2, height // 2 - highscore_text.get_height() // 2 + 20))
    screen.blit(retry_text, (width // 2 - retry_text.get_width() // 2, height // 2 - retry_text.get_height() // 2 + 50))
    pygame.display.update()

def reset_game():
    global current_pos, score, gap_start, floor_pattern, column_pos, board
    current_pos = 7
    score = 0
    gap_start = np.random.randint(0, row_count - 5)
    floor_pattern = [((col * 18) % 256, 0, 0) for col in range(col_count)]
    column_pos = col_count - 1
    board = create_board()


gap_start=np.random.randint(0,row_count -5)
#randomly creates the gap
floor_pattern = [((col * 18) % 256, 0, 0) for col in range(col_count)]
column_pos = col_count - 1 
# Start column at the rightmost position

    

board = create_board()
draw_board(board)
draw_floor(floor_pattern)
draw_pipes(column_pos,gap_start)
draw_score(score)

game_running = False
game_over = False


while True:
    if not game_running and not game_over:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_running = True
                    reset_game()
    
    elif game_running:
        upper = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_pos = draw_player(current_pos, "UP")
                    upper = True
        
        floor_pattern, column_pos = move_floor(floor_pattern, column_pos, gap_start)
        if column_pos == col_count - 1:
            gap_start = np.random.randint(0, row_count - 5)
        
        if not upper:
            current_pos = draw_player(current_pos, "DOWN")
        
        if check_collision(current_pos, column_pos, gap_start):
            game_running = False
            game_over = True
            if score > highscore:
                highscore = score
    
    elif game_over:
        draw_game_over_screen(score, highscore)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    game_running = True
                    reset_game()

    clock.tick(5)





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



