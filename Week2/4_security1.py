from hashlib import *

#create dictionary to save login info
#loginDict = {}

#hash definition
#take a string as input
def makeHash(password):
    return sha256(password.encode('utf-8')).hexdigest()

#login function
def login(loginDict):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if not username in loginDict:
        print ("You are not signed up yet.")
        password = input("Please enter a new password to sign up: ")
        loginDict[username] = makeHash(password)
        print ("You can now login with username: ", username)
    elif loginDict[username] != makeHash(password):
        print ("Step back, intruder!!!!!!")
    elif loginDict[username] == makeHash(password):
        print ("Congratulations! You're in!")

#login loop
def prompt():
    loginDict = {}
    option = 0
    while option != 0:
        #If students use this method, you may need to show them int(raw_input(...)).
        #raw_input(...) alone won't work.
        option = int(input("Please enter 1 to login or 0 to exit: "))
        if option == 1:
            login(loginDict)
            
prompt()