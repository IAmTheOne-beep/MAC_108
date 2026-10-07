total_bill = 0.00
coupon_code = "23782881"
coupon_value = 50
print("Welcome to the Byte and Brew Self-Service Kiosk")
print("If you have a special coupon, type it in after your selections please: ")

while True: 
    print("Here are out options: \n" \
    "1. Coffee = $3\n" \
    "2. Bagel = $2\n" \
    "3. Donut holes = 5 for $1\n" \
    "4. Checkout\n" \
    "Total so far =",total_bill, "\n")
    choice = input()
    if choice == "1":
        total_bill = total_bill + 3
    elif choice == "2":
        total_bill = total_bill + 2
    elif choice == "3":
        total_bill = total_bill + 1
    elif choice == "4":
        if total_bill < 0:
            total_bill = 0.00
        print("Your total is",total_bill,". Thank you for shopping with us")
        if coupon_value == 0:
            print("Thank you for using the coupon!")
        break
    elif choice == coupon_code:
        total_bill = total_bill - coupon_value
        coupon_value = 0
        print("You got a $50 discount! Select your next item or checkout.")
    else: 
        print("Invalid input, please try again.")