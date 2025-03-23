print("Welcome to my Bakery")
print("I will be helping you print your bill today!")
name = input ("Enter your name : ")

print ("Hello,{}. Let's start the process.".format(name))
total = 0
while True :
    print ("1. Cakes")
    print ("2. Bread")
    print ("3. Cookies")
    user_choice = int(input("Enter your choice : "))

    if user_choice == 1:
        num = int(input("How many cakes are you buying ? "))
        price_cloth = 6
        print ("Cost of each cloth = £", price_cloth)
        price_each = num * price_cloth

    elif user_choice == 2:
        num + int(input("How many bread are you buying ?"))
        price_grocery = 3.5
        print ("Cost of each grocery item = £",price_grocery)
        price_each = num * price_grocery

    elif user_choice == 3:
        num = int(input("How many cookies are you buying ? "))
        price_toys = 4
        print ("Cost of  each toy item = £",price_toys)
        price_each = num * price_toys

    total = total + price_each
    print ("Price = {}".format (price_each))
    print ("-"*40)
    
    yes_no = input ("Do you want to continue (y/n) ? ")
    if yes_no == "n" or yes_no == "No" or yes_no == "no" or yes_no == "NO" :
        break

print ("Your total bill = £",total)