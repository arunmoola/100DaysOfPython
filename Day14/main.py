from getpass import getpass as getpass

player_1 = input("Player 1, enter your name: ")
player_2 = input("Player 2, enter your name: ")

ch_1 = getpass("Player 1, your turn (R / P / S)? ")
ch_2 = getpass("Player 2, your turn (R / P / S)? ")

print("{} chose {}".format(player_1, ch_1))
print("{} chose {}".format(player_2, ch_2))

if ch_1 == 'R' or ch_1 == 'r':
  if ch_2 == 'R' or ch_2 == 'r':
    print("Well played both. It's a Tie!")
  elif ch_2 == 'P' or ch_2 == 'p':
    print("{} wins!".format(player_2))
  elif ch_2 == 'S' or ch_2 == 's':
    print("{} wins!".format(player_1))
  else:
    print("{}, Invalid Input".format(player_2))
elif ch_1 == 'P' or ch_1 == 'p':
  if ch_2 == 'R' or ch_2 == 'r':
    print("{} wins!".format(player_1))
  elif ch_2 == 'P' or ch_2 == 'p':
    print("Well played both. It's a Tie!")
  elif ch_2 == 'S' or ch_2 == 's':
    print("{} wins!".format(player_2))
  else:
    print("{}, Invalid Input".format(player_2))
elif ch_1 == 'S' or ch_1 == 's':
  if ch_2 == 'R' or ch_2 == 'r':
    print("{} wins!".format(player_2))
  elif ch_2 == 'P' or ch_2 == 'p':
    print("{} wins!".format(player_1))
  elif ch_2 == 'S' or ch_2 == 's':
    print("Well played both. It's a Tie!")
  else:
    print("{}, Invalid Input".format(player_2))
else:
  print("{}, Invalid Input".format(player_1))
  if ch_2 != 'R' and ch_2 != 'r' and ch_2 != 'S' and ch_2 != 's' and ch_2 != 'P' and ch_2 != 'p':
    print("{}, Invalid Input".format(player_2))
