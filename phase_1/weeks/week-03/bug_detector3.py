logged_in = True
role = "engineer" # changed the initialization position

if logged_in: # no colon
    if role == "admin": # missing equals sign
        print("Admin")

    elif role == "engineer": # no colon
        print("Engineer")

    else: # no colon
        print("Community")
else:
    print("Login Required") #identation error