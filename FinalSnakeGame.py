
# Imports
import turtle
import time
import random

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("yellow")  # Or use hex wn.bgcolor('#a83279')
wn.setup(600, 600)
wn.tracer(0)

# Snake Base Position
snake = turtle.Turtle()
snake.shape("square") # Other built in shapes : arrow, turtle, triangle, classic. You can also import your own image / gif. 
snake.color("black")
snake.penup()
snake.direction = "stop"  # stop is a place holder (doesn't mean anything)

#upload image example 
#image uploaded : my_shape.png
#code : wn.register_shape("my_shape.png") background image
# snake.shape("my_shape.png")

# Food Base Position
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100) # first apple position


# Defining Functions


def go_up():
    snake.direction = "up"


def go_down():
    snake.direction = "down"


def go_left():
    snake.direction = "left"


def go_right():
    snake.direction = "right"

# Defining Movements

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Adding arrow key bindings
# wn.onkeypress(go_up, "Up")  # Up arrow for up
# wn.onkeypress(go_down, "Down")  # Down arrow for down
# wn.onkeypress(go_left, "Left")  # Left arrow for left
# wn.onkeypress(go_right, "Right")  # Right arrow for right

# Game loop (Rules)
speed = 0.1

while True:
    wn.update()

    # Check collision with wall
    if abs(snake.xcor()) > 290 or abs(snake.ycor()) > 290:
        snake.goto(0, 0)
        snake.direction = "stop"
        speed = 0.1  # Reset speed when losing

    # Check collision with food
    if snake.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        speed *= 0.9  # Increase speed each time food is eaten

    move()  # makes the snake move based on it's direction
    time.sleep(speed)  # pauses the game a little bit controlling snakes speed

wn.mainloop()  # keeps window open and game running
