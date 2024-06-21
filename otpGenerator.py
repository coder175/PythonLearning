import secrets
import string

chars = string.ascii_letters + string.punctuation + string.digits


def OTPGenerator():
    randomOTP = ''
    print('Welcome to the OTP Generator!')
    OTPlength = input('How many digits do you want the OTP to be? ')
    while not OTPlength.isnumeric():
        OTPlength = input('Please give a number for how many digits you want your OTP to be. ')

    OTPlength = int(OTPlength)
    print('Here is your OTP:')

    for x in range(OTPlength):
        randomOTP += str(secrets.choice(chars))
    print(randomOTP)
    
    
OTPGenerator()
