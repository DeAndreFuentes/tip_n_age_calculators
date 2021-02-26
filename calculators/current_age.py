

def print_menu():
    print("-" * 25)
    print(" Age Calculator")
    print("-" * 25)


print_menu()


year = float(input("Enter Birth year yyyy: "))
current = float(input("Enter current year yyyy:  "))


result = 0.0

if(current > year):
    result = current - year


print("Your current age is:  " + " " + str(result))
