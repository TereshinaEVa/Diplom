CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    age INTEGER,
    grade INTEGER,
);

CREATE TABLE IF NOT EXISTS tasks_material (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    descript TEXTAREA NOT NULL,
    text_url TEXT,
    video_url TEXT,
);