import sqlite3
import csv
from sys import argv, exit

# get the csv file name as command line argument
# if incorrect number of command-line argument print an error and exit
if len(argv) < 2:
    print("error")
    exit(1)

csv_file = argv[1]

# create a sqlite3 connection
conn = sqlite3.connect('students.db')
c = conn.cursor()

# open the csv file
with open(csv_file, 'r') as characters:

    reader = csv.DictReader(characters)

    # read each row
    for row in reader:

        # parse the name to list of sperated names
        full_name = row['name'].split(' ')

        # if there is no middle name add Null to the db
        if len(full_name) < 3:
            student_data = [full_name[0], None,
                            full_name[1], row['house'], row['birth']]
            c.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                      student_data)
        else:
            student_data = [full_name[0], full_name[1],
                            full_name[2], row['house'], row['birth']]
            c.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                      student_data)


# Save (commit) the changes
conn.commit()

# close the connection
conn.close()
exit(0)
