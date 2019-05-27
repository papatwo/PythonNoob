import sqlite3

conn = sqlite3.connect('music.sqlite') # create memory space/link to space(file) if exist
cur = conn.cursor() # create cursor, like open() when dealing files

cur.execute("""DROP TABLE IF EXISTS Tracks""") # execute commands
# The first SQL command removes the Tracks table from the database if it
# exists. This pattern is simply to allow us to run the same program to create
# the Tracks table over and over again without causing an error.

# create table contents: 3"" can deal with multi lines, any punctuations 
cur.execute("""CREATE TABLE Tracks (
				title TEXT,
				plays INTEGER
			)""") 

# Insert data to table
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute("INSERT INTO Tracks VALUES ('My Way', 15)")

conn.commit()


# Select data from table by different methods
print('Tracks by loop:')
cur.execute('SELECT title, plays FROM Tracks')  
for row in cur:
	print(row)

print('Tracks by fetch:')
cur.execute('SELECT title, plays FROM Tracks') 
print(cur.fetchall())


print('Tracks by conditional select:')
cur.execute('SELECT * FROM Tracks WHERE plays = 20')
print(cur.fetchall())


# Delete data from table
cur.execute('DELETE FROM Tracks WHERE plays < 100') 
conn.commit()
conn.close()