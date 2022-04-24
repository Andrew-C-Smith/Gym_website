DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS user_types;

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
    date DATE
    time TIME
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
    user_id SERIAL REFERENCES user(id),
    classes_id SERIAL REFERENCES classes(id)
);
