#import the module we will use
import sqlite3

#connects to the db
conn = sqlite3.connect('test.db')

#creates a new table if it doesn't already exists
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_step222(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileName TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

#list of file names as a tuple
fileName_tuple = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#instruction to only add files that end with 'txt' to the table and then print them out
for x in fileName_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_step222 (col_fileName) VALUES (?)", (x,))
            print(x)

#close the program
conn.close()
