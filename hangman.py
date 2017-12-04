my_dict = ["discussion", "policeman", "mathematics", "exchange", "mysterious"]

from random import randint

word = ""
char_guesses = ""
wrong_turn = 0

def word_selector(my_dict, wrong_turn):
    word_num = randint(0, len(my_dict) - 1)
    print word_num
    word = my_dict[word_num]
    word = word.upper()
    print word
    print "_" * len(word)
    user_guess(word, char_guesses, wrong_turn)


guess = ""

def user_guess(word, char_guesses, wrong_turn):
        while wrong_turn < 10:
            if wrong_turn == "":
                break
            else:
                guess = raw_input("Guess a letter: ")
                guess = guess.upper()

                if guess == "":
                    print "Guess invalid. Please enter a letter."
                elif len(guess) > 1:
                    print "Guess invalid. Please enter only one letter."
                elif guess in char_guesses:
                    print "You already guessed that! Try again."
                else:
                    char_guesses += guess
                    wrong_turn = correct_guess(word, char_guesses, guess, wrong_turn)


def correct_guess(word, char_guesses, guess, wrong_turn):
    i_wrong_turn = wrong_turn
    wrong = 0
    for letter in word:
        if letter in char_guesses:
            print letter,
        else:
            print "_",
            wrong += 1
    if guess not in word:
        i_wrong_turn += 1
        print "Wrong"
        print i_wrong_turn
        if i_wrong_turn == 10:
            print "Sorry! You ran out of turns!"
    else:
        print "You got it right"
        if wrong == 0:
            print "You won!"
            return ""
    return i_wrong_turn


word_selector(my_dict, wrong_turn)
