import datetime
import pytz

today = datetime.datetime.today()

while True:
    pytz_or_datetime = input('''
Enter \'PYTZ\' to access the PYTZ guide.
Enter \'DT\' to access the Datetime guide.
''')
    if pytz_or_datetime == 'PYTZ':

        dt = datetime.datetime(2020, 8, 23, 12, 30, 45, tzinfo = pytz.UTC)

        dt_now = datetime.datetime.now(tz = pytz.UTC)

        dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)

        dt_now_HCMC = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))

        #____________________________________________________________________

        #Our datetime function
        datetime_function = datetime.datetime.now()

        #Our PYTZ timezone
        timezone_for_HCMC = pytz.timezone('Asia/Ho_Chi_Minh')

        #Using .localize() to sync the 2 variables
        datetime_for_HCMC = timezone_for_HCMC.localize(datetime_function)

        #____________________________________________________________________

        US_EASTERN_TIME = datetime_for_HCMC.astimezone(pytz.timezone('US/Eastern'))
        US_EASTERN_TIME_type = type(US_EASTERN_TIME)

        #____________________________________________________________________

        format_example = US_EASTERN_TIME.strftime('%B %d, %Y')
        format_example_type = type(format_example)

        #____________________________________________________________________
        datetime_to_string = US_EASTERN_TIME.strftime('%B %d, %Y')
        back_to_datetime = datetime.datetime.strptime(datetime_to_string, '%B %d, %Y')
        back_to_datetime_type = type(back_to_datetime)


        print('''
        The module PYTZ does not add any new functions but rather give us
        access to a list of timezones and arguments that we can pass into
        our datetime functions.

        For example:

                1) 'datetime.datetime(2020, 8, 23, 12, 30, 45, tzinfo = pytz.UTC)' woud give us:

                    {dt}

                2) 'datetime.datetime.now(tz = pytz.UTC)' would give us:

                    {dt_now}

                3) 'datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)' would give us

                    {dt_utcnow}

        Using pytz.timezone() :

                1) To show the current time in HCMC, we would use:

                    'datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))'

                    or

                    'datetime.datetime.now(tz = pytz.timezone('Asia/Ho_Chi_Minh'))'

                    {hcmc_now}




        Using .localize() :

                datetime_function = datetime.datetime.now()

                *Remeber that now() allows us to give it an argument, the timezone*

                timezone_for_HCMC = pytz.timezone('Asia/Ho_Chi_Minh')

                datetime_for_HCMC = timezone_for_HCMC.localize(datetime_function)

                    *NOTICE the '.localize()'*
                    We use this function to sync our 2 variables and assign it into
                    datetime_for_HCMC

                Printing datetime_for_HCMC would give us:

                        {HCMC_now}

        Using .astimezone() :

                The function '.astimezone()' is used to change the timzeone
                of a datetime function that already has an assigned timezone.

                For example, using the 'datetime_for_HCMC' variable from before.
                This variable is currently ultizing a datetime function with the HCMC
                timezone assigned to it.

                To change it, we would need to create a new variable:

                    US_EASTERN_TIME = datetime_for_HCMC.astimezone(pytz.timezone('US/Eastern'))

                This would result in:

                    {US_east_time}

        Using .strftime() :

                .strftime() is a function that enable us to format our datetime in
                various ways.

                FOR EXAMPLE:

                    format_example = US_EASTERN_TIME.strftime('%B %d, %Y')

                    print(format_example)
                    print(type(format_example))

                    print(type(US_EASTERN_TIME))

                This would give us:

                    {format_example}
                    {format_example_type}

                    {US_EASTERN_TIME_type}


                You may be wondering why we specifically use '%B %d, %Y' within
                our .strftime() function. The .strftime() function can format our
                datetime in a variety of different ways by changing the placement of
                the the 3 parts that you see in  %B %d, %Y' as well as their capitalization.

                    %B indicate the month, with its name written out fully

                    %d indicate the day, written with a zero attached to the front of the number if
                    it has only 1 digit (ex: 0,1,2,3,4,....,9)

                    %Y indicate the year, written with zero(s) attached to the front of
                    the year of it's below 1000. (ex: 998 would be written as 0998, 12 would
                    be written as 0012, 2014, will be written as 2014, 1020 would be
                    written as 1020)

                    To learn more about these isoformat syntax, visit:

                        https://docs.python.org/3/library/datetime.html



                Notice how it also converts the the 'type' of the datetime from
                'datetime.datetime' to a 'string'. By converting it to a string, it
                is then much easier for us to work with it in our program.


        Using .strptime() :

                .strptime() is the opposite of .strftime() in that rather than converting
                a datetime to a string for string operations, it converts a datetime string
                back into a datetime so that we can conduct datetime operations on it.

                FOR EXAMPLE:

                    datetime_to_string = US_EASTERN_TIME.strftime('%B %d, %Y')

                    back_to_datetime = datetime.datetime.strptime(datetime_to_string, '%B %d, %Y')

                    print(datetime_to_string)

                    print(back_to_datetime)
                    print(type(back_to_datetime))

                In this example, we are creating a new variable, back_to_datetime, and setting
                it up like any other datetime functions with 'datetime.datetime'. We then attach
                our .strptime() function with 2 arguments: a string that represent a certain date,
                and the representation format of said string. This would give us:

                    {datetime_to_string}

                    {back_to_datetime}
                    {back_to_datetime_type}


        To print out all the timezones in PYTZ (keep in mind that the list
        extremely long):

                for tz in pytz.all_timezones:
                print(tz)

        We can narrow our search by continents as the timezones are formatted
        like following examples below:

                Africa/Accra
                Africa/Addis_Ababa
                America/Chicago
                America/Mexico_City
                Asia/Ho_Chi_Minh
                Asia/Hong_Kong
                Australia/Sydney
                Europe/Paris

                There are a few exceptions such as:

                UTC
                Universal
                W-SU
                WET
                Zulu
                GB
                GB-Eire
                GMT

        '''.format(dt=dt, dt_now=dt_now, dt_utcnow=dt_utcnow, hcmc_now=dt_now_HCMC,
        HCMC_now=datetime_for_HCMC, US_east_time= US_EASTERN_TIME,
        format_example=format_example, format_example_type=format_example_type,
        US_EASTERN_TIME_type=US_EASTERN_TIME_type, datetime_to_string=datetime_to_string,
        back_to_datetime=back_to_datetime, back_to_datetime_type=back_to_datetime_type))










    elif pytz_or_datetime == 'DT':
        print('''
=============================
DATETIME MODULE GUIDE
=============================
''')

        def datetime_date():
            print('__________________________________________________________')
            print('SECTION: datetime.date\n')
            # prints the current date (year - month - day)
            today = datetime.date.today()
            print('Today\'s date is (date): ', today)

            # prints the dateiime format for any particular day (year, month, day)
            Any_day = datetime.date(2021, 8, 23)
            print('My birthday is on (date)', Any_day)

            # when you take a date and minus it from another day, it will return a 'tdelta' which the time difference between
            # 2 date. By defalt, the 'tdelta' value will be incremented in 'day(s)'.
            till_2021_bday = Any_day - today
            print(till_2021_bday, 'until my birthday!')

            print('\n')

            # prints just the current day:
            print('Today\'s day:', today.day)

            # prints just the current month:
            print('Today\'s month:', today.month)

            # prints just the current year:
            print('Today\'s year:', today.year)
        datetime_date()

        def datetime_datetime():
            print('__________________________________________________________')
            print('SECTION: datetime.datetime\n')

            # prints the current date AND time
            today_DATE_AND_TIME = datetime.datetime.today()
            print('Today\'s date is (datetime): ', today_DATE_AND_TIME)

            # prints the datetime format for any particulat date (year, month, day, hour, minutes, seconds, microseconds)
            Any_day_DATE_AND_TIME = datetime.datetime(2021, 8, 23, 12, 34, 2, 10000)
            print('My birthday is on (datetime)', Any_day_DATE_AND_TIME)

            print('\n')

            print('Today\'s date is: (.date)', today_DATE_AND_TIME.date())
            print('Today\'s time is: (.time)', today_DATE_AND_TIME.time())

            print('\n')


            # today() = prints the datetime base on the current locol time and date

            today_today = datetime.datetime.today()
            print('datetime.datetime.today(): ', today_today)

            # now() = same as today() but it allows for an optional argument, a timezone

            today_now = datetime.datetime.now()
            print('datetime.datetime.now(): ', today_now)

            # utcnow() =  prints the datetime base on the current UTC timezone
            # UTC = World's Time Standard

            today_utcnow = datetime.datetime.utcnow()
            print('datetime.datetime.utcnow(): ', today_utcnow)
        datetime_datetime()

        def weekday_isoweekday():
            print('__________________________________________________________')
            print('SECTION: weekday() & isoweekday()\n')

            # prints the weekday, with monday being 0 and sunday being 6
            print('weekday():', today.weekday())
            print('''This number, {num} represent the day of the week, since monday
            is 0 with\'weekday()\', {num} would represent the {num_plus_one}th day of the week
            '''.format(num=today.weekday(), num_plus_one=today.isoweekday()))

            # prints the weekday, witbh
            print('isoweekday():', today.isoweekday())
            print('''This number, {num} represent the day of the week, since monday
            is 1 with \'isoweekday()\', {num} would represent the {num}th day of the week
            '''.format(num=today.isoweekday()))
        weekday_isoweekday()

        def T_DELTA():
            print('__________________________________________________________')
            print('SECTION: tdelta\n')

            # tdelta
            # date 1 +/- tdelta = date 2
            # date 1 - date 2 = tdelta

            seven_days_from_date = datetime.timedelta(days=7)

            seven_days_from_today = today + seven_days_from_date
            print('Today\'s date is: ', today.date(), '| 7 days from today will be:', seven_days_from_today.date())
        T_DELTA()

        def type_test():
            print('__________________________________________________________')
            print('SECTION: datetime types testing\n')

            print(type(today))
            print(type(today.weekday()))
        type_test()
