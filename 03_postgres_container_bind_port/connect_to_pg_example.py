import psycopg2

# Connection settings (update as needed)
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="secret",
    host="localhost",  # or the container name if using Docker
    port="5432"
)

# Open a cursor to perform operations
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Insert a row
cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", ("Alice",))
inserted_id = cur.fetchone()[0]
print(f"Inserted user with ID: {inserted_id}")

cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", ("Bob",))
inserted_id = cur.fetchone()[0]
print(f"Inserted user with ID: {inserted_id}")

cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", ("Micheal",))
inserted_id = cur.fetchone()[0]
print(f"Inserted user with ID: {inserted_id}")


# Commit the transaction
conn.commit()

# Retrieve data
cur.execute("SELECT id, name FROM users;")
rows = cur.fetchall()

print("Current users in database:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}")

# Clean up
cur.close()
conn.close()
