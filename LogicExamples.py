import turtle as t
print ("1. Circle")
print ("2. Triange")
print ("3. Square")
print ("4. Pentagon")
print ("5. Hexagon")

user = int(input("Please select an option (1-5)"))
if user == 1:
    t.circle(100)
elif user == 2:
    for x in range (3):
        t.forward(100)
        t.left(360/3)
elif user == 3:
    for x in range (4):
        t.forward(100)
        t.left(360/4)
elif user == 4:
    for x in range (5):
        t.forward(100)
        t.left(360/5)
elif user == 5:
    for x in range (6):
        t.forward(100)
        t.left(360/6)

else:
   print("Invalid Option")

t.mainloop()