import sqlite3


con = sqlite3.connect('budget.db')
cur = con.cursor()


def create_history_balance():

    cur.execute("""CREATE TABLE IF NOT EXISTS budget(
    money REAL, 
    datestamp DATE, 
    description TEXT
    )""")


def insert(money, datestamp, description):

    cur.execute(f"INSERT INTO budget VALUES (?,?,?)", (money, datestamp, description))
    con.commit()


def showbalance():

    cur.execute("""SELECT SUM(money) FROM budget""")
    return cur.fetchall()


def balance_until(date_end):

    cur.execute("""SELECT SUM(money) FROM budget
    WHERE datestamp < ? 
    """, (date_end,))
    item = (str(cur.fetchall()).replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", ""))
    try:
        item = float(item)
        return item
    except ValueError:
        return 0

def summaryofmonth(date_start, date_end):

    cur.execute(f"""SELECT SUM(money) FROM budget
    WHERE datestamp >= ? and datestamp <= ?
    ORDER BY datestamp
    """, (date_start, date_end))
    return cur.fetchall()


def showtimeperiod(date_start, date_end):

    cur.execute(f"""SELECT * FROM budget
    WHERE datestamp >= ? and datestamp <= ?
    ORDER BY datestamp
    """, (date_start, date_end))
    return cur.fetchall()


def graphdata(date_start, date_end):

    cur.execute(f"""SELECT money, datestamp FROM budget 
    WHERE datestamp >= ? and datestamp <= ? 
    ORDER BY datestamp
    """, (date_start, date_end))

    cash = []
    date = []

    items = cur.fetchall()

    for item in items:
        cash.append(item[0])
        date.append(item[1])

    return cash, date


def showall():

    cur.execute(f"SELECT * FROM budget ORDER BY datestamp ")
    return cur.fetchall()


def allgraphdata():
    
    cur.execute(f"""SELECT money FROM budget 
        ORDER BY datestamp
        """)

    cash = []

    items = cur.fetchall()

    for item in items:
        cash.append(item[0])

    cur.execute(f"""SELECT MIN(datestamp), MAX(datestamp) FROM budget 
            ORDER BY datestamp
            """)

    date = cur.fetchone()

    date_start = date[0]
    date_end = date[1]

    return cash, date_start, date_end


def close():
    con.close()

