#________________________________________________________________________________________________________________
# Imports
import re
import datetime
import pytz
import time
#________________________________________________________________________________________________________________
# MAIN LISTS AND DICT:

Saving_Status = ''

To_do_MAIN = {}

Events_MAIN = {}



#________________________________________________________________________________________________________________
# Parsing


with open('Daily_Checklist.txt') as Daily_Checklist:
    for lines in Daily_Checklist:

        if lines.startswith('TODO'):

            lines = lines.replace('TODO|','')


            To_do_PARSE_details = {
                'Name': None,
                'Goal': None,
                'Date': None
            }

            To_do_PARSE_Name = None

            To_do_PARSE_Goal = {
                'Type':None,
                'Phrase':None,
                'Number':None,
                'Current Status':None
            }

            To_do_PARSE_Date = []


            To_do_splitter = lines.split('|')
            for details in To_do_splitter:
                details.replace('[','').replace(']','')
                To_do_splitter_2 = details.split(':')

                if To_do_splitter_2[0] == 'Name':
                    To_do_PARSE_Name = To_do_splitter_2[1]
                elif To_do_splitter_2[0] == 'Goal Type':
                    To_do_PARSE_Goal['Type'] = To_do_splitter_2[1]
                elif To_do_splitter_2[0] == 'Number':
                    To_do_PARSE_Goal['Number'] = To_do_splitter_2[1]
                elif To_do_splitter_2[0] == 'Phrase':
                    To_do_PARSE_Goal['Phrase'] = To_do_splitter_2[1]
                elif To_do_splitter_2[0] == 'Current Status':
                    To_do_PARSE_Goal['Current Status'] = To_do_splitter_2[1]
                elif To_do_splitter_2[0] == 'Date':

                    if '99' in To_do_splitter_2[1]:

                        To_do_PARSE_TD_dates_1 = To_do_splitter_2[1].replace('\n', '').replace('\'','')
                        To_do_PARSE_TD_dates_2 = re.findall('^\[99,(.*)\]', To_do_PARSE_TD_dates_1)
                        To_do_PARSE_Date = [99, To_do_PARSE_TD_dates_2[0].strip()]

                    else:

                        date_in_todo_PARSE = To_do_splitter_2[1].replace('[','').replace(']','').replace(' ','')
                        date_in_todo_PARSE_splitter = date_in_todo_PARSE.split(',')
                        for date in date_in_todo_PARSE_splitter:
                            To_do_PARSE_Date.append(int(date))

            To_do_PARSE_details['Name'] = To_do_PARSE_Name
            To_do_PARSE_details['Goal'] = To_do_PARSE_Goal
            To_do_PARSE_details['Date'] = To_do_PARSE_Date

            To_do_MAIN[To_do_PARSE_Name] = To_do_PARSE_details




        elif lines.startswith('EVENT'):

            Event_PARSE_details = {
                'Name':None,
                'Date':None,
                'Details':None

            }

            lines = lines.replace('EVENT|','').replace('\n','')

            event_splitter = lines.split('|')
            for details in event_splitter:
                event_splitter_2 = details.split(':')
                if event_splitter_2[0] == 'Name':
                    Event_PARSE_details['Name'] = event_splitter_2[1]
                elif event_splitter_2[0] == 'Date':
                    Event_PARSE_details['Date'] = event_splitter_2[1]
                elif event_splitter_2[0] == 'Details':
                    event_PARSE_phrases = event_splitter_2[1].replace('[\'','').replace('\', \'','|').replace('\']','')
                    event_PARSE_phrases_splitter = event_PARSE_phrases.split('|')

                    Event_PARSE_details['Details'] = event_PARSE_phrases_splitter



            Events_MAIN[Event_PARSE_details['Name']] = Event_PARSE_details


#________________________________________________________________________________________________________________
# Reset To-do

for details in To_do_MAIN.values():

    if details['Goal']['Type'] == 'NUM':

        details['Goal']['Current Status'] = 0

    elif details['Goal']['Type'] == 'YN':

        details['Goal']['Current Status'] = 'Uncompleted'






#________________________________________________________________________________________________________________
# Functions:


def Make_To_Do(done_with_to_do_name = 'NO'):

    to_do_details = {
        'Name': None,
        'Goal': None,
        'Date': None
    }

    done_with_to_do = 'NO'
    while done_with_to_do == 'NO':


        #_______________________________________________________
        # NAME:


        while done_with_to_do_name == 'NO':
            To_do_name = input('''    *Enter 'BACK' to exit*
    Enter the TO-DO name: ''')
            if To_do_name == 'BACK':

                cancel_todo_verification = input('''    ---------------------------------------------
    Enter 'Y' to confirm, 'N' to cancel the exit:
    ''')

                if cancel_todo_verification == 'Y':
                    return
                elif cancel_todo_verification == 'N':
                    continue

            to_do_details['Name'] = To_do_name
            done_with_to_do_name = 'YES'
            done_with_to_do_goal = 'NO'

        print('    -------------------------------------------')


        #_______________________________________________________
        # To-Do GOAL:

        def display_to_do_goal(goal_details):
            print('''
        =====================
        Current Goal Details:
        =====================
        ''')
            for keys,values in goal_details.items():
                print('        {key}: {value}'.format(key=keys,value=values))
            print('\n')


        while done_with_to_do_goal == 'NO':

            to_do_goal = {}

            done_with_goal_types = 'NO'
            while done_with_goal_types == 'NO':

                print('    *Enter \'INFO\' to learn about goal types*')
                to_do_goal_type = input('    Enter the Goal type: ')
                to_do_goal['Type'] = to_do_goal_type

                done_with_goal_types = 'YES'

                if to_do_goal_type == 'INFO':

                    print('''
        Goal Type is refering to how your goal for this
        to-do will be displayed. The goal type will also affect
        how your 'current status' for the goal will look as well.

        There are currently 2 available goal type:

            1) YES or NO

                    'YES or NO' goal types will allow you type in a phrase
                    that will be displayed at the 'goal' section of your to-do.
                    It is advised to keep the phrase short for aesthetic purposes
                    and that you will be given a different section to include
                    any details that you wish to be attached with the to-do.

                    The 'Current Status' section of your to-do will only have 2
                    possible statuses: 'YES' or 'NO', hence the name. In other word,
                    the statuses of the to-do with the 'YES or NO' goal type
                    can only be YES or NO; either you've done it or you haven't.


            2) Numerical

                    Numerical goal types are simple. You simply enter a
                    numerical goal attached with a customized metric. The
                    'Current Status' section of to-dos with numerical goal
                    types will have the updated numerical status of whatever the
                    goal may be (ex: savings, hours of study, etc.\n''')
                    continue

                elif to_do_goal_type == 'YN':

                    done_with_to_do_goal_phrase = 'NO'
                    while done_with_to_do_goal_phrase =='NO':
                        display_to_do_goal(to_do_goal)
                        to_do_goal_phrase = input('    Enter your phrase: ')

                        if to_do_goal_phrase == 'BACK':
                            break

                        to_do_goal['Phrase'] = to_do_goal_phrase
                        done_with_to_do_goal_phrase = 'YES'

                        done_with_to_do_goal_number = 'NO'
                        while done_with_to_do_goal_number == 'NO':

                            to_do_goal_number = 'NOT APPLICABLE'
                            to_do_goal['Number'] = to_do_goal_number

                            display_to_do_goal(to_do_goal)
                            done_with_to_do_goal_number = 'YES'

                            done_with_final_check_to_do_goal = 'NO'
                            while done_with_final_check_to_do_goal == 'NO':

                                to_do_goal_final_check = input('    To finalize, enter \'OK\', else enter \'BACK\': ')
                                if to_do_goal_final_check == 'BACK':
                                    done_with_to_do_goal_phrase = 'NO'
                                    break
                                elif to_do_goal_final_check == 'OK':
                                    to_do_goal['Current Status'] = 'Uncompleted'

                                    done_with_goal_types = 'YES'
                                    done_with_to_do_goal = 'YES'

                                    to_do_details['Goal'] = to_do_goal
                                    done_with_to_do_date = 'NO'
                                    break
                                else:
                                    continue


                elif to_do_goal_type == 'NUM':

                    display_to_do_goal(to_do_goal)


                    done_with_to_do_goal_number = 'NO'
                    while done_with_to_do_goal_number == 'NO':

                        to_do_goal_number = input('    Enter your number: ')
                        if to_do_goal_number == 'BACK':
                            break

                        try:
                            to_do_goal_number = float(to_do_goal_number)
                            to_do_goal['Number'] = to_do_goal_number
                            display_to_do_goal(to_do_goal)
                        except:
                            print('    Please enter numerical values only.')
                            continue

                        done_with_to_do_goal_number = 'YES'
                        done_with_to_do_goal_phrase = 'NO'
                        while done_with_to_do_goal_phrase == 'NO':

                            to_do_goal_phrase = input('    Enter your metric: ')

                            if to_do_goal_phrase == 'BACK':
                                done_with_to_do_goal_number = 'NO'
                                break

                            to_do_goal['Phrase'] = to_do_goal_phrase

                            display_to_do_goal(to_do_goal)

                            done_with_to_do_goal_phrase = 'YES'
                            done_with_final_check_to_do_goal = 'NO'
                            while done_with_final_check_to_do_goal == 'NO':

                                to_do_goal_final_check = input('    To finalize, enter \'OK\', else enter \'BACK\': ')
                                if to_do_goal_final_check == 'BACK':
                                    done_with_to_do_goal_phrase = 'NO'
                                    break
                                elif to_do_goal_final_check == 'OK':
                                    to_do_goal['Current Status'] = 0

                                    done_with_goal_types = 'YES'
                                    done_with_to_do_goal = 'YES'

                                    to_do_details['Goal'] = to_do_goal
                                    done_with_to_do_date = 'NO'
                                    break
                                else:
                                    continue

                elif to_do_goal_type == 'BACK':
                    done_with_to_do_goal = 'WAIT'
                    done_with_to_do_date = 'WAIT'
                    done_with_to_do_name = 'NO'
                    break

                else:
                    print('''
        !!!!!!!!!!!!!!!!!
        Invalid Goal Type
        !!!!!!!!!!!!!!!!!
        ''')
                    continue

        print('    -------------------------------------------')

        #_______________________________________________________
        # To-Do Date:


        if done_with_to_do_date == 'NO':

            dates_for_display = {
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Saturday',
        '7': 'Sunday'
    }

            def display_to_do_date(selected_dates):
                print('''
        ==========================
        This TO-DO will repeat on:
        ==========================
            ''')

                iteration_number = 1
                if type(selected_dates[1]) is str:
                    pass
                else:
                    selected_dates.sort()
                for num in selected_dates:

                    if type(num) is str:
                        print('        Just Today: {date}'.format(date=num))
                    elif num == 99:
                        continue
                    else:
                        num_to_weekday = str(num)
                        print('        {num}) {weekday}'.format(num=iteration_number, weekday=dates_for_display[num_to_weekday]))
                        iteration_number += 1

                print('\n')


            # Instructions for To_do_date
            print('''
    ================================
    Please select the day(s) of the
    week should this TO-DO appear
    ================================

    Assign to Monday: Enter 'M'
    Assign to Tuesday: Enter 'TU'
    Assign to Wednesday: Enter 'W'
    Assign to Thursday: Enter 'TH'
    Assign to Friday: Enter 'F'
    Assign to Saturday: Enter 'SA'
    Assign to Sunday: Enter 'SU'

    Assign to EVERY weekday, enter 'ALL'
    Assign to just Today, enter 'TD'

    Enter 'BACK' to re-do the 'TO-DO Goal' section.
        ''')

            List_of_official_to_do_dates = []
            List_of_to_do_dates_check = []

        while done_with_to_do_date == 'NO':
            to_do_date = input('''    *Enter 'DONE' to finalize the dates*
    Add Dates: ''')


            if to_do_date == 'BACK':
                done_with_to_do_goal = 'NO'

                break

            elif to_do_date in List_of_to_do_dates_check:
                print('''    ------------------------------
    Date has already been assigned.\n''')
                continue

            elif to_do_date == 'M':
                List_of_official_to_do_dates.append(1)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue
            elif to_do_date == 'TU':
                List_of_official_to_do_dates.append(2)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue
            elif to_do_date == 'W':
                List_of_official_to_do_dates.append(3)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue
            elif to_do_date == 'TH':
                List_of_official_to_do_dates.append(4)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue
            elif to_do_date == 'F':
                List_of_official_to_do_dates.append(5)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue
            elif to_do_date == 'SA':
                List_of_official_to_do_dates.append(6)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue
            elif to_do_date == 'SU':
                List_of_official_to_do_dates.append(7)
                List_of_to_do_dates_check.append(to_do_date)
                display_to_do_date(List_of_official_to_do_dates)
                continue

            elif to_do_date == 'DONE' or to_do_date == 'TD':

                if to_do_date == 'DONE':
                    if len(List_of_official_to_do_dates) == 0:
                        print('    You have not selected any dates')
                        continue
                elif to_do_date == 'TD':

                    List_of_official_to_do_dates = [99,Today_Date_DV]
                    display_to_do_date(List_of_official_to_do_dates)

                to_do_date_final_check = input('    To finalize, enter \'OK\', else enter \'BACK\': ')

                if to_do_date_final_check == 'BACK':
                    break
                elif to_do_date_final_check =='OK':
                    to_do_details['Date'] = List_of_official_to_do_dates

                    done_with_to_do_date = 'YES'
                    break
                else:
                    continue
            else:
                print('    Please enter a valid date. \n')

        #_______________________________________________________
        # Return

        if done_with_to_do_name == 'YES' and done_with_to_do_goal == 'YES' and done_with_to_do_date == 'YES':
            return to_do_details

def Make_events():

    Event_details = {
        'Name': None,
        'Date': None,
        'Details': []

    }

    Event_month_reference = {
        'JAN': ['January', 31],
        'FEB': ['February', 28],
        'MAR': ['March', 31],
        'APR': ['April', 30],
        'MAY': ['May', 31],
        'JUN': ['June', 30],
        'JUL': ['July', 31],
        'AUG': ['August', 31],
        'SEP': ['September', 30],
        'OCT': ['October', 31],
        'NOV': ['November', 30],
        'DEC': ['December', 31]
    }

    while True:
        event_name = input('''    ------------------------------
    *Enter 'BACK' to cancel*
    Enter the name of this event: ''')

        if event_name == 'BACK':
            cancel_event_verification = input('''    ---------------------------------------------
    Enter 'Y' to confirm, 'N' to cancel the exit:
    ''')
            if cancel_event_verification == 'Y':
                return
            elif cancel_event_verification == 'N':
                continue

        Event_details['Name'] = event_name

        # EVENT YEAR ASSIGNMENT
        while True:
            event_date_year = input('''    ------------------------------
    Enter the YEAR for this event: ''')
            if event_date_year =='BACK':
                break
            try:
                event_date_year = int(event_date_year)
            except:
                print('''
    !!! Please enter numerical values only !!!
    ''')
                continue

            # EVENT MONTH ASSIGNMENT
            while True:
                event_date_month = input('''    ------------------------------
    *Enter the first 3 letter of the month*
    *Example: 'Jan' for January*

    Enter the MONTH for this event: ''')
                if event_date_month == 'BACK':
                    break
                if event_date_month.upper() in Event_month_reference.keys():

                    event_date_month_full = Event_month_reference[event_date_month.upper()][0]

                else:
                    print('''
    !!! Invalid Month !!!
    ''')
                    continue

                # EVENT DAY ASSIGNMENT
                while True:
                    event_date_day = input('''    ------------------------------
    Enter the DAY for this event: ''')
                    if event_date_day == 'BACK':
                        break

                    # Checks the DAY is entered correctly
                    try:

                        event_date_day = int(event_date_day)
                        if event_date_day < 1:
                            print('''
    !!!Please Enter postive numbers only !!!
    ''')
                            continue
                        if event_date_day > Event_month_reference[event_date_month.upper()][1]:
                            print('''
    !!! The month of {month} only has {days} days !!!
    '''.format(month=Event_month_reference[event_date_month.upper()][0], days=Event_month_reference[event_date_month.upper()][1]))
                            continue

                    except:
                        print('''
    !!! Please enter numerical values only !!!
    ''')
                        continue


                    event_date = '{month} {day}, {year}'.format(month=event_date_month_full, day=event_date_day, year=event_date_year)
                    event_date_to_strptime = datetime.datetime.strptime(event_date, '%B %d, %Y')

                    if Today_Date.date() > event_date_to_strptime.date():
                        print('''
    !!! The Entered Date has already passed !!!''')
                        continue

                    print('''    ==============================
    Event Date: {eventdate}'''.format(eventdate=event_date))

                    while True:
                        event_date_comfirmation = input('''
    Enter 'Y' to confirm,
    Enter 'BACK' to go back

    Action: ''')
                        if event_date_comfirmation == 'Y':
                            Event_details['Date'] = event_date
                            break

                        elif event_date_comfirmation =='BACK':
                            break

                    if event_date_comfirmation == 'Y':

                        while True:
                            print('''    ------------------------------------
    EVENT DETAILS (optional):

        1) Enter 'INFO' for instructions on how
           to use enter the detaisl for your event*

        2) Enter 'SKIP' to skip this*

        3) Enter 'MAKE' to add a detail section
           your event*
    ''')

                            event_add_details_action = input('     Action: ')

                            if event_add_details_action == 'MAKE':

                                event_add_details_final_text = ''
                                print('\n')
                                print('        Enter detail here:\n')
                                while True:

                                    event_add_details = input('        ')

                                    if event_add_details == 'BACK':
                                        break
                                    if 'FIN' in event_add_details_final_text:
                                        event_add_details_final_text = event_add_details_final_text.replace('FIN','')
                                        break


                                    if event_add_details[-1:] != ' ':
                                        event_add_details_final_text += (event_add_details + ' ')
                                    elif event_add_details[-1:] == ' ':
                                        event_add_details_final_text += (event_add_details)

                                if event_add_details == 'BACK':
                                    continue

                                event_add_details_phrase = ''
                                list_of_event_add_detail_phrase = []

                                iteration_number = 0
                                iteration_number_2 = 0

                                for x in event_add_details_final_text:

                                    event_add_details_phrase += x
                                    iteration_number +=1
                                    iteration_number_2 += 1

                                    if iteration_number >= 60:
                                        if x != ' ':
                                            continue
                                        list_of_event_add_detail_phrase.append(event_add_details_phrase)
                                        event_add_details_phrase = ''
                                        iteration_number = 1

                                    if iteration_number_2 == len(event_add_details_final_text):
                                        list_of_event_add_detail_phrase.append(event_add_details_phrase)


                                print('''    ------------------------------------
    Event Details:
    ''')
                                for phrase in list_of_event_add_detail_phrase:

                                    print('        {phrase}'.format(phrase=phrase))

                                while True:
                                    list_of_event_add_detail_phrase_confirmation = input('''
    *Due to the limitation of python built-in display
    features, entering 'BACK' would require you to
    re-type your detail section*

    Enter \'Y\' to confirm, \'BACK\' to go back: ''')

                                    if list_of_event_add_detail_phrase_confirmation == 'BACK':
                                        break
                                    elif list_of_event_add_detail_phrase_confirmation == 'Y':
                                        Event_details['Details'] = list_of_event_add_detail_phrase

                                        return Event_details


                                if list_of_event_add_detail_phrase_confirmation == 'BACK':
                                    continue

                            elif event_add_details_action == 'INFO':
                                print('''
    =================================
    How to add details to your Event:
    =================================

    *Due to the limitation of Python built-in display features, entering
    paragraph of texts in a visually pleasing manner can be rather
    difficult. For that reason, it is highly advished that you should
    be as attentive as possible as you write to avoid re-typing any data*

        1) As you are about to enter the details for your
           event, the program will prompt for your input after a
           minor indent. This indicate that you may begin
           typing your details.

        2) There are two ways for which you may enter your
           details:

                a) METHOD 1: Enter all your details in a single line
                   Keep in mind that as soon as your press the ENTER
                   key, the program create a new line. Any data that
                   you've entered in the first line can no longer be
                   edited. *DO NOT press the ENTER key if you wish to
                   use this method*

                   The benefit of the using this method is
                   that you can easily edit your paragraph by simply
                   using the arrow keys to navigate between the
                   characters and insert new characters.

                   The downside is that it can be visually unpleasant.

                b) METHOD 2: Use the ENTER key to create a new line
                   anytime you wish. Keep in mind that creating a new line
                   will not allow you to go back and edit the data in the
                   previous line. As a result, if you had made a typo or wish
                   you re-enter something within the previous line, you would
                   have to re-enter the entire detail section.

                   The benefit of using this method is that it is much
                   more visually appealing but at the cost of feasibly
                   editing any data you've written.

        3) To finalize your detail section, enter 'FIN' at
           the end of your paragraph and then press ENTER again.
           Alternatively, you could press ENTER to create a new line
           and enter 'FIN' at the very start of the new line followed
           by pressing the ENTER key once again.
    ''')
                                while True:
                                    event_add_detail_info = input('    Enter \'BACK\' to go back: ')
                                    if event_add_detail_info == 'BACK':
                                        break
                                    else:
                                        continue

                            elif event_add_details_action == 'SKIP':
                                Event_details['Details'] = ['NONE']
                                return Event_details
                            elif event_add_details_action =='BACK':
                                break

                            else:
                                print('    !!! Invalid Action !!!\n')
                                continue

def Update_events():
    pass

def Update_To_Do():
    pass





#________________________________________________________________________________________________________________
# Display

while True:

    #_______________________________________________________
    # Today's Time for all uses

    Today_Date = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
    Today_Date_DV = Today_Date.strftime('%B %d, %Y')
    Day_of_the_week = Today_Date.isoweekday()



    #_______________________________________________________
    # Display Date

    print('''




    =======================================
    {Today} {Weekday}
    '''.format(Today=Today_Date_DV, Weekday=Day_of_the_week))

    #_______________________________________________________
    # Display Events

    print('''
    =======================================
    Today's Events
    ''')

    iteration_number = 1

    for names,details in Events_MAIN.items():
        event_date_strptime = datetime.datetime.strptime(details['Date'], '%B %d, %Y')

        if Today_Date.date() == event_date_strptime.date():
            if Events_MAIN[names]['Details'][0] == 'NONE':
                print('        {num}) {name} | Date: {date} | Details: NONE'.format(num=iteration_number,name=names, date = details['Date']))
            else:
                print('        {num}) {name} | Date: {date} | Details:\n'.format(num=iteration_number,name=names, date = details['Date']))
            iteration_number +=1

            for phrase in details['Details']:
                if phrase == 'NONE':

                    break
                print('            {Phrase}'.format(Phrase=phrase))


            print('\n')



    print('    Upcoming Events')
    #_______________________________________________________
    # Display To-Do

    print('''
    =======================================
    Today's To Do(s)
    ''')

    iteration_number = 1
    TD_todo_to_delete = []
    for names, details in To_do_MAIN.items():

        if Day_of_the_week in details['Date'] or 99 in details['Date']:

            if 99 in details['Date']:

                Parsing_TDtodo = datetime.datetime.strptime(details['Date'][1].strip(), '%B %d, %Y')
                if Parsing_TDtodo.date() != Today_Date.date():
                    TD_todo_to_delete.append(names)
                    continue

            if details['Goal']['Number'] == 'NOT APPLICABLE':
                print('        {num}) {name} | GOAL: {phrase} | CURRENT STATUS: {current_status} \n'.format(num=iteration_number,
                name=names, phrase = details['Goal']['Phrase'], current_status=details['Goal']['Current Status']))
            else:
                print('        {num}) {name} | GOAL: {number} {phrase} | CURRENT STATUS: {current_status} {phrase} \n'.format(num=iteration_number,
                name=names, phrase = details['Goal']['Phrase'], number=details['Goal']['Number'],
                current_status=details['Goal']['Current Status']))
                iteration_number += 1

    for keys in TD_todo_to_delete:
        del To_do_MAIN[keys]






    #_______________________________________________________
    # Actions
    while True:

        MAIN_ACTIONS = input('''
    ===============================================
    *To view all available actions, enter 'ACTION'*
    {Saving_Status}
    Action: '''.format(Saving_Status=Saving_Status))

        if MAIN_ACTIONS == 'TODO':

            new_to_do = Make_To_Do()
            if new_to_do is None:
                continue

            new_to_do_name = new_to_do['Name']
            To_do_MAIN[new_to_do_name] = new_to_do
            Saving_Status = '!!! You have made changes, remember to save !!!'


            #for keys,values in To_do_MAIN.items():
                #print(values)
            break






        elif MAIN_ACTIONS == 'EVENT':

            new_event = Make_events()
            if new_event is None:
                continue
            new_event_name = new_event['Name']
            Events_MAIN[new_event_name] = new_event
            Saving_Status = '!!! You have made changes, remember to save !!!'

            for keys,values in Events_MAIN.items():

                print(values)
            break

        elif MAIN_ACTIONS == 'SAVE':

            with open('Daily_Checklist.txt', 'w') as Daily_Checklist:

                # Saves new to-dos & re-writes old ones:
                for name,details in To_do_MAIN.items():

                    Daily_Checklist.write('TODO|Name:{name}|Goal Type:{goal_type}|Number:{number}|Phrase:{phrase}|Current Status:{current_status}|Date:{date}\n'.format(
                    name=name, goal_type=details['Goal']['Type'], number=details['Goal']['Number'], phrase=details['Goal']['Phrase'],
                    current_status=details['Goal']['Current Status'], date=details['Date']))


            Saving_Status = ''
            print('''
    <><><><><><><><><><><><><><><><><><><>
    Your Daily Checklist has been updated!
    <><><><><><><><><><><><><><><><><><><>
    ''')
            while True:
                return_to_main_screen = input('''    To return to the main screen, enter 'BACK'
    To exit the program, enter 'QUIT'
    Action: ''')
                if return_to_main_screen == 'BACK':
                    break
                elif return_to_main_screen =='QUIT':
                    exit()
                else:
                    continue
            break

        elif MAIN_ACTIONS == 'QUIT':
            exit()

        elif MAIN_ACTIONS == 'SHOW':
            for names, details in To_do_MAIN.items():
                print(names)
                print(details)

            break

        elif MAIN_ACTIONS == 'ACTION':
            print('''

    1) To create a To-Do, enter 'TODO'.
    2) To create an event, enter 'EVENT'
    3) To update a To-Do/Event, enter 'UPDATE'

    4) To re-display Today's To-Do(s) and Event(s)
       Enter 'SHOW'


    5) To exit the program, enter 'QUIT'


                    *NOTICE*
                    ========
    If you created any new events/to-do, be
    sure to save it by entering 'SAVE' before
    you exit the program

    ''')
            while True:
                return_to_main_screen = input('''    ==========================================
    To return to the main screen, enter 'BACK'
    To exit the program, enter 'QUIT'
    Action: ''')
                if return_to_main_screen == 'BACK':
                    break
                elif return_to_main_screen =='QUIT':
                    exit()
                else:
                    continue
            break

        elif MAIN_ACTIONS == 'UPDATE':
            while True:

                update_options = input('''

        1) To update the To-Do list, enter 'TODO'
        2) To update the Event list, enter 'EVENT'

        3) To go back, enter 'BACK'

        Action: ''')

                if update_options == 'BACK':
                    break
                elif update_options == 'TODO':

                    while True:
                        print('''
    -------------------------
    Avaiable To-do to update.
    ''')

                        iteration_number = 1
                        Today_Todo = {}
                        for keys, details in To_do_MAIN.items():

                            if Day_of_the_week in details['Date'] or Today_Date_DV == details['Date'][1]:

                                Today_Todo[keys] = details

                                print('        {num}) {name} | To update this Todo, enter \'{name}\'.'.format(num=iteration_number,
                                name=keys))
                                iteration_number += 1

                        print('\n')

                        while True:
                            todo_to_update = input('''    -------------------------------------------
    Enter \'BACK\' to exit*
    Enter the To-Do you wish to update: ''')
                            if todo_to_update in Today_Todo:

                                if Today_Todo[todo_to_update]['Goal']['Type'] == 'YN':

                                    print('''
    -------------------------------------------
    The current status of this goal is {Status}
    '''.format(Status=Today_Todo[todo_to_update]['Goal']['Current Status']))
                                    while True:
                                        todo_status_update = input('''    Enter \'Y\' to change the status to \'Complete\'
    Enter \'N\' to cancel: ''')
                                        if todo_status_update == 'Y':
                                            To_do_MAIN[todo_to_update]['Goal']['Current Status'] = 'Completed'
                                            break
                                        elif todo_status_update == 'N':
                                            break



                                elif Today_Todo[todo_to_update]['Goal']['Type'] == 'NUM':

                                    print('''
    -------------------------------------------
    The current status of this goal is {Status}
    '''.format(Status=Today_Todo[todo_to_update]['Goal']['Current Status']))
                                    while True:
                                        todo_status_update = input('''    *To use the timer function, enter '0'

    Enter a numerical value for which the
    current status for this goal will be updated by: ''')
                                        try:
                                            todo_status_update = float(todo_status_update)

                                        except:
                                            print('''
    !!! Please enter numerical values only !!!
    ''')
                                            continue


                                        if todo_status_update == 0:
                                            while True:
                                                timer_options = input('''
    ----------------------------------------------------------
    Timer Elapse Option:

        1) To record your elapse time in seconds, enter 'S'
        2) To record your elapse time in minutes, enter 'M'
        3) TO record your elapse time in hours, enter 'H'

    Timer Option: ''')
                                                if timer_options == 'S':
                                                    timer_divider = 1
                                                    timer_metric = 'Seconds'
                                                elif timer_options == 'M':
                                                    timer_divider = 60
                                                    timer_metric = 'Minutes'
                                                elif timer_options == 'H':
                                                    timer_divider = 3600
                                                    timer_metric = 'Hours'
                                                break

                                            while True:
                                                timer_starter = input('''
    To cancel, enter 'BACK'
    Enter \'Start\' to start the timer: ''')
                                                if timer_starter == 'Start':
                                                    timer_elapse_start = time.time()
                                                    while True:
                                                        timer_end = input('    Enter \'End\' to end the timer: ')
                                                        if timer_end == 'End':
                                                            timer_elapse_end = time.time()

                                                            elapse_time = int(timer_elapse_end - timer_elapse_start)
                                                            elapse_time = elapse_time/timer_divider
                                                            print('''
    ==================================
    The time elapse is {time} {metric}
    '''.format(time=elapse_time, metric=timer_metric))
                                                            break
                                                        else:
                                                            continue
                                                    while True:
                                                        confirm_elapse_timer = input('    Enter, \'Y\' to confirm, \'N\' to cancel: ')
                                                        if confirm_elapse_timer == 'Y':
                                                            To_do_MAIN[todo_to_update]['Goal']['Current Status'] += elapse_time
                                                            break
                                                        elif confirm_elapse_timer == 'N':
                                                            break
                                                    break

                                                elif timer_start == 'BACK':
                                                    break

                                                timer_start = time.time()


                                        elif todo_to_update == 'BACK':
                                            break

                                        To_do_MAIN[todo_to_update]['Goal']['Current Status'] += todo_status_update
                                        print('''
    =========================================
    Your To-do, '{}' has been updated!
    =========================================
    '''.format(todo_to_update))
                                        break








                            elif todo_to_update == 'BACK' or todo_status_update == 'Y':
                                break

                            else:
                                print('    !!! Invalid TO-DO !!!')
                                continue

                        if todo_to_update == 'BACK':
                            break



        else:
            print('''
    !!! Invalid Action !!!''')
            continue




































def this_is_nothing():
    pass
