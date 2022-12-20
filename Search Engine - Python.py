###DEFINE### Defines variables and lists and imports modules. 
from colorama import init,Fore,Back,Style #:)
from termcolor import colored #:)
import os
import winsound
import scratchattach as scratch3
from scratchattach import Encoding
init(autoreset=True)
search = None
items = ['cat','dog','cow','car','destroy','apple']
removed_items = []
added_items = []
credits_mine = "Credits: \nColor providers:\n>Termcolor - https://pypi.org/project/termcolor/\n>Colorama - https://pypi.org/project/colorama/\nSound provider:\n>Winsound\nProgram was made by Miles Krueger in Python 3.10.4 - Python 3.11.0"
searchs = sorted(items)
###FUNCTIONS###
def beep(frequency, duration):
    winsound.Beep(frequency, duration)
###Start actual program###
from os import system, name
def clear():
    if name == 'nt':
        _= system('cls')
while search != "/close":
    print('--------------------------------------------------------------------------------')
    print(colored('PySearch Search Engine. Enter something to search. If you need help, enter /help. ','red','on_white'))
    search = input()
    clear()
    print('--------------------------------------------------------------------------------')
    search = search.lower()
###COMMANDS### Checks if the user has entered a command.
    if search == "/items":
        print(colored('Here are all the items you can search for:','white','on_blue'))
        print(' ')
        item1 = 0
        for item in searchs:
            print(searchs[item1])
            item1 = item1 + 1
    elif search == "/help":
        print('Enter something to search. Enter a command to get a special result. Here is a list of commands: \
    \n-------------------------------------------------------------------------------- \
    \n  >/Close - Closes this application \
    \n  >/Add - Adds a item to the list of items you can search for. \
    \n  >/Items - Displays all the items you can search for. \
    \n  >/Credits - Prints the credits for this program.')
    
    elif search == "/add":
        print(colored('Enter something you want to add to the search list: ','blue','on_white'))
        dialouge = ""
        add = ""
        while add == "":
            add = input(dialouge)
            if add == "":
                dialouge = "Please enter something. To terminate this function, enter exit. "
        if add != "exit":
            add = add.lower()
            searchs.append(add)
            searchs = sorted(searchs)
            print(add + ' has been added to the list of items you can search for')
            added_items.append(add)
        else:
            print('Functon terminated')
    elif search == "/close":
        beep(400, 400)
    elif search =="/credits":
        print(credits_mine)
    elif search == "/remove":
        dialouge = ""
        item_remove = 0
        remove_item = ""
        print(colored('Enter something you want to remove from the search list: ','blue','on_white'))
        remove_input = input(dialouge)
        for item in searchs:
            if searchs[item_remove] == remove_input:
                remove_item = searchs[item_remove]
                item_remove_number = item_remove
                item_remove = item_remove + 1
            else:
                item_remove = item_remove + 1
        if remove_input == "":
            print('You did not enter anything into the input and nothing was removed')  
        elif remove_item == "":
            print("We did not find any results and couldn't remove any items. ")  
        else:
            searchs.remove(remove_item)
            print(remove_item + ' was sucsessfully removed from the search list')
            removed_items.append(remove_item)
    elif search == "/reset":
        reset = 0
        print('You have added:')
        for items in added_items:
            print(added_items[reset])
            reset = reset + 1
        print('to the search list, and removed:')
        reset = 0
        for items in removed_items:
            print(removed_items[reset])
            reset = reset + 1
        prompt = 'from the search list. Are you sure you want to continue (y/n) '
        a = 0
        while a != 'y' and a != 'n':
            a = input(prompt)
            a = a.lower()
            prompt = 'Your answer could not be understood. Do you want to reset the search items? (y/n) '
        if a == 'y':
            print('Search items have been reset')
            items = ['cat','dog','cow','car','destroy','apple']
            searchs = []
            searchs = sorted(items)
        elif a == 'n':
            print('Canceled.')
            
    elif search == "/scratchattach":
        print('Scratchattach can accses information via your Scratch (scratch.mit.edu) profile. If you have a scratch profile, this is usable with you.')
        a = 0
        prompt = 'Do you have Scratch profile? y/n.'
        while a != 'y' and a != 'n':
            a = input(prompt)
            a = a.lower()
            prompt = 'Your information could not be understood. Do you have a Scratch profile'
        if a == 'y':
            print('Great. You will need to give us information such as your Scrach username or password.')
            username = input('To start, what is your Scratch username? To cancel, enter "n."')
            if a == 'n':
                None
            else:
                print('Thanks! Now we need the password to your scratch account. NO INFORMATION IS BEING STORED.')
                password = input('')
                if password == 'n':
                    None
                else:
                    print('Thanks again')
                    print('Loading... If this frame goes away, the name and/or password is not valid.')
                    session = scratch3.login(username, password)
                    print('Alright, hello ' + str(username) + '. You can now use this program to retrive information from your profile.')
                    
                    
                
            
            
        elif a == 'n':
            print('Canceled.')
    
    else:
        item1 = 0
        results = []
        for item in searchs:
            if search in searchs[item1]:
                results.append(searchs[item1])
            item1 = item1 + 1
        if len(results) == 0:
            print('Sorry, no results founds')
        else:
            if len(results) == 1:
                print('I found ' + str(len(results)) + ' result:')
            else:
                print('I found ' + str(len(results)) + ' results:')
            print(' ')
            item1 = 0
            for item in results:
                print(results[item1])
                item1 = item1 + 1
