print("Please think of a number between 0 and 100!")

high = 100
low = 0
ans = 50

while True:
    ans = (high + low) // 2
    print("Is your secret number " + str(ans) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == "h":
        high = ans
    elif guess == "l":
        low = ans
    elif guess == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    else:
        print("Sorry, I did not understand your guess")

