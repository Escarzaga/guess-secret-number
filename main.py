secret = 77

guess = int(input("Guess the secret number: "))
if guess == secret:
    print("Congratulations, you guessed the secret number!")
elif guess>secret:
    print("Please enter some greater number")
elif guess<secret:
    print("Please enter some lesser number")
else:
    print("Input error!")



