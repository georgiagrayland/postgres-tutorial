import psycopg2


# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" columnfrom the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only "ArtistId" number 51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the Albums with "ArtistId" 51 on the "Album" Table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all trackers where the composer is "Queen" from "Track"
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Bach"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch a result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# Print results
for result in results:
    print(result)