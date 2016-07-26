"""
Mad Libs
inspired by 'Come Clean' by Hilary Duff (2004)

Let the rain fall down
And wake my dreams
Let it wash away
My sanity
'Cause I wanna feel the thunder
I wanna scream
Let the rain fall down
I'm coming clean, I'm coming clean
"""

print("We're going to play Mad Libs!")
noun1 = input("Give me a noun: ")
line1 = "Let the " + noun1 + " fall down"

verb1 = input("And now give me a verb!: ")
noun2 = input("Give me a noun that you own: ")
line2 = "And " + verb1 + " my " + noun2

verb2 = input("How 'bout another verb?: ")
noun3 = input("Another thing you own? ")
line3 = "Let it " + verb2 + " away my " + noun3

name = input("Oh how rude of me, I didn't ask you your name! What's your name?: ")
line4 = "'Cause " + name + " wants to feel the thunder"

verb3 = input("What's something you like to do?: ")
line5 = name + " wants to " + verb3

line6 = line1
line7 = "I'm coming clean!"

print("I have a song for you...")

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)