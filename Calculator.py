print ("Welcome to Mini Calculator Project")

num1 = float (input ("Enter First number : "))
num2 = float (input ("Enter Second number : "))

choice = input ("Enter an operator of your choice (+,-,/,*,**,//,%) : ")
if choice == "+" :
    print ("Addition = ", num1 + num2)
elif choice == "/" :
    print ("Division = ", num1 / num2)
elif choice == "-" :
    print ("Subtraction = ", num1 - num2)
elif choice == "*" :
    print ("Multiplication = ", num1 * num2)
elif choice == "//" :
    print ("Floor Division = ", num1 // num2)
elif choice == "**" :
    print ("Exponent = ", num1 ** num2)
elif choice == "%" :
    print ("Modulus = ", num1  % num2)
