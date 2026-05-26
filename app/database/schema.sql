DROP TABLE IF EXISTS source_link CASCADE;
DROP TABLE IF EXISTS review CASCADE;
DROP TABLE IF EXISTS media_genre CASCADE;
DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS movie CASCADE;
DROP TABLE IF EXISTS tv_show CASCADE;
DROP TABLE IF EXISTS media CASCADE;
DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS status CASCADE;
DROP TABLE IF EXISTS app_user CASCADE;


CREATE TABLE app_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE genre (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE media (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    release_year INTEGER,
    description TEXT,
    rating INTEGER CHECK (rating >= 0 AND rating <= 10),
    status_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_media_status
        FOREIGN KEY (status_id)
        REFERENCES status(id)
        ON DELETE RESTRICT
);


CREATE TABLE book (
    media_id INTEGER PRIMARY KEY,
    author VARCHAR(150),
    publisher VARCHAR(150),
    page_count INTEGER CHECK (page_count >= 0),
    isbn VARCHAR(30),

    CONSTRAINT fk_book_media
        FOREIGN KEY (media_id)
        REFERENCES media(id)
        ON DELETE CASCADE
);


CREATE TABLE movie (
    media_id INTEGER PRIMARY KEY,
    director VARCHAR(150),
    duration_minutes INTEGER CHECK (duration_minutes >= 0),

    CONSTRAINT fk_movie_media
        FOREIGN KEY (media_id)
        REFERENCES media(id)
        ON DELETE CASCADE
);


CREATE TABLE tv_show (
    media_id INTEGER PRIMARY KEY,
    creator VARCHAR(150),
    season_count INTEGER CHECK (season_count >= 0),
    episode_count INTEGER CHECK (episode_count >= 0),

    CONSTRAINT fk_tv_show_media
        FOREIGN KEY (media_id)
        REFERENCES media(id)
        ON DELETE CASCADE
);


CREATE TABLE media_genre (
    media_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,

    PRIMARY KEY (media_id, genre_id),

    CONSTRAINT fk_media_genre_media
        FOREIGN KEY (media_id)
        REFERENCES media(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_media_genre_genre
        FOREIGN KEY (genre_id)
        REFERENCES genre(id)
        ON DELETE CASCADE
);


CREATE TABLE review (
    id SERIAL PRIMARY KEY,
    media_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    score INTEGER CHECK (score >= 0 AND score <= 10),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_review_media
        FOREIGN KEY (media_id)
        REFERENCES media(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_review_user
        FOREIGN KEY (user_id)
        REFERENCES app_user(id)
        ON DELETE CASCADE
);


CREATE TABLE source_link (
    id SERIAL PRIMARY KEY,
    media_id INTEGER NOT NULL,
    platform_name VARCHAR(100) NOT NULL,
    url TEXT NOT NULL,
    availability_type VARCHAR(50),

    CONSTRAINT fk_source_link_media
        FOREIGN KEY (media_id)
        REFERENCES media(id)
        ON DELETE CASCADE
);


INSERT INTO status (name) VALUES
('Planned'),
('In Progress'),
('Completed'),
('Dropped'),
('On Hold');


INSERT INTO genre (name) VALUES
('Action'),
('Adventure'),
('Comedy'),
('Drama'),
('Fantasy'),
('Horror'),
('Romance'),
('Science Fiction'),
('Thriller'),
('Documentary');