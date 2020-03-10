def usage():
	print("""This option does not exist, please type the corresponding number.\n
	To exit, enter 5.""")

def print_recipe(name):
	if name in cookbook:
		print("\n Recipe for " + name + ":")
		print("Ingredients list: ")
		print(cookbook.get(name).get("ingredients"))
	else:
		print("No recipe named " + name)

cookbook = {
	"sandwich" : {
		"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
		"meal" : "lunch",
		"prep_time" : 10
	},
	"cake" : {
		"ingredients" : ["flour", "sugar", "eggs"],
		"meal" : "dessert",
		"prep_time" : 60
	},
	"salad" : {
		"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
		"meal" : "lunch",
		"prep_time" : 15
	}
}
while 42:
	option = input("""Please select an option by typing the corresponding number:\n
	1: Add a recipe\n
	2: Delete a recipe\n
	3: Print a recipe\n
	4: Print the cookbook\n
	5: Quit\n>> """)
	if option.isdigit() == False:
		usage()
	else:
		op = int(option)
		if op < 1 or op > 6:
			usage()
		elif op == 3:
			print_recipe(input("""Please enter the recipe's name to get its
			details:\n>> """))	
