import secrets
import string

chars = string.ascii_letters + string.punctuation + string.digits


def OTPGenerator():
    print('Welcome to the OTP Generator!')
    OTPlength = input('How many digits do you want the OTP to be? ')
    while not OTPlength.isnumeric():
        OTPlength = input('Please give a number for how many digits you want your OTP to be. ')

    for x in range(int(OTPlength)):
        print(str(secrets.choice(chars)), end="")
    
OTPGenerator()
