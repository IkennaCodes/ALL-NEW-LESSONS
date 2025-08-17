import random
import time
import turtle as t

t.speed(0)
sc = t.Screen()
sc.bgcolor("black")

t.colormode(255)

def circle ():
    t.penup()
    t.goto(random.randint(-200,200), random.randint(-180,180))


    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    t.begin_fill()
    t.pendown()
    t.circle(random.randint(40,80))
    t.penup()
    t.end_fill()

delay =  0.8
start_time = time.time()
for i in range (50):
    circle()
    time.sleep(delay)
    t.clear()
    delay = max(0.01,delay - 0.05)
end_time = time.time()

elapsed_time = round(end_time - start_time,2)

t.penup()
t.goto(0,0)
t.color("yellow")
t.write("total_time :{} seconds".format(elapsed_time),align = "center", font = ("preconnect",16,"italics"))

t.mainloop()

