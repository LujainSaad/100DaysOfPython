
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print("timmy")
# timmy.shape("turtle")
# timmy.color("pink")
# timmy.forward(100)
#
#
# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

########################################################

# To install packages : go to website called PYPI
# 1- Preferences
# 2- 'Project Name'
# 3- Project Interpreter
# 4-    +
# 5- Search package name
# 6- Install package

########################################################

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokémon", ["Abra", "Jolteon", "Falinks"])
table.add_column("Type", ["Psychic", "Electric", "Fighting"])

print(table)

