import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()


#auto-incrementing columns 
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)


# must be a tuple
user = (1, 'jose', "superpass")

# the ? signifies parameters we'll insert


# must insert tuple with the number of ? = the parameters
insert_query = "INSERT INTO USERS values (?, ?, ?)"

cursor.execute(insert_query, user)


users = [(2, 'jan', "superpass"), (3, 'anne', "superpass")]

# executemany for many rows vs just one row
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)


#commit = save
connection.commit()
# close the connection
connection.close()
