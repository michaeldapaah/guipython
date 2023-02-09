# country = input("Enter the name of your country ")
# if country.lower() == "canada":
#     print("so you muat like hockey")
# else:
#     print("You are not from canada")
# province = []
def provin_city(amount):
    province = input("Enter the name of your province")
    if province == 'Alberta':
        tax = 0.5 * amount
    elif province == 'Nunavut':
        tax = 0.05 * amount
    elif province == 'Ontario':
        tax = 0.13 * amount
    else:
        tax = 0.15 * amount
    print(tax)


provin_city(800)