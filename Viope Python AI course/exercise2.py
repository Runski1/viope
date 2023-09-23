# In the second exercise the idea is to create a small grocery shopping list with the list datastructure.
# In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3)
# print the list and quit.
#
# If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the
# list. If the user decides to remove something, the program informs the user about how many items there are on the list
# (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). If
# the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "
# The following items remain in the list:" followed by the remaining items one per line. If the user selects anything
# outside the options, including when deleting items, the program responds "Incorrect selection.". When the program
# works correctly it prints out the following:
grocery_list =[]
def error_print():
    print("Incorrect selection.")


def add_items():
    grocery = input("What will be added?: ")
    grocery_list.append(grocery)
# MIGHT NEED TO USE grocery_list AS PARAMETER
while True:
    user_input = input("Would you like to\n"
                       "(1)Add or\n"
                       "(2)Remove items or\n"
                       "(3)Quit?: ")
    match user_input:
        case "1":
            add_items()
        case "2":
            remove_items()
        case "3":
            for item in range(len(grocery_list)):
                print(grocery_list[item])
            quit()
        case _:
            error_print()




