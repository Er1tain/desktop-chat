from tkinter import messagebox, Tk

def set_nick(str_nick: str) -> None:
    if len(str_nick) == 0:
        messagebox.showerror(message="Ник обязателен!")
        return
    

    