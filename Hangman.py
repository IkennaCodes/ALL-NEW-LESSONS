import random

def hangman():
    words = ["python","hangman","learning","computer","rainbow"]
    word_to_guess = random.choice(words)
    guessed_words = ["_"] * len(word_to_guess)
    
    tries = 6
    attempts = 0
    guessed_letters = []

    print("Welcome to the Hangman game!")
    print("Guess one letter at a time!")
    print("word:" + " ".join(guessed_words))

    while attempts < tries and "_" in guessed_words:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess, retry")
            continue

        if guess in guessed_letters:
            print("You already guessed this! Try again...")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Great guess! '{}' is in the word".format(guess))
            for i in range (len(word_to_guess)):
                if word_to_guess [i] == guess:
                    guessed_words[i] = guess

        else:
            attempts += 1
            print("Wrong Guess! You have {} attemps remaining".format(tries - attempts))#

        print("word:" + " ".join(guessed_words))
        print("Guessed letters:" + ", ".join(guessed_letters))

    if "_" not in guessed_words:
        print("You guessed the word! The word was:", word_to_guess)
    else:
        print("You have not guessed it.. GAME OVER! Word was:", word_to_guess)

hangman()
