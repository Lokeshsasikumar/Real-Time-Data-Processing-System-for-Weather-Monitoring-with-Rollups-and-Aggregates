CREATE DATABASE weather_db;
USE weather_db;

-- Table to store weather data
CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    feels_like FLOAT,
    weather_condition VARCHAR(50),
    timestamp DATETIME,
    dt INT
);

-- Table to store daily rollups
CREATE TABLE daily_summaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    avg_temperature FLOAT,
    max_temperature FLOAT,
    min_temperature FLOAT,
    dominant_condition VARCHAR(50),
    date DATE
);
