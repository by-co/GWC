from hashlib import *

loginDict = {'Gerald': '4d416525fcdbdd87be5b3cda134e806dfa6613c682fb8b749ea552adeffab251', 
			'Carly Rae': '26e28199c2d54d3552fde1e615d8428bf9ac9bea0e36ca93a98652928c52f514',
			'Emily': 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78'}

def makeHash(password):
    return sha256(password).hexdigest()

def login(username,password):
    if not username in loginDict:
        print ("You are not signed up yet.")
        password = input("Please enter a new password to sign up: ")
        loginDict[username] = makeHash(password)
        print ("You can now login with username: ", username)
    elif loginDict[username] != makeHash(password):
        print ("Step back, intruder!!!!!!")
    elif username == 'Gerald':
    	if loginDict['Gerald'] == makeHash(password):
    		print ("Welcome, Gerald!")
    		print ("Here is a joke: ")
    		print ("Sally asks her friend, Lori, a computer programmer, 'Could you please go to the store for me and buy one carton of milk, and if they have eggs, get 6!' A short time later, Lori comes back with 6 cartons of milk. Sally asks her, 'Why did you buy 6 cartons of milk?'' Lori replied, 'They had eggs.'")
    elif loginDict[username] == makeHash(password):
        print ("Congratulations! You're in!")
    print ('hello')