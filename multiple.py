province = input("What province do you live?")
tax = 0

if province in('Alberta', 'Nunavut', 'yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)