global admin_login
global user1_login


admin_login = "Admin"
user1_login = "User1"
user1_pass = "user01"
admin_pass="admin0"
n_username = " "
n_pass = " "

print("-----FINANCE MANAGER----- v0.0.1B")


users = ["Admin", "User1"]
passwords = ["Admin : admin0","User1 : user01"]

def newuser():
    global n_username     
    global n_pass
    print("Hello! ")
    n_username = input("Enter new username : ")
    users.append(n_username)
    n_pass = input("Enter new password (must be atleast  8 characters!): ")
    if len(n_pass) < 8:
        print("password must be more than 8 characters! ") 
        n_pass = input("Enter new password (must be atleast  8 characters!): ")
        passwords.append(n_pass)
    else:
        n_pass = n_pass
        


def display_home():
    print("---Finance Manager---")
    

def admin():
    print("Welcome back admin! ")
    print("How can i help you today!? ")
    h = '''
            Enter the number to do the respective function!

                    1. Show all users
                    2. Show all passwords of users
                    3. Make new User
                    4. Delete all files   
                    5. Delete User  
                    6. See all Expenses of this week 
                    7. Logout

    ''' # 4 5 6 Does not work 
    while True:
        ih = int(input(h))
        if ih == 1:
            print(users)
        elif ih == 2:
            print(passwords)
        elif ih == 3:
            newuser()
        elif ih == 4:
            print("--DELETING ALL FILES--")
        elif ih == 5:
            #tried and gave up
            pass

        elif ih == 6:
            print(
                f"""
                User1 - week 2 : $200.0 for Rent 
                {n_username} - week 2 : $64.0 for Reason

                """
            )
        elif ih == 7:
            print("Logging out!")
            break
        else:
            print("Enter Number from list! ")
            print(h)
            
         

def n():
    print(f"Welcome {n_username}!")
    print("Start Out by telling us your salary per month! ")
    salary = int(input("Salary : $"))
    print("Perfect! Now you can insert A new expense! (type no in reason if you donot want to insert any expense!) \n")

    amount = int(input("How much did you spend : $"))
    reason = input("Enter Reason : ")
    print("okay making your home page...\n\n")
    nn = f'''
        Income : {salary}
        January 2023
        week 1 :

        week 2 : ${amount} for {reason}

    '''
    print(nn)
    print()
    print("Okay logging out now!")


def user1():
    print("Welcome back User1!\n") 
    print("Income : 10000$/month\n")
    print("Expenses : ")
    a = """
        January 2023
        week 1 : $20.0 for metro
                 $40.0 for Groceries 
                 $2304.0 for New Year's Party

        week 2 : $200.0 for Rent          

    """
    print(a)
    while True:
        new_e = input(f'Did you have any other expense? (Yes/No) : ')
        if new_e.lower() == "yes":
            print("Okay! Adding new expense to this week! (type no in reason if you donot want to insert any expense!)")
            amount = int(input("How much did you spend : $"))
            reason = input("Enter Reason : ")
            if reason.lower() == "no":
                print("Okay Logging out now! ")
                break
            else:
                a = f"""
                    January 2023
                    week 1 : $20.0 for metro
                            $40.0 for Groceries 
                            $2304.0 for New Year's Party

                    week 2 : $200.0 for Rent          
                            ${amount} for {reason}
                """
                print(a)   # If you want you can find out how to repeat and add new values or just close here it doesnt matter ( i.e. only one new input )
                # DELETE THE COMMENTS BEFORE PRINTING OR ANYTHING






while True:
    print(users)
    login = input("Username : ")

    if login == admin_login:
        password = input("Password : ")
        if password.lower() == admin_pass:
            admin()
            break
        else:
            print("Wrong Password, access denied")



    elif login == user1_login:
        password = input("Password : ")
        if password.lower() == user1_pass:
            user1()
            break
        else:
            print("Wrong password! ")
    elif login == n_username:
        password = input("Password : ")
        if password.lower() == n_pass:
            n()
            break
        else:
            print("Wrong password! ")

    else:
        print('No such User, would you like to create a new profile? ')
        new_prompt = input("New user? (Yes/No) : ")
        if new_prompt.lower() == "yes":
            newuser()

        else:
            print("okay! closing application")
            break
            
