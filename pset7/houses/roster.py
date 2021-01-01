import sqlite3
import csv
from sys import argv, exit

# get the csv file name as command line argument
# if incorrect number of command-line argument print an error and exit
if len(argv) < 2:
    print("error")
    exit(1)

house = argv[1]
# print(len(house))
# create a sqlite3 connection
conn = sqlite3.connect('students.db')
c = conn.cursor()

# query the students table in the students db for the students in that specific house
c.execute(
    "SELECT DISTINCT first, middle, last, birth FROM students WHERE house = ? ORDER BY last ASC, first ASC", (house,))
students = c.fetchall()

for student in students:

    first, middle, last, birth = student

    if student[1] == None:
        print(f"{first} {last}, born {birth}")
    else:
        print(f"{first} {middle} {last}, born {birth}")


# Save (commit) the changes
conn.commit()

# close the connection
conn.close()
exit(0)
