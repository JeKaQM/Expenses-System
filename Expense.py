class Expense_System:
    
    def __init__(self, desc, cat, amount):
        self.desc = desc
        self.cat = cat
        self.amount = amount
        
    Expense_list = []
    
    def menu():
        print("Welcome To Expenses system")
        choice = int(input("Please choose the mode, 1 = Edit Mode, 2 = Analysis mode: "))
        run = True
        while run == True:
            if choice == 1:
                run = False
                Expense_System.Edit_mode_menu()
            elif choice == 2:
                run = False
                Analysis_mode()
            else:
                print("Error, wrong choice")
    
    
    def Edit_mode_menu():
        print("Welcome to Edit Mode!")
        edit_choice = int(input("Please choose what you want to edit, 1 = Add Expense, 2 = Delete Expense"))
        edit_run = True
        while edit_run == True:
            if edit_choice == 1:
                edit_run = False
                Expense_System.Edit_mode_Add()
            elif edit_choice == 2:
                edit_run = False
                Edit_mode_Delete()
    
    def Edit_mode_Add():
        ExpenseAdd = list(map(str, input('Enter Description: ').split(',')))
        print("Expense has been successfully stored!")
        m_choice = input("Please choose if you want to return to main menu(1) or Edit Menu(2)")
        if m_choice == "1":
            Expense_System.menu()
        elif m_choice == "2":
            Expense_System.Edit_mode_menu()
        else:
            print("Invalid choice returning back to main menu!")
            Expense_System.Edit_mode_menu()
        
    
    def Edit_mode_Delete():
        pass
                
        
        
    def Analysis_mode():
        pass
    
                
Expense_System.menu()

