# """GUI  -> grafik foydalanuvchi interfeysi"""
# from tkinter import *
# m=Tk()
# """ vidjetlarni bu yerda"""
#
# m.mainloop()

# """GUI -> grafik foydalanuvchi interfeysi"""
# #  1- misol
# from tkinter import *
# m = Tk()  # bu biz yaratgan oyna
#
# # label yaratish
# meningLabelim = Label(m, text="Assalomu alaykum")
#
# # oynaga joylash
# meningLabelim.pack()
# m.mainloop()  # oynani ushlab turish

# """GUI -> grafik foydalanuvchi interfeysi"""
# #  2- misol Button
# from tkinter import *
# asosiyoyna = Tk()
# # oyna o\lchamini belgilash uchun
# asosiyoyna.geometry('600x400')
# # tugma qo'shish Button(oyna, text="math", bd="qalinligi", command="tugma boshlangandagi hodisa"
# tugma=Button(asosiyoyna, text="Yopish", bd="10", command=asosiyoyna.destroy)
# # buttonni oynaga joylash
# tugma.pack()
# asosiyoyna.mainloop()

# 3-misol Button turlari
# radio button
# from tkinter import *
# # asosiy oynani yasash
# asosiyoyna = Tk()
# # o'lcham berish
# asosiyoyna.geometry('400x400')
# v=StringVar(asosiyoyna, '1')
# qiymatlar={
#     'Radiobutton 1': "1",
#     'Radiobutton 2': "2",
#     'Radiobutton 3': "3",
#     'Radiobutton 4': "4",
#     'Radiobutton 5': "5"
# }
#
# for(matn, qiymat) in qiymatlar.items():
#     # Radiobutton qurish
#     tugma=Radiobutton(
#         asosiyoyna,
#         text=matn,
#         variable=v,
#         value=qiymat,
#         indicator=0,
#         background="light blue"
#     )
#     tugma.pack(fill=X, ipady=10)
# # oynani ushlab turish
# asosiyoyna.mainloop()

# # 4-misol
# # radio button
# from tkinter import *
# # asosiy oynani yasash
# asosiyoyna = Tk()
# # o'lcham berish
# asosiyoyna.geometry('400x400')
# v=StringVar(asosiyoyna, '1')
# qiymatlar={
#     'Erkak 1': "1",
#     'Ayol 2': "2"
#
# }
#
# for(matn, qiymat) in qiymatlar.items():
#     # Radiobutton qurish
#     tugma=Radiobutton(
#         asosiyoyna,
#         text=matn,
#         variable=v,
#         value=qiymat,
#         indicator=0,
#         background="light blue"
#     )
#     tugma.pack(fill=X, ipady=10)
# # oynani ushlab turish
# asosiyoyna.mainloop()

# # 5-misol
# # radio button
# from tkinter import *
# # asosiy oynani yasash
# asosiyoyna = Tk()
# # o'lcham berish
# asosiyoyna.geometry('400x400')
# v=StringVar(asosiyoyna, '1')
# qiymatlar={
#     'Radiobutton 1': "1",
#     'Radiobutton 2': "2",
#     'Radiobutton 3': "3",
#     'Radiobutton 4': "4",
#     'Radiobutton 5': "5"
# }
#
# for(matn, qiymat) in qiymatlar.items():
#     # Radiobutton qurish
#     tugma=Radiobutton(
#         asosiyoyna,
#         text=matn,
#         variable=v,
#         value=qiymat,
#         background="light blue"
#     )
#     tugma.pack(side=TOP, ipady=5)
# # oynani ushlab turish
# asosiyoyna.mainloop()

# # 6-misol checkBox
# from tkinter import *
# # oynani qurish
# asosiy_oyna=Tk()
# # o'lcham berish
# asosiy_oyna.geometry('400x400')
# # Label qurish
# w=Label(asosiy_oyna, text="Checbox lar", font="50", bg="red")
# # Labelni joylash
# w.pack()
# # checboxlarni int qiymat qabul qiladigan qilib e'lon qilish
# Checkbutton1=IntVar()
# Checkbutton2=IntVar()
# Checkbutton3=IntVar()
# button1=Checkbutton(asosiy_oyna, text="qora",
#                     variable=IntVar(),
#                     onvalue=1,
#                     offvalue=0,
#                     height=5,
#                     width=10)
# button2=Checkbutton(asosiy_oyna, text="yashil",
#                     variable=IntVar(),
#                     onvalue=1,
#                     offvalue=0,
#                     height=5,
#                     width=10)
# button3=Checkbutton(asosiy_oyna, text="Ko'k",
#                     variable=IntVar(),
#                     onvalue=1,
#                     offvalue=0,
#                     height=5,
#                     width=10)
# button1.pack()
# button2.pack()
# button3.pack()
# asosiy_oyna.mainloop()

# # 7-misol. Canvas
# # oddiy shakl yaratish
# from tkinter import *
# asosiy_oyna=Tk()
# # canvas yaratish
# C=Canvas(asosiy_oyna,
#          bg="yellow",
#          height=500,
#          width=800
# )
# # To'g'ri chiziq
# chiziq=C.create_line(100,120,320,40, fill="green", width=3)
# # aylana yaratish
# aylana=C.create_arc(180,150,80,210, start=0, extent=358)
# # burchak yaratish
# burchak=C.create_arc(280,250,180,310, start=0, extent=180, fill="red")
# # Oval yaratish
# oval=C.create_oval(80,30,140,150, fill="blue")
# C.pack()
# asosiy_oyna.mainloop()

# # 8-misol. Chizadigan ilova Canvas yordamida
# from tkinter import *
# asosiy_oyna=Tk()
# # Sarlavha
# asosiy_oyna.title(" Paint ilovasi ")
# # asosiy oynani o'lchami
# asosiy_oyna.geometry('500x350')
# def display(event):
#     x1, y1, x2, y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)
# #     rang berish
#     Colour="#000fff000"
# #     chiziq yaratish
#     doska.create_line(x1,y1,x2,y2, fill=Colour)
# doska=Canvas(asosiy_oyna, width="400", height="250")
# doska.bind('<B1-Motion>', display())
# asosiy_oyna.mainloop()

# kalkulyator
# Python program to create a simple GUI
# calculator using Tkinter

# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()