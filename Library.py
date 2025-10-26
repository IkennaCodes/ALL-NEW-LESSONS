LibraryOfJetlearn = {"The Boy Who Cried Wolf":"available","Harry Potter":"unavailable","Diary of a Wimpy Kid":"available","Coraline":"available","The Hunger Games":"unavailable","Heartstopper":"available"}
while True:
    print("Welcome to the Ultimate Libary Of Jetlearn")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Delete a book")
    print("5. How many available books?")
    print("6. How many unavailable books?")
    print ("7. What books are unavailable")
    print("8. What books are available?")
    print("9. View all books")
    print("10. Exit")

    choice = int(input("Enter your choice"))
    if choice == 1:
        choiceofbook = input("Enter a new book")
        if choiceofbook in LibraryOfJetlearn:
            print("Book already exists within library, try again.")
            choiceofbook = input("Enter a different book")
        availability = input ("Enter the availability")
        LibraryOfJetlearn [choiceofbook] = availability
        print("Book Added.")

    if choice == 2:
        bookToborrow = input("Enter the book you would like to borrow")
        if bookToborrow not in LibraryOfJetlearn or LibraryOfJetlearn [bookToborrow] == "unavailable":
            print("That book isn't availible!")
            bookToborrow = input("Enter the book you would like to borrow again")
        else:
            LibraryOfJetlearn [bookToborrow] = "unavailable"
            print(bookToborrow, "has been borrowed!")

    if choice == 3:
        bookToreturn = input("Enter the book you would like to return")
        if bookToreturn not in LibraryOfJetlearn or LibraryOfJetlearn [bookToborrow] == "available":
            print("That is not the book you borrowed.")
            bookToreturn = input("Enter the book u would like to return again")
        elif LibraryOfJetlearn [bookToborrow] == "unavailable":
            LibraryOfJetlearn [bookToborrow] == "available"
            print(bookToreturn, "has been returned!")

    if choice == 4:
        deletechoice = input("Which book would you like to remove?")
        if deletechoice not in LibraryOfJetlearn:
            print("You cannot delete this book as it doesn't exist within the library, retry!")
            deletechoice = input("Re-enter the book you want to remove")
        elif deletechoice in LibraryOfJetlearn:
            del LibraryOfJetlearn [deletechoice]

    if choice == 5:
        bookstatus = list(LibraryOfJetlearn.values())
        print(bookstatus)
        available = bookstatus.count("available")
        print (available)

    if choice == 7:
        for book in LibraryOfJetlearn:
            if LibraryOfJetlearn[book] == "unavailable":
                print(book)

    if choice == 8:
        for book in LibraryOfJetlearn:
            if LibraryOfJetlearn[book] == "available":
                print(book)

    if choice == 9:
        print(LibraryOfJetlearn)

    if choice == 10:
        print("Bye! Thanks for visiting our library!")
        break