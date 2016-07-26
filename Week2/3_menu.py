import random

adj_list =["crispy","crunchy","baked","mini","saucy",
"sweet","broiled","steamed","appetizing","sticky"]
cook_list =["deep-fried","American","Chinese","toasted",
"Italian","French","Filipino","Mexican","Brazilian","grilled"]
food_list =["bacon","burgers","fries","potato","cake",
"croutons","chicken","hot dog","twinkies","asparagus"]

for i in range(len(adj_list)):
	# Pick random items from each list
	adj = adj_list[random.randint(0, len(adj_list) - 1)]
	cook = cook_list[random.randint(0, len(cook_list) - 1)]
	food = food_list[random.randint(0, len(food_list) - 1)]

	# Remove item from list
	adj_list.remove(adj)
	cook_list.remove(cook)
	food_list.remove(food)
	
	# Print out random food name
	print(str(i) + ". " + adj.capitalize() + " " + 
		cook.capitalize() + " " + food.capitalize())