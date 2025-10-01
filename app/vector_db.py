import os
import psycopg


class VectorDB:
    """
    This class is a singleton that manages database connection parameters for PostgreSQL with pgvector.
    Only one instance of VectorDB will exist during the application's lifetime, ensuring consistent configuration.

    Args:
        db_host (str): Database host
        db_port (str): Database port
        db_user (str): Database user
        db_password (str): Database password
        db_name (str): Database name
    """
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VectorDB, cls).__new__(cls)
        return cls._instance

    def __init__(self):
            self.db_host = os.getenv("DB_HOST")
            self.db_port = os.getenv("DB_PORT")
            self.db_user = os.getenv("DB_USER")
            self.db_password = os.getenv("DB_PASSWORD")
            self.db_name = os.getenv("DB_NAME")

    def check_connection(self):
        """
        Establishes a connection to the PostgreSQL database using the provided parameters.
        
        Returns:
            connection: A psycopg connection object if successful, None otherwise.
        """
        try:
            connection = psycopg.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                password=self.db_password,
                dbname=self.db_name
            )

            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                logger.info("Database connection successful.")
                connection.close()
                cursor.close()
                return True
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            return False

    def connect_db(self):
        """
        Establishes a connection to the PostgreSQL database using the provided parameters.
        
        Returns:
            connection: A psycopg connection object if successful, None otherwise.
        """
        return psycopg.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_password,
            dbname=self.db_name
        )