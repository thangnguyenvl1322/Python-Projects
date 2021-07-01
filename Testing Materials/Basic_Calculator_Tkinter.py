from tkinter import *

root =Tk()

list_of_display_equation = []

# User Input:
user_entry = Entry(root, width=30, borderwidth=10)
user_entry.grid(row=0, column=0,columnspan=4)

# Functions:
def normal_press(num):
    current_value = user_entry.get()
    user_entry.delete(0, END)

    if num == '.':
        user_entry.insert(0, current_value + num)
    else:
        user_entry.insert(0, current_value + str(num))

def Clear():
    user_entry.delete(0, END)

def math_function(math_sign):
    global current_value
    global current_status
    global display_equation

    display_equation = user_entry.get()
    current_value = user_entry.get()
    user_entry.delete(0, END)

    if math_sign == '+':
        current_status = 'addition'
    elif math_sign == '-':
        current_status = 'subtraction'
    elif math_sign == '*':
        current_status = 'multiplication'
    elif math_sign == '/':
        current_status = 'division'

    display_equation = display_equation + math_sign
    print(display_equation)

def equal_function(list_of_display_equation):
    global display_equation


    value = user_entry.get()
    display_equation = display_equation + value + ' = '
    user_entry.delete(0, END)

    if current_status == 'addition':
        results = str( float(current_value) + float(value))
        user_entry.insert(0, results)


    elif current_status == 'multiplication':
        results = str( float(current_value) * float(value))
        user_entry.insert(0, results)

    elif current_status == 'subtraction':
        results = str( float(current_value) - float(value))
        user_entry.insert(0, results)

    elif current_status == 'division':
        results = str( float(current_value) / float(value))
        user_entry.insert(0, results)

    display_equation = display_equation + results
    list_of_display_equation.append(display_equation)

    row_num =1
    for equation in list_of_display_equation:

        History = Label(root, text=equation)
        History.grid(row=row_num, column=4)
        row_num+=1
        if row_num > 5:
            list_of_display_equation.remove(list_of_display_equation[0])

# Labels:
History_section = Label(root, text='History:', padx =50, borderwidth=5)

# Buttons:
button_add = Button(root, text='+', padx=20, pady=10, command=lambda:math_function('+'))
button_subtract = Button(root, text='-', padx=20, pady=10, command=lambda:math_function('-'))
button_multiply = Button(root, text='*', padx=20, pady=10, command=lambda:math_function('*'))
button_divide = Button(root, text='/', padx=20, pady=10, command=lambda:math_function('/'))
button_equal = Button(root, text='=', padx=20, pady=10, command=lambda:equal_function(list_of_display_equation))

button_0 = Button(root, text='0', padx=20, pady=10, command=lambda: normal_press(0))
button_dot = Button(root, text='.', padx=20, pady=10, command=lambda: normal_press('.'))

button_1 = Button(root, text='1', padx=20, pady=10, command=lambda: normal_press(1))
button_2 = Button(root, text='2', padx=20, pady=10, command=lambda: normal_press(2))
button_3 = Button(root, text='3', padx=20, pady=10, command=lambda: normal_press(3))

button_4 = Button(root, text='4', padx=20, pady=10, command=lambda: normal_press(4))
button_5 = Button(root, text='5', padx=20, pady=10, command=lambda: normal_press(5))
button_6 = Button(root, text='6', padx=20, pady=10, command=lambda: normal_press(6))

button_7 = Button(root, text='7', padx=20, pady=10, command=lambda: normal_press(7))
button_8 = Button(root, text='8', padx=20, pady=10, command=lambda: normal_press(8))
button_9 = Button(root, text='9', padx=20, pady=10, command=lambda: normal_press(9))

button_clear = Button(root, text='Clear', padx = 95, command=Clear)

# Grid:
button_add.grid(row=1, column=0)
button_subtract.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=1, column=3)
button_equal.grid(row=4, column=3)

button_0.grid(row=2, column=3)
button_dot.grid(row=3, column=3)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_clear.grid(row=5, column=0, columnspan=4)

History_section.grid(row=0, column=4)

root.mainloop()
