import logging
import psycopg2

from logging_config import setup_logging
from .connection import DatabaseConnection
from .settings import (
    DB_NAME,
    DATABSE_CREATE_TABLE_LOGNAME,
    DATABSE_CREATE_TABLE_LOGFILE
)

logging = setup_logging(
    DATABSE_CREATE_TABLE_LOGNAME,
    DATABSE_CREATE_TABLE_LOGFILE
)


def create_table() -> None:

    try:

        with DatabaseConnection() as conn:

            cursor = conn.cursor()
            sql = (
                f'CREATE TABLE IF NOT EXISTS {DB_NAME} ( '
                'id SERIAL PRIMARY KEY,'
                'site_url VARCHAR(255) NOT NULL,'
                'response_status INTEGER NOT NULL,'
                'response_time FLOAT NOT NULL,'
                'pattern_found BOOLEAN'
                ');'
            )
            cursor.execute(sql)
            conn.commit()

            logging.info(f"Table '{DB_NAME}' created successfully.")
    except psycopg2.Error as e:
        logging.error(f"Error creating table: {str(e)}")
