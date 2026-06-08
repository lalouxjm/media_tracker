from PIL import Image
import customtkinter as ctk

from app.repositories.media_repository import MediaRepository
from app.repositories.review_repository import ReviewRepository
from app.gui.review_page import ReviewPage


class MainWindow(ctk.CTkToplevel):

    def __init__(self, username, login_window):
        super().__init__()

        self.logged_username = username
        self.login_window = login_window

        self.title("Media Tracker")
        self.geometry("1300x700")

        self.media_repository = MediaRepository()
        self.review_repository = ReviewRepository()

        #Stars
        self.full_star = ctk.CTkImage(Image.open("assets/full_star.png"), size=(18, 18))
        self.half_star = ctk.CTkImage(Image.open("assets/half_star.png"), size=(18, 18))
        self.empty_star = ctk.CTkImage(Image.open("assets/empty_star.png"),size=(18, 18))

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.show_main_page()
        self.create_disconnect_button()

    def create_main_title(self):
        title_label = ctk.CTkLabel(
            self,
            text="Media Tracker",
            font=("Arial", 34, "bold")
        )
        title_label.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(20,10)
        )

    def create_titles(self):
        titles = ["Books", "Movies", "TV Shows"]

        for index, title in enumerate(titles):
            label = ctk.CTkLabel(
                self,
                text=title,
                font=("Arial", 24, "bold")
            )
            label.grid(row=1, column=index, padx=10, pady=10)

    def create_columns(self):
        self.books_frame = ctk.CTkScrollableFrame(self, fg_color="#1f1f1f")
        self.movies_frame = ctk.CTkScrollableFrame(self, fg_color="#1f1f1f")
        self.tv_shows_frame = ctk.CTkScrollableFrame(self, fg_color="#1f1f1f")

        self.books_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.movies_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.tv_shows_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    def load_media(self):
        books = self.media_repository.get_all_books()
        movies = self.media_repository.get_all_movies()
        tv_shows = self.media_repository.get_all_tv_shows()

        for book in books:
            self.add_media_card(self.books_frame, book, book.author)

        for movie in movies:
            self.add_media_card(self.movies_frame, movie, movie.director)

        for tv_show in tv_shows:
            self.add_media_card(self.tv_shows_frame, tv_show, tv_show.creator)

    def add_media_card(self, parent, media, creator_label):

        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            border_width=1,
            border_color=("#3a3a3a", "#555555"),
            fg_color=("#e8e8e8","#2b2b2b"),
        )

        card.pack(fill="x", padx=8, pady=6)

        card.bind(
            "<Button-1>",
            lambda event: self.show_review_page(media)
        )

        title_label = ctk.CTkLabel(
            card,
            text=f"{media.title} \nby {creator_label}",
            font=("Arial", 15, "bold"),
            anchor="w",
            justify="left"
        )
        title_label.pack(fill="x", padx=12, pady=(12, 4), anchor="w")

        title_label.bind(
            "<Button-1>",
            lambda event: self.show_review_page(media)
        )

        rating_frame = ctk.CTkFrame(card, fg_color="transparent")
        rating_frame.pack(fill="x", padx=10, pady=2)

        rating_frame.bind(
            "<Button-1>",
            lambda event: self.show_review_page(media)
        )

        self.display_stars(rating_frame, media.rating, media)

        rating_text = ctk.CTkLabel(
            rating_frame,
            text=f" {media.rating}/10"
        )
        rating_text.pack(side="left", padx=5)

        rating_text.bind(
            "<Button-1>",
            lambda event: self.show_review_page(media)
        )

        genre_text = ", ".join(media.genres) if media.genres else "No genre"

        genre_label = ctk.CTkLabel(
            card,
            text=f"Genre: {genre_text}",
            anchor="w"
        )
        genre_label.pack(fill="x", padx=10, pady=2)

        genre_label.bind(
            "<Button-1>",
            lambda event: self.show_review_page(media)
        )

        source_text = ", ".join(
            media.source_link) if media.source_link else "No source"

        source_label = ctk.CTkLabel(
            card,
            text=f"Available at: {source_text}",
            anchor="w",
            wraplength=300,
            justify="left"
        )
        source_label.pack(fill="x", padx=10, pady=(2, 10))

        source_label.bind(
            "<Button-1>",
            lambda event: self.show_review_page(media)
        )

    def create_disconnect_button(self):
        self.disconnect_container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.disconnect_container.place(relx=0.985, rely=0.025, anchor="ne")

        label = ctk.CTkLabel(
            self.disconnect_container,
            text="Disconnect",
            font=("Arial", 12)
        )
        label.pack(side="left", padx=(0,6))

        button = ctk.CTkButton(
            self.disconnect_container,
            text="⏻",
            width=38,
            height=38,
            corner_radius=8,
            fg_color="#b22222",
            hover_color="#8b0000",
            text_color="white",
            font=("Arial", 22, "bold"),
            command=self.disconnect
        )
        button.pack(side="left")

    def disconnect(self):
        self.destroy()
        self.login_window.deiconify()

        self.login_window.username_entry.delete(0, "end")
        self.login_window.password_entry.delete(0, "end")

    def display_stars(self, parent, rating, media):
        full_stars = rating // 2
        has_half_star = rating % 2 == 1
        empty_stars = 5 - full_stars - (1 if has_half_star else 0)

        for _ in range(full_stars):
            label = ctk.CTkLabel(parent, image=self.full_star, text="")
            label.pack(side="left")

        if has_half_star:
            label = ctk.CTkLabel(parent, image=self.half_star, text="")
            label.pack(side="left")

        for _ in range(empty_stars):
            label = ctk.CTkLabel(parent, image=self.empty_star, text="")
            label.pack(side="left")


    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_main_page(self):
        self.clear_window()
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_main_title()
        self.create_titles()
        self.create_columns()
        self.load_media()

        self.create_disconnect_button()

    def show_review_page(self, media):
        self.clear_window()

        ReviewPage(
            parent=self,
            media=media,
            logged_username=self.logged_username,
            review_repository=self.review_repository,
            on_back=self.show_main_page,
            on_disconnect=self.disconnect
        )