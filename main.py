import customtkinter as ctk

from app.gui.login_window import LoginWindow
from app.database.connection import DatabaseConnection



#Turn the string blue
def blue(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;34m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string purple
def purple(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;35m{value}{value2}{value3}{value4}{value5}\033[0m"
#Separator
def sep():
    print(purple("+" * 40, "=" * 50, "+" * 40),sep='')



sep()

connection = DatabaseConnection.get_connection()
print("Connected successfully!")

sep()



sep()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = LoginWindow()
app.mainloop()