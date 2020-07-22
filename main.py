import sqlite3
from sqlite3 import Error

def main():
    conn = sqlite3.connect('example.db')
    print("Database connection")

    createTable(conn)
    insert(conn)
    save(conn)

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    print("Database closed")


def createTable(conn):
    c = conn.cursor()
    
    # Create table
    try:
        c.execute('''CREATE TABLE stocks
                     (date text, trans text, symbol text, qty real, price real)''')
        print("Database created")
    except Error as e:
        print(e)

def insert(conn):
    c = conn.cursor()

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    c.execute("INSERT INTO stocks VALUES ('2012-02-02','SELL','RHAT',1099,0.8)")

def save(conn):
    # Save (commit) the changes
    conn.commit()



if __name__ == '__main__':
    main()
