# this function will return the initials of the names
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initials = name[0:1].upper()
    else:
        initials = name[0:1]
    return initials


firstname = input("Enter your first name ")
firstname_initial = get_initial(name=firstname)

lastname = input("Enter your last name ")
lastname_initial = get_initial(name=lastname)

print(f'Your initials is {firstname_initial}.{lastname_initial}')
