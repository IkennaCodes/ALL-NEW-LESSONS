import turtle as t
import random 

t.speed(0)

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
t.mainloop()

