import turtle as t
import random 

t.speed(0)

t.penup()
t.goto(-300,-100)
t.pendown()

#sand box
t.color("#EEDC9A")
t.begin_fill()
for x in range (2):
    t.forward(600)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

#sand particles
for x in range (60):
    t.penup()
    x = random.randint(-300,300)
    y = random.randint(-300,-100)
    t.goto (x,y)
    t.pendown()
    t.color("#C2B280")
    t.dot()

t.mainloop()
