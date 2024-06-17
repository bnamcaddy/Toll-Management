
import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'root',  # default XAMPP MySQL username
    'password': '',  # default XAMPP MySQL password (leave empty if no password is set)
    'host': '127.0.0.1',
    'database': 'tollbooth',
    'raise_on_warnings': True
}

def initialize_database():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            license_plate VARCHAR(255),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            amount DECIMAL(10, 2)
        )
        ''')
        
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def record_transaction(license_plate, amount):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO transactions (license_plate, amount) VALUES (%s, %s)
        ''', (license_plate, amount))
        
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(err)