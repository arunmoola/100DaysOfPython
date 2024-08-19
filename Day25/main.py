def rollDice(max):
    import random
    dice = random.randint(1, max)
    return dice

def healthStats():
    return rollDice(6)*rollDice(8)

print('Character Stats Generator!')
print()
isContinue = 'y'
while isContinue != 'n' and isContinue != 'N':
    name = input('Name your warrior: ')
    print('Health of',name,'is:',str(healthStats())+"hp")
    print()
    isContinue = input("Do you want to create more warriors (y/n)? ")