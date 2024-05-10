import random

# List of items
items = ["apple", "banana", "orange", "grape", "watermelon"]

# Select a random item from the list
selected_item = random.choice(items)

# Game instructions
print("Welcome to the Guess the Item game!")
print("I have selected an item from the following list:")
print(items)
print("Can you guess which item I selected?")

# Take the user's guess
guess = input("Enter your guess: ")

# Check if the guess is correct
if guess == selected_item:
    print("Congratulations! You guessed correctly.")
else:
    print(f"Sorry, the correct item was '{selected_item}'. Try again next time.")
