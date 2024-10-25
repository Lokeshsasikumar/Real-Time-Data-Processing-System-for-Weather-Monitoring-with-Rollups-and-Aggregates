import pymysql
from sqlalchemy import create_engine
from config import DB_CONFIG

def store_weather_data(data):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO weather_data (city, temperature, feels_like, weather_condition, dt, timestamp)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (data['city'], data['temperature'], data['feels_like'],
                                 data['weather_condition'], data['dt'], data['timestamp']))
        connection.commit()
    finally:
        connection.close()

def store_daily_summary(summary):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO daily_summaries (city, avg_temperature, max_temperature, min_temperature, dominant_condition, date)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (summary['city'], summary['avg_temperature'], summary['max_temperature'],
                                 summary['min_temperature'], summary['dominant_condition'], summary['date']))
        connection.commit()
    finally:
        connection.close()
