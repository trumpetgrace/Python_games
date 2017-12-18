print "This is my dice roller."

from random import randint

<<<<<<< HEAD

# For use after first turn
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
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

<<<<<<< HEAD
# Function for one die
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
def d_one():
    one_d = randint(1, 7)
    print "*Dice Rolls*"
    print "The dice landed on " + str(one_d)
    asking = True
<<<<<<< HEAD
    # Handles validity of input, redirects to play_again function
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
    while asking:
        second_turn = raw_input("Would you like to play again? ")
        second_turn = second_turn.lower()
        if second_turn == "yes" or second_turn == "no":
            play_again(second_turn)
            asking = False
        else:
            print "Answer invalid. Please choose either 'yes' or 'no'."

<<<<<<< HEAD
# Function for two dice
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
def d_two():
    one_d = randint(1, 7)
    two_d = randint(1, 7)
    total_d = one_d + two_d
    print "*Dice Rolls*"
    print "The first dice landed on " + str(one_d)
    print "The second dice landed on " + str(two_d)
    print "Together, the total is " + str(total_d)
<<<<<<< HEAD
    # Handles validity of input, redirects to play_again function
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
    asking = True
    while asking:
        second_turn = raw_input("Would you like to play again? ")
        second_turn = second_turn.lower()
        if second_turn == "yes" or second_turn == "no":
            play_again(second_turn)
            asking = False
        else:
            print "Answer invalid. Please choose either 'yes' or 'no'."

<<<<<<< HEAD
# Takes in decision from play, redirects to function chosen
def turn(play):
    if play == "yes":
=======
def turn(y_or_n):
    if y_or_n == "yes":
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
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

<<<<<<< HEAD
# Initial choice of yes/no for playing. Play differs from play_again which is used after first turn
asking = True
while asking:
    play = raw_input("Would you like to play? ")
    play = play.lower()
    if play == "yes" or play == "no":
        turn(play)
=======
asking = True
while asking:
    y_or_n = raw_input("Would you like to play? ")
    y_or_n = y_or_n.lower()
    if y_or_n == "yes" or y_or_n == "no":
        turn(y_or_n)
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
        asking = False
    else:
        print "Answer invalid. Please choose either 'yes' or 'no'."
