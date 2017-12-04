my_dict = ["discussion", "policeman", "mathematics", "exchange", "mysterious"]

from random import randint

word = ""
def word_selector(my_dict):
    word_num = randint(0, len(my_dict) - 1)
    print word_num
    word = my_dict[word_num]
    word = word.upper()
    print word
    print "_" * len(word)
    user_guess()


char = ""
def user_guess():
    char = raw_input("Guess a letter: ")
    char = char.upper()
    print char
    correct_guess(word, char)

def correct_guess(word, char):
    for letter in word:
        if letter != char:
            print "_",
        else:
            print char,
    print



word_selector(my_dict)
# user_guess()
# correct_guess(word)
