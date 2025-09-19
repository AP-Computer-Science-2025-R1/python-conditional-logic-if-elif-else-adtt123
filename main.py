username = input("What is your username?: ")
print("Hello " + username)
password_length = input("Put in your password: ")
if username == "admin":
    if len(password_length) >= 10:
        print("Login successful.")
    else:
        print("Admin password incorrect.")
else:
    if len(password_length) >= 6:
        print("Login successful.")
    else:
        print("User password must be 6+.")