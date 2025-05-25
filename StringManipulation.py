# STRING Manipulation
x = "     Adanna    Ikenna    Sangeeta.    "
print(x.lower())           # convert every letter to small letters
print(x.upper())           # convert every letter to capital letters
print(x.strip())           # strip away excess/extra space from starting and ending
x = "Adanna Ikenna Sangeeta 123"    # split – converts the string to list
print(x.split(" "))
print(x.split("n"))
x = ["ABC", "QWERTY", "ASDA"]       # join – converts list to string
print("#".join(x))
