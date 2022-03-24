# Author JRI 3/23/22


import turtle


window = turtle.Screen() # window for the turtle
window.setup(1000, 1000)
window.screensize(100,100)
window.title("Lab 1")

snail = turtle.Turtle() # turtle name

# shows turtle where to go
snail.forward(250)
snail.right(90)
snail.forward(100)
snail.right(90)
snail.forward(250)
snail.right(90)
snail.forward(100)

window.mainloop() # keeps window open