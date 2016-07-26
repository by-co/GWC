start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''

done = False


print(start) # print the first line

tupl = (1,2)
lst = [a,b,c,d,e]
for i in lst:
	print i
lst[0] = 4

dictionary = {"key": 1}

lst1 = [a,b, [a,[b,[c,[d]], 1, 2, ]]]
lst1[2]
while a < 3:
	a += 1

while not done:
	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()
	if user_input == "left":
	    print("You decide to go left and you find a mysterious wardrobe. Go in? (yes/no)")
	    wardrobe = input()
	    if wardrobe == "yes":
	    	print("You're in Narnia! The End.")
	    	done = True
	    elif wardrobe == "no":
	    	print("Oh. Okay then. The End.")
	    	done = True
	    else:
	    	print("This is a yes or no question! Yes or no?")
	    	wardrobe = input()
	elif user_input == "right":
	    print("You choose to go right and nothing happens. The End.") # finished the story writing what happens
	    done = True
