from tkinter import Tk, Frame, Label, Entry, Button

class GroupChatFrame(Frame):
    instance = ""

    def __init__(self, window: Tk):
        # Одиночка
        try:
            if GroupChatFrame.instance != "":
                raise Exception("Может быть только один фрейм чата!")
        except Exception as e:
            print(e)

        GroupChatFrame.instance = super().__init__(window)    
        # 

        self.messages_frame = Frame(self, width=930, height=500, background='white')
        self.messages_frame.pack(anchor="n")
        
        self.text_field = Entry(self, width=115, font='Times 16')
        self.text_field.place(x=0, y=435)

        # Панель с кнопками под окном с чатом
        self.frame_btns = Frame(self, width=930, height=50)

        self.back_button = Button(self.frame_btns, text="Сменить ник")
        self.back_button.place(x=100, y=0)

        self.send_message_button = Button(self.frame_btns, text="Отправить")
        self.send_message_button.place(x=750, y=0)

        self.frame_btns.place(x=0, y=460)

    def place(self, x: float, y: float):
        super().place(x=x, y=y)    