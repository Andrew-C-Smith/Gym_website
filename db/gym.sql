DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS user_types;

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    date VARCHAR(100),
    time VARCHAR (20)
);

CREATE TABLE user_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    user_type_id INT REFERENCES user_types(id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(id),
    classes_id SERIAL REFERENCES classes(id)
);


INSERT INTO classes (name, date, time) VALUES ('Spin Class', '1 May 2022', '08:00');
INSERT INTO classes (name, date, time) VALUES ('I know Kung Fu', '1 May 2022', '10:00');
INSERT INTO classes (name, date, time) VALUES ('Gun Builder', '1 May 2022', '12:00');
INSERT INTO classes (name, date, time) VALUES ('Spin Class', '1 May 2022', '14:00');
INSERT INTO classes (name, date, time) VALUES ('HIIT', '1 May 2022', '17:00');
INSERT INTO classes (name, date, time) VALUES ('Body Pump', '1 May 2022', '18:00');
INSERT INTO classes (name, date, time) VALUES ('Spin Class', '2 May 2022', '08:00');
INSERT INTO classes (name, date, time) VALUES ('HIIT', '1 May 2022', '10:00');
INSERT INTO classes (name, date, time) VALUES ('Gun Builder', '2 May 2022', '12:00');
INSERT INTO classes (name, date, time) VALUES ('Spin Class', '2 May 2022', '14:00');
INSERT INTO classes (name, date, time) VALUES ('Helicopter programme', '2 May 2022', '17:00');
INSERT INTO classes (name, date, time) VALUES ('Body Pump', '2 May 2022', '18:00');




INSERT INTO user_types (name) VALUES ('member');
INSERT INTO user_types (name) VALUES ('admin');


-- INSERT INTO users (name) VALUES ('Neo');
-- INSERT INTO users (name) VALUES ('Morpheus');
-- INSERT INTO users (name) VALUES ('Trinity');
-- INSERT INTO users (name) VALUES ('Tank');
-- INSERT INTO users (name) VALUES ('The Oracle');
-- INSERT INTO users (name) VALUES ('Mouse');
-- INSERT INTO users (name) VALUES ('Switch');
-- INSERT INTO users (name) VALUES ('Agent Smith');
-- INSERT INTO users (name) VALUES ('Agent Jones');


INSERT INTO bookings (user_id, classes_id) VALUES (1, 1);

