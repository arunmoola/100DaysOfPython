from getpass import getpass as getpass

player_1 = input("Player 1, enter your name: ")
player_2 = input("Player 2, enter your name: ")

rounds = 0
player_1_score = 0
player_2_score = 0
while True:
  rounds += 1
  ch_1 = getpass("Player 1, your turn (R / P / S)? ")
  ch_2 = getpass("Player 2, your turn (R / P / S)? ")

  print("Round #{}:".format(rounds))
  print("{} chose {}".format(player_1, ch_1))
  print("{} chose {}".format(player_2, ch_2))

  if ch_1 == 'R' or ch_1 == 'r':
    if ch_2 == 'R' or ch_2 == 'r':
      print("Well played both. It's a Tie!")
    elif ch_2 == 'P' or ch_2 == 'p':
      print("{} wins this round!".format(player_2))
      player_2_score += 1
    elif ch_2 == 'S' or ch_2 == 's':
      print("{} wins this round!".format(player_1))
      player_1_score += 1
    else:
      print("{}, Invalid Input".format(player_2))
  elif ch_1 == 'P' or ch_1 == 'p':
    if ch_2 == 'R' or ch_2 == 'r':
      print("{} wins this round!".format(player_1))
      player_1_score += 1
    elif ch_2 == 'P' or ch_2 == 'p':
      print("Well played both. It's a Tie!")
    elif ch_2 == 'S' or ch_2 == 's':
      print("{} wins this round!".format(player_2))
      player_2_score += 1
    else:
      print("{}, Invalid Input".format(player_2))
  elif ch_1 == 'S' or ch_1 == 's':
    if ch_2 == 'R' or ch_2 == 'r':
      print("{} wins this round!".format(player_2))
      player_2_score += 1
    elif ch_2 == 'P' or ch_2 == 'p':
      print("{} wins this round!".format(player_1))
      player_1_score += 1
    elif ch_2 == 'S' or ch_2 == 's':
      print("Well played both. It's a Tie!")
    else:
      print("{}, Invalid Input".format(player_2))
  else:
    print("{}, Invalid Input".format(player_1))
    if ch_2 != 'R' and ch_2 != 'r' and ch_2 != 'S' and ch_2 != 's' and ch_2 != 'P' and ch_2 != 'p':
      print("{}, Invalid Input".format(player_2))

  print("Round #{} results: {}:{} {}:{}".format(rounds, player_1, player_1_score, player_2, player_2_score ))
  print()
  if player_1_score < 3 and player_2_score < 3:
    continue
  elif player_1_score == 3:
    print(player_1, "wins the game!")
    break
  else:
    print(player_2, "wins the game!")
    break