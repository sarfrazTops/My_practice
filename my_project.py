menu={
    "Pizza":80,
    "Pasta":50,
    "Burger":60,
    "Salad":30,
    "Coffee":20
    }
print("Welcome to Khan Restaurant")
print(" Pizza: Rs80\n Pasta: Rs50\n Burger: Rs60\n Salad: Rs30\n Coffe: Rs20")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print("order item {item_1} in not avaialbe yet")

another_order = input("Do you want to add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to roder")
    else:        
        print(f"order item {item_2} is not available!")
print(f"The total amount of items to pay is {order_total}")        
    

    
