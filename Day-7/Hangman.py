import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
word = random.choice(word_list)
print(word)

placeholder = ""

for number in range(len(word)):
    placeholder += "_"

print(f"Word to guess: {placeholder}")

lives = 6

guessed_letters = []

game_over = False

while not game_over:
    print(f"\n****************************{lives}/6 LIVES LEFT****************************\n")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in word:
        if guess == letter:
            display += letter
            guessed_letters.append(guess)
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if "_" not in display:
        game_over = True
        print("\n****************************YOU WIN****************************\n")
    elif lives == 0:
        print(f"\n***********************IT WAS {word}! YOU LOSE**********************\n")
        game_over = True

    print(stages[lives])




