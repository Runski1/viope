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
# works correctly, it prints out the following:

grocery_list = []


def error_print():
    print("Incorrect selection.")


def add_items():
    grocery = input("What will be added?: ")
    grocery_list.append(grocery)


def remove_items():
    str1 = "There are "
    str2 = " items in the list."
    print(str1 + str(len(grocery_list)) + str2)
    removable = input("Which item is deleted?: ")
    try:
        grocery_list.pop(int(removable))
    except (ValueError, IndexError):
        error_print()


def quit_code():
    print("The following items remain in the list:")
    for item in range(len(grocery_list)):
        print(grocery_list[item])
    quit()


while True:
    user_input = input("Would you like to\n"
                       "(1)Add or\n"
                       "(2)Remove items or\n"
                       "(3)Quit?: ")
# Match case is for python 3.10 only
# Use dictionary or elif monster instead
#     match user_input:
#         case "1":
#             add_items()
#         case "2":
#             remove_items()
#         case "3":
#             quit_code()
#         case _:
#             error_print()

# Here's the code for dictionary
    input_options = {
        "1": add_items,
        "2": remove_items,
        "3": quit_code,
    }
    selected_option = input_options.get(user_input)
    if selected_option:
        selected_option()
    else:
        error_print()
