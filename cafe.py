"""
The program have a menu list with the items in a cafe.
02 dictionary, one with the stock of menu item and 
another with the price of the menu item.

The program calculate the value of each stock item
and the total stock value.

"""

#the menu item list
menu_list = ["Espresso", "Chocolate Coffee", "Iced Tea","Cheese Sandwish"]

#the menu item stock dictionary
stock = {'Espresso': 55, 
         'Chocolate Coffee': 20, 
         'Iced Tea': 35,
         'Cheese Sandwish': 50
        }

#the menu item price dictionary
price = {'Espresso': 5.0, 
         'Chocolate Coffee': 7.0, 
         'Iced Tea': 4.0,
         'Cheese Sandwish': 8.0
        }

#variable initialization
total_stock = 0

#for loop to go thru menu item list
for items in menu_list:
    #Calculate the item value
    item_value = (stock[items] * price[items])
    print(f"{items} Total value is - {item_value}")
    total_stock += item_value

print("The Total stock item value is: "+str(total_stock))
