import random
word_list = ["video","coding","towel","fridge","human","garbage","cleaning","laptop","comb","vacuum","dishwasher","umbrella","island"]

def jumble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def get_hint(word):
    return "the first letter of the word is: {}".format(word[0].upper())

def play_game():
    score = 0
    rounds = 5

    print("Welcome to the scrambler game!")
    for round_number in range (1, rounds+1):
        word = random.choice(word_list)
        scrambled_word = jumble_word(word)

        print(f"/n round {round_number}")
        print(f"Here is the scrambled word {scrambled_word}")

        hint_choice = input("Would you  like to use a hint?(yes/no)").lower()
        if hint_choice == "yes":
            print(get_hint(word))

        guess = input("Guess the original word").lower()

        while not guess.isalpha():
            print("Please enter a valid word")
            guess = input("Guess the original word").lower()

        if guess == word:
            print("Congratulations!")

            score = score + 1
        else:
            print("The correct string  is: {}".format(word))
    print("Your final score is {}/{}".format(score,rounds))

play_game()



