from tkinter import *

root = Tk()
#----------------------------------------------------------------------------------------------------------------
# LABELS:

Label_labels = Label(root, text='Label Sections')
Button_labels = Label(root, text='Button Sections:')
UserInputs_labels = Label(root, text='User Input Section')

Testing_Label1 = Label(root, text='Testing Label 1')
text_color_label = Label(root, text='The text color is changed', fg='blue')
background_color_label = Label(root, text ='The background color is changed', bg='red')
Columnspans_label =Label(root, text='-------------------------------This label will span across 3 columns-------------------------------')


Button_labels.grid(row=0, column=1)
Label_labels.grid(row=0, column=0)
UserInputs_labels.grid(row=0, column=2)

Testing_Label1.grid(row=1,column=0)
text_color_label.grid(row=2, column=0)
background_color_label.grid(row=3, column=0)
Columnspans_label.grid(row=12, column=0, columnspan=3)

#----------------------------------------------------------------------------------------------------------------
# Creating button functions:

def Print_text_function():
    label = Label(root, text='This is printed!')
    label.grid(row=6, column=1)

def Print_user_input():
    label = Label(root, text=User_input.get())
    label.grid(row=8,column=1)
#----------------------------------------------------------------------------------------------------------------
# BUTTONS:

Button_testing = Button(root, text='Click me!')
Disabled_button = Button(root, text='This button is dead', state=DISABLED)
Long_button = Button(root, text='This button\'s \'pad\' is adjusted', padx=50)
Tall_button = Button(root, text='This button\'s \'pady\' is adjusted', pady=50)
Printing_button = Button(root, text='This button will print something', command=Print_text_function)

Print_User_User_input = Button(root, text='This will print inputs of the first user entry!', command=Print_user_input)
Print_User_User_input.grid(row=7, column=1)

Button_testing.grid(row=1, column=1)
Disabled_button.grid(row=2, column=1)
Long_button.grid(row=3, column=1)
Tall_button.grid(row=4, column=1)
Printing_button.grid(row=5,column=1)



#----------------------------------------------------------------------------------------------------------------
# USER INPUTS:

User_input = Entry(root)
Bordered_User_input = Entry(root, borderwidth=10)
Long_User_input = Entry(root, width=50)

Worded_user_input = Entry(root, width=50)
Worded_user_input.insert(0,'Enter your name here:')

User_input.grid(row=1, column=2)
Bordered_User_input.grid(row=2,column=2)
Long_User_input.grid(row=3,column=2)
Worded_user_input.grid(row=4,column=2)



root.mainloop()
