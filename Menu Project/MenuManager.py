import re


# This class is used later in the program to create editable Menus.
class Menu:
    def __init__(self, name, number_of_items ,name_and_cost, name_and_stock, starting_time, ending_time):
        self.name = name
        self.num_of_items = number_of_items
        self.name_and_cost = name_and_cost
        self.name_and_stock = name_and_stock
        self.starting_time = starting_time
        self.ending_time = ending_time

    def __repr__(self):
        msg = '''
Menu: {name}
Number of item: {number_of_items}
Start Time: {start}
End Time: {end}

List of items and their respective cost ($):

{items_and_cost}

List of items and their respective stock:

{items_and_stock}
_______________________________________________________
        '''.format(name=self.name, number_of_items=self.num_of_items, items_and_cost=self.name_and_cost, items_and_stock=self.name_and_stock, start=self.starting_time, end=self.ending_time)

        return msg

Menu_names = []
Menu_num_of_items = []
Menu_name_cost = []
Menu_name_stock = []
Menu_start = []
Menu_end = []

#This 2 chunk of code will read through the text file containing all of menus' details
#and return us with a series of variables and lists that will be necessary to create our editable Menus later.
with open('TodaysMenus.txt') as today_menu:
    for line in today_menu:

        if line.startswith('Menu:'):
            Menu_names.append(re.findall('^Menu: (.*);', line)[0])

        if line.startswith('Number of item:'):
            Menu_num_of_items.append(re.findall('([0-9]+);', line)[0])

        if line.startswith('Start'):
            Menu_start.append(re.findall('^Start Time: (.*);', line)[0])

        if line.startswith('End'):
            Menu_end.append(re.findall('^End Time: (.*);', line)[0])

        if line.startswith('C:'):
            Menu_name_cost.append(re.findall('^C: {(.*)}', line)[0])

        if line.startswith('S: '):
            Menu_name_stock.append(re.findall('^S: {(.*)}', line)[0])

#________________________________________________________________________________________________
# FUNCTION SECTION

#This function convert the text version of the MENU into computer data for various computation.
def text_info_to_menu_objects(menu_names, num_of_items, menu_name_and_cost, menu_name_and_stock, starting, ending):
    try:
        all_menu_txt_to_objects = []
        startn = 0
        all_menu_name_cost_list = []
        all_menu_name_stock_list = []
        for x in [menu_name_and_cost, menu_name_and_stock]:
            for number in range(len(menu_names)):
                name_cost_or_stock_dict = {}
                names_cost_splitter = x[number].split(', ')
                for menu_item in names_cost_splitter:
                    names_cost_splitter2 = menu_item.split(': ')
                    COST_OR_STOCKS_KEYS = names_cost_splitter2[0].replace('\\','').replace('\'','').replace('\"','')
                    name_cost_or_stock_dict[COST_OR_STOCKS_KEYS] = names_cost_splitter2[1].replace('\'', '')

                if x == menu_name_and_cost:
                    all_menu_name_cost_list.append(name_cost_or_stock_dict)
                elif x == menu_name_and_stock:
                    all_menu_name_stock_list.append(name_cost_or_stock_dict)

        for x in range(len(menu_names)):
            x = [menu_names[startn], num_of_items[startn], all_menu_name_cost_list[startn], all_menu_name_stock_list[startn], starting[startn], ending[startn]]
            all_menu_txt_to_objects.append(x)
            startn +=1

        return all_menu_txt_to_objects
    except:
        print('''
_____________________________________________________
Menu is currently Empty.
Please Create a Menu using \'Menu Creator\'!''')
        exit()

#This function takes menu details and info from List_of_all_Menu_detail to create a MENU CLASS
def make_menu(menu_details):
    menu_details_name = menu_details[0]
    menu_details_item_count = menu_details[1]
    menu_details_cost = menu_details[2]
    menu_details_stock = menu_details[3]
    menu_details_start = menu_details[4]
    menu_details_end = menu_details[5]

    Menu_class = Menu(menu_details_name, menu_details_item_count, menu_details_cost, menu_details_stock, menu_details_start,menu_details_end)
    return Menu_class

#This function takes a list of menu details from List_of_all_Menu_detail to create a readable structural display of the menu(s).
#Use this function if you want to re-write the menu into a text file after you've updated in some way.
def write_menu(menu_list):


    with open('TodaysMenus.txt', 'w') as T_menu:
        for menu in menu_list:
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

def MAIN_MENU(LIST_of_all_Menu_detail):
    list_that_stores_menu_name = []
    for MENU_detais in LIST_of_all_Menu_detail:
        list_that_stores_menu_name.append(MENU_detais[0].title())

    return list_that_stores_menu_name

def REMOVE_and_ADD_menu(action):

    if action == 'ADD':
        print('''
_____________________________________________________

INSTRUCTION:

In order to ADD a new menu, the following information is needed:

1) Menu's name.
2) The number of items this menu will feature.
3) The Cost of each respective items.
4) The Stock of each respective items.
5) The Starting time at which this menu will be available.
6) The Ending time at which this menu will no longer be available.

At any given point, enter\'CANCEL\' to EXIT.

In case you wish to cut the menu short, enter \'STOP\'
when the program prompt you for the next menu item NAME.

The program will then create a new menu with only the
information you've provided before \'STOP\'.

To go back, enter \'BACK\'.

''')
        add_menu_details = {}
        def display_add_menu(add_menu_details):
            print('''
_____________________________________________________
=====================
Current Menu Details:
=====================
''')


            for key,value in add_menu_details.items():
                print('{key}: {value}'.format(key=key,value=value))

            print('\n')

        menu_add_name = is_it_right_or_wrong('Enter the name of the menu: ')
        if menu_add_name == 'BACK':
            return

        add_menu_details['Menu name'] = add_menu_details.get('Menu name', menu_add_name.title())
        display_add_menu(add_menu_details)


        while True:
            menu_add_item_count = input('Enter the number of item(s) this menu will feature: \n')
            if menu_add_item_count == 'CANCEL': exit()
            try:
                menu_add_item_count = int(menu_add_item_count)
                break
            except:
                print('Please enter integer values only.')
                continue

        add_menu_details['Menu item count'] = add_menu_details.get('Menu item count', menu_add_item_count)
        display_add_menu(add_menu_details)

        menu_add_name_cost = {}
        menu_add_name_stock = {}
        menu_item_iteration_num = 1
        for item in range(int(menu_add_item_count)):

            menu_item_info = []

            item_add_name = is_it_right_or_wrong('Enter the name of item number {num}: \n'.format(num=menu_item_iteration_num))
            if item_add_name == 'STOP':
                add_menu_details['Menu item count'] = menu_item_iteration_num -1
                break

            while True:
                try:
                    item_add_cost = float(is_it_right_or_wrong('Enter the cost of item number {num}: \n'.format(num=menu_item_iteration_num)))
                    break
                except:
                    print('Please enter integer values only.')
                    continue


            while True:
                try:
                    item_add_stock = int(is_it_right_or_wrong('Enter the number of available stock of item number {num}: \n'.format(num=menu_item_iteration_num)))
                    break
                except:
                    print('Please enter integer values only.')
                    continue


            menu_add_name_cost.update({item_add_name:(item_add_cost)})
            menu_add_name_stock.update({item_add_name:(item_add_stock)})

            menu_item_iteration_num += 1


        add_menu_details['Menu item cost'] = add_menu_details.get('Menu item cost', menu_add_name_cost)
        add_menu_details['Menu item stock'] = add_menu_details.get('Menu item stock', menu_add_name_stock)
        display_add_menu(add_menu_details)

        menu_add_start_time = is_it_right_or_wrong('''
_____________________________________________________
Enter the starting time for this Menu:
*For aesthetic purposes, format the time like the following example: \'11:00am\', \'12:45pm\', \'1:12pm\'\n

Time: ''')
        add_menu_details['Starting Time'] = add_menu_details.get('Starting Time', menu_add_start_time)
        display_add_menu(add_menu_details)

        menu_add_end_time = is_it_right_or_wrong('''
_____________________________________________________
Enter the ending time for this Menu:
*For aesthetic purposes, format the time like the following example: \'11:00am\', \'12:45pm\', \'1:12pm\'\n

Time: ''')
        add_menu_details['Ending Time'] = add_menu_details.get('Ending Time', menu_add_end_time)

        NEW_MENU_FINAL_LIST_OF_DETAILS = []
        for value in add_menu_details.values():
            NEW_MENU_FINAL_LIST_OF_DETAILS.append(value)
#_____________________________________________________________________________________________
# FINAL CHECK BEFORE A NEW MENU IS CREATED
        while True:

            display_add_menu(add_menu_details)

            final_check_for_new_menu = input('''
_____________________________________________________
*NOTICE*

Before we finalize your new menu, make sure all the
menu information has been entered correctly.

Enter \'OK\' to proceed, or enter \'EDIT\' to make changes.
''')

            if final_check_for_new_menu == 'OK':
                display_add_menu(add_menu_details)

                List_of_all_Menu_detail.append(NEW_MENU_FINAL_LIST_OF_DETAILS)
                MAIN_MENU_NAMES.append(NEW_MENU_FINAL_LIST_OF_DETAILS[0])

                print('''
=============
Updated Menu:
=============\n''')

                fDISPLAY_ALL_MENU(List_of_all_Menu_detail)

                break



            elif final_check_for_new_menu == 'EDIT':
                while True:
                    display_add_menu(add_menu_details)
                    changes_to_menu_action = is_it_right_or_wrong('''
_____________________________________________________
===================================
Available options for Menu Editing:
===================================

Option 1: REMOVE | To REMOVE an item, enter \'REMOVE\'.
Option 2: ADD | To ADD an item, enter \'ADD\'.
Option 3: EDIT | To make changes to a particular element, enter \'EDIT\'.

To continue finalizating your menu, enter \'OK\'.

''')
                    if changes_to_menu_action == 'OK':
                        break

                    if changes_to_menu_action == 'REMOVE':
                        while True:
                            print('''
_____________________________________________________
===========================
Current list of menu items:
===========================
''')
                            for key in add_menu_details['Menu item cost'].keys():
                                print('To remove item \'{key}\' from the menu, please enter \'{key}\'.'.format(key=key))
                            item_to_remove_MENU_ADD = is_it_right_or_wrong('''
*You may enter \'STOP\' to cancel*
Which menu item would you like to remove:
''')
                            if item_to_remove_MENU_ADD == 'STOP':
                                break
                            if item_to_remove_MENU_ADD in add_menu_details['Menu item cost'].keys():
                                del add_menu_details['Menu item cost'][item_to_remove_MENU_ADD]
                                del add_menu_details['Menu item stock'][item_to_remove_MENU_ADD]
                                menu_add_item_count = len(add_menu_details['Menu item cost'])
                                break
                                print('\'{item}\' has been deleted from the menu.'.format(item=item_to_remove_MENU_ADD))
                            elif item_to_remove_MENU_ADD not in add_menu_details['Menu item cost'].keys():
                                print('The entered menu item does not exist, please re-enter a new value.')

                    if changes_to_menu_action == 'ADD':
                        while True:
                            back_to_final_check_for_menu = 'NO'
                            print('''
_____________________________________________________
Current list of menu items:
''')
                            iteration_number_for_adding_item_ADD_MENU = 1
                            for item in add_menu_details['Menu item cost'].keys():
                                print('Item {num}: \'{item}\'.'.format(num=iteration_number_for_adding_item_ADD_MENU, item=item))
                                iteration_number_for_adding_item_ADD_MENU += 1
                            print('\n')
                            print('At any given, point, you may enter \'STOP\' to cancel.')
                            item_name_to_add_MENU_ADD = is_it_right_or_wrong('''
Enter the name of the item you want to add:
''').title()
                            if item_name_to_add_MENU_ADD == 'Stop':
                                break

                            while True:
                                item_cost_to_add_MENU_ADD = is_it_right_or_wrong('Enter the cost of the item: ')
                                if item_cost_to_add_MENU_ADD == 'STOP':
                                    back_to_final_check_for_menu = 'YES'
                                    break
                                try:
                                    item_cost_to_add_MENU_ADD = float(item_cost_to_add_MENU_ADD)
                                    break
                                except:
                                    print('Please enter numerical values only. ')
                                    continue

                            if back_to_final_check_for_menu == 'NO':
                                while True:
                                    item_stock_to_add_MENU_ADD = is_it_right_or_wrong('Enter the number of available stock for the item: ')
                                    if item_stock_to_add_MENU_ADD == 'STOP':
                                        back_to_final_check_for_menu = 'YES'
                                        break
                                    try:
                                        item_stock_to_add_MENU_ADD = int(item_stock_to_add_MENU_ADD)
                                        break
                                    except:
                                        print('Please enter integer values only. ')
                                        continue


                            if back_to_final_check_for_menu == 'NO':
                                print('''
THe following item and its details
will be added to your new menu:

Item Name: {name}
Item Cost: {cost}
Item Stock: {stock}
'''.format(name=item_name_to_add_MENU_ADD, cost=item_cost_to_add_MENU_ADD, stock=item_stock_to_add_MENU_ADD))

                            if back_to_final_check_for_menu == 'NO':
                                while True:
                                    Confirm_new_item_EDIT_ADD_MENU = is_it_right_or_wrong('''
        To Confirm, please enter \'OK\'.
        To Cancel, please enter \'NO\'
        ''')
                                    if Confirm_new_item_EDIT_ADD_MENU == 'OK':
                                        add_menu_details['Menu item cost'].update({item_name_to_add_MENU_ADD:item_cost_to_add_MENU_ADD})
                                        add_menu_details['Menu item stock'].update({item_name_to_add_MENU_ADD:item_stock_to_add_MENU_ADD})
                                        add_menu_details['Menu item count'] = len(add_menu_details['Menu item cost'])
                                        back_to_final_check_for_menu = 'YES'
                                        break
                                    elif Confirm_new_item_EDIT_ADD_MENU == 'NO':
                                        back_to_final_check_for_menu == 'YES'
                                        break

                            if back_to_final_check_for_menu == 'YES':
                                break
                            else:
                                continue

                    if changes_to_menu_action == 'EDIT':


                        while True:
                            display_add_menu(add_menu_details)
                            menu_element_to_change_MENU_ADD = input('''
To change the MENU NAME, please enter \'NAME\'.
To change the MENU STARTING TIME, please enter \'S\'.
To change the MENU ENDING TIME, please enter \'E\'.

To edit the cost of a particular item, please enter \'COST\'.
To edit the stockpile of a particular item, please enter \'STOCK\'.

*You may enter \'STOP\' at any given point to cancel, the
only exception is when the program prompt the user for confirmation*

To go back, enter \'STOP\'.
''')
                            back_to_final_check_for_menu = 'NO'

                            if menu_element_to_change_MENU_ADD == 'STOP':
                                break


                            elif menu_element_to_change_MENU_ADD == 'NAME':
                                change_name_MENU_ADD = is_it_right_or_wrong('Changing the menu\'s current name, \'{current_name}\', to: '.format(current_name=add_menu_details['Menu name']))
                                if change_name_MENU_ADD == 'STOP':
                                    back_to_final_check_for_menu = 'YES'
                                    break
                                else:
                                    add_menu_details['Menu name'] = change_name_MENU_ADD
                                    break

                            elif menu_element_to_change_MENU_ADD == 'S':
                                change_start_time_MENU_ADD = is_it_right_or_wrong('Changing the menu\'s current starting time, \'{start_time}\', to: '.format(start_time=add_menu_details['Starting Time']))
                                if change_start_time_MENU_ADD == 'STOP':
                                    back_to_final_check_for_menu = 'YES'
                                    break
                                else:
                                    add_menu_details['Starting Time'] = change_start_time_MENU_ADD
                                    break

                            elif menu_element_to_change_MENU_ADD == 'E':
                                change_end_time_MENU_ADD = is_it_right_or_wrong('Changing the menu\'s current ending time, \'{end_time}\', to: '.format(end_time=add_menu_details['Ending Time']))
                                if change_end_time_MENU_ADD == 'STOP':
                                    back_to_final_check_for_menu = 'YES'
                                    break
                                else:
                                    add_menu_details['Ending Time'] = change_end_time_MENU_ADD
                                    break

                            elif menu_element_to_change_MENU_ADD == 'COST':
                                print('''
_____________________________________________________
List of currently featured item(s) and their
respective cost(s):
''')
                                iteration_number_for_editing_cost_MENU_ADD = 1
                                for keys,values in add_menu_details['Menu item cost'].items():
                                    print('''
Item {num}: \'{key}\' : {cost} | To change the cost of this item, enter \'{key}\'\n.'''.format(num=iteration_number_for_editing_cost_MENU_ADD, key=keys, cost=values))
                                    iteration_number_for_editing_cost_MENU_ADD += 1


                                while True:
                                    change_item_cost_MENU_ADD = is_it_right_or_wrong('Which item\' cost would you like to change: ')
                                    if change_item_cost_MENU_ADD == 'STOP':
                                        back_to_final_check_for_menu = 'YES'
                                        break
                                    if change_item_cost_MENU_ADD in add_menu_details['Menu item cost'].keys():
                                        while True:
                                            change_item_cost_MENU_ADD2 = is_it_right_or_wrong('Changing the item, {item}, current cost\'s from \'{cost}\' to: '.format(item=change_item_cost_MENU_ADD, cost=add_menu_details['Menu item cost'][change_item_cost_MENU_ADD]))
                                            if change_item_cost_MENU_ADD2 == 'STOP':
                                                back_to_final_check_for_menu = 'YES'
                                                break
                                            try:
                                                change_item_cost_MENU_ADD2 = float(change_item_cost_MENU_ADD2)
                                                break
                                            except:
                                                print('Please enter numerical values only.')
                                                continue
                                    else:
                                        print('The item, \'{item}\', does not exist in this menu, please re-enter another value. '.format(item=change_item_cost_MENU_ADD))
                                        continue

                                    if back_to_final_check_for_menu == 'NO':
                                        add_menu_details['Menu item cost'][change_item_cost_MENU_ADD] = change_item_cost_MENU_ADD2
                                    break

                            elif menu_element_to_change_MENU_ADD == 'STOCK':
                                print('''
_____________________________________________________
List of currently featured item(s) and their
respective stock(s):
''')
                                iteration_number_for_editing_stock_MENU_ADD = 1
                                for keys,values in add_menu_details['Menu item stock'].items():
                                    print('''
Item {num}: \'{key}\' : {stock} | To change the stock of this item, enter \'{key}\'\n.'''.format(num=iteration_number_for_editing_stock_MENU_ADD, key=keys, stock=values))
                                    iteration_number_for_editing_stock_MENU_ADD += 1


                                while True:
                                    change_item_stock_MENU_ADD = is_it_right_or_wrong('Which item\' stock would you like to change: ')
                                    if change_item_stock_MENU_ADD == 'STOP':
                                        back_to_final_check_for_menu = 'YES'
                                        break
                                    if change_item_stock_MENU_ADD in add_menu_details['Menu item stock'].keys():
                                        while True:
                                            change_item_stock_MENU_ADD2 = is_it_right_or_wrong('Changing the item, {item}, current cost\'s stock \'{stock}\' to: '.format(item=change_item_stock_MENU_ADD, stock=add_menu_details['Menu item stock'][change_item_stock_MENU_ADD]))
                                            if change_item_stock_MENU_ADD2 == 'STOP':
                                                back_to_final_check_for_menu = 'YES'
                                                break
                                            try:
                                                change_item_stock_MENU_ADD2 = int(change_item_stock_MENU_ADD2)
                                                break
                                            except:
                                                print('Please enter integet values only.')
                                                continue
                                    else:
                                        print('The item, \'{item}\', does not exist in this menu, please re-enter another value. '.format(item=change_item_stock_MENU_ADD))
                                        continue

                                    if back_to_final_check_for_menu == 'NO':
                                        add_menu_details['Menu item stock'][change_item_stock_MENU_ADD] = change_item_stock_MENU_ADD2
                                    break

                        if back_to_final_check_for_menu == 'YES':
                            break
                        else:
                            continue

#________________________________________________________________________________________________
# REMOVE MENU

    elif action == 'REMOVE':
        bypass_remove_check = 'NO'
        while True:
            print('List of available Menu: ')
            iteration_number_for_removing_menu = 1
            for menU in MAIN_MENU_NAMES:
                print('Menu {num}: \'{menu}\' | To remove this menu, enter \'{menu}\'.'.format(num=iteration_number_for_removing_menu, menu=menU))
                iteration_number_for_removing_menu += 1


            print('To go back, enter \'BACK\'.')
            print('\n')
            removed_menu = is_it_right_or_wrong('Which Menu would you like to remove: \n')
            if removed_menu == 'BACK':
                bypass_remove_check = 'OK'
                break

            check_if_menu_is_available_to_remove = []
            menu_is_indeed_avaialble_to_remove = 'NO'
            for menu_d in List_of_all_Menu_detail:
                if menu_d[0] == removed_menu:
                    menu_is_indeed_avaialble_to_remove = 'YES'
                    break
            if menu_is_indeed_avaialble_to_remove == 'YES':
                break
            elif menu_is_indeed_avaialble_to_remove == 'NO':
                print('''
_____________________________________________________
The menu you wish to delete does not exist,
please re-enter another menu.
''')

        if bypass_remove_check == 'NO':
            while True:
                are_you_sure_remove_menu = input('''
_____________________________________________________
Deleting a menu will permanently remove it.

To cancel, enter \'CANCEL\'.
To proceed, enter\'OK\'

        ''')
                if are_you_sure_remove_menu == 'OK':
                    for menu_d in List_of_all_Menu_detail:
                        if menu_d[0] == removed_menu.title():
                            List_of_all_Menu_detail.remove(menu_d)
                            MAIN_MENU_NAMES.remove(removed_menu.title())

                    write_menu(List_of_all_Menu_detail)

                    print('''
_____________________________________________________
=============
Updated Menu:
=============\n''')
                    break

                elif are_you_sure_remove_menu == 'CANCEL':
                    print('''
_____________________________________________________
========================
No Menu has been deleted.
========================
''')
                    break


            DISPLAY_ALL_MENU(List_of_all_Menu_detail)
        else:
            return
    write_menu(List_of_all_Menu_detail)

def MAIN_EDIT_ADD_REMOVE_OPTIONS():
    iteration_number_for_menu_prompting = 1
    print('''
_____________________________________________________
===========================
Currently Featured Menu(s):
===========================
''')
    for menu in MAIN_MENU_NAMES:
        print('Menu {num}: \'{Menu}\' | To Edit this Menu, please enter \'{Menu}\'.'.format(num=iteration_number_for_menu_prompting, Menu=menu))
        iteration_number_for_menu_prompting += 1


    whattodonext = input('''
To Remove a Menu, please enter \'REMOVE\'.\n
To Add a Menu, please enter \'ADD\'.\n
To Exit, please enter \'EXIT\'.\n
To view the content of all available menu, please enter \'VIEW\'.

To go back to the main screen, please enter \'BACK\'.
''')

    return whattodonext

def is_it_right_or_wrong(statement):
    while True:

        prompt_user = input(statement)
        if prompt_user == 'CANCEL': exit()
        if prompt_user == 'STOP': return 'STOP'

        while True:
            confirm_user = input('Enter \'Y\' to confirm \'{name}\' or \'N\' to re-enter a new value: '.format(name=prompt_user))
            if confirm_user == 'Y':
                break
            elif confirm_user == 'CANCEL': exit()

            elif confirm_user == 'N':
                break
            else:
                continue
        if confirm_user == 'Y':
            break
        else:
            continue

    return prompt_user

def EDIT_MENU(action):
    num_to_keep_tract_of_menu_location = 0
    for menu in List_of_all_Menu_detail:
        if menu[0] == action:
            Menu_to_edit = menu
            break
        num_to_keep_tract_of_menu_location += 1

    while True:
        menu_edit_options = input('''
_____________________________________________________

INSTRUCTION:

You are currently editing the \'{menu_name}\' Menu.

    MENU DETAILS:
    _____________

    Menu: {menu_name}
    Number of item(s): {menu_num}
    Start Time: {start}
    End Time: {end}

    List of items and their respective cost ($):

    {list_of_cost}

    List of items and their respective stock:

    {list_of_stock}

To change the name of this menu, enter \'NAME\'.

To ADD an item to this menu, enter \'ADD\'.
To REMOVE an item from this menu, enter \'REMOVE\'.
To change the cost of a particular item, enter \'COST\'.
To change the stock of a particular item, enter \'STOCK\'

To change the starting time of this menu, enter \'START\'.
to change the ending time of this menu, enter \'END\'.

If this is not the menu you wish to make changes to, you may
enter \'BACK\' to go back.
'''.format(menu_name=Menu_to_edit[0], menu_num = str(Menu_to_edit[1]), list_of_cost=Menu_to_edit[2], list_of_stock=Menu_to_edit[3],
start=Menu_to_edit[4], end=Menu_to_edit[5]))

        if menu_edit_options == 'BACK':
            break
        elif menu_edit_options == 'NAME':
            menu_name_change = is_it_right_or_wrong('Changing the menu\'s current name, \'{current_name}\', to: '.format(current_name=Menu_to_edit[0]))
            if menu_name_change == 'STOP':
                continue
            else:
                Menu_to_edit[0] = menu_name_change
                continue
        elif menu_edit_options == 'START':
            menu_start_time_change = is_it_right_or_wrong('Changing the menu\'s current starting time, \'{start_time}\', to: '.format(start_time=Menu_to_edit[4]))
            if menu_start_time_change == 'STOP':
                continue
            else:
                 Menu_to_edit[4] = menu_start_time_change
                 continue
        elif menu_edit_options == 'END':
            menu_end_time_change = is_it_right_or_wrong('Changing the menu\'s current ending time, \'{end_time}\', to: '.format(end_time=Menu_to_edit[5]))
            if menu_end_time_change == 'STOP':
                continue
            else:
                 Menu_to_edit[5] = menu_end_time_change
                 continue
        elif menu_edit_options == 'COST':
            while True:
                print('''
_____________________________________________________
List of currently featured item(s) and their
respective cost(s):
''')
                iteration_number_for_editing_cost_MENU_ADD = 1
                for keys,values in Menu_to_edit[2].items():
                    print('''
Item {num}: \'{key}\' : {cost} | To change the cost of this item, enter \'{key}\'.\n'''.format(num=iteration_number_for_editing_cost_MENU_ADD, key=keys, cost=values))
                    iteration_number_for_editing_cost_MENU_ADD += 1

                print('Enter \'BACK\' to go back.\n')
                menu_change_cost = is_it_right_or_wrong('Which item\' cost would you like to change: ')

                if menu_change_cost in Menu_to_edit[2].keys():
                    while True:
                        menu_change_cost_2 = is_it_right_or_wrong('Changing the item, {item}, current cost\'s from \'{cost}\' to: '.format(item=menu_change_cost, cost=Menu_to_edit[2][menu_change_cost]))
                        if menu_change_cost_2 == 'STOP':
                            break
                        try:
                            menu_change_cost_2 = float(menu_change_cost_2)
                            Menu_to_edit[2][menu_change_cost] = menu_change_cost_2
                            break
                        except:
                            print('Please enter numerical values only.')
                            continue
                elif menu_change_cost == 'BACK':
                    break

                else:
                    print('The item, \'{item}\', does not exist in this menu, please re-enter another value. '.format(item=menu_change_cost))
                    continue
        elif menu_edit_options == 'STOCK':
            while True:
                print('''
_____________________________________________________
List of currently featured item(s) and their
respective stock(s):
''')
                iteration_number_for_editing_stock_MENU_ADD = 1
                for keys,values in Menu_to_edit[3].items():
                    print('''
Item {num}: \'{key}\' : {cost} | To change the cost of this item, enter \'{key}\'.\n'''.format(num=iteration_number_for_editing_stock_MENU_ADD, key=keys, cost=values))
                    iteration_number_for_editing_stock_MENU_ADD += 1

                print('Enter \'BACK\' to go back.\n')

                menu_change_stock = is_it_right_or_wrong('Which item\' stock would you like to change: ')

                if menu_change_stock in Menu_to_edit[3].keys():
                    while True:
                        menu_change_stock_2 = is_it_right_or_wrong('Changing the item, {item}, current stock\'s from \'{stock}\' to: '.format(item=menu_change_stock, stock=Menu_to_edit[3][menu_change_stock]))
                        if menu_change_stock_2 == 'STOP':
                            break
                        try:
                            menu_change_stock_2 = int(menu_change_stock_2)
                            Menu_to_edit[3][menu_change_stock] = menu_change_stock_2
                            break
                        except:
                            print('Please enter integer values only.')
                            continue
                elif menu_change_stock == 'BACK':
                    break

                else:
                    print('The item, \'{item}\', does not exist in this menu, please re-enter another value. '.format(item=menu_change_stock))
                    continue
        elif menu_edit_options == 'REMOVE':
            while True:
                print('''
_____________________________________________________
===========================
Current list of menu items:
===========================
''')
                for key in Menu_to_edit[2].keys():
                    print('To remove item \'{key}\' from the menu, please enter \'{key}\'.'.format(key=key))
                menu_remove_item = is_it_right_or_wrong('''
*You may enter \'BACK\' to go back*
Which menu item would you like to remove:
''')

                if menu_remove_item == 'BACK':
                    break
                if menu_remove_item in Menu_to_edit[2].keys():
                    while True:
                        are_you_sure_remove_menu_item = input('''
_____________________________________________________
Deleting this menu item will permanently deletes it.
To proceed, enter \'OK\'.
To Cancel, enter \'CANCEL\'.

''')
                        if are_you_sure_remove_menu_item == 'OK':
                            del Menu_to_edit[2][menu_remove_item]
                            del Menu_to_edit[3][menu_remove_item]
                            Menu_to_edit[1] = len(Menu_to_edit[2])
                            break
                            print('\'{item}\' has been deleted from the menu.'.format(item=menu_remove_item))
                        elif are_you_sure_remove_menu_item == 'CANCEL':
                            break


                elif menu_remove_item not in Menu_to_edit[2].keys():
                    print('The entered menu item does not exist, please re-enter a new value.')
        elif menu_edit_options == 'ADD':
            while True:
                print('''
_____________________________________________________
Current list of menu items:
''')
                iteration_number_for_adding_item = 1
                for item in Menu_to_edit[2].keys():
                    print('Item {num}: \'{item}\'.'.format(num=iteration_number_for_adding_item, item=item))
                    iteration_number_for_adding_item += 1
                print('\n')
                print('At any given, point, you may enter \'STOP\' to cancel.')


                new_item_name = is_it_right_or_wrong('''
Enter the name of the item you want to add:
To go back to list of editing options, please enter \'BACK\'
''').title()

                if new_item_name =='Stop':
                    continue
                elif new_item_name =='Back':
                    break

                bypass_menu_add_item = 'NO'

                while True:
                    new_item_cost = is_it_right_or_wrong('Enter the cost for the item: ')
                    if new_item_cost == 'STOP':
                        bypass_menu_add_item = 'YES'
                        break
                    else:
                        try:
                            new_item_cost = float(new_item_cost)
                            break
                        except:
                            print('Please enter numerical values only.')
                            continue

                if bypass_menu_add_item == 'NO':
                    while True:
                        new_item_stock = is_it_right_or_wrong('Enter the number of available stock for the item: ')
                        if new_item_stock == 'STOP':
                            bypass_menu_add_item == 'YES'
                            break
                        else:
                            try:
                                new_item_stock = int(new_item_stock)
                                break
                            except:
                                print('Please enter integer values only.')
                                continue

                if bypass_menu_add_item == 'NO':
                    print('''
The following item and its details
will be added to your new menu:

Item Name: {name}
Item Cost: {cost}
Item Stock: {stock}
'''.format(name=new_item_name, cost=new_item_cost, stock=new_item_stock))

                    while True:
                        Confirm_new_item = is_it_right_or_wrong('''
To Confirm, please enter \'OK\'.
To Cancel, please enter \'NO\'
''')
                        if Confirm_new_item == 'OK':
                            Menu_to_edit[2].update({new_item_name:new_item_cost})
                            Menu_to_edit[3].update({new_item_name:new_item_stock})
                            Menu_to_edit[1] = len(Menu_to_edit[2])
                            bypass_menu_add_item = 'YES'
                            break
                        elif Confirm_new_item == 'NO':
                            bypass_menu_add_item == 'YES'
                            break


                if bypass_menu_add_item == 'YES':
                    break
                else:
                    continue

    List_of_all_Menu_detail[num_to_keep_tract_of_menu_location] = Menu_to_edit
    write_menu(List_of_all_Menu_detail)

def DISPLAY_ALL_MENU(listofmenudetails):
    for menu_detail in listofmenudetails:
         x = make_menu(menu_detail)
         print(x)

def calculate_bill(items_and_quantities):
    pass

def dictionary_of_all_menu_item_cost_stock(listofmenudetails):
    All_menu_price_cost_dict = {}

    for menu in listofmenudetails:

        cost_and_price_list = []
        cost_IN_ALL_MENU = {}
        stock_IN_ALL_MENU = {}

        menu_name_for_dict = menu[0]

        for key,values in menu[2].items():
            cost_IN_ALL_MENU[key] = values

        for key,values in menu[3].items():
            stock_IN_ALL_MENU[key] = values

        cost_and_price_list.append(cost_IN_ALL_MENU)
        cost_and_price_list.append(stock_IN_ALL_MENU)
        All_menu_price_cost_dict[menu_name_for_dict] = cost_and_price_list

    return All_menu_price_cost_dict



List_of_all_Menu_detail = text_info_to_menu_objects(Menu_names, Menu_num_of_items, Menu_name_cost, Menu_name_stock, Menu_start, Menu_end)

while True:
    
    PROGRAM_MAIN_FUNCTION = input('''
=============================================
      RESTAURANT MENUS & ORDER MANAGER
=============================================

Available Functions:

1) EDIT MENU - To view and edit menu(S), enter \'MENU\'.

2) GENERATE ORDER - To generate an order, enter \'ORDER\'.

To Exit, enter \'EXIT\'.

''')

    if PROGRAM_MAIN_FUNCTION == 'MENU':
        print('''===========================================
These will be our featured Menus for today:
===========================================
''')

        DISPLAY_ALL_MENU(List_of_all_Menu_detail)

        #Will you edit?
        bypass_view_menu_edit_options = 'NO'
        while True:
            will_you_edit = input('Enter \'OK\' to exit, \'EDIT\' to edit, or \'BACK\' to go back to the main screen.\n')
            if will_you_edit == 'OK':
                exit()
            elif will_you_edit == 'EDIT':
                print('\n')
                break
            elif will_you_edit == 'BACK':
                bypass_view_menu_edit_options = 'YES'
                break
            else:
                continue
        if bypass_view_menu_edit_options == 'NO':
            while True:
                MAIN_MENU_NAMES = MAIN_MENU(List_of_all_Menu_detail)
                action = MAIN_EDIT_ADD_REMOVE_OPTIONS()


                if action in MAIN_MENU_NAMES:
                    EDIT_MENU(action)
                elif action == 'EXIT':
                    exit()
                elif action == 'ADD' or action == 'REMOVE':
                    REMOVE_and_ADD_menu(action)
                elif action == 'VIEW':
                    DISPLAY_ALL_MENU(List_of_all_Menu_detail)
                elif action == 'BACK':
                    break





    elif PROGRAM_MAIN_FUNCTION == 'ORDER':

        All_menu_price_cost_dict = dictionary_of_all_menu_item_cost_stock(List_of_all_Menu_detail)

        print('''
================================
    TẤT CẢ MENU VÀ CHI TIẾT
================================
''')
        iteration_number_menu = 1
        for menu in List_of_all_Menu_detail:
            menu_name = menu[0]

            print('''
____________________________________________________________
Thực đơn {num}: {name}
'''.format(num=iteration_number_menu,name=menu_name))

            iteration_number = 1
            for item in menu[2].keys():

                print('''Món số {iteration_number}: {item}

    | Giá: {price} | Phận còn lại: {stock} |
'''.format(iteration_number=iteration_number, item=item, price=menu[2][item],
                stock=menu[3][item]))
                iteration_number += 1

            iteration_number_menu += 1

        instruction_for_generating_order = '''
=====================================
Có 2 cách để thêm món ăn vào đơn hàng:
=====================================

    1) Nhập chính xác tên món ăn.

        (Ví dụ: \'Fried Chicken\')

    2) Nhập 'M', tiếp theo là số thực đơn, tiếp theo là 'D' và cuối cùng là số món ăn.

        (Ví dụ: \'M1D1\' *M1D1 sẽ đề cập đến món đầu tiên trong menu đầu tiên*)
'''
        print(instruction_for_generating_order)

        Item_to_order = {}

        done = 'NO'
        while True:
            table_number = is_it_right_or_wrong('''*Để quay lại, hãy nhập \'BACK\'*
Nhập số bàn: ''')
            if table_number == 'BACK':
                done ='YES'
                break
            try:
                table_number = int(table_number)
                break
            except:
                print('Vui lòng chỉ nhập giá trị số nguyên.')
                continue



        while done == 'NO':


            def display_order(**item_to_order):
                print('''
=================
Hóa đơn hiện tại:
=================
Bảng số: {table}'''.format(table=table_number))
                total_billing_cost = 0
                for key,values in item_to_order.items():
                    item_to_order_cost = values[0]

                    item_to_order_quantity = values[1]
                    total_cost_for_item_to_order = item_to_order_cost * item_to_order_quantity
                    total_billing_cost += total_cost_for_item_to_order
                    print('''
    {key} | Giá (1): {price} | x {quantity} | Giá (tất cả): {total}
'''.format(key=key, price=item_to_order_cost, quantity=item_to_order_quantity, total=total_cost_for_item_to_order))
                print('''
_____________________________
Tổng giá: {total_bill}
Thuế dịch vụ: 6%
_____________________________
Tổng cộng: {grand_total}

'''.format(total_bill=total_billing_cost, grand_total=int(total_billing_cost*1.06)))

            Item_price_and_quanitty = []

            order_item = input('''
_____________________________________________________________
*Để hủy, hãy nhập \'STOP\'*
*Để hoàn tất đơn hàng, hãy nhập \'END\'*

*Để xóa một món ăn trong thực đơn, hãy nhập \'REMOVE\'*
Để thay đổi số lượng món ăn trong thực đơn, hãy nhập \'Q\'*

Nhập món ăn bạn muốn thêm vào đơn đặt hàng này: ''')

            if order_item == 'STOP' or order_item == 'END':
                done = 'YES'
            elif order_item == 'Q':
                done_Q = 'NO'
                while done_Q == 'NO':

                    if bool(Item_to_order) is False:
                        print('''
=======================
Hóa đơn hiện đang trống.
=======================''')
                        break

                    what_item_to_change_quantity = input('Nhập tên của bi hiện tại bạn muốn thay đổi số lượng trong hóa đơn hiện tại: ')

                    if what_item_to_change_quantity in Item_to_order.keys():
                        current_q = Item_to_order[what_item_to_change_quantity][1]
                        while True:
                            changing_the_quantity = is_it_right_or_wrong('Thay đổi số lượng cho, \'{item}\', from \'{current_q}\' to: '.format(item=what_item_to_change_quantity, current_q=current_q))
                            try:
                                changing_the_quantity = int(changing_the_quantity)
                                Item_to_order[what_item_to_change_quantity][1] = changing_the_quantity
                                done_Q = 'YES'
                                break
                            except:
                                print('Vui lòng chỉ nhập giá trị số nguyên.')
                                continue
                    else:
                        print('Hóa đơn hiện tại không có món, \'{item}\'.'.format(item=what_item_to_change_quantity))
                        continue
                    display_order(**Item_to_order)

            elif order_item =='REMOVE':
                pass

            else:
                    bypass_item_does_not_exist = 'NO'
                    for menu in All_menu_price_cost_dict.keys():
                        if order_item in All_menu_price_cost_dict[menu][0].keys():
                            item_to_order_cost = float(All_menu_price_cost_dict[menu][0][order_item])
                            Item_price_and_quanitty.append(item_to_order_cost)

                            while True:
                                quantity_of_item = is_it_right_or_wrong('Nhập số lượng cho \'{item}\':'.format(item=order_item))
                                if quantity_of_item == 'STOP':
                                    break

                                try:
                                    quantity_of_item = int(quantity_of_item)
                                    Item_price_and_quanitty.append(quantity_of_item)
                                    Item_to_order[order_item] = Item_price_and_quanitty

                                    bypass_item_does_not_exist = 'YES'
                                    break
                                except:
                                    print('Vui lòng chỉ nhập giá trị số nguyên.')
                                    continue

                    if bypass_item_does_not_exist == 'NO':
                        print('Món, \'{item}\' không tồn tại trong bất kỳ menu nào.'.format(item=order_item))
                        continue


                    display_order(**Item_to_order)

    elif PROGRAM_MAIN_FUNCTION == 'EXIT':
        exit()

    else:
        continue
