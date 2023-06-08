#This program calculates the total stock worth in the cafe

#The below command creates a 'menu' list which contains 4 items
menu=["coffee", "donuts", "cookies",  "mocktail"]
#The following commands creates a 'stock' and 'price' dictionaries that contains the stock value and price for each item on the menu respectively
stock={'coffee':8,
       'donuts':3,
       'cookies':5,
       'mocktail':4}
price={'coffee':1.0,
       'donuts':2.0,
       'cookies':1.0,
       'mocktail':3.0}
#The below command initializes a variable 'total_stock' as 0
total_stock=0
#The below loop calculates the item value of each items and adds them to get the total stock price in the cafe
#'item' represents each item in the menu list
for item in menu:
    item_value=(stock[item]*price[item])
    total_stock=total_stock+item_value
#The following commands displays the cafe menu and the total stock worth in the cafe
print('Goodvibes Cafe! We are serving {}, {}, {} and {}'.format(menu[0], menu[1], menu[2], menu[3]))
print("The total stock price : ",total_stock)