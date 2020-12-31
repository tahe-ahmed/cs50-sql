# import cs50
import sqlite3
import csv

# Create database
open("shows4.db", "w").close()
# db = cs50.SQL("sqlite:///shows4.db")
conn = sqlite3.connect('shows4.db')
c = conn.cursor()

# Create tables
c.execute("CREATE TABLE shows (id INT, title TEXT, year NUMERIC, PRIMARY KEY(id))")
c.execute("CREATE TABLE genres (show_id INT, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows(id))")

# Open TSV file
# https://datasets.imdbws.com/title.basics.tsv.gz
with open("title.basics.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

        # If non-adult TV show
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            # If year not missing
            if row["startYear"] != "\\N":

                # If since 1970
                startYear = int(row["startYear"])
                if startYear >= 1970:

                    # Trim prefix from tconst
                    id = int(row["tconst"][2:])

                    show_data = [id, row["primaryTitle"], startYear]
                    # Insert show
                    c.execute("INSERT INTO shows (id, title, year) VALUES(?, ?, ?)",
                              show_data)

                    # Insert genres
                    if row["genres"] != "\\N":
                        for genre in row["genres"].split(","):
                            genres_data = [id, genre]
                            c.execute(
                                "INSERT INTO genres (show_id, genre) VALUES(?, ?)", genres_data)

# Save (commit) the changes
conn.commit()

# close the connection
conn.close()
