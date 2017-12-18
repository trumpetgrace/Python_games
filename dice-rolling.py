print "This is my dice roller."

from random import randint


# For use after first turn
def play_again(second_turn):
    if second_turn == "yes":
        asking = True
        while asking:
            user_choice = raw_input("Would you like one or two dice? ")
            user_choice = user_choice.lower()
            if user_choice == "one":
                d_one()
                asking = False
            elif user_choice == "two":
                d_two()
                asking = False
            else:
                print "Answer invalid. Please choose either 'one' or 'two'."
    elif second_turn == "no":
        print "Thanks for playing!"

# Function for one die
def d_one():
    one_d = randint(1, 7)
    print "*Dice Rolls*"
    print "The dice landed on " + str(one_d)
    asking = True
    # Handles validity of input, redirects to play_again function
    while asking:
        second_turn = raw_input("Would you like to play again? ")
        second_turn = second_turn.lower()
        if second_turn == "yes" or second_turn == "no":
            play_again(second_turn)
            asking = False
        else:
            print "Answer invalid. Please choose either 'yes' or 'no'."

# Function for two dice
def d_two():
    one_d = randint(1, 7)
    two_d = randint(1, 7)
    total_d = one_d + two_d
    print "*Dice Rolls*"
    print "The first dice landed on " + str(one_d)
    print "The second dice landed on " + str(two_d)
    print "Together, the total is " + str(total_d)
    # Handles validity of input, redirects to play_again function
    asking = True
    while asking:
        second_turn = raw_input("Would you like to play again? ")
        second_turn = second_turn.lower()
        if second_turn == "yes" or second_turn == "no":
            play_again(second_turn)
            asking = False
        else:
            print "Answer invalid. Please choose either 'yes' or 'no'."

# Takes in decision from play, redirects to function chosen
def turn(play):
    if play == "yes":
        asking = True
        while asking:
            user_choice = raw_input("Would you like one or two dice? ")
            user_choice = user_choice.lower()
            if user_choice == "one":
                d_one()
                asking = False
            elif user_choice == "two":
                d_two()
                asking = False
            else:
                print "Answer invalid. Please choose either 'one' or 'two'."

    elif y_or_n == "no":
        print "Fine. :("

# Initial choice of yes/no for playing. Play differs from play_again which is used after first turn
asking = True
while asking:
    play = raw_input("Would you like to play? ")
    play = play.lower()
    if play == "yes" or play == "no":
        turn(play)
        asking = False
    else:
        print "Answer invalid. Please choose either 'yes' or 'no'."
