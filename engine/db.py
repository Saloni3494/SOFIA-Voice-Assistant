import csv
import sqlite3

con = sqlite3.connect("sofia.db")
cursor = con.cursor()

# Create a table sys_command
# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# Insert into Table
# query = "INSERT INTO sys_command VALUES (null,'notepad++','C:\\Program Files\\Notepad++\\notepad++.exe')"
# cursor.execute(query)
# con.commit()

#Create a table web_command
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# Insert into Table
# query = "INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

#Create a table with the desired columns
# cursor.execute('CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)')

# Specify the colummn indices you want to import (0-based index)
# Example: Importing the 1st and 33rd columns
# desired_columns_indices = [0, 33]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding="utf-8") as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute('''INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

#Insert single contact
# query = "INSERT INTO contacts VALUES (null, 'abc', '1234567890','null')"
# cursor.execute(query)



#Commit changes and close connection
# con.commit()
# con.close()

# To search a contact
# query = 'mummy'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])

query = "UPDATE contacts SET mobile_no='+919503997896' WHERE id=27"
cursor.execute(query)
con.commit()

# query = "DELETE FROM contacts WHERE id=29"
# cursor.execute(query)
# con.commit()