pcuser = "Developer.I"
pcpassword = "1234"

while True:
    user = input("User name: ")
    password = input("Password: ")

    if user == pcuser and password == pcpassword:
        print("Welcome", user)
        break

    elif user != pcuser and password == pcpassword:
        print("Wrong username!")

    elif user == pcuser and password != pcpassword:
        print("Wrong password!")

        answer = input("Forgot password? Change it? (Y/N): ")

        if answer == "Y":
            newpassword = input("New password: ")
            print("Please wait...")
            pcpassword = newpassword
            print("Password changed successfully!")

    else:
        print("Username and password are wrong!")
