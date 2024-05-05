import random

print("Welcome to hangman!")
print("You get 5 guesses")

words = ["blueberry", "potpie", "chapel"]

secret_word = random.choice(words)

display_word = []

for letter in secret_word:
    display_word += "_"

print(display_word)

guessnum = 0
game_over = False
while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        guessnum += 1
        guessleft = 5 - guessnum
        print(f"You have {guessleft} guesses left")
        if guessnum >= 5:
            print("You Lose")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win!")
        game_over = True
