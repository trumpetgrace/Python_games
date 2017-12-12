a_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "D", 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, "G", 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1], \
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
[1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], \
[1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, "V", 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], \
[1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1], \
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, "T", 1, 0, 0, 0, 1], \
[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1], \
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "E", 1, 1, 1, 1, 1]]

rpx = 1
rpy = 1
a_door = True
a_gate = True
a_vault = True
a_tunnel = True


def door(a_map, rpx, rpy, a_door):
  if a_door == True:
    print "There is a door ahead of you.\n\n*There doesn't seem to be anywhere else you can go...\n\n*You try the handle... and nothing happens.*\n\n*You try again... and still nothing.*\n\n*You push against the door as hard as you can and it swings open, throwing you through*"
    return True
  else:
    print "*At closer inspection you see there is no handle on your side of the door.*"
    return False


def gate(a_map, rpx, rpy, a_gate):
  if a_gate == True:
    print "*Around the corner you see an wrought iron gate.*\n*You hesitate. This looks promising but what if slams behind like the door?*\n"
    return True
  else:
    print "*Why on earth would you want to go back there?!*"
    return False

def vault(a_map, rpx, rpy, a_vault):
  if a_vault == True:
    print "*As you turn the corner you come face to face with what appears to be a vault.*\n*On the right hand side you see a large combination lock*\n*How are you meant to proceed...?*\n*Suddenly you remember the note you found earlier.* \
    \n*It had three numbers written on it... It's a silly thought but maybe that's the combination?*"
    return True
  else:
     "The Vault is closed."
     return False

def tunnel(a_map, rpx, rpy, a_tunnel):
  if a_tunnel == True:
    print "*You find a small tunnel, close to the ground.*\n*Looks a little crampt... but there doesn't seem to be any other way you can go now*\n*You hear high pitched giggling coming from a corridor near you*\n*You speed up, crouching down and crawling through the tunnel*"
    return True
  else:
    print "The Tunnel is blocked."
    return False

def end_game():
  print "*You run ahead towards what looks like an exit*\n\n*You reach towards the door and begin to walk forward.*\n\n*You push the door open and see a forest. A forest near your home.*\n\n*As you step forward you hear a voice behind you.*\n\n*You turn around and see the same blue eyes and fair hair you saw earlier... a young girl?*\
  \n\n" "-" + str(name) + ". Why are you leaving?- \n\n *How does she know your name?*\n\n*As you pause she grins a little, her teeth glinting*\n\n*You push the door closed just as she tries to grab you*\n\n\n\n*The door slams, trapping her inside*\n\n*You take a moment to realise you are free*\
  \n\n*You start walking*\n\n\n\n*You wake up in a dark corridor...*\n\n*All alone...*"



def print_map(a_map, rpx, rpy):
  i = 0
  temp_str = ""
  for row in a_map:
      j = 0
      for x in row:
          if (j == rpx or j == rpx + 1 or j == rpx - 1) and (i == rpy or i == rpy + 1 or i == rpy - 1):
              if (i == rpy and j == rpx):
                  temp_str = temp_str + 'P'
              else:
                  temp_str = temp_str + str(x)
          else:
              temp_str = temp_str + '.'
          j = j + 1
      temp_str = temp_str + '\n'
      i = i + 1
  print temp_str
name = raw_input("What is your name? ")
asking = True
while asking:
    if name == "":
        print "Please enter a valid name."
    else:
        asking = False


print "The Labyrinth\n\nOne day you were out walking...\n\nAnd woke up in a dark corridor... \n\nAll alone... \n\n  \n\n*You feel around you, trying to see if you can reach anything* \n\n*You can feel a cold metal object* \
 \n\n*You find a switch and press it* \n\n--You found a torch-- \n\nYou shine your torch around and wonder where you are... \n\nThere doesn't seem to be much around you, just an empty corridor... \n\nIt's a little creepy in here... \n\n*You decide to start moving, maybe you can find a way out*\n"

def move(rpx, rpy,a_door, a_gate, a_vault, a_tunnel):
    turn = 0
    asking = True
    while asking:
        direction = raw_input("Pick a direction: ")
        direction = direction.lower()
        if turn == 1 and a_door == True:
          print "*You have a bad feeling about this. It seems like the faster you can get out the better*"
        if turn == 3 and a_door == True:
          print "*You slip on some steps. You point your torch down and see a strange substance on the floor. Seems like you probably shouldn't touch it. You continue*"
        if turn == 6 and a_door == True:
          print "*The corridor is damp. You see water dripping from above into a puddle on the ground.*"
        if turn == 10 and a_door == True:
            print "*It's getting cold. Maybe it's nearly night time? You walk faster"
        if turn == 1 and a_door == False and a_gate == True:
          print "*You hear foot steps which seem to be coming from the other side of the door. You run a little*"
        if turn == 3 and a_door == False and a_gate == True:
          print "*The running took a lot of effort. You stop to breathe*"
        if turn == 5 and a_door == False and a_gate == True:
          print "*You see something ahead, on the floor*\n*At a closer glance you see it's some sort of blanket. Brand new, clean, and folded. Strange...*\n\n--You found a blanket--"
        if turn == 3 and a_gate == False and a_vault == True:
          print "*You lace is undone. As you lean down to tie it you think you glimpse bright blue eyes behind you.*\n*You jump up and guard yourself but there's nothing there.*"
        if turn == 8 and a_gate == False and a_vault == True:
          print "*Your stomach grumbles, echoing in the quiet room. You remember you haven't eaten since... You can't remember when. That's odd.*"
        if turn == 11 and a_gate == False and a_vault == True:
          print "*Now that you think about, you haven't had anything to drink in a long time. Hopefully you'll be out before that becomes a problem."
        if turn == 15 and a_gate == False and a_vault == True:
          print "*There's something white on the floor which glints as you shine your torch over it*\n*You lean down and grab it, it's a piece of paper with three numbers written on it*\n\n--You got a note--"
        if turn == 18 and a_gate == False and a_vault == True:
          print "*Faintly, you hear a song being sung... like a nursery rhyme? You recognise it but can't remember where you know it from*"
        if turn == 20 and a_gate == False and a_vault == True:
            print "*Along the corridor a little you spot a bottle of water.*\n*It's clean and looks as though it's just been placed there...*\n*At least you won't need to worry about water anymore?*\n\n--You got a bottle of water--"
        if turn == 1 and a_vault == False and a_tunnel == True:
            print "*You hear a laugh and see a flash of fair hair rush past you*\n*You spin around trying to keep whatever it was in your line of sight*\n*But you are too late, the darkness is silent as if nothing ever happened*"
        if turn == 3 and a_vault == False and a_tunnel == True:
            print "*You are beginning to feel weak. It feels as though you've been walking for hours.*\n*You think about stopping for a while. Resting. You have a blanket and water, you could just wait here a while...* \
             \n*Your thoughts clear. How on earth could you be so careless?! Thoughts like that won't get you out of here.*"
        if turn == 4 and a_vault == False and a_tunnel == True:
            print "The ceiling appears to be getting lower, you crouch down a little but stay on guard.*"

        if direction == "w":
            if a_map[rpy - 1][rpx] == 0:
                rpy = rpy - 1
                print_map(a_map, rpx, rpy)
                turn = turn + 1

            elif a_map[rpy - 1][rpx] == 1:
                print "There's a wall there, you can't go that way."

            elif a_map[rpy - 1][rpx] == "T":
                if tunnel(a_map, rpx, rpy, a_tunnel) == True:
                  a_tunnel = False
                  print "*The tunnel starts to close in. You wonder if you've made a horrible mistake.*\n*Just as you're about to turn back the tunnel begins to widen again*\n*You breathe a sigh of relief, starting to feel a little calmer* \
                  \n*The tunnel finishes, leading out into a small room*\n*You climb out and look around.*\n*Ahead is a door.*"
                  rpy = rpy + 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "*You aren't sure that'll take you the right way... and it looks as though the door ahead might be relevant to this pointless game*"

        elif direction == "a":
            if a_map[rpy][rpx - 1] == 0:
                rpx = rpx - 1
                print_map(a_map, rpx, rpy)
                turn = turn + 1

            elif a_map[rpy][rpx - 1] == 1:
                print "There's a wall there, you can't go that way."

            elif a_map[rpy][rpx - 1] == "D":
                if door(a_map, rpx, rpy, a_door) == True:
                  a_door=False
                  print "*As soon as you fall through the door slams behind you, sounding as though it locks*"
                  rpx = rpx + 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "Best keep walking then..."

            elif a_map[rpy][rpx - 1] == "G":
                if gate(a_map, rpx, rpy, a_gate) == True:
                  a_gate = False
                  print "*You feel a presence behind you. You look behind you and see a row of sharp teeth, gleaming from the light of your torch. You don't think, you just run, pushing the iron gate open.* \
                  \n\n*Fortunately for you, whatever it was doesn't seem to have followed you, but you aren't going to stick around to check*"
                  rpx = rpx - 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "*Onwards, you go.*"

            elif a_map[rpy][rpx -1] == "V":
                if vault(a_map, rpx, rpy, a_vault) == True:
                  a_vault = False
                  print "*You enter the code and spin the wheel*\n*The door opens with ease*\n*You wonder if that was a little easy...*\n*The vault swings closed behind you*\n*Right.*"
                  rpx = rpx + 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "You continue your journey."

        elif direction == "s":
            if a_map[rpy + 1][rpx] == 0:
                rpy = rpy + 1
                print_map(a_map, rpx, rpy)
                turn = turn + 1

            elif a_map[rpy + 1][rpx] == 1:
                print "There's a wall there, you can't go that way."

            elif a_map[rpy + 1][rpx] == "E":
                end_game()
                break

            elif a_map[rpy + 1][rpx] == "T":
                if tunnel(a_map, rpx, rpy, a_tunnel) == True:
                  a_tunnel = False
                  print "*The tunnel starts to close in. You wonder if you've made a horrible mistake.*\n*Just as you're about to turn back the tunnel begins to widen again*\n*You breathe a sigh of relief, starting to feel a little calmer* \
                  \n*The tunnel finishes, leading out into a small room*\n*You climb out and look around.*\n*Ahead is a door.*"
                  rpy = rpy + 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "*You aren't sure that'll take you the right way... and it looks as though the door ahead might be relevant to this pointless game*"

        elif direction == "d":
            if a_map[rpy][rpx + 1] == 0:
                rpx = rpx + 1
                print_map(a_map, rpx, rpy)
                turn = turn + 1

            elif a_map[rpy][rpx + 1] == 1:
                print "There's a wall there, you can't go that way."

            elif a_map[rpy][rpx + 1] == "D":
                if door(a_map, rpx, rpy, a_door) == True:
                  a_door = False
                  print "*As soon as you fall through the door slams behind you, sounding as though it locks*"
                  rpx = rpx + 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "Best keep walking then..."

            elif a_map[rpy][rpx + 1] == "G":
                if gate(a_map, rpx, rpy, a_gate) == True:
                  a_gate = False
                  print "*You feel a presence behind you. You look behind you and see a row of sharp teeth, gleaming from the light of your torch. You don't think, you just run, pushing the iron gate open.* \
                  \n\n *Fortunately for you, whatever it was doesn't seem to have followed you, but you aren't going to stick around to check*"
                  rpx = rpx - 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "*Onwards, you go.*"

            elif a_map[rpy][rpx + 1] == "V":
                if vault(a_map, rpx, rpy, a_vault) == True:
                  a_vault = False
                  print "*You enter the code and spin the wheel*\n*The door opens with ease*\n*You wonder if that was a little easy...*\n*The vault swings closed behind you*\n*Right.*"
                  rpx = rpx + 2
                  print_map(a_map, rpx, rpy)
                  turn = 0
                else:
                  print_map(a_map, rpx, rpy)
                  print "You continue your journey."

        else:
            print "Invalid direction. You must choose 'w', 'a', 's', or 'd'."





print_map(a_map, rpx, rpy)
move(rpx, rpy,a_door, a_gate, a_vault, a_tunnel)
