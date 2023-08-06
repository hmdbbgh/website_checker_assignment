import logging
import psycopg2

from logging_config import setup_logging
from .connection import DatabaseConnection
from .settings import (
    DB_NAME,
    DATABSE_STORE_LOGNAME,
    DATABSE_STORE_LOGFILE
)

logging = setup_logging(
    DATABSE_STORE_LOGNAME,
    DATABSE_STORE_LOGFILE
)


def store_to_database(
    *,
    website_url: str,
    status_code: int,
    response_time: int,
    pattern_found: bool | None,
) -> None:

    try:
        with DatabaseConnection() as conn:

            cursor = conn.cursor()
            sql = (
                f'INSERT INTO {DB_NAME} '
                '(site_url, response_status, pattern_found, response_time) '
                'VALUES (%s, %s, %s, %s);'
            )
            values = (
                website_url,
                status_code,
                pattern_found,
                response_time,
            )
            cursor.execute(sql, values)
            conn.commit()

            logging.info("Data stored to database successfully.")
    except psycopg2.Error as e:
        logging.error(f"Error storing data to database: {str(e)}")
