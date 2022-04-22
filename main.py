from turtle import *
#cicek
bgcolor('black')
speed(0)
hideturtle()

for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(30)
    forward(2)

done()