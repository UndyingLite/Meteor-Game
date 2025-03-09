import pygame as pyg 		#Import pygame from computer, and rename to pyg
import random			#Import random function

def set_speed(score):		#Create function “set_speed” with parameter “score”
    # if score <= 25:			
    #     speed = 10			#When score is less than 25, the speed of drop is 10
    # elif score <= 50:
    #     speed = 15			#When score is less than 50, the speed of drop is 15
    # elif score <= 75:
    #     speed = 20			#When score is less than 75, the speed of drop is 20
    # else:
    #     speed = 25			#Sets speed to 25 in all other conditions
    # return speed			#Returns value speed
    speed = (score * math.log(score + 1)) + 10
    return speed


def draw_meteors(met_list, met_dim, screen, yellow): #Takes from list and draws the meteors
    for i in range(len(met_list)):				
        x = met_list[i][0]					     #Adds to x and y for length of met_list
        y = met_list[i][1]           
        pyg.draw.rect(screen, yellow, (x, y, met_dim, met_dim))	#Draw rectangle for meteors
        
def drop_meteors(met_list, met_dim, width):#This defines a non-void function with 3 #parameters
    chance = random.randint(0,100)		#Sets chance as a random number
    if chance < 15:				
        y = 0					#If chance is < 15 set y to 0
        x = random.randrange(0, width, met_dim)
        coords = [x,y]				#Coords equal new x and y vals
        met_list.append(coords)    
    else:
        pass				#This makes it so if chance is >15, it passes through
    
def update_meteor_positions(met_list, height, score, speed): #Defines new 4 param. function
    '''
    update_meteor_positions takes four inputs: a nested list of meteor positions
    '''
    for i, values in enumerate(met_list):			
        met_list[i][1] += speed			#Adds the speed to met_list
        
        if met_list[i][1] >= height:		#Adds the height to met_list
            score += 1
            del met_list[i]       
            
            
    return score                                             #this returns the score to the overall function
            
def dectect_collision(player_possition, meteor_possition, player_size, meteor_size):
    player_x, player_y = player_pos
    # Loop through each meteor's position
    for meteor in meteor_positions:
        meteor_x, meteor_y = meteor
        # Check for overlap between the player and the meteor
        if (player_x < meteor_x + meteor_size and player_x + player_size > meteor_x and
            player_y < meteor_y + meteor_size and player_y + player_size > meteor_y):
            return True
    return False
					


def collision_check(collision):	#Defines new non-void function with one parameter
    '''
    Is a non-void function that takes four input: a list of
    meteor positions, a list of positions of the player, the
    size of the player, and the size of the meteors. The function
    calls the detect_collision for each meteor and will return True 
    to main if a collision is detected. Otherwise, it will continue
    to return false.
    '''
    if collision == True:
        return True
    if collision == False:
        return False

 

def main():			#Defines void function with no parameters
    '''
    Initialize pygame and pygame parameters.  Note that both player and meteors
    are square.  Thus, player_dim and met_dim are the height and width of the
    player and meteors, respectively.  Each line of code commented.
    '''
    pyg.init()                # initialize pygame

    width = 800               # set width of game screen in pixels
    height = 600              # set height of game screen in pixels

    red = (255,0,0)           # rgb color of player
    yellow = (244,208,63)     # rgb color of meteors
    background = (0,0,156)    # rgb color of sky (midnight blue)

    player_dim = 50           # player size in pixels
    player_pos = [width/2, height-2*player_dim]  # initial location of player
                                                 # at bottom middle; height
                                                 # never changes

    met_dim = 20              # meteor size in pixels
    met_list = []             # initialize list of two-element lists
                              # giving x and y meteor positions

    screen = pyg.display.set_mode((width, height)) # initialize game screen

    game_over = False         # initialize game_over; game played until
                              # game_over is True, i.e., when collision
                              # is detected

    score = 0                 # initialize score

    clock = pyg.time.Clock()  # initialize clock to track time

    my_font = pyg.font.SysFont("monospace", 35) # initialize system font

    while not game_over:                       # play until game_over == True
        for event in pyg.event.get():          # loop through events in queue
            if event.type == pyg.KEYDOWN:      # checks for key press
                x = player_pos[0]              # assign current x position
                y = player_pos[1]              # assign current y position
                if event.key == pyg.K_LEFT:    # checks if left arrow;
                    x -= player_dim            # if true, moves player left
                elif event.key == pyg.K_RIGHT: # checks if right arrow;
                    x += player_dim            # else moves player right
                player_pos = [x, y]            # reset player position
            
        screen.fill(background)                # refresh screen bg color
        drop_meteors(met_list, met_dim, width) # read PA prompt
        speed = set_speed(score)               # read PA prompt
        score = update_meteor_positions(met_list, height, score, speed)
                                               # read PA prompt
        text = "Score: " + str(score)              # create score text
        label = my_font.render(text, 1, yellow)    # render text into label
        screen.blit(label, (width-250, height-40)) # blit label to screen at
                                                   # given position; for our 
                                                   # purposes, just think of
                                                   # blit to mean draw
        draw_meteors(met_list, met_dim, screen, yellow) # self-explanatory;
                                                        # read PA prompt

        pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))                                        # draw player

        collision = dectect_collision(player_pos, met_list, player_dim, met_dim)
        if collision:
            game_over = True                       # read PA prompt
    
        clock.tick(30)                             # set frame rate to control
                                                   # frames per second (~30); 
                                                   # slows down game

        pyg.display.update()                       # update screen characters
    # Outside while-loop now.
    print('Final score:', score)                   # final score
    pyg.quit()                                     # leave pygame

main()


