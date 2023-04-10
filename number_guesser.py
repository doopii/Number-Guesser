import random

while True:
    top_of_range = input("Set the range: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Number must be GREATER than 0")
            continue
        else:
            break
    else:
        print("NUMBER only!")
        continue

print(f"The range will be 0 to {top_of_range} ")

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_answer = input("Guess the number: ")
    if user_answer.isdigit():
        user_answer = int(user_answer)
    else:
        print("NUMBER only!")
        continue
    
    guesses += 1
    if user_answer == random_number:
        print("You got it right!")
        break
    elif user_answer > random_number:
        print("your guess is GREATER than the number")
    else:
        print("your guess is LESSER than the number")

print("Guesses:", guesses)