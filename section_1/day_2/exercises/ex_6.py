import random

guess_counter = 0

word_list = ["banana", "grape", "apple"]

random_word = random.choice(word_list)

scrambled_word = "".join(random.sample(random_word, len(random_word)))

while guess_counter < 3:
    user_guess = input("Guess the word: ")

    if user_guess != random_word:
        print("Wrong! Try again.")
        guess_counter += 1
    else:
        print(f"Right answer! The word was: {random_word}")
        break


if guess_counter == 3:
    print(f"Out of guesses. The word was: {random_word}")
