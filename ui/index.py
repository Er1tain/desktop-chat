from tkinter import *
from widgets.InputNickFrame import InputNickFrame

root = Tk()
root.title("Чат")
root.maxsize(1000, 600)
root.minsize(1000,600)

frame_input_nick = InputNickFrame(root)
frame_input_nick.place(x=400, y=150)

root.mainloop()