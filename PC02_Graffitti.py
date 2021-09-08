#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
t = turtle.Turtle()
t.speed(3)

t.pencolor("blue")
t.pensize(3)

#J
t.penup()
t.goto(-250,325)
t.pendown()
t.fd(25)
t.rt(90)
t.fd(125)
t.rt(90)
t.fd(75)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.left(90)
t.fd(25)
t.left(90)
t.fd(100)

t.pencolor("red")
t.pensize(1)
#E
t.penup()
t.goto(-200,325)
t.pendown()
t.bk(125)
t.rt(90)
t.fd(75)
t.left(90)
t.fd(25)
t.left(90)
t.fd(50)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.left(90)
t.fd(25)
t.left(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(50)
t.left(90)
t.fd(25)
t.left(90)
t.fd(75)

t.pencolor("yellow")
t.pensize(4)
#F1
t.penup()
t.goto(-100,325)
t.pendown()
t.left(90)
t.fd(125)
t.left(90)
t.fd(25)
t.left(90)
t.fd(50)
t.rt(90)
t.fd(25)
t.left(90)
t.fd(25)
t.left(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(50)
t.left(90)
t.fd(25)
t.left(90)
t.fd(75)

t.pencolor("green")
t.pensize(2)
#F2
t.penup()
t.goto(0,325)
t.pendown()
t.left(90)
t.fd(125)
t.left(90)
t.fd(25)
t.left(90)
t.fd(50)
t.rt(90)
t.fd(25)
t.left(90)
t.fd(25)
t.left(90)
t.fd(25)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(50)
t.left(90)
t.fd(25)
t.left(90)
t.fd(75)

t.pencolor("red")
t.fillcolor("red")
#Nose
t.penup()
t.goto(20,105)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
