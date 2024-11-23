from tkinter import *
from set_nick import set_nick

root = Tk()
root.title("Чат")
root.maxsize(1000, 600)
root.minsize(1000,600)

frame_input_nick = Frame(root)

label=Label(frame_input_nick, text="Представьтесь, пожалуйста", font="Times 20")
label.pack(anchor=N)

nick_entry = Entry(frame_input_nick, font="Times 20")
nick_entry.pack(anchor=N)

set_nick_button = Button(frame_input_nick, text="Продолжить", font="Times 14", background="lime", command=lambda: set_nick(nick_entry.get()))
set_nick_button.pack(anchor=N)

frame_input_nick.place(x=400, y=150)

root.mainloop()