import turtle as t
import random 

t.speed(0)
t.bgcolor("#DFF6FF")

t.penup()
t.goto(-300,-100)
t.pendown()

#sand box
t.color("#C2B280","#EEDC9A")
t.begin_fill()
for x in range (2):
    t.forward(600)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

#sand particles
for x in range (30):
    t.penup()
    x = random.randint(-300,300)
    y = random.randint(-300,-100)
    t.goto (x,y)
    t.pendown()
    t.color("#C2B280")
    t.dot()


#triangle
t.penup()
t.goto(-200,-100)
t.pendown()
t.color("#C2B280","#EEDC9A")
t.begin_fill()
for x in range (3):
    t.forward(200)
    t.left(120)
t.end_fill()

#triangle lines

t.penup()
t.goto(-177,-60)
t.pendown()
t.forward(155)

t.penup()
t.goto(-153,-20)
t.pendown()
t.forward(107)

t.penup()
t.goto(-130,20)
t.pendown()
t.forward(62)


#semi circle
t.penup()
t.goto(150,-100)
t.pendown()
t.begin_fill()
t.setheading(90)
t.circle(60,180)
t.end_fill()

#cactus
t.width(1.5)
t.penup()
t.goto(80,-42)
t.pendown()
t.begin_fill()
t.color("black","#75A14F")
t.right(180)
t.forward(20)
t.penup()
t.forward(20)
t.pendown()
t.seth(180)
t.circle(10,180)
t.penup()
t.right(270)
t.forward(20)
t.pendown()
t.right(0)
t.forward(30)
t.seth(-90)
t.circle(15,-180)
t.back(10)
t.seth(180)
t.circle(15,-180)
t.right(90)
t.forward(33)
t.end_fill()

#sun
t.penup()
t.goto(0,200)
t.pendown()
t.color("yellow")
for x in range (20):
   t.forward(100)
   t.right(150)
   t.width(2)
t.mainloop()
