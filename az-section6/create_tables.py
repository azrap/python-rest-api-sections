import sqlite3


# first we create the data.db. can really call data.db anything we want I believe (VERIFY)
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# ********************************

# auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)


# must be a tuple
user = (1, 'jose', "superpass")

# the ? signifies parameters we'll insert
# must insert tuple with the number of ? = the parameters
insert_query = "INSERT INTO USERS values (?, ?, ?)"

# execute the query above
cursor.execute(insert_query, user)

# additional rows we would want to add
users = [(2, 'jan', "superpass"), (3, 'anne', "superpass")]

# executemany for many rows vs just one row
cursor.executemany(insert_query, users)

# test to see it worked
select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

# ********************************
# now we create the items table
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES (1, 'test', 10.99)")

for row in cursor.execute("SELECT * FROM items"):
    print(row)


#commit = save
connection.commit()
# close the connection
connection.close()
