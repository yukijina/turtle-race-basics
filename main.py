from turtle import Turtle, Screen

speedy = Turtle()
screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make youe bet.", prompt="Which turtle will win the game?")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtles_objects= []



def create_turtles():
  """create turtle"""
  #turtle starting point
  x = -230
  y = 150
  for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    y -= 60
    turtles_objects.append(turtle)
    
create_turtles()




screen.exitonclick()