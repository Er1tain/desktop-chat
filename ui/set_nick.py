from tkinter import messagebox, Tk, Frame
from widgets.GroupChatFrame import GroupChatFrame

def set_nick(root: Tk, frame_input_nick: Frame, str_nick: str) -> None:
    if len(str_nick) == 0:
        messagebox.showerror(message="Ник обязателен!")
        return
    
    # Закрытие фрейма для ввода ника
    frame_input_nick.destroy()
    
    # Открытие общего чата
    group_chat_frame = GroupChatFrame(root)
    group_chat_frame.place(x=35, y=20)