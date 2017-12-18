<<<<<<< HEAD
# Fruit machine function (from guardian pairing tasks)
import random

# Class to handle the data of machine float, money, and free spins
=======
import random

>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
class Machine_state:
    pass

mc = Machine_state()

<<<<<<< HEAD
# Slot options
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
colours = ["Black", "White", "Green", "Yellow"]

asking = True
print "FRUIT MACHINE"
print "============="
print unichr(163) + "1 per spin"
print "Winning combinations:\nTwo or three of the same adjacent colour- " + unichr(163) + "5\nOne of each colour- Half the Jackpot.\nFour of the same colour- Jackpot!!!"
mc.machine_float = 500
mc.money = 10
mc.free_spins = 0

<<<<<<< HEAD
# Prize funtion. Rewards winning combinations with set proportions/amounts of machine float money. Free spins are rewarded when the machine float is too low
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
def prize(asking, colours, slot_1, slot_2, slot_3, slot_4, mc):
    if slot_1 != slot_2 and slot_1 != slot_3 and slot_1 != slot_4:
        print "One of each colour!"
        print "YOU WIN!!!"
        print "Prize: " + unichr(163) + str((mc.machine_float / 2))
        mc.money += (mc.machine_float / 2)
        mc.machine_float = mc.machine_float / 2

    elif (slot_1 == slot_2) or (slot_2 == slot_3) or (slot_3 == slot_4):
        print "Two of the same adjacent!"
        print "YOU WIN!!!"
        if mc.machine_float >= 5:
            print "Prize: " + unichr(163) + "5"
            mc.machine_float -= 5
            mc.money += 5

        else:
            mc.free_spins = 5 - mc.machine_float
            mc.money += mc.machine_float
            print "Prize: " + unichr(163) + str(mc.machine_float) + " and " + str(mc.free_spins) + " free spins"
            mc.machine_float = 0

    elif ((slot_1 == slot_2) and (slot_2 == slot_3)) or ((slot_1 == slot_2) and (slot_3 == slot_4)) or ((slot_2 == slot_3) and (slot_3 == slot_4)):
        print "Two pairs of same adjacent!"
        print "YOU WIN!!!"
        if mc.machine_float >= 10:
            print "Prize: " + unichr(163) + "10"
            mc.machine_float -= 10
            mc.money += 10
        else:
            mc.free_spins = 10 - mc.machine_float
            mc.money += mc.machine_float
            print "Prize: " + unichr(163) + str(mc.machine_float) + " and " + str(mc.free_spins) + " free spins"
            mc.machine_float = 0

    elif (slot_1 == slot_2 == slot_3) or (slot_2 == slot_3 == slot_4):
        print "Three of the same adjacent!"
        print "YOU WIN!!!"
        if mc.machine_float >= 5:
            print "Prize: " + unichr(163) + "5"
            mc.machine_float -= 5
            mc.money += 5
        else:
            mc.free_spins = 5 - mc.machine_float
            mc.money += mc.machine_float
            print "Prize: " + unichr(163) + str(mc.machine_float) + " and " + str(mc.free_spins) + " free spins"
            mc.machine_float = 0

    elif slot_1 == slot_2 == slot_3 == slot_4:
        print "FOUR IN A ROW!"
        print "YOU WIN THE JACKPOT!!!"
        print "Prize: " + str(mc.machine_float)
        mc.money += mc.machine_float
        mc.machine_float = 0

    else:
        print "No win :("
        print "Better luck next time!"

<<<<<<< HEAD
# Spin function. Displays the current data (machine float, money, free spins)
=======

>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
def spin(asking, colours, mc):
    while asking:
        print "\n\nJackpot: " + unichr(163) + str(mc.machine_float)
        print "You have " + str(mc.free_spins) + " free spins!"
        print "You have " + unichr(163) + str(mc.money) + " in your wallet!"
<<<<<<< HEAD
        # Choose to spin
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
        spin_choice = raw_input("\n\nSpin? ")
        spin_choice = spin_choice.lower()
        if spin_choice == "no":
            print "\n\nGAME OVER"
            asking = False
        if spin_choice == "yes":
<<<<<<< HEAD
            # Checks if machine float is empty
            if mc.machine_float < 1:
                print "Machine needs to be refilled"
            # Checks has either money or free spins in order to play
            elif mc.money >= 1 or mc.free_spins > 1:
                # Picks four random colours
=======
            if mc.machine_float < 1:
                print "Machine needs to be refilled"
            elif mc.money >= 1 or mc.free_spins > 1:
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
                print "\n\n*Machine spins...*\n\n*Machine slows...*\n\n*Machine stops*\n\n"
                slot_1 = (random.choice(colours))
                slot_2 = (random.choice(colours))
                slot_3 = (random.choice(colours))
                slot_4 = (random.choice(colours))
                print "Slot One: " + slot_1 + "   " + "Slot Two: " + slot_2 + "   " + "Slot Three: " + slot_3 + "   " + "Slot Four: " + slot_4
<<<<<<< HEAD
                # Reduces free spins/money after play
=======
>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
                if mc.free_spins > 1:
                    mc.free_spins -= 1
                else:
                    mc.money -= 1
                    mc.machine_float += 1
<<<<<<< HEAD

                # Redirects to prize function which handles winning combos
                prize(asking, colours, slot_1, slot_2, slot_3, slot_4, mc)
            # Prevents spinning if money/free spins are too low
            elif mc.money < 1 and mc.free_spins == 0:
                print "Not Enough Cash"
        # Checks validity of input
        else:
            "Input invalid, please enter either 'yes' or 'no'"

# Starts game
=======
                    
                prize(asking, colours, slot_1, slot_2, slot_3, slot_4, mc)
            elif mc.money < 1 and mc.free_spins == 0:
                print "Not Enough Cash"
            elif mc.machine_float < 1:
                print "Machine needs to be refilled"
        else:
            "Input invalid, please enter either 'yes' or 'no'"

>>>>>>> 2b45bb03a2c4687ad2f69dcec50af69801f8848c
spin(asking, colours, mc)
