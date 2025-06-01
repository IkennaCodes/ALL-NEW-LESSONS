my_dict = {}

while True:
    print("Mini Dictionary App")
    print("1. Add / Update a word")
    print("2. Retrieve a word")
    print("3. Delete a word")
    print("4. View all words")
    print("5. Exit")

    choice = input("Enter a number")

    if choice == 1:
        word = input("Enter a word").strip()
        definition = input("Enter the definition").strip()
        print(f"Word {word} added/updated successfully!")

    if choice == 2:
        word = input("Enter the word to be retrieved")
        if word in my_dict:
            print(f"{word}:{dict[word]}")
        else:
            print("Word cannot be found")

    if choice == 3:
        word = input("Enter the word you would like to delete")
        if word in my_dict:
            del my_dict[word]
        else:
             print("Word cannot be found")

    
