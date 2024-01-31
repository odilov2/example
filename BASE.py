import psycopg2 as psql
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Database:
    @staticmethod
    def connect(query):
        postgres_db = psql.connect(
            database=os.getenv("DATABASE_DATABASE"),
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD")
        )

        cursor = postgres_db.cursor()
        cursor.execute(query)
        postgres_db.commit()
        return "ok"






