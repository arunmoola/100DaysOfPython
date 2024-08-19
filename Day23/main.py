def login():
    from getpass import getpass as getpass
    print('Replit Login System:')
    print()

    while True:
        username = input("Username>")
        password = getpass("Password>")
        if username == 'admin' and password == 'admin':
            print('Welcome to Replit!\n')
            break
        else:
            print('Invalid username or password. Try again. \n')

login()