
# Mad libs game, takes user input and outputs a story
print "Time to play Mad Libs!"
print "Please answer the questions and wait for your generated story!"

# Ensures a word is given, could potentially use a dictionary in a more complex version of the game to ensure real words are used

asking = True
while asking:
    ml_adjective = raw_input("Pick an adjective: ")
    if ml_adjective == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_nationality = raw_input("Pick a nationality: ")
    if ml_nationality == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_name = raw_input("Pick a name: ")
    if ml_name == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_noun = raw_input("Pick a noun: ")
    if ml_noun == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_adjective_two = raw_input("Pick an adjective: ")
    if ml_adjective_two == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_noun_two = raw_input("Pick a noun: ")
    if ml_noun_two == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_adjective_three = raw_input("Pick another adjective: ")
    if ml_adjective_three == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_adjective_four = raw_input("Pick another adjective: ")
    if ml_adjective_four == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_plural_noun = raw_input("Pick a plural noun: ")
    if ml_plural_noun == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_noun_three = raw_input("Pick a noun: ")
    if ml_noun_three == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_num = raw_input("Pick a number: ")
    if ml_num == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_shape = raw_input("Pick a plural shape: ")
    if ml_shape == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_food = raw_input("Pick a food: ")
    if ml_food == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_food_two = raw_input("Pick another food: ")
    if ml_food_two == "":
        print "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_num_two = raw_input("Pick a number: ")
    if ml_num_two == "":
        print "Input is invalid"
    else:
        asking = False


print "Pizza was invented by a " + ml_adjective + " " + ml_nationality + " chef named " + ml_name + ". To make pizza, you need \
to take a lump of " + ml_noun + ", and make a thin, round " + ml_adjective_two + " " + ml_noun_two + ". Then you cover it with " + ml_adjective_three + " \
sauce, " + ml_adjective_four + " cheese, and fresh chopped " + ml_plural_noun + ". Next you have to bake it in a very hot " + ml_noun_three + ". When \
it is done, cut it into " + ml_num + " " + ml_shape + ". Some people like " + ml_food + " pizza the \
best, but my favourite is the " + ml_food_two + " pizza. If I could, I would eat pizza " + ml_num_two + " times a day!"
