import customtkinter as ctk

class MediaListPage(ctk.CTkFrame):
    def __init__(self, parent, media_repository, on_back):
        super().__init__(parent)

        self.parent = parent
        self.media_repository = media_repository
        self.on_back = on_back

        self.all_media = self.media_repository.get_all_media()

        self.show_books = ctk.BooleanVar(value=True)
        self.show_movies = ctk.BooleanVar(value=True)
        self.show_tv_shows = ctk.BooleanVar(value=True)

        self.pack(fill="both", expand=True)

        self.create_page()

    def create_page(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        top_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=15)

        back_button = ctk.CTkButton(
            top_bar,
            text="← Back",
            command=self.on_back
        )
        back_button.pack(side="left")

        title = ctk.CTkLabel(
            self,
            text="All Medias",
            font=("Arial", 32, "bold")
        )
        title.grid(row=1, column=0, pady=(5, 15))

        filters_frame = ctk.CTkFrame(self, fg_color="transparent")
        filters_frame.grid(row=2, column=0, sticky="nw", padx=30, pady=(0, 10))

        books_checkbox = ctk.CTkCheckBox(
            filters_frame,
            text="Books",
            variable=self.show_books,
            command=self.refresh_list
        )
        books_checkbox.pack(side="left", padx=10)

        movies_checkbox = ctk.CTkCheckBox(
            filters_frame,
            text="Movies",
            variable=self.show_movies,
            command=self.refresh_list
        )
        movies_checkbox.pack(side="left", padx=10)

        tv_checkbox = ctk.CTkCheckBox(
            filters_frame,
            text="TV Shows",
            variable=self.show_tv_shows,
            command=self.refresh_list
        )
        tv_checkbox.pack(side="left", padx=10)

        self.list_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=12
        )
        self.list_frame.grid(row=3, column=0, sticky="nsew", padx=30, pady=(0, 30))

        self.grid_rowconfigure(3, weight=1)

        self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        filtered_media = []

        for media in self.all_media:
            media_type = media.get_type()

            if media_type == "BOOK" and self.show_books.get():
                filtered_media.append(media)

            elif media_type == "MOVIE" and self.show_movies.get():
                filtered_media.append(media)

            elif media_type == "TV_SHOW" and self.show_tv_shows.get():
                filtered_media.append(media)

        filtered_media.sort(key=lambda media: media.title.lower())

        if not filtered_media:
            empty_label = ctk.CTkLabel(
                self.list_frame,
                text="No Media Selected",
                font=("Arial", 16)
            )
            empty_label.pack(pady=30)
            return
        for media in filtered_media:
            self.add_media_row(media)

    def add_media_row(self, media):

        TYPE_LABELS = {
            "BOOK": "Book",
            "MOVIE": "Movie",
            "TV_SHOW": "TV Show"
        }

        COLUMN_WIDTHS = {
            "title": 320,
            "creator": 240,
            "type": 100,
            "genres": 360
        }

        row = ctk.CTkFrame(
            self.list_frame,
            corner_radius=8,
            border_width=1,
            fg_color=("#eeeeee", "#2b2b2b")
        )
        row.pack(fill="x", padx=10, pady=6)

        row.grid_columnconfigure(0, weight= 4)
        row.grid_columnconfigure(1, weight= 3)
        row.grid_columnconfigure(2, weight= 2)
        row.grid_columnconfigure(3, weight= 3)

        creator = self.get_creator_text(media)

        media_type = media.get_type()

        display_type = TYPE_LABELS.get(media_type, media_type)

        genres = ", ".join(media.genres) if media.genres else "No genre"

        title_label = ctk.CTkLabel(
            row,
            text=self.shorten_text(media.title, 38),
            width=COLUMN_WIDTHS["title"],
            anchor="w",
            font=("Arial", 14, "bold")
        )
        title_label.grid(row=0, column=0, sticky="w", padx=12, pady=10)

        creator_label = ctk.CTkLabel(
            row,
            text=self.shorten_text(creator, 28),
            width=COLUMN_WIDTHS["creator"],
            anchor="w",
            font=("Arial", 14)
        )
        creator_label.grid(row=0, column=1, sticky="w", padx=12)

        type_label = ctk.CTkLabel(
            row,
            text=display_type,
            width=COLUMN_WIDTHS["type"],
            anchor="w",
            font=("Arial", 14)
        )
        type_label.grid(row=0, column=2, sticky="w", padx=12)

        genre_label = ctk.CTkLabel(
            row,
            text=self.shorten_text(genres, 45),
            width=COLUMN_WIDTHS["genres"],
            anchor="w",
            font=("Arial", 14)
        )
        genre_label.grid(row=0, column=3, sticky="w", padx=(8, 12))

    def shorten_text(self, text, max_length):
        if text is None:
            return ""
        return text if len(text) <= max_length else text[:max_length -3] + "..."

    def get_creator_text(self, media):
        if hasattr(media, "author"):
            return media.author
        if hasattr(media, "director"):
            return media.director
        if hasattr(media, "creator"):
            return media.creator

        return "Unknown"
