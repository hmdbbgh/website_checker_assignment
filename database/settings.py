from decouple import config


DB_USER = config('DB_USER', default='postgres')
DB_HOST = config('DB_HOST', default='localhost')
DB_PORT = config('DB_PORT', default=5432, cast=int)
DB_NAME = config('DB_NAME', default='website_checker')
DB_PASSWORD = config('DB_PASSWORD', default=1234, cast=int)

db_configs = {
    "host": DB_HOST,
    "user": DB_USER,
    "port": DB_PORT,
    "database": DB_NAME,
    "password": DB_PASSWORD,
}

MIN_CONN = config('MIN_CONN', default=1, cast=int)
MAX_CONN = config('MAX_CONN', default=5, cast=int)

connection_configs = {
    "minconn": MIN_CONN,
    "maxconn": MAX_CONN,
}


DATABSE_CONNECTION_LOGNAME = config(
    'DATABSE_CONNECTION_LOGNAME',
    default="database_connection"
)
DATABSE_CONNECTION_LOGFILE = config(
    'DATABSE_CONNECTION_LOGFILE',
    default='logs/database_connection.log'
)

DATABSE_CREATE_TABLE_LOGNAME = config(
    'DATABSE_CREATE_TABLE_LOGNAME',
    default='create_table'
)
DATABSE_CREATE_TABLE_LOGFILE = config(
    'DATABSE_CREATE_TABLE_LOGFILE',
    default='logs/create_table.log'
)

DATABSE_STORE_LOGNAME = config(
    'DATABSE_STORE_LOGNAME',
    default='store_to_database'
)
DATABSE_STORE_LOGFILE = config(
    'DATABSE_STORE_LOGFILE',
    default='logs/store_to_database.log'
)
