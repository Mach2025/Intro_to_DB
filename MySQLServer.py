import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Use your MySQL root password if set
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
