#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#israel taylor
#Date
#12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl



#create turtle
penny = trtl.Turtle()
penny.speed(0)
turtleshape = "arrow"
shapesize = 0
turtlecolor = "black"
penny.ht()
turtlesize = 0

penny.fillcolor("black")
penny = trtl.Turtle(shape=turtleshape)
penny.color(turtlecolor)
pencolor = "black"


penny.resizemode(turtleshape)
penny.resizemode()

def resize():
    penny.resizemode()





#movement functions
def o():
    penny.shapesize(10)

def p():
    penny.shapesize(-10)



def up():
    penny.setheading(90)
    penny.forward(20)
    penny.degrees(360)

def down():
    penny.setheading(270)
    penny.forward(20)
    penny.degrees(360)

def right():
    penny.setheading(0)
    penny.forward(20)
    penny.degrees(360)

def left():    
    penny.setheading(180)
    penny.forward(20)
    penny.degrees(360)

def color():
    penny.color(turtlecolor)



    

#color/drawing functions



#create screen


wn = trtl.Screen()
#bind to keypresses


wn.onkeypress(o,"O")
wn.onkeypress(p,"P")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(up,"Up")


#listen
wn.listen()

#mainloop
wn.mainloop()