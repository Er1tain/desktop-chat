from tkinter import *
from set_nick import set_nick

root = Tk()
root.title("Чат")
root.maxsize(1000, 600)
root.minsize(1000,600)


label=Label(text="Представьтесь, пожалуйста", font="Times 20")
label.place(x=400, y=230)

nick_entry = Entry(font="Times 20")
nick_entry.place(x=400, y=260)

set_nick_button = Button(text="Продолжить", font="Times 14", background="lime", command=lambda: set_nick(nick_entry.get()))
set_nick_button.place(x=470, y=300)
root.mainloop()