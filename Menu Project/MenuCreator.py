#This program will create 3 menus by prompting the kitchen staff for the following
#inputs: menu item (name), cost, stock, time availability:

#The program will categorize each item and their respective information information
#3 different menu: Breakfast Menu, Lunch Menu, Dinner menu

#These 3 menu will then be access via another program where a waiter could
#refer to these menu in order to create a bill that can be accessed by the kitchen
#staff and the front of house (in order to print bills)

#breakfast menu will be availbel from 6am to 11am
#lunch menu will be availbe from from 11am to 5pm
#dinner menu will be available from 5pm to 10pm


Num_of_total_items = input('Enter the number of menu items that will be available today: \n')

main_list_of_all_items = []

Breakfast_menu_start = '6am'
Breakfast_menu_end = '11am'
Lunch_menu_start = '11am'
Lunch_menu_end = '5pm'
Dinner_menu_start = '5pm'
Dinner_menu_end = '10pm'

Breakfast_items_and_cost = {}
Lunch_items_and_cost = {}
Dinner_items_and_cost = {}

Breakfast_items_and_stock = {}
Lunch_items_and_stock = {}
Dinner_items_and_stock = {}

for items in range(int(Num_of_total_items)):

    item_name = input('Enter the name of the item: \n')
    item_cost = input('Enter the cost of the item: \n')
    item_stock = input('Enter the number of available stock for this item: \n')
    item_menu = input('Enter which menu this item will be a part of: \n')

    ITEM = [{item_name:float(item_cost)}, {item_name:int(item_stock)}, item_menu]
    main_list_of_all_items.append(ITEM)

    #items and cost here:
    for item in main_list_of_all_items:
        if item[2].title() == 'Breakfast':
            Breakfast_items_and_cost.update(item[0])
            Breakfast_items_and_stock.update(item[1])

        elif item[2].title() == 'Lunch':
            Lunch_items_and_cost.update(item[0])
            Lunch_items_and_stock.update(item[1])
        elif item[2].title() == 'Dinner':
            Dinner_items_and_cost.update(item[0])
            Dinner_items_and_stock.update(item[1])

breakfast_menu_details = ['Breakfast', len(Breakfast_items_and_cost), Breakfast_items_and_cost, Breakfast_items_and_stock, Breakfast_menu_start, Breakfast_menu_end]

lunch_menu_details = ['Lunch', len(Lunch_items_and_cost), Lunch_items_and_cost, Lunch_items_and_stock, Lunch_menu_start, Lunch_menu_end]

dinner_menu_details = ['Dinner', len(Dinner_items_and_cost), Dinner_items_and_cost, Dinner_items_and_stock, Dinner_menu_start, Dinner_menu_end]

all_menus = [breakfast_menu_details, lunch_menu_details, dinner_menu_details]

with open('TodaysMenus.txt', 'w') as T_menu:
    for menu in all_menus:
        T_menu.write('''

Menu: {name};
Number of item: {number_of_items};
Start Time: {start};
End Time: {end};

List of items and their respective cost ($):

C: {items_and_cost};

List of items and their respective stock:

S: {items_and_stock};
_______________________________________________________
'''.format(name=menu[0], number_of_items=menu[1], items_and_cost=menu[2], items_and_stock=menu[3], start=menu[4], end=menu[5]))
