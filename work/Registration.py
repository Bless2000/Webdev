from tkinter import *

window = Tk()

window.geometry('500x500')

Label(window, text = 'REGISTRATION', font = 'times' '25' 'bold').grid(row = 0, column = 3)

name = Label(window, text = 'Name', font = 'bold')
name.grid(row=2, column=2)

age = Label(window, text = 'Age', font = 'bold')
age.grid(row=3, column=2)

gender = Label(window, text = 'Gender', font = 'bold')
gender.grid(row=4, column=2)

course = Label(window, text = 'Course', font = 'bold')
course.grid(row= 5, column=2)

name_value = StringVar
age_value  = StringVar

name_entry = Entry(window, text = 'Name')
name_entry.grid(row= 2, column= 3)

age_entry = Entry(window, text = 'Age')
age_entry.grid(row = 3, column=3)

gender_box = Radiobutton(window, text= 'Male',  value= 'Male').grid(row = 4, column= 3)
gender_box.set(None)

gender_box1 = Radiobutton(window, text= 'Female', value= 'Female').grid(row = 4, column= 5)
gender_box1.set(None)

window.mainloop()
