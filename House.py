import turtle as t
t.bgcolor("#ADD8E6")
t.width(3)

#Preparing the functions
def triangle (l,c):
    t.color(c)
    t.begin_fill()
    for x in range (3):
        t.forward(l)
        t.left(120)
    t.end_fill()

def rect (l,h,c,d):
    t.color(c,d)
    t.begin_fill()
    for x in range (2):
        t.forward(l)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def circle (r,c,d):
    t.color(c,d)
    t.begin_fill()
    for x in range(1):
        t.circle(r)
    t.end_fill()
        
def go (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#Making the house
go(-320,-300)
rect (650,200,"brown", "brown")

go(-300,-100)
rect(220,220,"yellow", "yellow")

go(-300,120)
triangle(220,"red")

go(-270,-100)
rect (70,100,"black", "black")

go(-250,-50)
circle(10,"gray","gray")

go(-180,0)
rect (80,80, "black", "white")

go(-140,0)
t.seth(90)
t.forward(80)

go(-180,40)
t.seth(180)
t.back(80)

#Making the tree
go(100,-100)
t.seth(0)
rect(30,200,"brown","brown")

go(115,100)
circle(80,"#006400","green")

#Making the grass
go(-320,-100)
for x in range (26):
    triangle(25,"green")
    t.forward(25)

t.mainloop()
