from tkinter import *


def convert():
    gram_value=float(el_variable.get())*1000
    pound_value=float(el_variable.get())*2.20462
    ounce_value=float(el_variable.get())*35.274
    text1.insert(END, pound_value)
    text2.insert(END,ounce_value)
    text3.insert(END,gram_value)



window = Tk()

b1 = Button(window, text='Convert', command=convert)
b1.grid({'row': 0, 'column': 1})

label1 = Label(window, text="Value in Kilograms")
label1.grid({'row': 0, 'column': 0})

el_variable = StringVar()
e1 = Entry(window,textvariable=el_variable)
e1.grid({'row': 0, 'column': 2})

label2 = Label(window, text="Value in pounds")
label2.grid({'row': 1, 'column': 0})
text1=Text(window, height=1, width=20)
text1.grid({'row': 2, 'column': 0})

label3 = Label(window, text="Value in ounces")
label3.grid({'row': 1, 'column': 1})
text2=Text(window, height=1, width=20)
text2.grid({'row': 2, 'column': 1})

label4 = Label(window, text="Value in grams")
label4.grid({'row': 1, 'column': 2})
text3=Text(window, height=1, width=20)
text3.grid({'row': 2, 'column': 2})

window.mainloop()