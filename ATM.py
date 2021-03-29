from datetime import datetime  # Import datetime

kay = datetime.now()
currentDate_Time = kay.strftime("%Y:%m:%d %H:%M:%S")
print(currentDate_Time, "\n")  # Display the current time

# Prompt the user to input their name
name = input("Please enter your name \n")

# Create a list of names of acceptable users
allowedUsers = ["Kizito", "Xyluz", "Toonie", "Femi"]
allowedPassword = ["8888", "5555", "7777", "2222"]  # List of valid passwords
accountBalance = [50000, 100000, 45750, 38800] # List of users account balance

# Check if name is in the list of allowed users
if name in allowedUsers:
    password = input("Enter your password: \n")
    userId = allowedUsers.index(name)  # Create a user Id for each user

    if password == allowedPassword[userId]: # Check if password entered matches valid password
        print("\nYou are now logged in\n")
        print(f"Welcome {name}\n")
        print("These are the available options: ")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint \n")

        choice = "y"
        # A loop that allows users with the option to make another transaction or not
        while choice.lower() == "y":
            selectedOption = eval(input("Please select "
                                        "an option: \n"))

            if selectedOption == 1:  # Withdrawal
                withdrawCash = eval(input("\nHow much would you "
                                     "like to withdraw?\n"))

                # Check if amount entered is more than what is in account
                if withdrawCash > accountBalance[userId]:
                    print("\nInsufficient funds. " 
                        "Make a deposit and try again")
                if withdrawCash <= accountBalance[userId]:
                    print("\nPlease take your cash")

            elif selectedOption == 2:  #Cash deposit option
                amountDeposit = eval(input("\nHow much would you "
                                     "like to deposit? "))
                currentBalance = accountBalance[userId] + amountDeposit
                print(f"Deposit successful. Your current balance is #{currentBalance}")

            elif selectedOption == 3:  #Complaint option
                complaint = input("\nWhat issue would you like to report?\n")
                print("Your complaint has been recorded. Thank you for contacting us")

            else:  #Executes if option selected is not in list of options
                print("Invalid Option. Try again and select a valid option")

            
            choice = input("\nWould you like to perform "  # Ask the user if he wants to continue
                      "another transaction? (y/n): ")

        print("\nThank you for banking with us")

    elif password != allowedPassword[userId]:  # Executes if password entered is incorrect
        print("\nPassword Incorrect!"
              " Please confirm password and try again")

else:  # Executes if name entered is invalid
    print("\nName not found, please try "
          "again and enter a valid name")