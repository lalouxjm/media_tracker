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


INSERT INTO genre (name)
VALUES
('Action'),
('Adventure'),
('Animation'),
('Biography'),
('Comedy'),
('Crime'),
('Documentary'),
('Drama'),
('Fantasy'),
('Historical'),
('Horror'),
('Mystery'),
('Psychological'),
('Romance'),
('Science Fiction'),
('Slice of Life'),
('Sports'),
('Superhero'),
('Thriller'),
('War'),
('Western'),
('Cyberpunk'),
('Post-Apocalyptic'),
('Steampunk'),
('Young Adult'),
('Magic'),
('Detective'),
('Suspense'),
('Political'),
('Philosophical');

INSERT INTO media (title, release_year, description, rating, status_id)
VALUES
('The Hobbit', 1937, 'Fantasy adventure novel.', 9, 3),
('1984', 1949, 'Dystopian political novel.', 10, 3),
('Dune', 1965, 'Epic science fiction novel.', 9, 3),
('Pride and Prejudice', 1813, 'Classic romance novel.', 8, 3),
('The Name of the Wind', 2007, 'Fantasy coming-of-age story.', 9, 2),
('The Catcher in the Rye', 1951, 'Teenage alienation story.', 7, 3),
('Brave New World', 1932, 'Science fiction dystopia.', 8, 3),
('The Lord of the Rings', 1954, 'Epic fantasy trilogy.', 10, 3),
('The Martian', 2011, 'Survival story on Mars.', 8, 3),
('To Kill a Mockingbird', 1960, 'Classic social justice novel.', 9, 3),
('Harry Potter and the Sorcerer''s Stone', 1997, 'Wizarding world fantasy.', 9, 3),
('Mistborn', 2006, 'Fantasy heist adventure.', 9, 2),
('Foundation', 1951, 'Sci-fi galactic empire saga.', 8, 3),
('Neuromancer', 1984, 'Cyberpunk classic.', 8, 3),
('The Way of Kings', 2010, 'Epic fantasy novel.', 10, 2),
('The Hunger Games', 2008, 'Dystopian survival competition.', 8, 3),
('Frankenstein', 1818, 'Classic gothic horror.', 7, 3),
('Dracula', 1897, 'Classic vampire novel.', 7, 3),
('The Road', 2006, 'Post-apocalyptic survival story.', 8, 3),
('Project Hail Mary', 2021, 'Science fiction survival adventure.', 9, 2);

INSERT INTO book (media_id, author, publisher, page_count, isbn)
VALUES
(1, 'J.R.R. Tolkien', 'Allen & Unwin', 310, '9780261102217'),
(2, 'George Orwell', 'Secker & Warburg', 328, '9780451524935'),
(3, 'Frank Herbert', 'Chilton Books', 412, '9780441172719'),
(4, 'Jane Austen', 'T. Egerton', 279, '9780141439518'),
(5, 'Patrick Rothfuss', 'DAW Books', 662, '9780756404741'),
(6, 'J.D. Salinger', 'Little, Brown and Company', 277, '9780316769488'),
(7, 'Aldous Huxley', 'Chatto & Windus', 311, '9780060850524'),
(8, 'J.R.R. Tolkien', 'Allen & Unwin', 1178, '9780618640157'),
(9, 'Andy Weir', 'Crown Publishing', 369, '9780553418026'),
(10, 'Harper Lee', 'J.B. Lippincott & Co.', 281, '9780061120084'),
(11, 'J.K. Rowling', 'Bloomsbury', 309, '9780747532699'),
(12, 'Brandon Sanderson', 'Tor Books', 541, '9780765311788'),
(13, 'Isaac Asimov', 'Gnome Press', 255, '9780553293357'),
(14, 'William Gibson', 'Ace Books', 271, '9780441569595'),
(15, 'Brandon Sanderson', 'Tor Books', 1007, '9780765326355'),
(16, 'Suzanne Collins', 'Scholastic Press', 374, '9780439023481'),
(17, 'Mary Shelley', 'Lackington, Hughes, Harding, Mavor & Jones', 280, '9780486282114'),
(18, 'Bram Stoker', 'Archibald Constable and Company', 418, '9780486411095'),
(19, 'Cormac McCarthy', 'Alfred A. Knopf', 287, '9780307387899'),
(20, 'Andy Weir', 'Ballantine Books', 496, '9780593135204');

INSERT INTO media (
    title,
    release_year,
    description,
    rating,
    status_id
)
VALUES
('Inception', 2010, 'Mind-bending sci-fi thriller.', 9, 3),
('The Dark Knight', 2008, 'Batman faces the Joker.', 10, 3),
('Interstellar', 2014, 'Space exploration to save humanity.', 9, 3),
('The Matrix', 1999, 'Reality is a simulation.', 10, 3),
('Blade Runner 2049', 2017, 'Cyberpunk detective story.', 8, 3),
('Mad Max: Fury Road', 2015, 'Post-apocalyptic action film.', 9, 3),
('Parasite', 2019, 'Dark social satire thriller.', 9, 3),
('Whiplash', 2014, 'Intense music school drama.', 9, 3),
('The Shawshank Redemption', 1994, 'Prison friendship and hope.', 10, 3),
('Fight Club', 1999, 'Underground fight society.', 9, 3),
('Pulp Fiction', 1994, 'Interconnected crime stories.', 9, 3),
('The Lord of the Rings: The Fellowship of the Ring', 2001, 'Epic fantasy adventure.', 10, 3),
('The Godfather', 1972, 'Classic mafia family drama.', 10, 3),
('Alien', 1979, 'Sci-fi horror aboard spaceship.', 8, 3),
('Arrival', 2016, 'Linguist communicates with aliens.', 8, 3),
('Gladiator', 2000, 'Roman revenge epic.', 8, 3),
('The Social Network', 2010, 'Story of Facebook creation.', 8, 3),
('Everything Everywhere All at Once', 2022, 'Multiverse action comedy drama.', 9, 2),
('Django Unchained', 2012, 'Western revenge story.', 8, 3),
('Spider-Man: Into the Spider-Verse', 2018, 'Animated multiverse superhero film.', 9, 3);

INSERT INTO movie (
    media_id,
    director,
    duration_minutes
)
VALUES
(21, 'Christopher Nolan', 148),
(22, 'Christopher Nolan', 152),
(23, 'Christopher Nolan', 169),
(24, 'The Wachowskis', 136),
(25, 'Denis Villeneuve', 164),
(26, 'George Miller', 120),
(27, 'Bong Joon-ho', 132),
(28, 'Damien Chazelle', 106),
(29, 'Frank Darabont', 142),
(30, 'David Fincher', 139),
(31, 'Quentin Tarantino', 154),
(32, 'Peter Jackson', 178),
(33, 'Francis Ford Coppola', 175),
(34, 'Ridley Scott', 117),
(35, 'Denis Villeneuve', 116),
(36, 'Ridley Scott', 155),
(37, 'David Fincher', 120),
(38, 'Daniel Kwan & Daniel Scheinert', 139),
(39, 'Quentin Tarantino', 165),
(40, 'Peter Ramsey', 117);

INSERT INTO media (
    title,
    release_year,
    description,
    rating,
    status_id
)
VALUES
('Breaking Bad', 2008, 'Chemistry teacher becomes drug kingpin.', 10, 3),
('Game of Thrones', 2011, 'Fantasy war for the Iron Throne.', 9, 3),
('Stranger Things', 2016, 'Supernatural mysteries in a small town.', 8, 2),
('The Office', 2005, 'Mockumentary workplace comedy.', 9, 3),
('Sherlock', 2010, 'Modern adaptation of Sherlock Holmes.', 9, 3),
('Dark', 2017, 'German sci-fi time travel mystery.', 9, 3),
('The Last of Us', 2023, 'Post-apocalyptic survival drama.', 9, 2),
('Arcane', 2021, 'Animated steampunk fantasy series.', 10, 2),
('House of the Dragon', 2022, 'Game of Thrones prequel.', 8, 2),
('The Mandalorian', 2019, 'Star Wars bounty hunter adventure.', 8, 2),
('Attack on Titan', 2013, 'Humanity fights giant titans.', 10, 3),
('Better Call Saul', 2015, 'Lawyer origin story from Breaking Bad.', 9, 3),
('The Boys', 2019, 'Dark satire of superheroes.', 8, 2),
('Mr. Robot', 2015, 'Hacker fights corrupt corporations.', 9, 3),
('Black Mirror', 2011, 'Anthology exploring technology dangers.', 8, 3),
('Friends', 1994, 'Sitcom about six friends in New York.', 8, 3),
('True Detective', 2014, 'Crime anthology series.', 8, 3),
('Severance', 2022, 'Workers separate work and personal memories.', 9, 2),
('The Witcher', 2019, 'Fantasy monster hunter adventure.', 7, 2),
('Avatar: The Last Airbender', 2005, 'Animated elemental fantasy adventure.', 10, 3);

INSERT INTO tv_show (
    media_id,
    creator,
    season_count,
    episode_count
)
VALUES
(41, 'Vince Gilligan', 5, 62),
(42, 'David Benioff & D.B. Weiss', 8, 73),
(43, 'The Duffer Brothers', 4, 34),
(44, 'Greg Daniels', 9, 201),
(45, 'Steven Moffat & Mark Gatiss', 4, 13),
(46, 'Baran bo Odar & Jantje Friese', 3, 26),
(47, 'Craig Mazin & Neil Druckmann', 1, 9),
(48, 'Christian Linke & Alex Yee', 1, 9),
(49, 'Ryan Condal & George R. R. Martin', 2, 18),
(50, 'Jon Favreau', 3, 24),
(51, 'Hajime Isayama', 4, 89),
(52, 'Vince Gilligan & Peter Gould', 6, 63),
(53, 'Eric Kripke', 4, 32),
(54, 'Sam Esmail', 4, 45),
(55, 'Charlie Brooker', 6, 27),
(56, 'David Crane & Marta Kauffman', 10, 236),
(57, 'Nic Pizzolatto', 4, 30),
(58, 'Dan Erickson', 2, 19),
(59, 'Lauren Schmidt Hissrich', 3, 24),
(60, 'Michael Dante DiMartino & Bryan Konietzko', 3, 61);

INSERT INTO media_genre (media_id, genre_id)
VALUES

-- BOOKS

(1, 9),   -- Fantasy
(1, 2),   -- Adventure

(2, 15),  -- Science Fiction
(2, 29),  -- Political

(3, 15),  -- Science Fiction
(3, 2),   -- Adventure

(4, 14),  -- Romance
(4, 8),   -- Drama

(5, 9),   -- Fantasy
(5, 25),  -- Young Adult

(6, 8),   -- Drama

(7, 15),  -- Science Fiction
(7, 29),  -- Political

(8, 9),   -- Fantasy
(8, 2),   -- Adventure

(9, 15),  -- Science Fiction
(9, 2),   -- Adventure

(10, 8),  -- Drama

(11, 9),  -- Fantasy
(11, 25), -- Young Adult
(11, 26), -- Magic

(12, 9),  -- Fantasy
(12, 2),  -- Adventure

(13, 15), -- Science Fiction

(14, 22), -- Cyberpunk
(14, 15), -- Science Fiction

(15, 9),  -- Fantasy
(15, 2),  -- Adventure

(16, 15), -- Science Fiction
(16, 25), -- Young Adult
(16, 23), -- Post-Apocalyptic

(17, 11), -- Horror
(17, 15), -- Science Fiction

(18, 11), -- Horror

(19, 23), -- Post-Apocalyptic
(19, 8),  -- Drama

(20, 15), -- Science Fiction
(20, 2),  -- Adventure


-- MOVIES

(21, 15), -- Science Fiction
(21, 19), -- Thriller

(22, 1),  -- Action
(22, 18), -- Superhero
(22, 19), -- Thriller

(23, 15), -- Science Fiction
(23, 2),  -- Adventure

(24, 15), -- Science Fiction
(24, 22), -- Cyberpunk

(25, 15), -- Science Fiction
(25, 22), -- Cyberpunk

(26, 1),  -- Action
(26, 23), -- Post-Apocalyptic

(27, 8),  -- Drama
(27, 19), -- Thriller

(28, 8),  -- Drama

(29, 8),  -- Drama
(29, 5),  -- Crime

(30, 8),  -- Drama
(30, 12), -- Mystery
(30, 19), -- Thriller

(31, 5),  -- Crime
(31, 19), -- Thriller

(32, 9),  -- Fantasy
(32, 2),  -- Adventure

(33, 5),  -- Crime
(33, 8),  -- Drama

(34, 15), -- Science Fiction
(34, 11), -- Horror

(35, 15), -- Science Fiction
(35, 8),  -- Drama

(36, 1),  -- Action
(36, 8),  -- Drama

(37, 8),  -- Drama
(37, 29), -- Political

(38, 15), -- Science Fiction
(38, 5),  -- Comedy

(39, 21), -- Western
(39, 8),  -- Drama

(40, 18), -- Superhero
(40, 3),  -- Animation


-- TV SHOWS

(41, 5),  -- Crime
(41, 8),  -- Drama

(42, 9),  -- Fantasy
(42, 1),  -- Action

(43, 15), -- Science Fiction
(43, 11), -- Horror

(44, 5),  -- Comedy

(45, 27), -- Detective
(45, 12), -- Mystery

(46, 15), -- Science Fiction
(46, 12), -- Mystery

(47, 23), -- Post-Apocalyptic
(47, 8),  -- Drama

(48, 3),  -- Animation
(48, 24), -- Steampunk

(49, 9),  -- Fantasy
(49, 1),  -- Action

(50, 15), -- Science Fiction
(50, 2),  -- Adventure

(51, 1),  -- Action
(51, 9),  -- Fantasy

(52, 5),  -- Crime
(52, 8),  -- Drama

(53, 18), -- Superhero
(53, 5),  -- Crime

(54, 22), -- Cyberpunk
(54, 19), -- Thriller

(55, 15), -- Science Fiction
(55, 19), -- Thriller

(56, 5),  -- Comedy
(56, 14), -- Romance

(57, 5),  -- Crime
(57, 19), -- Thriller

(58, 15), -- Science Fiction
(58, 19), -- Thriller

(59, 9),  -- Fantasy
(59, 1),  -- Action

(60, 3),  -- Animation
(60, 9);  -- Fantasy

INSERT INTO source_link (
    media_id,
    platform_name,
    url,
    availability_type
)
VALUES

-- BOOKS

(1, 'Amazon', 'https://amazon.com/hobbit', 'BUY'),
(2, 'Amazon', 'https://amazon.com/1984', 'BUY'),
(3, 'Amazon', 'https://amazon.com/dune', 'BUY'),
(4, 'Amazon', 'https://amazon.com/pride-and-prejudice', 'BUY'),
(5, 'Amazon', 'https://amazon.com/name-of-the-wind', 'BUY'),
(6, 'Amazon', 'https://amazon.com/catcher-in-the-rye', 'BUY'),
(7, 'Amazon', 'https://amazon.com/brave-new-world', 'BUY'),
(8, 'Amazon', 'https://amazon.com/lord-of-the-rings', 'BUY'),
(9, 'Amazon', 'https://amazon.com/the-martian', 'BUY'),
(10, 'Amazon', 'https://amazon.com/to-kill-a-mockingbird', 'BUY'),
(11, 'Amazon', 'https://amazon.com/harry-potter-1', 'BUY'),
(12, 'Amazon', 'https://amazon.com/mistborn', 'BUY'),
(13, 'Amazon', 'https://amazon.com/foundation', 'BUY'),
(14, 'Amazon', 'https://amazon.com/neuromancer', 'BUY'),
(15, 'Amazon', 'https://amazon.com/way-of-kings', 'BUY'),
(16, 'Amazon', 'https://amazon.com/hunger-games', 'BUY'),
(17, 'Amazon', 'https://amazon.com/frankenstein', 'BUY'),
(18, 'Amazon', 'https://amazon.com/dracula', 'BUY'),
(19, 'Amazon', 'https://amazon.com/the-road', 'BUY'),
(20, 'Amazon', 'https://amazon.com/project-hail-mary', 'BUY'),

-- MOVIES

(21, 'Netflix', 'https://netflix.com/inception', 'STREAM'),
(22, 'Netflix', 'https://netflix.com/the-dark-knight', 'STREAM'),
(23, 'Prime Video', 'https://primevideo.com/interstellar', 'RENT'),
(24, 'Netflix', 'https://netflix.com/the-matrix', 'STREAM'),
(25, 'Prime Video', 'https://primevideo.com/blade-runner-2049', 'RENT'),
(26, 'Max', 'https://max.com/mad-max-fury-road', 'STREAM'),
(27, 'Hulu', 'https://hulu.com/parasite', 'STREAM'),
(28, 'Netflix', 'https://netflix.com/whiplash', 'STREAM'),
(29, 'Prime Video', 'https://primevideo.com/shawshank-redemption', 'RENT'),
(30, 'Disney+', 'https://disneyplus.com/fight-club', 'STREAM'),
(31, 'Netflix', 'https://netflix.com/pulp-fiction', 'STREAM'),
(32, 'Max', 'https://max.com/lotr-fellowship', 'STREAM'),
(33, 'Prime Video', 'https://primevideo.com/godfather', 'RENT'),
(34, 'Hulu', 'https://hulu.com/alien', 'STREAM'),
(35, 'Netflix', 'https://netflix.com/arrival', 'STREAM'),
(36, 'Prime Video', 'https://primevideo.com/gladiator', 'RENT'),
(37, 'Netflix', 'https://netflix.com/social-network', 'STREAM'),
(38, 'Prime Video', 'https://primevideo.com/everything-everywhere', 'RENT'),
(39, 'Netflix', 'https://netflix.com/django-unchained', 'STREAM'),
(40, 'Disney+', 'https://disneyplus.com/spiderverse', 'STREAM'),

-- TV SHOWS

(41, 'Netflix', 'https://netflix.com/breaking-bad', 'STREAM'),
(42, 'Max', 'https://max.com/game-of-thrones', 'STREAM'),
(43, 'Netflix', 'https://netflix.com/stranger-things', 'STREAM'),
(44, 'Peacock', 'https://peacocktv.com/the-office', 'STREAM'),
(45, 'BBC iPlayer', 'https://bbc.co.uk/sherlock', 'STREAM'),
(46, 'Netflix', 'https://netflix.com/dark', 'STREAM'),
(47, 'Max', 'https://max.com/the-last-of-us', 'STREAM'),
(48, 'Netflix', 'https://netflix.com/arcane', 'STREAM'),
(49, 'Max', 'https://max.com/house-of-the-dragon', 'STREAM'),
(50, 'Disney+', 'https://disneyplus.com/the-mandalorian', 'STREAM'),
(51, 'Crunchyroll', 'https://crunchyroll.com/attack-on-titan', 'STREAM'),
(52, 'Netflix', 'https://netflix.com/better-call-saul', 'STREAM'),
(53, 'Prime Video', 'https://primevideo.com/the-boys', 'STREAM'),
(54, 'Prime Video', 'https://primevideo.com/mr-robot', 'STREAM'),
(55, 'Netflix', 'https://netflix.com/black-mirror', 'STREAM'),
(56, 'Max', 'https://max.com/friends', 'STREAM'),
(57, 'Max', 'https://max.com/true-detective', 'STREAM'),
(58, 'Apple TV+', 'https://tv.apple.com/severance', 'STREAM'),
(59, 'Netflix', 'https://netflix.com/the-witcher', 'STREAM'),
(60, 'Netflix', 'https://netflix.com/avatar-last-airbender', 'STREAM');