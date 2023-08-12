print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    print("You have choose Small size.")
    if add_pepperoni == "Y":
        bill += 2
        print("Pepperoni was added to your order.")
        if extra_cheese == "Y":
            bill += 1
            print("Extra cheese was added to your order.")


elif size == "M":
    bill = 20
    print("You have choose Medium size.")
    if add_pepperoni == "Y":
        bill += 3
        print("Pepperoni was added to your order.")
        if extra_cheese == "Y":
            bill += 1
            print("Extra cheese was added to your order.")


else:
    bill = 25
    print("You have choose Large size.")
    if add_pepperoni == "Y":
        bill += 3
        print("Pepperoni was added to your order.")
        if extra_cheese == "Y":
            bill += 1
            print("Extra cheese was added to your order.")

final_bill = bill
print(f"Your final bill is: ${final_bill}.")