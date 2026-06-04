from textwrap import fill

from PIL import Image
import customtkinter as ctk
from app.repositories.media_repository import MediaRepository
from app.repositories.review_repository import ReviewRepository


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

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

        self.display_stars(rating_frame, media.rating)

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

    def display_stars_small(self, parent, rating):

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

    def show_review_page(self, media):
        self.clear_window()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        back_button = ctk.CTkButton(
            self,
            text="← Back",
            command=self.show_main_page
        )
        back_button.grid(row=0, column=0, sticky="w", padx=20, pady=(15,5))

        title_label = ctk.CTkLabel(
            self,
            text=f"Reviews for {media.title}\nby {media.author}",
            font=("Arial", 28, "bold"),
        )
        title_label.grid(row=1, column=0, pady=(5,10))

        reviews_frame = ctk.CTkScrollableFrame(
            self,
            width=1000,
            height=520,
            corner_radius=12,
        )
        reviews_frame.grid(
            row=2,
            column=0,
            padx= 40,
            pady=(10,30),
            sticky="nsew"
        )

        reviews = self.review_repository.get_reviews_by_media_id(media.id)

        if not reviews:
            empty_label = ctk.CTkLabel(
                reviews_frame,
                text="No reviews yet.",
                font=("Arial", 18)
            )
            empty_label.pack(pady=30)
            return
        for review in reviews:
            self.add_review_card(reviews_frame, review)

    def add_review_card(self, parent, review):
        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            border_width=1,
            border_color=("#c0c0c0","#444444"),
            fg_color=("#e8e8e8", "#2b2b2b")
        )
        card.pack(fill="x", padx=14, pady=10)

        reviewer_label = ctk.CTkLabel(
            card,
            text=review.username,
            font=("Arial", 20, "bold"),
            anchor="w",
            justify="left"
        )
        reviewer_label.pack(fill="x", padx=16, pady=(12,2), anchor="w")

        created_date = review.created_at.strftime("%d/%m/%y")

        date_label = ctk.CTkLabel(
            card,
            text=f"Created: {created_date}",
            font=("Arial", 12),
            anchor="w",
            justify="left"
        )
        date_label.pack(fill="x", padx=16, pady=(0,6), anchor="w")

        rating_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )
        rating_frame.pack(fill="x", padx=16, pady=(0,8), anchor="w")

        self.display_stars_small(rating_frame, review.score)

        comment_label = ctk.CTkLabel(
            card,
            text=review.comment,
            font=("Arial", 15),
            anchor="w",
            justify="left",
            wraplength=950
        )
        comment_label.pack(fill="x", padx=16, pady=(0,14), anchor="w")
