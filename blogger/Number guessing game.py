import random
random_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == random_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < random_number:
        print("Too low! Try again")
        break
    elif guess > random_number:
        print("Too high! try again")
        break
    elif guess == random_number:
        print("Congratulations, You have guessed correctly!")