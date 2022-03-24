# Author JRI 3/23/22

import turtle

def forward(): # creating functions to move forward, backward, left, and right
    snail.forward(50)
def backward():
    snail.backward(50)
def left():
    snail.left(90)
def right():
    snail.right(90)


window = turtle.Screen() # creating the window


snail = turtle.Turtle() # turtle names snail


window.onkey(forward, "Up")
window.onkey(backward, "Down")
window.onkey(left, "Left")
window.onkey(right, "Right")
window.mainloop()




left()
right()
backward()
forward()