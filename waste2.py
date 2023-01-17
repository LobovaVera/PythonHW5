# # Import the required libraries
# from tkinter import *

# # Create an instance of tkinter frame or window
# win=Tk()

# # Set the size of the tkinter window
# win.geometry("700x350")

# def cal_sum():
#    t1=int(a.get())
#    t2=int(b.get())
#    sum=t1+t2
#    label.config(text=sum)
#    if t1<t2:
#     print("hi")

# # Create an Entry widget
# Label(win, text="Enter First Number", font=('Calibri 10')).pack()
# a=Entry(win, width=35)
# a.pack()
# Label(win, text="Enter Second Number", font=('Calibri 10')).pack()
# b=Entry(win, width=35)
# b.pack()

# label=Label(win, text="Total Sum : ", font=('Calibri 15'))
# label.pack(pady=20)

# Button(win, text="Calculate Sum", command=cal_sum).pack()

# win.mainloop()
# import tkinter as tk
# from tkinter import *

# win=tk.Tk()
# count = 1
# score_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# text = ''
# def score(a):
#     # score_list[n] = 1
#     # if count == 1:
#     #     text = 'O'
#     #     count = 2
#     # else:
#     #     text = 'X'
#     #     count = 1
#     # match n:
#     #     case 0:
#     global text
#     text += a 
#     btn1['text'] = f'{text}'

# btn1 = tk.Button(win, text =  f'{text}', command = lambda: score('1') )
# btn1.grid(row = 0, column = 0, stick='wens')

# win.mainloop()

from tkinter import *

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

t = Entry(root, textvariable = var)
t.pack()

root.mainloop()
# графическое оформление
# win = tk.Tk()
# photo = tk.PhotoImage(file = 'candy2.png')
# win.iconphoto(0, photo)
# win.config( bg = '#F5CAF2')
# win.title("Конфетки")
# win.geometry("500x500+100+100")
# win.resizable(0, 0)

# btn1 = tk.Button(win,
# f'{text}'= "Играем вдвоем",
# bg = "pink",
# font = ('Arial', 15, 'bold'),
# relief = tk.RAISED,
# bd = 10,
# command = two_players_mode
# )
# btn1.pack()

# btn2 = tk.Button(win,
# f'{text}'= "Игра против бота",
# bg = "pink",
# font = ('Arial', 15, 'bold'),
# relief = tk.RAISED,
# bd = 10,
# command = bot_mode)
# btn2.pack()

# win.mainloop()