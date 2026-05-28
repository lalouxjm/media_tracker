from PIL import Image
import customtkinter as ctk
from app.repositories.media_repository import MediaRepository


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Media Tracker")
        self.geometry("1300x700")

        self.media_repository = MediaRepository()

        #Stars
        self.full_star = ctk.CTkImage(Image.open("assets/full_star.png"), size=(18, 18))
        self.half_star = ctk.CTkImage(Image.open("assets/half_star.png"), size=(18, 18))
        self.empty_star = ctk.CTkImage(Image.open("assets/empty_star.png"),size=(18, 18))

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_main_title()
        self.create_titles()
        self.create_columns()
        self.load_media()

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
        self.books_frame = ctk.CTkScrollableFrame(self)
        self.movies_frame = ctk.CTkScrollableFrame(self)
        self.tv_shows_frame = ctk.CTkScrollableFrame(self)

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
        card = ctk.CTkFrame(parent)
        card.pack(fill="x", padx=8, pady=6)

        title_label = ctk.CTkLabel(
            card,
            text=f"{media.title} \nby {creator_label}",
            font=("Arial", 15, "bold"),
            anchor="w",
            justify="left"
        )
        title_label.pack(fill="x", padx=10, pady=(10, 4), anchor="w")

        rating_frame = ctk.CTkFrame(card, fg_color="transparent")
        rating_frame.pack(fill="x", padx=10, pady=2)

        self.display_stars(rating_frame, media.rating)

        rating_text = ctk.CTkLabel(
            rating_frame,
            text=f" {media.rating}/10"
        )
        rating_text.pack(side="left", padx=5)

        genre_text = ", ".join(media.genres) if media.genres else "No genre"

        genre_label = ctk.CTkLabel(
            card,
            text=f"Genre: {genre_text}",
            anchor="w"
        )
        genre_label.pack(fill="x", padx=10, pady=2)

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

    def display_stars(self, parent, rating):
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
"""
    def display_stars(self, parent, rating):

        full_stars = rating // 2
        half_star = rating % 2

        stars = "★" * full_stars

        if half_star:
            stars += "½"

        empty_stars = 5 - full_stars - half_star

        stars += "☆" * empty_stars

        label = ctk.CTkLabel(
            parent,
            text=f"{stars}",  #({rating}/10)",
            font=("Arial", 14)
        )

        label.pack(side="left")
"""