def rollDice(max):
    import random
    dice = random.randint(1, max)
    return dice

max = input("How many sides?: ")
while True:
    dice = rollDice(int(max))
    print('You rolled:', dice)
    print()
    ch = input("Do you want to roll again (y/n)? ")
    if ch == 'n' or ch == 'N':
        break