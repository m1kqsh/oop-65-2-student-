import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER
);
""")


cursor.executemany("INSERT INTO users (name) VALUES (?)", [
    ('Alex',),
    ('Maria',),
    ('John',),
    ('Aigerim',),
    ('Timur',)
])

cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", [
    ('Inception', 'Sci-Fi'),
    ('Titanic', 'Romance'),
    ('Interstellar', 'Sci-Fi'),
    ('Joker', 'Drama'),
    ('Avatar', 'Fantasy')
])

cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", [
    (1, 1, 9),
    (1, 2, 8),
    (2, 1, 10),
    (2, 3, 9),
    (3, 4, 7),
    (3, 5, 8),
    (4, 2, 6),
    (4, 3, 9),
    (5, 1, 10),
    (5, 5, 9)
])


cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id;
""")

print("JOIN 1:")
for row in cursor.fetchall():
    print(row)


cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id;
""")

print("\nJOIN 2:")
for row in cursor.fetchall():
    print(row)


cursor.execute("SELECT AVG(rating) FROM reviews;")
print("\nAVG:", cursor.fetchone()[0])

cursor.execute("SELECT MAX(rating) FROM reviews;")
print("MAX:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews;")
print("MIN:", cursor.fetchone()[0])

conn.commit()
conn.close()