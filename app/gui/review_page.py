import customtkinter as ctk

class ReviewPage(ctk.CTkFrame):
    def __init__(self, parent, media, logged_username, review_repository,
                 on_back, on_disconnect, display_stars):
        super().__init__(parent)

        self.parent = parent
        self.media = media
        self.logged_username = logged_username
        self.review_repository = review_repository
        self.on_back = on_back
        self.on_disconnect = on_disconnect
        self.display_stars = display_stars

        self.pack(fill="both", expand=True)

        self.create_page()

    def create_page(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 5))
        top_bar.grid_columnconfigure(0, weight=1)
        top_bar.grid_columnconfigure(1, weight=0)

        back_button = ctk.CTkButton(
            top_bar,
            text="← Back",
            command=self.on_back
        )
        back_button.grid(row=0, column=0, sticky="w")

        disconnect_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        disconnect_frame.grid(row=0, column=1, sticky="e")

        disconnect_label = ctk.CTkLabel(
            disconnect_frame,
            text="Disconnect",
            font=("Arial", 12)
        )
        disconnect_label.pack(side="left", padx=(0, 6))

        disconnect_button = ctk.CTkButton(
            disconnect_frame,
            text="⏻",
            width=38,
            height=38,
            corner_radius=8,
            fg_color="#b22222",
            hover_color="#8b0000",
            text_color="white",
            font=("Arial", 22, "bold"),
            command=self.on_disconnect
        )
        disconnect_button.pack(side="left")

        title_label = ctk.CTkLabel(
            self,
            text=f"Reviews for {self.media.title}\nby {self.get_creator_text(self.media)}",
            font=("Arial", 30, "bold")
        )
        title_label.grid(row=1, column=0, pady=(5, 10))

        reviews_frame = ctk.CTkScrollableFrame(
            self,
            width=1000,
            height=520,
            corner_radius=12
        )
        reviews_frame.grid(row=2, column=0, padx=40, pady=(10, 30), sticky="nsew")

        reviews = self.review_repository.get_reviews_by_media_id(self.media.id)

        if not reviews:
            empty_label = ctk.CTkLabel(
                reviews_frame,
                text="No reviews yet.",
                font=("Arial", 18)
            )
            empty_label.pack(pady=30)
        else:
            for review in reviews:
                self.add_review_card(reviews_frame, review)

        self.add_review_form(reviews_frame)

    def add_review_form(self, parent):
        form = ctk.CTkFrame(
            parent,
            corner_radius=12,
            border_width=1,
            fg_color=("#eeeeee", "#252525")
        )
        form.pack(fill="x", padx=14, pady=(25, 10))

        title = ctk.CTkLabel(
            form,
            text=f"Write a review as {self.logged_username}",
            font=("Arial", 20, "bold"),
            anchor="w"
        )
        title.pack(fill="x", padx=16, pady=(14, 8))

        self.review_textbox = ctk.CTkTextbox(form, height=100)
        self.review_textbox.pack(fill="x", padx=16, pady=8)

        score_frame = ctk.CTkFrame(
            form,
            fg_color="transparent"
        )
        score_frame.pack(fill="x", padx=16, pady=8)

        score_label = ctk.CTkLabel(
            score_frame,
            text="Score:",
            font=("Arial", 14, "bold")
        )
        score_label.pack(side="left", padx=(0,8))

        self.score_option = ctk.CTkOptionMenu(
            score_frame,
            values=[str(i) for i in range(1, 11)],
            width=90
        )
        self.score_option.set("10")
        self.score_option.pack(side="left")

        post_button = ctk.CTkButton(
            form,
            text="Add review",
            command=self.post_review
        )
        post_button.pack(anchor="w", padx=16, pady=(8, 14))

    def post_review(self):
        comment = self.review_textbox.get("1.0", "end").strip()
        score = int(self.score_option.get())

        if not comment:
            return

        already_exists= self.review_repository.user_has_reviewed_media(
            self.media.id,
            self.logged_username
        )

        if already_exists:
            self.show_replace_review_popup(score, comment)
            return

        self.save_new_review(score, comment)

    def show_replace_review_popup(self, score, comment):
        popup = ctk.CTkToplevel(self)
        popup.title("Replace review")
        popup.geometry("380x180")
        popup.resizable(False, False)
        popup.grab_set()

        message = ctk.CTkLabel(
            popup,
            text="You already reviewed this media.\nYour previous review will be replaced",
            font=("Arial", 15),
            justify="center"
        )

        message.pack(padx=20, pady=(30,20))

        button_frame = ctk.CTkFrame(
            popup,
            fg_color="transparent"
        )
        button_frame.pack(pady= 10)

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            width=100,
            fg_color="#555555",
            hover_color="#444444",
            command=popup.destroy
        )
        cancel_button.pack(side="left", padx=10)

        accept_button = ctk.CTkButton(
            button_frame,
            text="Accept",
            width=100,
            fg_color="#b22222",
            hover_color="#8b0000",
            command=lambda: self.confirm_replace_review(popup, score, comment)
        )
        accept_button.pack(side="left", padx=10)

    def confirm_replace_review(self, popup, score, comment):
        popup.destroy()
        self.save_new_review(score, comment)

    def save_new_review(self, score, comment):
        success = self.review_repository.add_review(
            media_id=self.media.id,
            username=self.logged_username,
            score=score,
            comment=comment
        )

        if success:
            self.refresh()

    def add_review_card(self, parent, review):
        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            border_width=1,
            border_color=("#c0c0c0", "#444444"),
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
        reviewer_label.pack(fill="x", padx=16, pady=(12, 2), anchor="w")

        rating_frame = ctk.CTkFrame(card, fg_color="transparent")
        rating_frame.pack(fill="x", padx=16, pady=(0, 8), anchor="w")

        self.display_stars(rating_frame, review.score)

        score_label = ctk.CTkLabel(
            rating_frame,
            text=(f"{review.score}/10"),
            font=("Arial", 13)
        )
        score_label.pack(side="left", padx=(8, 0))

        comment_label = ctk.CTkLabel(
            card,
            text=review.comment,
            font=("Arial", 15),
            anchor="w",
            justify="left",
            wraplength=950
        )
        comment_label.pack(fill="x", padx=16, pady=(0, 14), anchor="w")

        created_date = review.created_at.strftime("%d/%m/%y - %H:%M")

        date_text = f"Created: {created_date}"

        if review.updated_at != review.created_at:
            edited_date = review.updated_at.strftime("%d/%m/%y - %H:%M")
            date_text += f"\nEdited:  {edited_date}"

        date_label = ctk.CTkLabel(
            card,
            text=date_text,
            font=("Arial", 11),
            text_color=("gray40", "gray70"),
            anchor="w",
            justify="left"
        )

        date_label.pack(fill="x", padx=16, pady=(0, 12), anchor="w")

        if review.username == self.logged_username:
            edit_button = ctk.CTkButton(
                card,
                text="Edit",
                width=80,
                command=lambda: self.show_edit_review_form(card, review)
            )
            edit_button.pack(anchor="e", padx=16, pady=(0, 12))

    def show_edit_review_form(self, parent_card, review):
        edit_box = ctk.CTkTextbox(parent_card, height=80)
        edit_box.pack(fill="x", padx=16, pady=8)
        edit_box.insert("1.0", review.comment)

        bottom_frame = ctk.CTkFrame(
            parent_card,
            fg_color="transparent"
        )
        bottom_frame.pack(fill="x", padx=16, pady=(8,12))

        right_frame = ctk.CTkFrame(
            bottom_frame,
            fg_color="transparent"
        )
        right_frame.pack(side="right")

        score_label = ctk.CTkLabel(
            right_frame,
            text="Score:",
            font=("Arial", 14)
        )
        score_label.pack(
            side="left",
            padx=(0,12),
            pady=2
        )

        score_option = ctk.CTkOptionMenu(
            right_frame,
            values=[str(i) for i in range(1, 11)],
            width=90,
            height=32,
            anchor="center"
        )
        score_option.set(str(review.score))
        score_option.pack(side="left", padx=(0, 16))

        save_button = ctk.CTkButton(
            right_frame,
            text="Save",
            width=90,
            height=32,
            command=lambda: self.save_review_edit(
                review,
                score_option,
                edit_box
            )
        )
        save_button.pack(side="left")

    def save_review_edit(self, review, score_option, edit_box):
        new_comment = edit_box.get("1.0", "end").strip()
        new_score = int(score_option.get())

        if not new_comment:
            return

        success = self.review_repository.update_review(
            review_id=review.id,
            username=self.logged_username,
            score=new_score,
            comment=new_comment
        )

        if success:
            self.refresh()

    def refresh(self):
        self.destroy()

        ReviewPage(
            parent=self.parent,
            media=self.media,
            logged_username=self.logged_username,
            review_repository=self.review_repository,
            on_back=self.on_back,
            on_disconnect=self.on_disconnect,
            display_stars=self.display_stars
        )

    def get_creator_text(self, media):
        if hasattr(media, "author"):
            return media.author
        if hasattr(media, "director"):
            return media.director
        if hasattr(media, "creator"):
            return media.creator
        return "Unknown"
    """
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
    """