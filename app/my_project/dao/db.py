from mysql.connector import pooling
from app.my_project.utils.config_loader import load_config

# Load configuration once on module import
_config = load_config()
_db_cfg = _config["database"]

# Create a global connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="tour_agency_pool",
    pool_size=5,
    host=_db_cfg["host"],
    port=_db_cfg["port"],
    user=_db_cfg["user"],
    password=_db_cfg["password"],
    database=_db_cfg["name"],
    charset="utf8mb4",
    collation="utf8mb4_unicode_ci",
)


def get_connection():
    """
    Get a connection object from the global connection pool.

    Returns
    -------
    mysql.connector.connection.MySQLConnection
        Connection ready to use for executing SQL statements.
    """
    return connection_pool.get_connection()
