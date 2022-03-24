# Author JRI 3/23/22

import turtle


window = turtle.Screen() # window created

window.setup()
window.screensize()
window.title("Lab 4")
window.bgcolor("green") # background color



meatloaf = turtle.Turtle()
meatloaf.shape("turtle")
meatloaf.pencolor("black") # sets the color of the pen and the fill color
meatloaf.fillcolor("white")
meatloaf.speed(5)
meatloaf.stamp()
meatloaf.setposition(100, 100)


meatloaf.begin_fill() # fills in the area
meatloaf.goto(100, 0) # shows turtle where to go
meatloaf.goto(0, 0)
meatloaf.goto(0, 100)
meatloaf.goto(100, 100)
meatloaf.end_fill()
window.mainloop() # window stays open