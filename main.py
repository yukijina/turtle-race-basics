from turtle import Turtle, Screen
import random

speedy = Turtle()
screen = Screen()

is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make youe bet.", prompt="Which turtle will win the game?\n(Type: red, orange, green, blue, yellow or purple)")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtles_objects= []



def create_turtles():
  """create 6 color of turtles"""
  #turtle starting point
  x = -230
  y = 150
  for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    y -= 60
    turtles_objects.append(turtle)
    
create_turtles()

if user_bet:
  is_race_on= True

while is_race_on:
  for turtle in turtles_objects:
    turtle.forward(random.randint(1,10))

    if turtle.xcor() > 230:
      print(turtle.pencolor())
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        screen.title(f"The turle {winning_color} won the game!🏆")
      else:
        screen.title(f"The winner is {winning_color} turtle. You lost the game😭")  
      
      is_race_on = False   
  




screen.exitonclick()