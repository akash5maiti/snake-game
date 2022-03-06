####
#this a program for basic snake game
###
import turtle
import random
import time           
##we are using the turtle,for the graphics and animation
##random mainly used to create food at random positions as required
##time is used indelaying the time to start a new game after the game is over
 
w = 500
h = 500     
food_size = 10
delay = 100
global score,highest_score ## globalizing the variables so it can be used within some functions
highest_score=0
score=0    
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}
## we are initializing important variables as in food_size for food size,w_h for the width and height of the window,others are scores,except offset.

pe = turtle.Turtle()

pe.color('white')
pe.penup()
pe.hideturtle()
pe.goto(216, 228)
pe.write('Score: 0', align='right', font=('ubuntu', 14, 'bold')) 
##creating object pe to display score on turtle screen with specifications

rop=turtle.Turtle()
rop.color('gold')
rop.penup()
rop.hideturtle()
rop.goto(-246,228)
rop.write('Highest Score: 0',align='left',font=('ubuntu',15,'italic'))
##creating object pe to display highest score on turtle screen with specifications


def reset():
    global snake, snake_dir, food_position  ##to use the globalized variables
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
##created a function reset , to start a new game after a game over
     
def move_snake():          ## function to control and animate the movement of the snake
    global snake_dir
    
    new_head = snake[-1].copy()      ##creating new heads
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
 
     
    if new_head in snake[:-1]:        ##setting a condition for game over
        game_over()    ## calling the function game over as the head of the snake hits its body/tail
        reset()        ##to reset the game after game over
        pe.clear()     ##to clear the score and reset at 0
    else:
        snake.append(new_head)    ##creating a new head/body as it eats a food
 
     
        if not food_collision():
            snake.pop(0)
        else:
            global score
            score=score+10         ## increasing score for a food eaten
            pe.clear()
            pe.write(f'Score: {score} ', align='right',font=('ubuntu', 14, 'bold'))      ##rewriting the increased score

        
 
 
        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
        ## if the snake goes out of the boundary,then making the snake head come out of its opposite end
 
 
        pen.clearstamps()
 
         
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
 
         
        screen.update()
 
        turtle.ontimer(move_snake, delay)
 
def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False
##setting condition for the snake to eat food make the food dissapear
 
def get_random_food_position():
    x = random.randint(- w / 2 + food_size, w / 2 - food_size)
    y = random.randint(- h / 2 + food_size, h / 2 - food_size)
    return (x, y)
##function to assign food randomly to continue the game
 
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance
## we use this function to know if snake has gotten closer to the food

def go_up():
    global snake_dir
    if snake_dir != "down":
        snake_dir = "up"  
 
def go_right():
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"
 
def go_down():
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"
 
def go_left():
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
##go_up/doe/right/left are the main controls that the player would use to control the movement of the snake 

def game_over():     ##function game over.
    t =turtle.Turtle()
    t.goto(0, 0)
    t.color('orange')
    t.penup()
    t.hideturtle()
    t.write('Game Over\n', align='center', font=('ubuntu', 26, 'bold'))
    t.write('Please wait a while to play again!!',
            align='center', font=('ubuntu', 14, 'bold'))   ##game over message
    time.sleep(3)
    t.clear()
    time.sleep(1)  ## delaying time to reset()
    global score,highest_score

    rop.clear()
    if score>highest_score:
        highest_score=score          
    rop.write(f'Highest_Score: {highest_score} ', align='left',font=('ubuntu', 15, 'italic'))      ##writing/rewriting the highest sore

    score=0     ##setting the score to 0 again

    
screen = turtle.Screen()
screen.setup(w, h)
screen.title("snake(akash)")
screen.bgcolor("indigo")
screen.setup(500, 500)
screen.tracer(0)
##completing the screen set up
 
 
pen = turtle.Turtle("circle")
pen.penup()
pen.color('orange')
##object pen to create snake
 
 
food = turtle.Turtle()
food.shape("turtle")
food.color("red")
food.shapesize(food_size / 20)
food.penup()
##object food for the foodof snake
 
 
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
##using onkey to trace the keyboard buttons pressed by the player and operate accordingly 
 
reset()
turtle.done()

