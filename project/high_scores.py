import sqlite3
from sqlite3 import Cursor, Connection

def high_scores() -> list:
    """
    Returns the high scores obtained from the database, ordered by the most recent first.
    """
    # Connect to the database
    conn: Connection = sqlite3.connect('high_scores.db')

    # Cursor to execute SQL commands
    cursor: Cursor = conn.cursor()

    # Create high_scores table if it doesn't exist yet
    cursor.execute('''CREATE TABLE IF NOT EXISTS high_scores
                    (player_name text, victories integer, date text)''')

    # Check if the table is empty
    cursor.execute("SELECT COUNT(*) FROM high_scores")
    table_count = cursor.fetchone()[0]

    if table_count == 0:
        # Fill the table with some data
        cursor.execute("INSERT INTO high_scores VALUES ('Antonio', 10, '2022-05-20 12:03:15')")
        cursor.execute("INSERT INTO high_scores VALUES ('Laura', 5, '2023-02-19 11:51:03')")
        cursor.execute("INSERT INTO high_scores VALUES ('Ramiro', 6, '2023-02-19 10:12:06')")

        # Commit the changes to the database
        conn.commit()

    # Select the high scores ordered by most recent victories
    cursor.execute("SELECT player_name, victories, date FROM high_scores ORDER BY date DESC")

    # Fetch all the results
    results: list = cursor.fetchall()

    # Close the database connection
    conn.close()

    return results

if __name__ == "__main__":
    """
    Standard python boilerplate.
    """
    # This is executed when run from the command line:
    high_scores()