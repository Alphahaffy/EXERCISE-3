# EXERCISE-3
#CLASS TASK



signup_password = ""
signup_username = ""

yes=('y')
while yes==('y'):
    
    print("1. Sign Up")
    print("2. Sign In")

    # get value from user
    val = input("Select an Optioin: ")

    # check which option is selected
    if val == "1":
        # if user select 1
        print("Sign Up")
        print("Create Account")
        # get username and password for create account
        signup_username = input("Enter username: ")
        signup_password = input("Enter Password: ")
        print("Your account has been created successfully")
    elif val == "2":
        # if user select 2
        print("Sign In")
        # get username and password
        login_username = input("Enter your username: ")
        login_password = input("Enter your password: ")

        # check the username and password is correct or not
        if signup_username == login_username and signup_password == login_password:
            # if username and passwords both are correct
            print("Loged In")
        else:
            # if password or username is not correct
            print("Username and password is invalid")
    else:
        # if user selects rather than 1 or 2
        print("Invalid Option")
        yes=input("Do you want to continue:y/n?")
print("THANK YOU FOR USING OUR SERVICE")
