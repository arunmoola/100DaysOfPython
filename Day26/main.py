#from replit import audio
import os, time

def play():
    vol = 1
    #source = audio.play_file('audio.wav', True)
    #source.paused = False
    #source.volume = vol
    while True:
        os.system("clear")
        print('🎵 MyPOD Music Player!')
        print()
        #print('Playing',source.name,'...')
        print()
        print('press + to increase volume')
        print('press - to decrease volume')
        print('press m to mute')
        print('press p to play')
        print('press anything else to go to main menu')
        #print('volume', source.vol)
        ch = input('Enter your choice: ')
        if ch == '+' or ch == '=':
            vol += 1
            #source.volume = vol
        elif ch == '-' or ch == '_':
            vol -= 1
            #source.volume = vol
        elif ch == 'm' or ch == 'M':
            #source.paused = True
            True
        elif ch == 'p' or ch == 'P':
            #source.paused = False
            True
        else:
            break
        time.sleep(0.1)

while True:
    os.system('clear')
    print('🎵 MyPOD Music Player!')
    print()
    print('press 1 to play')
    print('press 2 to exit')
    print()
    print('press anything else to see the menu again...')
    print()
    ch = input('Enter your choice: ')
    if ch == '1':
        play()
    elif ch == '2':
        break
    else:
        continue