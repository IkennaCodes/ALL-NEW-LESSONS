import pgzrun
import random
import time

TITLE = "Ordering Burgers"
WIDTH = 720
HEIGHT = 480

Burgers = []
NoOfBurgers = 10
StartScreen = False
Start_Button = Rect((100,300),(100,50))

def CreateBurger():
    for i in range(NoOfBurgers):
        burger = Actor("cuteburger.png")
        burger.pos = random.randint(50,670) , random.randint(50,430)
        Burgers.append(burger)

def draw():
    screen.clear()
    if StartScreen == True:
        screen.fill("black")
        screen.draw.filled_rect(Start_Button, color = "white")
        screen.draw.text("START", (0,0), color="black", fontsize=40)
    else:
        screen.blit("colourfulbg.png",(0,0))
        number = 1
        #draw each burger from the list one by one using loop
        for i in Burgers: 
            i.draw()
    
def on_mouse_down(pos):
    global StartScreen

    if StartScreen and Start_Button(pos):
        # Hide start screen
        StartScreen = False

CreateBurger()
pgzrun.go()
