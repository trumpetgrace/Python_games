print "Time to play Mad Libs!"
print "Please answer the questions and wait for your generated story!"

asking = True
while asking:
    ml_adjective = raw_input("Pick an adjective: ")
    if ml_adjective == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_nationality = raw_input("Pick a nationality: ")
    if ml_nationality == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_name = raw_input("Pick a name: ")
    if ml_name == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_noun = raw_input("Pick a noun: ")
    if ml_noun == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_adjective_two = raw_input("Pick an adjective: ")
    if ml_adjective_two == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_noun_two = raw_input("Pick a noun: ")
    if ml_noun_two == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_adjective_three = raw_input("Pick another adjective: ")
    if ml_adjective_three == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_adjective_four = raw_input("Pick another adjective: ")
    if ml_adjective_four == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_plural_noun = raw_input("Pick a plural noun: ")
    if ml_plural_noun == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_noun_three = raw_input("Pick a noun: ")
    if ml_noun_three == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_num = raw_input("Pick a number: ")
    if ml_num == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_shape = raw_input("Pick a plural shape: ")
    if ml_shape == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_food = raw_input("Pick a food: ")
    if ml_food == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_food_two = raw_input("Pick another food: ")
    if ml_food_two == "":
        "Input is invalid"
    else:
        asking = False

asking = True
while asking:
    ml_num_two = raw_input("Pick a number: ")
    if ml_num_two == "":
        "Input is invalid"
    else:
        asking = False


print "Pizza was invented by a " + ml_adjective + " " + ml_nationality + " chef named " + ml_name + ". To make pizza, you need \
to take a lump of " + ml_noun + ", and make a thin, round " + ml_adjective_two + " " + ml_noun_two + ". Then you cover it with " + ml_adjective_three + " \
sauce, " + ml_adjective_four + " cheese, and fresh chopped " + ml_plural_noun + ". Next you have to bake it in a very hot " + ml_noun_three + ". When \
it is done, cut it into " + ml_num + " " + ml_shape + ". Some people like " + ml_food + " pizza the \
best, but my favourite is the " + ml_food_two + " pizza. If I could, I would eat pizza " + ml_num_two + " times a day!"
