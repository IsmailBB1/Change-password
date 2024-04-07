
Pcuser = "Developer.I"
Pcpassword = "1234"

while (True):
    user = input ("User name:")
    password = input ("password:")
    if ((user == Pcuser) and (password == Pcpassword)):
        print ("Welcome", user)
        break
    elif (user != Pcuser ) and (password == Pcpassword):
        print("You entered your username incorrectly")

    elif ((user == Pcuser ) and (password != Pcpassword)):
       print("Forgot your password?")
       print ("Would you like to change the password? (Y/N)")
    answer = input ()
    if (answer == "Y"):
    
     newpassword = input ("New password:")
    print = ("Please wait")
    Pcpassword = newpassword
    print = ("Your password has been changed successfully")
else:
 print = ("Try again")