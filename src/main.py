 # -- coding: utf-8 --
from structure import List
from GUI import *

# Function to check if date is a number
# and a certain format (8 numbers)
def date_checker(question):
    date_check = True
    while date_check: 
        date = input(question)
        if date.isdecimal() and len(date) == 8:
            date_check = False
            return date
        elif len(date) == 0:
            date = date + "00000000"
            date_check = False
            return date
        elif len(date) < 8:
            print(f"{date} is not in the correct format, try again!")
        else:
            print(f"{date} is not a date, try again!")

def query_lists_name(list_name, stored_Lists):
    result = []
    # take out array of list names (dictionary keys)
    for packing_list in stored_Lists.keys():
        if list_name in packing_list:
            result.append(packing_list)

    return result

def query_lists_date(todays_date, stored_Lists):
    result = []
    # take out array of list names
    # .values() takes out the values from the dict
    for packing_list in stored_Lists.values():
        if int(packing_list.date) >= int(todays_date):
            result.append(packing_list)

    # sort with the attribute date for object
    # to have descneding, just add reverser=True after x.date
    # but before last parentheses
    result.sort(key=lambda x: x.date)
    return result

def create_list(list_name, list_date):
    return List(list_date, list_name)

def ask_for_list(list_name, search, stored_Lists):
    if len(search) > 0:
        if len(search) == 1:
            return search[0]
        elif len(search) > 1:
            print(f"There are multiple queries for the search '{list_name}'") 
        i = 0 #counter for indexing
        for x in search:
            i += 1
            # take out the list object from dictionary stored_Lists
            current_list = stored_Lists[x]
            print(f"{i}. {current_list.print_list()}")
    
        while True:
            list_index = input("Type the number of which planner you would like to choose.\n:")
            if list_index.isdecimal():
                # convert string input to int
                index = int(list_index)
                # eg 0 < index < 10
                if index > 0 and index < len(search) + 1: 
                    return search[index - 1]
                else: 
                    print("Incorrect index!")
            else:
                print("Try again, the input supplied was not a number.")
    else:
        print(f"There are no lists with the search '{list_name}'")
        return None

def remove_item(list_to_remove_from):
    list_to_remove_from.print_content()

    while True:
        print("Input is case sensitive!")
        item_to_remove = input(":")
        if item_to_remove in list_to_remove_from.items_in_list:
            list_to_remove_from.items_in_list.remove(item_to_remove)
            print(f"{item_to_remove} is now removed from the system.")
            return
        else:
            print(f"{item_to_remove} does not exist in {list_to_remove_from.name}")
            print("Try again!")

def look_for_list(list_name, stored_Lists):
    # Contains all the lists with the searched list_name
    # eg. search = [ "mikael", "test", ....]
    search = query_lists_name(list_name, stored_Lists)
    return ask_for_list(list_name, search, stored_Lists)

def remove_list(list_name, stored_Lists):
    # Query for list(s) in system
    list_to_remove = look_for_list(list_name, stored_Lists)
    print(f"{list_to_remove} is now removed from the system!")
    stored_Lists.pop(list_to_remove)

def remove_item_from_list(list_name, stored_Lists):
    # Query for list(s) in system
    list_to_remove_from = look_for_list(list_name, stored_Lists)
    remove_item(stored_Lists[list_to_remove_from])

def date_coming_list(todays_date, stored_Lists):
    # search for which dates that comes after todays date
    search = query_lists_date(todays_date, stored_Lists)

    if len(search) > 0:
        print(f"Following planners are from {todays_date}")
        i = 0
        for coming_list in search:
            i += 1
            print(f"{i}. {coming_list.print_list()}")
    else:
        print(f"There are no planners coming after {todays_date}")

def reminder(todays_date, stored_Lists):
    search = query_lists_date(todays_date, stored_Lists)
    if len(search) > 0:
        return search[0]

def show_content_list(stored_Lists):
    list_name = input("What name does the planner have?\n:")
    list_to_print = look_for_list(list_name, stored_Lists)
    if list_to_print is not None:
        stored_Lists[list_to_print].print_content()

def add_item_list(stored_Lists):
    list_name = input("What name does the planner have?\n:")
    list_to_add_items = look_for_list(list_name, stored_Lists)
    item_to_add = input("What would you like to add?\n>>>")
    if list_to_add_items is not None:
        stored_Lists[list_to_add_items].add_item(item_to_add)


def initiate_file(stored_Lists):
    # open file and store it as variable f
    with open("storedPlanners/plans.txt", "r", encoding="UTF-8") as f:
        for line in f:
            extracted_list = line.split('/') # list is returned
            if len(extracted_list) > 1:
                created_list = create_list(extracted_list[0], extracted_list[1])
                stored_Lists[extracted_list[0]] = created_list

                for item in extracted_list[2:]:
                    created_list.add_item(item)

def shutdown(stored_Lists):
    with open("storedPlanners/plans.txt", "w", encoding="UTF-8") as f:
        for available_list in stored_Lists.values():
            all_items = available_list.name + "/" + available_list.date

            for item in available_list.items_in_list:
                all_items = all_items + "/" + item 
            
            f.write(all_items)

def eventLoop(date, stored_Lists):
    running_state = True
    while running_state:
        print("\nN - New planner")
        print("I - Show content in planner")
        print("S - Add item to a planner")
        print("A - Show incoming planners")
        print("R - Remove planner")
        print("B - Remove item from planner")
        print("Q - Quit.")

        choice = input(":")
        
        if choice == 'N' or choice == 'n':
            list_name = input("What would you like to name the planner?\n:")
            list_date = date_checker(f"What date is the {list_name} due?\n:")

            created_list = create_list(list_name, list_date)
            stored_Lists[created_list.name] = created_list
            print(f"{list_name} has been created!!")
        elif choice == 'I' or choice == 'i':
            show_content_list(stored_Lists)
        elif choice == 'S' or choice == 's':
            add_item_list(stored_Lists)
        elif choice == 'A' or choice == 'a':
            date_coming_list(date, stored_Lists)
        elif choice == 'R' or choice == 'r':
            list_name = input("Which planner would you like to remove?\n:")
            remove_list(list_name, stored_Lists)
        elif choice == 'B' or choice == 'b':
            list_name = input("Which planner would you like to remove from?\n>:")
            remove_item_from_list(list_name, stored_Lists)
        elif choice == 'Q' or choice == 'q':
            shutdown(stored_Lists)
            running_state = False
        else:
            print("Please, supply the letters provided above.")

def clear_screen():
    print(chr(27) + '[2j' + '\033c'+'\x1bc')


def main():
    # clears the screen
    clear_screen()
    print("===================================")
    print("|         Pack Planner             |")
    print("===================================")
    stored_Lists = {} # Dictionary for lists in program
    date = date_checker("Todays date: ")

    initiate_file(stored_Lists)
        
    remind_list = reminder(date, stored_Lists)
    if remind_list is not None:
        print("=======\nThere are planners coming up!")
        list_to_print = remind_list.print_list()
        print("Following planner is the closest to todays date:\n* " + list_to_print + "\n=======\n")

    eventLoop(date, stored_Lists)
    clear_screen()

run_window()
main()


    
