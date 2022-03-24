# Author JRI 3/23/22

import turtle


window = turtle.Screen() # window settings
window.setup(500, 500)
window.screensize(100,100)
window.title("Lab 3")
window.bgcolor("white")

snail = turtle.Turtle() # name of turtle 
snail.shape("turtle") #shape
snail.pencolor("green") # color

for x in range(200): # for loop for the direction for the turtle 
    snail.back(200)
    snail.right(120)

window.mainloop()