warehouse= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, "C", 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, "C", 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

rpx = 1
rpy = 1
asking = True
loading = False

def grab_crate(warehouse, rpx, rpy, crate):
  if loading == False:
    return True
  else:
    return True

def drop_crate(warehouse, rpx, rpy, crate):
  if crate == True:
    return True
  else:
    return False


def print_map(warehouse, rpx, rpy):
  i = 0
  temp_str = ""
  for row in warehouse:
      j = 0
      for x in row:
          if (i == rpy and j == rpx):
              temp_str = temp_str + 'R'
          else:
              if x != 1:
                  temp_str = temp_str + str(x)
          j = j + 1
      temp_str = temp_str + '\n'
      i = i + 1
  print temp_str


def move(rpx, rpy, loading):
    asking = True
    while asking:
        direction = raw_input("Direction input [N, E, S, W, G, or D]: ")
        direction = direction.lower()
        for x in direction:
            if x == "n":
                if warehouse[rpy - 1][rpx] == 0:
                    rpy = rpy - 1

                elif warehouse[rpy - 1][rpx] == "C":
                    rpy = rpy - 1

                elif warehouse[rpy - 1][rpx] == 1:
                    print "There's a wall there, you can't go that way."

            elif x == "w":
                if warehouse[rpy][rpx - 1] == 0:
                    rpx = rpx - 1

                elif warehouse[rpy][rpx - 1] == "C":
                    rpx = rpx - 1

                elif warehouse[rpy][rpx - 1] == 1:
                    print "There's a wall there, you can't go that way."

            elif x == "s":
                if warehouse[rpy + 1][rpx] == 0:
                    rpy = rpy + 1

                elif warehouse[rpy + 1][rpx] == "C":
                    rpy = rpy + 1

                elif warehouse[rpy + 1][rpx] == 1:
                    print "There's a wall there, you can't go that way."

            elif x == "e":
                if warehouse[rpy][rpx + 1] == 0:
                    rpx = rpx + 1

                elif warehouse[rpy][rpx + 1] == "C":
                    rpx = rpx + 1

                elif warehouse[rpy][rpx + 1] == 1:
                    print "There's a wall there, you can't go that way."
            elif x == " ":
                print_map(warehouse, rpx, rpy)

            elif x == "g":
                if loading == False:
                    if warehouse[rpy][rpx] == "C":
                        loading = True
                        warehouse[rpy][rpx] = 0
                        print "You now have a crate"

                    elif warehouse[rpy][rpx] == 0:
                        print"There is no crate to pick up"

                elif loading == True:
                    print "You already have a crate"

            elif x == "d":
                if loading == True:
                    if warehouse[rpy][rpx] == 0:
                        loading = False
                        warehouse[rpy][rpx] = "C"
                        print "Crate has been dropped off"

                    elif warehouse[rpy][rpx] == "C":
                        print "Cannot drop crate on another crate"

                elif loading == False:
                    print "No crate to drop"

            else:
                print "Invalid direction. You must choose 'N', 'E', 'S', 'W', 'G', or 'D'."
        print_map(warehouse, rpx, rpy)



print "ROBOT WAREHOUSE"
print_map(warehouse, rpx, rpy)
move(rpx, rpy, loading)
