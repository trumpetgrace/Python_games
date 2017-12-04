print "Welcome to my game!"
print "In this game you must guess the number I'm thinking of..."
print "I'll tell you if it's too high or too low"


from random import randint

answer = randint(1, 101)

turn = 0
for turn in range(100):
    print "Turn", turn + 1
    turn = turn + 1
    user_guess = int(raw_input("Guess a number between 1 and 100: "))

    if user_guess == answer:
        print "Congratulations! You got it right!"
        print "You got my number in " + str(turn) + " turns"
        break
    else:
        if user_guess < 1 or user_guess > 100:
            print "Not in range. Please try again."
        elif user_guess > answer:
            print "Too high"
        elif user_guess < answer:
            print "Too low"
        else:
           if turn == 100:
               print "Game Over."

    turn = turn + 1
