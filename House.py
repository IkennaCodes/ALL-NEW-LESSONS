import turtle as t

def triangle (l,c):
    t.color(c)
    t.begin_fill()
    for x in range (3):
        t.forward(l)
        t.left(120)
    t.end_fill()

def rect (l,h,c):
    t.color(c)
    t.begin_fill()
    for x in range (2):
        t.forward(l)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def circle (r,c):
    t.color(c)
    t.begin_fill()
    for x in range(1):
        t.circle(r)
    t.end_fill()
        
def go (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

go(-320,-300)
rect (650,200,"brown")

go(-300,-100)
rect(220,220,"yellow")

go(-300,120)
triangle(220,"red")

go(-270,-100)
rect (70,100,"black")

go(30,100,"white")

t.mainloop()