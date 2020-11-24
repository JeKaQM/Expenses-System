class Expense_System:
    
    def __init__(self, desc, cat, amount):
        self.desc = desc
        self.cat = cat
        self.amount = amount
    
    def menu():
        print("Welcome To Expenses system")
        choice = int(input("Please choose the mode, 1 = Edit Mode, 2 = Analysis mode: "))
        run = True
        while run == True:
            if choice == 1:
                run = False
                Edit_mode()
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
                Edit_mode_Add()
            elif edit_choice == 2:
                edit_run = False
                Edit_mode_Delete()
                
                
        
        
    def Analysis_mode():
        print()
    
                
            

