#import module
from tkinter import *

def generate_email():
    first_name = first_name_tf.get()
    last_name = last_name_tf.get()
    company_name = company_name_tf.get()

    disp_tf.insert(0,f'{first_name}{last_name}@{company_name}.com')

#create root window    
root = Tk()

#title and window dimensions
root.title('PythonGuides')
root.geometry('360x300')
root.config(bg='black')

header = Label(root, text ='E-Mail Generator', bg='cyan', fg='blue', height = 1, width = 24)
header.config(font =("times new roman", 24))
header.place(relx = 0.5, y=50, anchor = CENTER)

my_name = Label(root, text ='- Abhinav B', bg='cyan', fg='blue', height = 1, width = 24)
my_name.config(font =("times new roman", 8))
my_name.place(x=220, y=240)

#entries
first_name_tf = Entry(root)
last_name_tf = Entry(root)
company_name_tf = Entry(root)

#labels
first_name_lbl = Label(
    root,
    text='First Name',
    bg='black',
    fg='white')

last_name_lbl = Label(
    root,
    text='Last Name',
    bg='black',
    fg='white')

company_name_lbl = Label(
    root,
    text='Company Name',
    bg='black',
    fg='white')

#labels placement
first_name_lbl.place(x=10, y=100)
first_name_tf.place(x=200, y=100)
last_name_lbl.place(x=10, y=120)
last_name_tf.place(x=200, y=120)
company_name_lbl.place(x=10, y=140)
company_name_tf.place(x=200, y=140)

#button
btn = Button(
    root,
    text='Generate Email',
    relief=SOLID,
    command=generate_email
)
btn.place(relx = 0.5, y = 180, anchor = CENTER)

#output display
disp_tf = Entry(
    root,
    width=30,
    font=('Arial', 14)
    )

disp_tf.place(relx = 0.5, y = 220, anchor = CENTER)

root.mainloop()
