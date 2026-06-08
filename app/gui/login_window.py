import customtkinter as ctk
from app.gui.main_window import MainWindow
from app.repositories.user_repository import UserRepository


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.user_repository = UserRepository()

        self.title("Login")
        self.geometry("400x300")
        self.resizable(width=False, height=False)

        self.create_widgets()

        self.bind("<Return>", self.login)

    def create_widgets(self):
        title = ctk.CTkLabel(
           self,
            text="Media Tracker",
            font=("Arial", 28, "bold"),
        )
        title.pack(pady=(30,30))

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Username",
            width=260
        )
        self.username_entry.pack(pady=8)

        self.password_entry = ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*",
            width=260
        )
        self.password_entry.pack(pady=(8,2))

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#ff4d4d",
            font=("Arial", 12),
        )
        self.error_label.pack(pady=(0,2))

        login_button = ctk.CTkButton(
            self,
            text="Login",
            width=260,
            command=self.login
        )
        login_button.pack(pady=(6,8))

        create_account = ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Arial", 13, "underline"),
            cursor="hand2"
        )
        create_account.pack(pady=5)

        create_account.bind("<Button-1>", self.create_account_clicked)

    def login(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.user_repository.verify_login(
            username,
            password
        )

        if user is None:
            self.error_label.configure(
                text="Incorrect Username or Password"
            )
            return

        self.error_label.configure(text="")
        self.withdraw()

        self.username_entry.bind(
            "<Key>",
            lambda event: self.error_label.configure(text="")
        )
        self.password_entry.bind(
            "<Key>",
            lambda event: self.error_label.configure(text="")
        )

        self.main_window = MainWindow(username=username, login_window=self)
        self.main_window.protocol(
            "WM_DELETE_WINDOW",
            self.close_app
        )

    def create_account_clicked(self, event):
        print("Create Account under construction")

    def close_app(self):
        self.main_window.destroy()
        self.destroy()
