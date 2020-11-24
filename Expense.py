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
        desc = input("What is the description?")
        cat = input("What is the category")
        amount = int(input("What is the amount"))
        Expense_System.Expense_list.append(Expense_System(desc, cat, amount))
        e = Expense_System(desc, cat, amount)
        print(str(e))
        
        
        
        
    
    def Edit_mode_Delete():
        pass
                
        
        
    def Analysis_mode():
        pass
    
    def __str__(self):
        return Expense_System(self.desc, self.cat, self.amount)
                
Expense_System.menu()

