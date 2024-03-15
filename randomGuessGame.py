"""
Random guess game
---
code made in October 2023
"""
import random

def guess_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\n_| Welcome to the Guess Game |_")
    print("Try to guess a number between 1 and 100 that I chose\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Write your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Try a higher number...")
            elif guess > secret_number:
                print("Try a lower number...")
            else:
                print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please insert a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

guess_game()
