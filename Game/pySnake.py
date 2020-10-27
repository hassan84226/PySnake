#imports
import turtle # imports the "turtle" module, used for presenting game 
import time  # imports the "time" module, used for delays
import random # imports the "random" function, used for giving random coordinates for the apple 



# -*-*-*-*-*-*-*-*-*-*DATA MODEL-*-*-*-*-*-*-*-*-*-*
#direction constant values
DIR_UP = 0 #constant value for up direction is 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
direction = -1 #marks that original direction is none

# board dimensions
SCALE = 10
board_dim=20

# snake original attributes
snakeInitialLength=4 #starting length of the snake
initHeadPosition = (10, 10) #where the sbnake head starts off at
snake = [] #array of turtles of the FULL snake
snake_t = [] #array of turles of the snake body ONLY

# apple original attributes
apple = (100, 100) #where the apple starts off at
apple_t = turtle.Turtle() #marks that apple is a trutle object

# score
score_count=turtle.Turtle() #marks that the score counter is a turtle object, so that we can print it on the screen
score=0 #initial score is 0



#-*-*-*-*-*-*-*-*-*-*PRESENTATION-*-*-*-*-*-*-*-*-*-*
# screen
wn = turtle.Screen() #makes the screen presentable by turtle module
wn.tracer(0, 0) #Turn turtle animation on/off and set delay for update drawings
wn.bgcolor("green") #background color of the turtle screen is green
wn.screensize(SCALE*board_dim, SCALE*board_dim) #size of the screen (values are from the data model above)
wn.setworldcoordinates(0,0,SCALE*board_dim, SCALE*board_dim) #sets where 0,0 is on the screen



#-*-*-*-*-*-*-*-*-*-*FUCNTIONS-*-*-*-*-*-*-*-*-*-*
# function to initialize board, snake and apple
def initBoard() :
    global snake #collects snake list as a global value
    global apple #collects apple value as a global value
    global snakeInitialLength #collects initial snake length as a global value
    global initHeadPosition #collects initial head position as a global value

    # initialize snake
    for i in range(0, snakeInitialLength) : #for loop to append body parts to the empty snake list
        snake.append( (initHeadPosition[0]-i, initHeadPosition[1]) )#appends body parts to snake list
        t = turtle.Turtle() #'t' means snake head. makes 't' a turtle object
        t.shape("square") #makes the snake head a square
        if (i==0) : #means if i is in the first part of the snake list (is the head):
            t.color("blue") #the snake color will be blue, meaning it is the head
        else : #else, if i is not 0, then that means it is the body
            t.color("orange") #the square color will be orange, to symbolise the initial body
        t.up() #pen up while we are transpoting the turtles SO IT DOES NOT LEAVE A MARK ON THE BOARD
        t.goto( SCALE*(initHeadPosition[0]-i), SCALE*(initHeadPosition[1]) ) #will transport turtlized snake to its initial values in the data model
        t.down() #pen down now for snake turtles
        snake_t.append(t) #appends the initial body parts to the empty snake body list in the data model

    newApplePosition() #spawns the apple at a random posisiton




# generate a random position for the apple
def newApplePosition() :
    global apple #collects apple as a global value
    apple = (random.randint(1,board_dim), random.randint(1,board_dim)) #makes new apple coordinates a random position ON THE BOARD, NOT OUTSIDE
    printApple() #prints apple array (for testing purposes)
    apple_t.shape("circle") #makes apple shape a turtle and circular
    apple_t.color("red") #makes apple color red
    apple_t.up() #pen up for apple while we are transporting it to its new random position SO IT DOES NOT LEAVE A MARK ON THE BOARD
    apple_t.goto(SCALE*apple[0], SCALE*apple[1]) #transports apple to its new position
    apple_t.down() #pen down now for apple

    printApple() #prints apple location (for testing purposes)




# function to keep snake body trailing the snake head
def moveSnake(direction):
    global snake #collects snake array as a global value

    # move head
    head_x = snake[0][0] #indicates that the head of the snake is the first item in the array, and its 'x' is the [0] of that item
    head_y = snake[0][1] #indicates that the head of the snake is the first item in the array, and its 'y' is the [1] of that item
    if direction == DIR_UP : #if statement for if direction is equal to up
        head_y += 1 #the y coordinate of the snake head will increase by one
    elif direction == DIR_DOWN : #if statement for if direction is equal to down
        head_y -= 1 #the y coordinate of the snake head will decrease by one
    elif direction == DIR_LEFT : #if statement for if direction is equal to left
        head_x -= 1 #the x coordinate will decrease by one
    elif direction == DIR_RIGHT : #if statement for if direction is equal to right 
        head_x += 1 #the x cordinate will increase by one

    snake = [(head_x, head_y)] + snake[:len(snake)-1] #this is a line of code to make the first part of the body take the position of the snake head, and then the second body part will take that position

    for i in range (0, len(snake)) : 
        snake_t[i].up() #calls up function below to move snake_t[i]
        snake_t[i].goto(SCALE*snake[i][0], SCALE*snake[i][1]) #moves snake[i] to designated location on the scale
        snake_t[i].down()#calls down function below to move snake_t[i] 
        
    printSnake() #prints snake array (for testing purposes)




# function to check if the new head position collides with apple
def isAppleCollision(direction):
    global snake #collects snake array as a global value
    global apple #collects apple array as a global value

    head_x = snake[0][0] #indicates that the head of the snake is the first item in the array, and its 'x' is the [0] of that item
    head_y = snake[0][1] #indicates that the head of the snake is the first item in the array, and its 'y' is the [1] of that item
    if direction == DIR_UP : #the following lines up to the hashtags indicate the direction controls for the snake
        head_y += 1
    elif direction == DIR_DOWN :
        head_y -= 1
    elif direction == DIR_LEFT :
        head_x -= 1
    elif direction == DIR_RIGHT :
        head_x += 1 ################################################################################################################

    if (head_x == apple[0]) and (head_y == apple[1]): #if statement to check if the snake head collided with the apple coordinates
        print("Apple collision")
        return True #if the if condition is true, the function will return true
    return False #if the if condition is false, the function will return false




# function to check if the new head position collides with body
def isBodyCollision (direction):
    global snake #collects snake array as a global value
    if snake[0] in snake[1:]: #if condidion to check if the snake value if anywhere between snake[i] and the end of the list
        return True #if the if condiditon above is true, that means that the snake head collidied with the body, which means that the function returns true
    return False #if the if condiditon above is false, that means that the snake head did not collide with the body, which means that the function returns false




# check if the new head position collides with boarder
def isBoarderCollision(direction):
    global snake #collects snake array as a global value
    global board_dim #colects board_dim (in the data model above) as a global value. we need this value because we need to know where the walls of the board are located

    head_x = snake[0][0]#indicates that the head of the snake is the first item in the array, and its 'x' is the [0] of that item
    head_y = snake[0][1]#indicates that the head of the snake is the first item in the array, and its 'y' is the [1] of that item
    if direction == DIR_UP : #the following lines up to the hashtags indicate the direction controls for the snake
        head_y += 1
    elif direction == DIR_DOWN :
        head_y -= 1
    elif direction == DIR_LEFT :
        head_x -= 1
    elif direction == DIR_RIGHT :
        head_x += 1################################################################################################################

    if ( (head_x > board_dim) or (head_x < 0) or (head_y > board_dim) or (head_y < 0) ) : #checks if the snake head is anywhere in the boarder of the board
        print("BOARDER COLLISION")
        return True #if the conditions of the if statement are met, then that means the head collided with the wall, and the function will return true
    return False




# function to check for collisions and continue playing
# returns:
#   0: continue
#   1: apple collition
#   2: boarder collision or body collision
def checkCollisionsAndMove(direction) :
    global score #collects score and score_count as a global value, because we will increment it in this function
    global score_count 
    if (direction < 0) : #if direction is smaller than zero, meaning there is know direction, the game will resume, or in this case pause
        return 0 #the function will return zero to continue the game

    if (isBoarderCollision(direction)) or (isBodyCollision(direction)): #if the snake collides with the wall or collides with its own body, the game will end
        print("BORDER COLLISION OR BODY COLLISION")
        return 2 # the function will return 2 to stop the game

    tail = snake[len(snake)-1]  # stores last tail position
    appleCollision = isAppleCollision(direction) # checks for apple collision
    moveSnake(direction)# move snake to new position
    if (appleCollision == True) : #if the apple collision condition is met
        score_count.clear() #the score count will clear itself from its value
        score+=1 #and increment by one       
        score_count.penup() #penup for the score count
        score_count.hideturtle() #hiding turtle for the score count
        wn.update() #updating window to display the new snake value
        score_count.goto(100,180) #displays score count at the middle of the screen
        score_count.write("Your Score:"+(str)(score), align="center", font=("MS Serif", 24, "normal")) #prints the score in a certain font (cosmetic)
        wn.bgcolor("blue") #turns the screen blue for 0.05 seconds when the snake eats an apple
        time.sleep(0.05) 
        wn.bgcolor("green") #then the screen turns green again
        print("growing snake...") 
        snake.append(tail) # grow snake by adding the stored tail earlier
        t = turtle.Turtle() #adds that stored tail as a turtle
        t.shape("square") #makes it a square
        t.color("red") #that is red
        t.up() #pen up while it is moving to its location
        t.down() #then pen back down
        snake_t.append(t) #appending that value to the snake_t list in the data model
        printSnake() #prints snake (for testing purposes)
        newApplePosition() #spawns a new apple, since the last one was consumed
        time.sleep(0.0000000000000000000000001) #fast time sleep
        return 1 # function return 1 to indicate apple collision

    return 0 # else, if none of the above conditions are met, or after the snake eats an apple, return 0 to continue playing



# function for the game end or to refresh window if the game resumes
def next_frame():
    global direction
    
    if (checkCollisionsAndMove(direction) == 2) : #if the return from the check collision and move functuion is 2, the game ends
        wn.bye() #ends the game, by closing the window, after playing sound

    wn.ontimer(next_frame, 50) #updates the frame after 50 milliseconds, for smooth gameplay
    wn.update() #updates our window 
    time.sleep(0.1) #sleeps for 0.1 seconds 




# print snake array (for testing purposes)
def printSnake():
    print("snake: ", snake) 




# print apple position (for testing purposes)
def printApple() : 
    print("apple: ", apple)




#-*-*-*-*-*-*-*-*-*-*KEYBOARD HANDLING-*-*-*-*-*-*-*-*-*-*
def up():
    global direction #collects direction as a global
    if direction != DIR_DOWN: #if we are travelling up and user presses down, nothing happens (! means not)
        direction = DIR_UP  #else the directuion will be up

def down():
    global direction
    if direction != DIR_UP:
        direction = DIR_DOWN

def left():
    global direction
    if direction != DIR_RIGHT:
        direction = DIR_LEFT

def right():
    global direction

    if direction != DIR_LEFT:
        direction = DIR_RIGHT

#function to pause the game, by making direction = -1, which means nothing happens
def escape():
    global direction
    direction = -1







#
# -*-*-*-*-*-*-*-*-*-*MAIN PROGRAM-*-*-*-*-*-*-*-*-*-*
#
initBoard()
printSnake()

wn.onkeypress(up, 'Up') #up button press means calling up function
wn.onkeypress(down, 'Down')#down button press means calling down function
wn.onkeypress(left, "Left")#left button press means calling left function
wn.onkeypress(right, "Right")#right button press means calling right function
wn.onkeypress(escape, "Escape")#escape button press means calling pause function

next_frame() #calls next frame functuion, to update window for smooth gameplay
wn.listen() #listens for any keyboard presses
wn.mainloop() #turtle built in for end of program


print("**** GAME OVER ****")
