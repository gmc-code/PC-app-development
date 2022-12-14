# Turtle Game using the package 'turtle'! Refactored
# We want two players in this game and the idea is that whoever
# gets to the other side wins!

# Import relevant modules
import turtle
import random
import time

# Setting up a nice screen for our game!
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Background a lightblue colour


# Player one - basic set up
player_one = turtle.Turtle()
player_one.color("blue")
player_one.speed(0)
player_one.shape("turtle")
player_one.penup()
player_one.goto(-300, 200)


# Player two - basic set up
player_two = player_one.clone()
player_two.color("red")
player_two.goto(-300, -200)

# draw a finish line!
def finish_line(x, y):
    setout_t = turtle.Turtle()
    setout_t.penup()
    setout_t.ht()
    setout_t.speed(0)
    setout_t.goto(x, y)
    setout_t.left(90)
    setout_t.pendown()
    setout_t.color("black")
    setout_t.forward(500)
    setout_t.write("Finish!", font=24)


finish_line(x=300, y=-250)

# We need to make sure both players have their pens down
player_one.pendown()
player_two.pendown()

# Let's create values for the die
die = [1, 2, 3, 4, 5, 6]

# Let's create the game!!

for i in range(30):
    if player_one.xcor() >= (300):
        break
    elif player_two.xcor() >= (300):
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        die_roll = random.choice(die)
        player_two.forward(30 * die_roll)
        time.sleep(1)


# announce winner
def winner(x, y):
    winner_t = turtle.Turtle()
    winner_t.penup()
    winner_t.ht()
    winner_t.speed(0)
    winner_t.goto(x, y)
    winner_t.pendown()
    winner_t.color("red")
    if player_one.xcor() > player_two.xcor():
        winner_t.write("Player One wins race!", font=48)
    else:
        winner_t.write("Player Two wins race!", font=48)


winner(0, 300)

# This keeps the turtle drawing on the screen!
turtle.done()
