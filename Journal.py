from datetime import datetime

def add_entry():
    entry = input("Write your journal entry")
    with open ("journal.txt", "a") as file:
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        file.write("[{}]{}\n".format(date,entry))
    print ("Entry Saved!")

def view_entry():
    with open ("journal.txt", "r") as file:
        print("Your Journal Entry")
        counter = 0
        for line in file:
            print("{}.{}".format(counter,line.strip()))
            counter += 1

while True:
    print("1. Add an Entry")
    print("2. View an Entry")

    choice == 1
