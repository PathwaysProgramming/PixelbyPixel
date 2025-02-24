
# Imports
import 
import 
import 

# Screen setup
wn = turtle.Screen()
wn.("")             # Pick a name for your Window!
wn.bgcolor("")     
wn.setup(600, 600)       # The Size of the Window (x,y)
wn.tracer()             # Prevents Refreshing every step of the way (Makes it run smoother)(0 for off)
                         

# Snake Base Position
snake = turtle.Turtle()   #Create a Brush
snake.shape("")      #Shape of Brush
snake.color("")      #Color of the Brush
snake.penup()             #Gives us the Ability to lift the brush
snake.direction = "stop"  # stop is a place holder (doesn't mean anything)


# Food Base Position
food = turtle.Turtle()
food.
food.
food.
food.goto(, ) # first apple position (x,y)


# Acknowledge Functions


def go_up():
    snake.direction = "up"     #This ones Provided do the rest!


def go_down():
    


def go_left():
    


def go_right():
    

# Defining Functions

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
                                     #You Try!
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right":      
                                     #You Try!
        


# Keyboard bindings
wn.listen()                   #Tells computer to listen for input 
wn.onkeypress(go_up, "w")     #This ones done for you try the other three directions!


# Game loop (Rules)
speed = 0.1

while True:
    wn.update() #Constantly updates the screen when things move

    # Check collision with wall
    if abs(snake.xcor()) > 290 or abs(snake.ycor()) > 290:
                             #Where does the snake go to when it hits the edge
        snake.direction =    #How do we stop the snake from moving?
        speed =              # Reset speed when losing

    # Check collision with food
    if snake.distance(food) < 20:     #when the snake eats the apple then...
        food.goto(random.randint(-290, 290), random.randint(-290, 290)) #The apple goes between these integers
        speed *= 0.9  # Increase speed each time food is eaten

    move()  # makes the snake move based on it's direction
    time.sleep(speed)  # pauses the game a little bit controlling snakes speed

wn.mainloop()  # keeps window open and game runnin
