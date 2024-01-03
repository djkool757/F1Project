import psycopg2
from psycopg2 import sql
from config import config

def create_table(conn, cursor):
    try:
        # Define the table schema with primary key
        create_table_query = """
            CREATE TABLE IF NOT EXISTS driverinfo (
                id SERIAL PRIMARY KEY,
                "Name" VARCHAR(255) NOT NULL,
                "Number" INT NOT NULL,
                "Team" VARCHAR(255),
                "Points" INT,
                UNIQUE ("Name", "Number")
            );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully!")
    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Establish a connection to the PostgreSQL database
    line = config("database.ini", "postgresql")
    conn = psycopg2.connect(user=line['user'], password=line['password'], host=line['host'], port=line['port'], dbname=line['database'])
    cursor = conn.cursor()
    print("Connected!\n")

    # Create the table with primary key
    create_table(conn, cursor)

    # Insert data into the table
    cursor.execute("""
        INSERT INTO driverinfo ("Name", "Number", "Team", "Points") VALUES
         ('Max Verstappen', 1, 'RedBull', 575),
                   ('Sergio Perez', 11, 'RedBull', 285),
                   ('Lewis Hamilton', 44, 'Mercedes', 234),
                   ('Fernando Alonso', 14, 'Aston Martin', 206),
                   ('Charles Leclerc', 16, 'Ferrari', 206),
                   ('Lando Norris', 4, 'Mclaren', 205),
                   ('Carlos Sainz', 55, 'Ferrari', 200),
                   ('George Russell', 63, 'Mercedes', 175),
                   ('Oscar Piastri', 81, 'Mclaren', 97),
                   ('Lance Stroll', 18, 'Aston Martin', 74),
                   ('Pierre Gasly', 10, 'Alpine', 62),
                   ('Esteban Ocon', 31, 'Alpine', 58),
                   ('Alexander Albon', 23, 'Williams', 27),
                   ('Yuki Tsunoda', 22, 'Alphatauri', 17),
                   ('Valtteri Bottas', 77, 'Alfa Romeo', 10),
                   ('Nico Hulkenberg', 27, 'Haas', 9),
                   ('Daniel Ricciardo', 3, 'Alphatauri', 6),
                   ('Zhou Guanyu', 24, 'Alfa Romeo', 6),
                   ('Kevin Magnussen', 20, 'Haas', 3),
                   ('Liam Lawson', 40, 'Alphatauri', 2),
                   ('Logan Sargeant', 2, 'Williams', 1),
                   ('Nyck De Vries', 21, 'Alphatauri', 0)
        ON CONFLICT ("Name", "Number") DO NOTHING;  -- Ignore duplicates
    """)
    conn.commit()
    print("Data inserted successfully, Yay!")

    # Close the cursor and connection
    cursor.close()
    conn.close()
