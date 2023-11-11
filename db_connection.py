import mysql.connector

# Replace these values with your database information
host = "localhost"
user = ""
password = ""
database = ""
# Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example: Execute a SELECT query
    cursor.execute("SELECT * FROM city")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
