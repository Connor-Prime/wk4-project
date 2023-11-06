
class Property():

    default_expense_dict={
        "tax":0, 
        "insurance":0, 
        "utilities":{
            "electric": 0,
            "water": 0,
            "sewer": 0,
            "garbage": 0,
            "gas": 0
        },
        "total_utilities": 0,
        "repairs":0,
        "vacancy": 0,
        "property_management": 0,
        "mortgage": 0,
        "other" : 0
    }


    upfront_costs={
        "down_payment": 0,
        "closing_costs":0,
        "Rehab_budget":0,
        "Other":0
    }    


    def __init__(self, units= {}):
        self.utility_math = "each"
        self.units = units
        self.expenses = Property.default_expense_dict
        self.expenses_total = 0
        self.upfront_costs = Property.upfront_costs
        self.upfront_cost_total = 0

# The data for the property is supposed to be sent on creation, but cna be reset later
        self.add_units()
        self.calculate_upfront_investment()
        self.enter_monthly_expenses()

        self.view_units()
        self.view_monthly_expense_list()
        self.view_upfront_cost()
        self.show_ROI()

    def reset_unit_data(self):

        while True:
            print("Are you sure you want to reset the unit rent data? 'yes' or 'no'?")
            user_input = input().strip()
            if user_input == "no":
                return
            elif user_input=="yes":
                break
            else:
                print("I didn't quite get that.")

        self.units = {}
        self.add_units()


# Adds units based on the amounts of different rent values.

    def add_units(self):
        if self.units == {}:
            print("This property has no recorded rental units.")
        else:
           self.view_units()
    
        while True:
            print("\n\nWould you like to add some unit's to the ROI calculator for this property?")
            user_input = input("type 'yes' for yes or 'no' for no.         ").strip().lower()

            if user_input == "no" or user_input == "quit":
                return
            elif user_input == "yes":
                break
            else:
                print("I didn't quite get that.")

        print("To add units, first enter the rent of the unit's you'll add. Then add the number units that charge that much for rent.")
            
        prompt = "Please enter the rent of the unit(s) you'll add as a decimal number, or enter 'quit' to quit.          " 

        while True:
            units_rent = input(prompt).strip().lower()

            if units_rent=="quit" or units_rent=="q":
                return
            try:
                units_rent = float(units_rent)
                break            
            except:
                print("I didn't quite get that.")


        prompt2 = f"Please enter the number of unit(s) that charge {units_rent} for rent.             "

        while True:
            units_amount = input(prompt2).strip().lower()

            if units_amount=="quit" or units_amount=="q":
                return
            try:
                units_amount = int(units_amount)
                self.units[units_rent] = units_amount
                break
            except:
                print("I didn't quite get that.")

        prompt3 = "Enter 'add' to add more units or 'quit' to quit.          "
        while True:
            self.view_units()
            user_input = input(prompt3).strip()

            if user_input=="quit" or user_input=="q":
                return
            elif user_input == "add":
                self.add_units()
                break

        self.view_units()

    def view_units(self):
            total = 0
            for k,v in self.units.items():
                print(f"Your property contains {v} unit(s) that charge {k} for rent.")
                total += k * v
            print(f"Your total monthly income from rent on these units is ${total}")


    
    def enter_monthly_expenses(self):
        print("\n\nPlease fill out the following information on the possible monthly expendetures:")

        self.expenses_total = 0

        for k in self.expenses:

            if k != "utilities":
                if k != "total_utilities" or self.utility_math != "each":
                    user_input = input(f'Enter the monthly estimate of {k} expenses on this property. Or "quit" to quit.           ').strip()

                    if user_input == "quit":
                        return

                    try:
                        user_input = float(user_input)
                        self.expenses[k] = user_input
                        self.expenses_total += user_input
                    except:
                        print("Please enter a valid decimal number or 'quit' to quit.")
            else:

                # Utilities can be entered by a sub dictionary or just the sum.
                while True:
                    user_input = input("Would like to enter each utily or the sum. 'each' for each, 'sum' for sum or 'quit' for quit.")

                    if user_input == 'each':

                        self.utility_math = 'each'

                        utility_total = 0

                        for k in self.expenses["utilities"]:
                            user_input = input(f'Enter the monthly estimate of {k} expenses on this property. Or "quit" to quit.           ').strip()

                            if user_input == "quit":
                                break

                            try:
                                user_input = float(user_input)
                                self.expenses["utilities"][k] = user_input
                                self.expenses_total += user_input
                                utility_total += user_input
                            except:
                                print("Please enter a valid decimal number or 'quit' to quit.         ")
                        
                        self.expenses["total_utilities"] = utility_total
                        break
                    elif user_input == "sum":
                        self.utility_math = 'sum'
                        break
                    elif user_input == "quit":
                        return
                    else:
                        print("I didn't quit get that.")
                

        self.view_monthly_expense_list()

    def reset_monthly_expense(self):
        while True:
            print("Are you sure you want to reset the monthly expense data? 'yes' or 'no'?")
            user_input = input().strip()
            if user_input == "no":
                return
            elif user_input=="yes":
                break
            else:
                print("I didn't quite get that.")

        self.expenses = Property.default_expense_dict
        self.enter_monthly_expenses()

    def view_monthly_expense_list(self):
        print("\n\nMonthly Property Expense:\n --------------------------------------------------------------------")

        total = 0
        for k,v in self.expenses.items():
            if k != "utilities":
                if k != "total_utilities" or self.utility_math != "each":
                    print(f"{k}  : ${v}")
                    total+= v
            elif k=="utilities" and self.utility_math == "each":

                utilities_total = self.expenses["total_utilities"]
                total += utilities_total

                print(f"utilities total:      ${utilities_total}")
                for k,v in self.expenses["utilities"].items():
                    print(f"           -{k}  : ${v}")

                


        print(f"----------------------------------------------------\nTotal: ${total}")
 
    
    def change_monthly_expenses(self):

        print("Your expense list is as follows\n\n")

        self.view_monthly_expense_list()


        while True:
            user_input = input("\n\nSelect an expense value you would like to change. or 'quit' to quit.\n\n")

            if user_input == "quit":
                return
            if user_input in self.expenses:
                user_input2 = input(f'Enter the monthly estimate of {user_input} expenses on this property. Or "quit" to quit.           ').strip()

                if user_input2 == "quit":
                    return
                try:
                    user_input2 = float(user_input2)
                    self.expenses[user_input] = user_input2
                    self.expenses_total += user_input
                    print(f"The monthly estimate of {user_input} expenses on this property is now ${user_input2}.")

                except:
                    print("Please enter a valid decimal number or 'quit' to quit.")
            else:
                print("That expense is not on the expense list. Retype it or change 'other' to account for that amount.")

    def reset_upfront_investment(self):
        while True:
            print("Are you sure you want to reset the upfront expense data? 'yes' or 'no'?")
            user_input = input().strip()
            if user_input == "no":
                return
            elif user_input=="yes":
                break
            else:
                print("I didn't quite get that.")

        self.expenses = Property.upfront_costs
        self.calculate_upfront_investment()

    def calculate_upfront_investment(self):
        print("\n\nPlease fill out the following information on the possible monthly expendetures:")

        self.upfront_cost_total = 0

        for k in self.upfront_costs:
            user_input = input(f'Enter the upfront cost estimate of {k} for this property. Or "quit" to quit.           ').strip()

            if user_input == "quit":
                return

            try:
                user_input = float(user_input)
                self.upfront_costs[k] = user_input
                self.upfront_cost_total += user_input
            except:
                print("Please enter a valid decimal number or 'quit' to quit.")
        self.view_upfront_cost()
    
    def view_upfront_cost(self):
        
        print("Upfront Property Expenses:\n --------------------------------------------------------------------")

        total = 0
        for k,v in self.upfront_costs.items():
            print(f"{k}  : ${v}")
            total+= v

        print(f"----------------------------------------------------\nTotal: ${total}")
        self.upfront_cost_total = total

    def get_ROI(self):
        rent = 0
        monthly_expenses = 0
        upfront_costs = 0

        for k,v in self.units.items():
            rent+=k*v
        for v in self.expenses.values():
            if type(v) == float or type(v) == int:
                monthly_expenses+=v
        for v in self.upfront_costs.values():
            upfront_costs+=v

        if upfront_costs != 0:
            return round(((rent-monthly_expenses)/upfront_costs)*100,4)
        else:
            return "more data needed"
    
    def show_ROI(self):
        print(f"This property's ROI is {self.get_ROI()}%")


class User():

    def __init__(self,username,password):
        self.password = password
        self.username = username
        self.properties ={}
        self.loggedIn=True

    def login(self, password):
        if password == self.password:
            print(f"Welcome {self.username}")
            self.main_menu()
        else:
            print("Invalid username and/or password")

    def add_property(self):
        print("\n\nAdding new Property:")
        user_input = input("What is the address or name of the added property?").strip()
        property = Property()
        self.properties[user_input] = property
        print("Property Added.")
        self.view_properties()



    def view_properties(self):

        if (self.loggedIn):
            if self.properties != {}:
                print("\n\n Your Current Properties are:")
                for p in self.properties:
                    print(p)
                print("\n\n")
            else:
                print("You have no properties recorded in your account")
            
    def select_property(self):
        print("\n\nSelecting Properties")
        self.view_properties() 

        while True:
            user_input=input("Enter the name of the property you'd like to select or 'quit' to quit.").strip()
            if user_input =="quit":
                break
            elif user_input in self.properties:
                self.open_property_menu(self.properties[user_input])
            else:
                print("I didn't quite get that.")


    def main_menu(self):

        option1 = "Enter 'add' to add a property."
        option2 = "Enter 'view' to view properties"
        option3 = "Enter 'select' to select a property from your list of properties."
        option4 = "Enter 'quit' to logout."

        while True:
            print("Main Menu\n\n")
            user_input = input(f"{option1}\n{option2}\n{option3}\n{option4}\n\n").strip()

            match user_input:
                case "quit":
                    break
                case 'view':
                    self.view_properties()
                case 'select':
                    self.select_property()
                case 'add':
                    self.add_property()
                case _ :
                    print("I didn't quite get that.")


    def open_property_menu(self, property):

        option1= "Enter 'roi' to see the property's return on intrest."
        option2 = "Enter 'monthly_expenses' to view, reset, or change the monthly expenses records."
        option3 ="Enter 'upfront_cost' to view, reset, or change the monthly costs."
        option4 = "Enter 'rent' to view or reset the unit rent rate data."
        option5 = "Enter 'back' or 'quit' to return to the main menu"


        while True:
            print(f"Property menu for {property} ")
            user_input = input(f"{option1} \n  {option2} \n {option3} \n {option4}\n {option5} \n\n")

            match user_input:
                case "roi":
                    property.show_ROI()
                case 'monthly_expenses':
                    self.monthly_expense_menu(property)
                case "upfront_cost":
                    self.upfront_expense_menu(property)
                case "rent":
                    self.rental_units_menu(property)
                case "back":
                    break
                case "quit":
                    break
                case _ :
                    print("I didn't quite get that.")


    def monthly_expense_menu(self, property):
        while True:
            print("Monthly Expense Menu\n\n")

            option1 = "Type 'change' to change monthly expense records"
            option2 = "Type 'reset' to reset monthly expense records."
            option3 = "Type 'view' to view monthly expense records."
            option4 = "Type 'back' or 'quit' to go back a menu."

            user_input = input(f"{option1} \n {option2} \n {option3}\n {option4} \n\n").lower().strip()

            match user_input:
                case "change":
                    property.change_monthly_expenses()
                case "reset":
                    property.reset_monthly_expense()
                case "view":
                    property.view_monthly_expense_list()
                case "back":
                    return
                case "quit":
                    return
                case _ :
                    print("I didn't wuote get that.")
                
    def upfront_expense_menu(self, property):
            while True:
                print("Upfront Expense Menu\n\n")

                option1 = "Type 'reset' to reset upfront expense records."
                option2 = "Type 'view' to view upfront expense records."
                option3 = "Type 'back' or 'quit' to go back a menu."

                user_input = input(f"{option1} \n {option2}\n {option3} \n\n").lower().strip()

                match user_input:
                    case "reset":
                        property.reset_upfront_investment()
                    case "view":
                        property.view_upfront_cost()
                    case "back":
                        return
                    case "quit":
                        return
                    case _ :
                        print("I didn't quite get that.")
                    
    def rental_units_menu(self,property):
         while True:
                print("Rental Units Menu\n\n")

                option1 = "Type 'reset' to reset rental units records."
                option2 = "Type 'view' to view rental units records."
                option3 = "Type 'back' or 'quit' to go back a menu."

                user_input = input(f"{option1} \n {option2}\n {option3} \n\n").lower().strip()

                match user_input:
                    case "reset":
                        property.reset_unit_data()
                    case "view":
                        property.view_units()
                    case "back":
                        return
                    case "quit":
                        return
                    case _ :
                        print("I didn't quite get that.")

class Pockets_Portal():
    def __init__(self):
        self.users = {}
    
    def join(self):

        print("Create a new account or enter 'quit' to go to the main page.")

        user_input = input("Enter a username for your new account")

        if user_input == 'quit':
            return
        
        user_input2 = input("Enter a password for your new account or enter 'quit' to go to the main page.")

        if user_input2 == 'quit':
            return
        
        self.users[user_input]=User(username=user_input, password=user_input2)

        print(f"{user_input} your account has been created. Sending you to the login page.")
    
    def login(self):

        print("Welcome to the Pockets Portal Login")

        user_input = input("Enter a username for your account or enter 'quit' to go to the main page.")

        if user_input == 'quit':
            return
        
        user_input2 = input("Enter a password for your account or enter 'quit' to go to the main page.")

        if user_input2 == 'quit':
            return
        

        if user_input in self.users:
            self.users[user_input].login(user_input2)
        else:
            print("Username and password invalid.")

    def open(self):

        while True:
            print("Welcome to Pockets Portal")

            option1 = "Enter 'join' to create an account."
            option2 = "Enter 'login' to login."
            option3 = "enter 'quit' to quit."

            user_input = input(f"{option1}\n{option2}\n{option3}").strip().lower()

            match user_input:
                case "join":
                    self.join()
                case "login":
                    self.login()
                case "quit":
                    return

homepage = Pockets_Portal()
homepage.open()