
import psycopg2.pool

from logging_config import setup_logging
from .settings import (
    db_configs,
    connection_configs,
    DATABSE_CONNECTION_LOGFILE,
    DATABSE_CONNECTION_LOGNAME,
)


logging = setup_logging(
    DATABSE_CONNECTION_LOGNAME,
    DATABSE_CONNECTION_LOGFILE
)
connection_pool = psycopg2.pool.SimpleConnectionPool(
    **connection_configs,
    **db_configs
)


class DatabaseConnection:

    def __enter__(self):
        try:
            self.conn = connection_pool.getconn()
            return self.conn
        except psycopg2.Error as e:
            raise Exception(f"Error connecting to the database: {str(e)}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            connection_pool.putconn(self.conn)
        except psycopg2.Error as e:
            raise Exception(
                f"Error returning the database connection to the pool: {str(e)}")
