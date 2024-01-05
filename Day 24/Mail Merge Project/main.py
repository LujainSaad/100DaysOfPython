# #Reading names into a list
# with open("Input/Names/invited_names.txt") as file:
#     namesStr = file.read()
#
# namesList = namesStr.split()
#
# #Reading the letter
# with open("Input/Letters/starting_letter.txt") as file:
#     letter = file.read()
#
#
# #Printing the letter with the names
# for name in namesList:
#     newletter = letter.replace("[name]", name)
#     print(newletter)


with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()  # Return lines to a list

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        newName = name.strip()
        newLetter = letter.replace("[name]", newName)
        with open(f"./Output/ReadyToSend/letter_for_{newName}", mode="w") as done:
            done.write(newLetter)
