from tkinter import messagebox, Tk, Frame

def set_nick(root: Tk, frame_input_nick: Frame, str_nick: str) -> None:
    if len(str_nick) == 0:
        messagebox.showerror(message="Ник обязателен!")
        return
    
    # Закрытие фрейма для ввода ника
    frame_input_nick.destroy()
    