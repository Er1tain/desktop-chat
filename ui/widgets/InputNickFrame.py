from tkinter import Tk, Frame, Label, Entry, Button
from set_nick import set_nick

class InputNickFrame(Frame):
    instance = ""

    def __init__(self, window: Tk):
        # Одиночка
        try:
            if InputNickFrame.instance != "":
                raise Exception("Может быть только один фрейм ввода ника!")
        except Exception as e:
            print(e)

        InputNickFrame.instance = super().__init__(window)    
        # 

        self.label=Label(self, text="Представьтесь, пожалуйста", font="Times 20")
        self.label.pack(anchor="n")

        self.nick_entry = Entry(self, font="Times 20")
        self.nick_entry.pack(anchor="n")

        self.set_nick_button = Button(self, text="Продолжить", font="Times 14", background="lime", command=lambda: set_nick(window, self, self.nick_entry.get()))
        self.set_nick_button.pack(anchor="n")

    def place(self, x: float, y: float):
        super().place(x=x, y=y)


   
    
