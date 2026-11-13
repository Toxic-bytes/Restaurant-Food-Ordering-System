import csv
from datetime import datetime

class Restaurant:

    def generate_order_id(self):
        last_order_id = 1000

        with open("orders.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                order_id = int(row["order_id"])

                if order_id > last_order_id:
                    last_order_id = order_id

        return last_order_id + 1

    
    #Display food menu 
    def display_menu(self):
        print("\n------ FOOD MENU ------")

        with open("menu.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(f"{row['food_id']}. {row['food_name']} - Rs.{row['price']}")


    # place customer order 
    def place_order(self):
        food_id = input("Enter Food ID: ")
        
        try:
           quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Please enter numbers only!")
            return


        if quantity <= 0:
            print("Please enter a valid quantity!")
            return

        with open("menu.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['food_id'] == food_id:
                    food_name = row['food_name']
                    price = int(row['price'])


                    # Generate unique Order ID
                    order_id = self.generate_order_id()

                    # Get current date
                    order_date = datetime.now().strftime("%d-%m-%Y")

                    # Calculate bill
                    subtotal = price * quantity

                    # Apply 10% discount if subtotal is above Rs.500
                    if subtotal > 500:
                        discount = subtotal * 10 // 100
                    else:
                         discount = 0

                    # Calculate final amount
                    final_amount = subtotal - discount

                    # Save order in csv file
                    with open("orders.csv", "a+", newline="") as file:
                         file.seek(0)
                         content = file.read()

                         if content and not content.endswith("\n"):
                             file.write("\n")

                         writer = csv.writer(file)
                         writer.writerow([order_id, order_date, food_id, food_name, price, quantity, subtotal, discount, final_amount])
                    
                    # Display formatted bill receipt
                    print("\n========== ORDER RECEIPT ==========")
                    print("Order ID:", order_id)
                    print("Date:", order_date)
                    print("-----------------------------------")
                    print("Food Name:", food_name)
                    print("-----------------------------------")
                    print("Price: Rs.", price)
                    print("Quantity:", quantity)
                    print("-----------------------------------")
                    print("Subtotal: Rs.", subtotal)
                    print("Discount: Rs.", discount)
                    print("-----------------------------------")
                    print("Final Amount: Rs.", final_amount)
                    print("===================================")
                    return

            print("Invalid Food ID!")

    
    
    
    def display_orders(self):
        print("\n------ ALL ORDERS ------")

        with open("orders.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print("\n-----------------------------------")
                print("Order ID:", row['order_id'])
                print("Date:", row['order_date'])
                print("Food Name:", row['food_name'])
                print("Price: Rs.", row['price'])
                print("Quantity:", row['quantity'])
                print("Subtotal: Rs.", row['subtotal'])
                print("Discount: Rs.", row['discount'])
                print("Final Amount: Rs.", row['final_amount'])
                print("-----------------------------------")

       
# Create Restaurant object
restaurant = Restaurant()

while True:
    print("\n------ RESTAURANT FOOD ORDERING SYSTEM ------")
    print("1. Display Food Menu")
    print("2. Place Order")
    print("3. View All Orders")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        restaurant.display_menu()

    elif choice == "2":
        restaurant.place_order()

    elif choice == "3":
        restaurant.display_orders()

    elif choice == "4":
        print("Thank you! Please visit again!")
        break
    else:
        print("Invalid choice! Please try again.")