import re

file_name = input('Insert a file for analysis: ')
file_access = open(file_name)

dict1 = dict()
num_value = list()
count = 0
dict1['Certain'] = 0
dict1['Unlikely'] = 0
dict1['Can Not Be Determined'] = 0

for x in file_access:

    text_find = re.findall('^Results.*Status:_(.*)', x)
    for x2 in text_find:
        if x2 == 'Certain':
            dict1['Certain'] = dict1['Certain'] + 1
        elif x2 == 'Unlikely':
            dict1['Unlikely'] = dict1['Unlikely'] + 1
        elif x2 == 'Can_not_be_determined':
            dict1['Can Not Be Determined'] = dict1['Can Not Be Determined'] + 1

    number_find = re.findall('^Results.*score: (\S+?.\S+?)', x)
    if len(number_find) < 1: continue
    print(number_find)
    for x3 in number_find:
        actualNUM = float(x3)
        num_value.append(actualNUM)
        count = count + 1

print('Score avg: ', sum(num_value)/count)

print('Text Results: ',dict1)
