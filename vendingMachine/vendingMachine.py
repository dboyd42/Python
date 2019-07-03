# Program vendingMachine.py
# Description:
#     Creates and simulates a vending machine.
# Author: David Boyd
# Date: 9 December 2017
# Revised:
#       16 December 2017
#       15 December 2017
#     09 December 2017

# list libraries used
import os, json, time

# Declare global constants

DEF_VEND_MACH = {'1': ['Snickers', 2.25, 1], '2': ['PopTarts', 1.50, 3], '3': ['A Russian Wife', 2.25, 5],
                 '4': ['CupCakes', 2.25, 7], '5': ['M&Ms', 1.75, 0], '6': ['Skittles', 1.25, 10],
                 '7': ['Funyuns', 2.00, 10], '8': ['Shoelaces', 2.00, 10], '9': ['Hersheys', 2.25, 10],
                 '10': ['Boogers', 59.95, 10] }


##########
# Run program
##########
def main():

    # Declare variables
    Run_VM = dict()

    # Display prgm message, ask user to create vending machine
    IntroMessage()
    Run_VM = Create_VM_Question()
    os.system('cls')

    def Menu():

        # Declare local variables
        menuChoice = ''

        print("============Vending Machine Menu=================")
        print("|| Enter: '1' || To check stock.               ||")
        print("|| Enter: '2' || To enter purchase.            ||")
        print("|| Enter: '3' || To save your hard work.       ||")
        print("|| Enter: '4' || To read your saved file.      ||")
        print("|| Enter: 'q' || To quit the vending program.  ||")
        print("=================================================\n")

        # Ask user selection
        menuChoice = input("What would you like to do? ").lower()
        while ((menuChoice != '1') and (menuChoice != '2') and (menuChoice != '3') \
               and (menuChoice != '4') and (menuChoice != 'q') and (menuChoice != 'quit')):
            print("Not a valid entry, please try again.")
            menuChoice = input("What would you like to do? ").lower()


        os.system('cls')

        # Return values
        return menuChoice

    # Assign call Menu to a variable
    run = Menu()

    while True:
        if run == '1':
            PrettyPrintMenu(Run_VM)
            time.sleep(3)
            run = Menu()

        # End if

        # Purchase from menu
        elif run == '2':
            PurchaseFromMenu(Run_VM)
            run = Menu()

        # End elif

        # Save file
        elif run == '3':
            venFile = SaveFile(Run_VM)
            run = Menu()

        # End elif

        # Display from file
        elif run == '4':
            ReadFile(Run_VM)
            run = Menu()

        # End elif

        # Quit prgm
        elif run == 'q' or run == 'quit':
            Quit(Run_VM)
            run = Menu()

        # End elif

    # End Menu() Function

##########
# End program
##########

# Function IntroMessage
# Description:
#    Displays explaination of program
# Calls:
#    none
# Parameters:
#    none
# Returns:
#    none

def IntroMessage():

    # Declare local variables

    # Dispaly program message
    os.system('cls')
    print("“Make $500 an Hour in the Vending Business!”\n"\
          "“Earn Money While You Sleep in a Vending Machine Business!”\n")
    os.system('pause')

    print()
    print("This program allows users to to store files saved as '.json' files in which they can\n" \
          "later edit in other 3rd party text editing programs, such as textedit and notepad.\n")
    print("These files then can be simulated through a vending machine by the user playing the customer.\n" \
          "The program will allow the customer to make purchases through credit and reduce stock accordingly.\n")
    print("Enjoy!")
    os.system('pause')
    print()

    # Return values

# End IntroMessage() Function

# Function createQuestion_VM
# Description:
#       Asks user which if they want to create a vending machine,
#       use default vending machine, or Quit program.
# Calls:
#    CreateMenu
#       Quit
#       Quit2
# Parameters:
#    none
# Returns:
#    Dictionary vendMach

def Create_VM_Question():

    # Declare local variables
    createQuestion_VM = dict()
    ynCreate = ''

    os.system('cls')

    # Ask user for type of vending machine
    print("Do you want to create your own vending machine?")
    print("Enter: 'y' || Yes! I want to create my own vending machine.\n" \
          "Enter: 'i' || Import! I want to import my vending machine.\n" \
          "Enter: 'n' || No! I want to use the preloaded vending machine.\n" \
          "Enter: 'q' || Quit! I want to quit the program.\n")

    ynCreate = input("Enter [y/i/n/q]: ").lower()

    if (ynCreate == 'y') or (ynCreate == 'yes'):
        createQuestion_VM = CreateMenu()

    # End if

    elif (ynCreate == 'n') or (ynCreate == 'no'):
        createQuestion_VM = DEF_VEND_MACH

    # End elif

    elif (ynCreate == 'q') or (ynCreate == 'Quit'):
        Quit2()

    # End elif

    # Import
    elif (ynCreate == 'i') or (ynCreate == 'import'):

       createQuestion_VM = ImportFile()

    # End elif

    # yNCreate while validation
    while (ynCreate != 'y') and (ynCreate != 'yes') and (ynCreate != 'n') and (ynCreate != 'no') and (ynCreate != 'q') and (ynCreate != 'Quit')and (ynCreate != 'i'and (ynCreate != 'import')):
        print("Not a valid entry.")
        print("Enter: 'y' || Yes! I want to create my own vending machine.\n" \
              "Enter: 'i' || Import! I want to import my vending machine.\n" \
              "Enter: 'n' || No! I want to use the preloaded vending machine.\n" \
              "Enter: 'q' || Quit! I want to quit the program.\n")

        ynCreate = input("Enter [y/i/n/q]: ").lower()

        if (ynCreate == 'y') or (ynCreate == 'yes'):
            createQuestion_VM = CreateMenu()

        # End if

        elif (ynCreate == 'n') or (ynCreate == 'no'):
            createQuestion_VM = DEF_VEND_MACH

        # End elif

        elif (ynCreate == 'q') or (ynCreate == 'quit'):
            Quit2()

        # End elif

        # IMPORT FILE
        elif (ynCreate == 'i') or (ynCreate == 'import'):

           creatQuestion_VM = ImportFile()

        # End elif

    print()

    return createQuestion_VM

# End Create_VM_Question() function

# Function CreateMenu
# Description:
#       Create dictionary based menu from user input
#       Dictionary key is of string name and values is an array containing additional data
# Calls:
#    none
# Parameters:
#    none
# Returns:
#    Dictionary createMenu_VM

def CreateMenu():

    # Declare local variabels
    createMenu_VM = dict()
    escapeValueItemAmt = 0
    escapeValuePrice = 0
    escapeValueQty = 0
    itemAmount = 0
    itemMarker = ''
    tempItemName = ''
    tempItemPrice = 0.00
    tempItemQuantity = 0

    os.system('cls')
    # Ask user for number of items
    while escapeValueItemAmt == 0:       # itemAmount validiation
        try:
            itemAmount = int(input("Number of items in vending machine: "))
            print()

        except ValueError:
            print("Number of items is not a valid amount, please try again.")
            continue

        # End except

        if (itemAmount <= 0):
            print("Your vending machine won't make money without products!")
            print("Number of items has to be greater than 0.")
            continue

        # End if

        else:
            escapeValueItemAmt = 1
            print()

        # End else

        # End try

    # End while

    # Get user vending machine input            // { 'itemMarker' : ['name', float(price), int(qty)] }
    print("Enter '0' in Item name to cancel.")
    for x in range(0, itemAmount):
        itemMarker = str(x + 1)

        # Reset validation loops
        escapeValuePrice = 0
        escapeValueQty = 0

        # Input item name
        tempItemName = input("Item " + itemMarker + " name: ")

        # Prevent empty dictionary validation
        while x == 0 and tempItemName == '0':
            os.system('cls')

            print("You're vending machine won't make MONEY without products!")
            print("Enter name or '00' to 'quit' program.")
            tempItemName = input("Item " + itemMarker + " name: ")

            # Quit program
            if tempItemName == '00':
                Quit2()

            # End if

        # End While

        # Stop appending items
        if tempItemName == '0':
            break

        # End if

        # Price validation & float conversion
        while escapeValuePrice == 0:
            try:
                tempItemPrice = float(input("Enter price of " + str(tempItemName) + ": $"))

            except ValueError:
                print("Price is not a valid amount, please try again")
                continue

            if (tempItemPrice <= 0):
                print("Price has to be greater than FREE!")
                continue

            # End if

            else:
                tempItemPrice = format(tempItemPrice,',.2f')
                escapeValuePrice = 1

            # End else

            # End try

        # End while

        # Quantity validation
        while escapeValueQty == 0:
            try:
                tempItemQuantity = int(input("Enter " + str(tempItemName) + " quantity: "))

            except ValueError:
                print("Quantity is not a valid amount, please try again.")
                continue

            # End except

            if (tempItemQuantity) < 0:
                print("Quantity has to be 0 or greater, please try again.")
                continue

            # End if

            else:
                escapeValueQty = 1

            # End else
            # End try

        # End while

        # Append inputted data to dictionary
        createMenu_VM[itemMarker] = [tempItemName, tempItemPrice, tempItemQuantity]

    # End for

    # Return values
    return createMenu_VM

# End CreateMenu() Function

# Function PrettyPrintMenu
# Description:
#    Displays vending machine menu
# Calls:
#
# Parameters:
#    print_VM
# Returns:
#    none

def PrettyPrintMenu(print_VM):

    # Declare local variables


    # Display Vending Machine
    os.system('cls')

    print("||=============VENDING MACHINE=================||")
    for key in print_VM.keys():
        print('|| ID:[' +key+ '] ' +print_VM[key][0]+ ': $' +str(print_VM[key][1])+ ' Qty:' +str(print_VM[key][2]))
    print("||=============================================||")

    # Return values

# End PrettyPrintMenu() Function

# Function PurchaseFromMenu
# Description:
#       Asks for which item to purchase
#       Asks for money or cancelation
#       Checks for sufficient funds or keep asking
#       Makes purchase
#       Provides change if necessary
# Calls:
#        CheckMenuItem
#       CheckUserCancel
#       PrettyPrintMenu
#       UpdateMenuQuantity
# Parameters:
#    pfMenu_VM
# Returns:
#    pfMenu_VM

def PurchaseFromMenu(pfMenu_VM):

    # Declare local variables

    itemToPurchase = ''
    itemPrice = dict()
    itemPriceName = ''
    priceInserted = 0.00
    yN_Purchase = ''
    escapeValueItemPrice = 0

    PrettyPrintMenu(pfMenu_VM)

    # Ask user to select purchase
    itemToPurchase = input("\nPlease enter the ID:[number]\n"
                           "     Or press '0' to cancel: ")

    # Cancel purchase
    if itemToPurchase == '0':
        os.system('cls')
        PrettyPrintMenu(pfMenu_VM)
        print("Canceled by user.\n")
        os.system('pause')

    # End if

    # Ready to make purchase
    elif (CheckMenuItem(itemToPurchase, pfMenu_VM)):
        itemPrice = pfMenu_VM[itemToPurchase][1]

        # Price validation
        escapeValueItemPrice = 0
        while escapeValueItemPrice == 0:
            try:
                priceInserted = float(input("Please insert $" + str(itemPrice)+ " ('0' to cancel): $"))

            except Exception:
                os.system('cls')
                PrettyPrintMenu(pfMenu_VM)
                print("\nPrice is not a valid amount, please try again.")
                os.system('pause')
                escapeValueItemPrice = 1

            # Insufficient funds loop
            if ((priceInserted) < float(itemPrice) and float(priceInserted) != 0):
                os.system('cls')
                PrettyPrintMenu(pfMenu_VM)
                print()
                print("Insufficient credit.\n")
                os.system('pause')
                escapeValueItemPrice = 1

            # Cancel purchase
            elif (float(priceInserted) == 0):
                os.system('cls')
                PrettyPrintMenu(pfMenu_VM)
                print("Canceled by user.\n")
                os.system('pause')
                escapeValueItemPrice = 1

            # Change
            elif (float(priceInserted) >= float(itemPrice)):
                change1 = float(priceInserted) - float(itemPrice)
                change = format(change1, ',.2f')

                # Purchased
                UpdateMenuQuantity(itemToPurchase, pfMenu_VM)
                print("Thank you for your purchase!")
                print("You have received item: " + pfMenu_VM[itemToPurchase][0] + "\n")
                print("Please take your change: $" + str(change))
                os.system('pause')
                os.system('cls')
                escapeValueItemPrice = 1

            # End elif

            else:
                escapeValueItemPrice = 1

            # End else

        # End while

    # End elif
    else:
        pass

    # Return values
    return pfMenu_VM

# End PurchaseFromMenu() Function

# Function SaveFile
# Description:
#        Create and write the vending machine to a json file
# Calls:
#    none
# Parameters:
#    Run_VM
# Returns:
#    title

def SaveFile(Run_VM):

    # Declare local variables
    title = ''
    newFile = ''

    # Display overwrite warning
    print("WARNING! THIS WILL OVERWRITE FILES WITH THE SAME NAME!\n")
    os.system('pause')
    os.system('cls')
    print("WARNING! THIS WILL OVERWRITE FILES WITH THE SAME NAME!\n")
    print("Do not enter '.json' or any other file extension.")

    # Ask for filename
    title = input("Enter name of file\n" \
                  "(Or press '0' to cancel): ")

    # Catch invalid filename
    while (len(title) <= 0):
        print("\nNot a valid entry.\n")
        title = input("Enter name of file\n" \
                      "(Or press '0' to cancel): ")

    # End while

    # Cancel save
    if ((title == 'q') or (title == 'quit') or (title == '0')):
        return

    # End if

    # ==========JSON WRITE/READ================#
    # writes/dumps code to a text file
    json.dump(Run_VM, open(title+'.json', 'w'))# indent = 4)
    # =========================================#
    print(title + " was written to file!")
    os.system('pause')

    # Return values
    return title

# End SaveFile() Function

# Function ReadFile
# Description:
#        Displays dictionary from file
# Calls:
#    none
# Parameters:
#    dictionary dictVM
# Returns:
#    none

def ReadFile(dictVM):

    try:
        print(json.dumps(dictVM, indent = 4))
        print("\nYour file has been read successfully!")
        os.system('pause')
        os.system('cls')

    except Exception:
        print("No dictionary found.")
        os.system('pause')

    # End try

    # Return values


# Function ImportFile
# Description:
#        Imports a dictionary '.json' file into prgm
#       The file is then used as the items in a vending machine
# Calls:
#    main()
# Parameters:
#    none
# Returns:
#    dictionary json1_data


def ImportFile():

    #Declare local variables
    escapeValue = 0
    readFile = ''


    # filename validation while loop
    escapeValue = 0
    while escapeValue == 0:

        # Warn user of filename restrictions
        os.system('cls')
        print("TO IMPORT FILE:\n")
        print("File must be in same directory as vendingMachine.py program.")
        print("File must have been written by this program previously.")
        print("Do not enter '.json' or any other file extension.")
        print("File must be a JSON file.")
        print("Enter only the filename.")
        print("Press '0' to cancel")
        print()

        # Ask user for filename
        readFile = input("Enter filename: ") + '.json'

        # Cancel import
        if readFile == '0'+'.json':
            print("Restarting program.")
            os.system('pause')
            main()

        # End if

        # try filename validity
        else:
            try:
                json1_file = open(readFile)
                json1_str = json1_file.read()
                json1_data = json.loads(json1_str)
                print("\nFile imported successfully!")
                os.system('pause')
                escapeValue = 1

            except Exception:
                print("\nFile not found.")
                os.system('pause')
                continue

            # End try

        # End else

    # Return values
    return json1_data

# Function CheckMenuItem
# Description:
#       Checks if item exists in menu
#       Then checks if item is in stock
# Calls:
#       CheckMenuItem
#       PrettyPrintMenu
# Parameters:
#        item
#       chkMenuItm_VM
# Returns:
#        Boolean

def CheckMenuItem(item, chkMenuItm_VM):

    # Declare local variables
    if (item in chkMenuItm_VM.keys()):
        if (chkMenuItm_VM[item][2] > 0):
            return True

        # End if

        else:
            print()
            PrettyPrintMenu(chkMenuItm_VM)
            print()
            print(chkMenuItm_VM[item][0] + " is out of stock.\n")
            os.system('pause')

        # End else

    else:
        PrettyPrintMenu(chkMenuItm_VM)
        print("\nItem " + str(item) + " does not exist in vending machine.\n")
        os.system('pause')

    # End else

    # Return values
    return False

# End CheckMenuItem() Function

# Function CheckUserCancel
# Description:
#       Checks if user's input is a cancel
# Calls:
#        none
# Parameters:
#        userInput
# Returns:
#        Boolean

def CheckUserCancel(userInput):

    # Declare local variables
    if (userInput == 0):
        print("Canceled by user")
        return True

    # End if

    # Return values
    return False

# End CheckUserCancel() Function

# Function UpdateMenuQuantity
# Description:
#        Update menu item's quantity
#       Displays updated vending machine dict
# Calls:
#        PrettyPrintMenu
# Parameters:
#        item
#       updateMQ_VM
# Returns:
#       none

def UpdateMenuQuantity(item, updateMQ_VM):

    # Declare local variables

    # Update vending machine quantity
    updateMQ_VM[item][2] -= 1
    PrettyPrintMenu(updateMQ_VM)

    # Return values

# End UpdateMenuQuantity() Function

# Function Quit
# Description:
#        Exit option menu:
#       continue, save, restart, or quit prgm
# Calls:
#       main
# Parameters:
    #    Run_VM
# Returns:
#    none

def Quit(Run_VM):

    # Declare local variables
    escapeValue = 0
    yN = ''

    os.system('cls')
    print("Sorry to see you go!")
    print("Enter: 'c' || Continue! I want to continue the program.\n"
          "Enter: 's' || Save! I want to save my vending machine.\n"
          "Enter: 'r' || Restart! I want to restart the program.\n"
          "Enter: 'q' || Quit! I want to quit the program.\n")

    # Ask for user option
    yN = input("Enter [c/s/r/q]: ").lower()

    while escapeValue == 0:

        # Continue from previous menu
        if yN == 'c' or yN == 'continue':
            escapeValue = 1
            os.system('cls')

        # End if

        # Save before exiting prgm
        if yN == 's' or yN == 'save':
            SaveFile(Run_VM)
            print("\nThank you for playing.  Have a nice day!")
            os.system('pause')
            exit()

        # End elif

        # Restart prgm
        elif yN == 'r' or yN == 'restart':
            print()
            print("Restarting program...")
            os.system('pause')
            main()

        # End elif

        # Quit the prgm
        elif yN == 'q' or yN == 'quit':
            print("\nThank you for playing.  Have a nice day!")
            os.system('pause')
            exit()

        # End elif

        # Stay in loop
        elif yN != 'c' and yN != 'continue' and yN != 's' and yN != 'save' and yN != 'r' and yN != 'restart' and yN != 'q' and yN != 'quit':
            print("Not a valid entry.")

        # End elif

    # End while
    escapeValue = 1

    # Return values

# End Quit Function

# Function Quit2
# Description:
#        Exit option menu with no option to save files
# Calls:
#       main
#       exit
# Parameters:
#       none
# Returns:
#        none

def Quit2():

    # Declare local variables
    escapeValue = 0
    yN = ''

    # Confirm exiting prgm
    os.system('cls')
    print("Are you sure you want to quit?!")
    print("Enter: 'r' || Restart! I want to restart the program.\n" \
          "Enter: 'q' || Quit! I want to quit the program.\n")

    # while validation -> invalid response
    while escapeValue == 0:

        # Ask user for selection
        yN = input("Enter [r/q]: ").lower()

        # Exit the prgm
        if yN == 'q' or yN == 'quit':
            print("\nThank you for playing.  Have a nice day!")
            os.system('pause')
            exit()

        # End if

        # Restart prgm
        elif yN == 'r' or yN == 'restart':
            print()
            print("Restarting program...")
            print('\n\n')
            main()

        # End elif

        else:
            print("Not a valid entry.")

        # End else

    # End while

    # Return values

# End Quit2() Function

# End Program //Call to main function::
main()
