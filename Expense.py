class Expense_System:
      
    global Expense_list #Sets the expense list to global 
    Expense_list = []
    
    def menu():
        print("Welcome To Expenses system")
        choice = int(input("Please choose the mode, 1 = Edit Mode, 2 = Analysis mode: "))
        run = True
        while run == True: #Creates a while loop until the correct choice is given
            if choice == 1:
                run = False
                Expense_System.Edit_mode_menu() #Calls another method
            elif choice == 2:
                run = False
                Expense_System.Analysis_mode()
            else: #Makes sure the program doesnt crash when ivalid input is given
                print("Error, wrong choice")
    
    
    def Edit_mode_menu():
        print("Welcome to Edit Mode!")
        edit_choice = int(input("Please choose what you want to edit, 1 = Add Expense, 2 = Delete Expense: "))
        edit_run = True
        while edit_run == True:#While loop
            if edit_choice == 1:
                edit_run = False
                Expense_System.Edit_mode_Add()#Calls the edit mode method
            elif edit_choice == 2:
                edit_run = False
                Expense_System.Edit_mode_Delete()
    
    def Edit_mode_Add():
        Desc = input("Please enter the description: ")#Asks user for the nessecary inputs
        Cat = input("Please enter the category: ")
        Amount = int(input("Please enter the amount: "))
        NewList = [] #Creates a list
        NewList.append(Desc)#Adds each of the elements entered to that list
        NewList.append(Cat)
        NewList.append(Amount)
        Expense_list.append(NewList) #Note this gets stored in one singular list meaning we cant actually access the data like desc or Category etc, needs a fix
        print("Expense has been successfully stored!")
        m_choice = input("Please choose if you want to return to main menu(1) or Edit Menu(2): ")
        if m_choice == "1":
            Expense_System.menu()
        elif m_choice == "2":
            Expense_System.Edit_mode_menu()
        else:
            print("Invalid choice returning back to main menu!")
            Expense_System.Edit_mode_menu()
        
    
    def Edit_mode_Delete():
        re = input("Please enter the description of the expense: ")
        for list in Expense_list:#Goes throguh the list to find the specific description
            if re in list: 
                Expense_list.remove(list) #Note this clears the list regardless of whats been inputted its meant to clear the list if it has found the expense that matches description. Needs a fix
                print("This has been succseffuly removed!")
                print(Expense_list)#Prints the list after its been emptied
            else:
                print("No Expense found!")
                Expense_System.Edit_mode_Delete() #Error prevention
                
                
        
        
    def Analysis_mode(): ## This needs to be fixed where for each list the correct values need to be displayed 
        print("Welcome to the Analysis mode!")
        print("Below you will find all the details of your expenses")
        print("Here can be seen the list of all the epxenses", Expense_list[0])#prints the list of all the expenses
        print("The average spend per item is", Expense_list[0])
        print("Total Expenditure is", Expense_list[0])
        while True:
            ch = int(input("To go back to main menu please press 1, to exit press 2: "))#while loop to see if the user wants to go back or quit
            if ch == 1:
                Expense_System.menu();
            elif ch == 2:
                break;
            else:
                print("Error wrong choice")
            
    
                
Expense_System.menu()#Runs the application starting with main method

