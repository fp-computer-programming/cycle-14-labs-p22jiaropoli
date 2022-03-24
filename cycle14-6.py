# Author JRI 3/23/22

import turtle


window = turtle.Screen() # creating the window

# turtle name
craig = turtle.Turtle()


craig.color(window.textinput("Color?", "What color? ")) # input for color

size = int(window.textinput("Size?", "What size do you want the turtle to be (1-5)? ")) # input for the size




if size > 5: # different sizes based off of input
    craig.shapesize(5)
elif size < 1:
    craig.shapesize(1)
else:
    craig.shapesize(size)


craig.begin_fill() 

# all of the directions for the turtle
craig.forward(50)
craig.right(90)
craig.forward(10)
craig.right(90)
craig.forward(10)
craig.right(45)
craig.forward(10)
craig.end_fill()

window.mainloop() # keeps the window open