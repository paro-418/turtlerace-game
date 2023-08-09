import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=1000, height=600)
user_bet = screen.textinput(title='Make your bet', prompt='which turtle will do you think win? enter color')
is_race_on = False
colors = ['red','orange','black','green','blue','purple']
topLineStart = 80
all_turtle = []

for color in colors:
    new_turtle  = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-470, y = topLineStart)
    topLineStart -= 30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 500:
            winning_color  =turtle.pencolor()
            print(f"{winning_color} won the race")
            if winning_color == user_bet:
                print("you won")
            else:
                print('you lost')
            is_race_on  = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()