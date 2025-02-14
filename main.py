order_num = []
order = []
order_meal = []
total = 0
price = 0
def welcome_message():
    print("Hello, welcome to [restaurant name]!\nBelow is the menu, please follow the instructions given.")
    print("Please enter the number of the item you'd like to purchase.")

def menu():
    global total
    global price
    while True:
        print("1) Cheeseburger\n2) Hamburger\n3) Chicken Sandwich\n4) Fries\n5) Fountain Drink")
        num = input("Input number here: ")
       # meal = input("Would you like it to be a meal? ") -- add after v1 is finished
        order_num.append(num)
        if num == 1:
            order.append("Cheeseburger")
            price = 2
        elif num == 2:
            order.append("Hanburger")
            price = 2
        elif num == 3:
            order.append("Chicken Sandwich")
            price = 2
        elif num == 4:
            fry_size = input("What size fries? ")
            fry_size.strip()
            fry_size.lower()
            if fry_size == "large":
                order.append("Large Fry")
            if fry_size == "medium":
                order.append("Medium Fry")
            if fry_size == "Small":
                order.append("Small Fry")
                price = 2
            else:
                print("Invaild Size, please re-order and use the following sizes: Large, Medium, and Small")
        elif num == 5:
            drink = input("What drink would you like? ")
            order.append(drink)
            price = 2
        
        total = total + price
        temp = input("Do you want to order another item? y/n ")
        temp.strip()
        temp.lower()
        
        if temp == "y":
            temp = "y"
        elif temp == "n":
            print("Your total is $" + str(total))
            break
        else:
            print("Invaild Input.")
            print("Your total is $" + str(total))
            break
            #make more user friendly, add ability to return to the temp prompt


        


welcome_message()
menu()