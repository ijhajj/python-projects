import sqlite3

def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BOOK_DETAILS(BOOK_ID INTEGER PRIMARY KEY,BOOK_NAME TEXT,AUTHOR_NAME TEXT, YEAR_PUBLISH DATE,ISSUED_IND TEXT,ISSUED_ON_DT DATE,ISSUED_TILL_DT DATE,ISSUED_CLIENT_ID INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS MEMBERSHIP_DETAILS(CLIENT_ID INTEGER PRIMARY KEY,FIRST_NAME TEXT,LAST_NAME TEXT,ADDRESS TEXT,MOBILE_NUMBER INTEGER,CLIENT_STATUS TEXT)")
    conn.commit()
    conn.close()

def addBook(book_name,author_name,year_publish):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO BOOK_DETAILS VALUES (NULL,?,?,?,?,?,?,?)",(book_name,author_name,year_publish,'N','9999-01-01','9999-01-01','',))
    conn.commit()
    conn.close()

def addMember(first_name,last_name,address,mobile_number):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO MEMBERSHIP_DETAILS VALUES(NULL,?,?,?,?,?)",(first_name,last_name,address,mobile_number,'A',))
    conn.commit()
    conn.close()

def searchBook(bookParam):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK_DETAILS WHERE BOOK_NAME=? OR AUTHOR_NAME=?",(bookParam,bookParam,))
    rows = cur.fetchall()
    conn.close()
    return rows

def searchAllBooks():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK_DETAILS")
    rows = cur.fetchall()
    conn.close()
    return rows

#Returns only Active Members
def searchMember(memberParam):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MEMBERSHIP_DETAILS WHERE FIRST_NAME = ? OR LAST_NAME = ? OR MOBILE_NUMBER = ? AND CLIENT_STATUS=?", (memberParam, memberParam, memberParam,'A',))
    rows=cur.fetchall()
    conn.close()
    return rows

def searchAllMembers():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MEMBERSHIP_DETAILS")
    rows = cur.fetchall()
    conn.close()
    return rows

def updateBook(title_edit,author_edit,year_edit,book_id):
    conn=sqlite3.connect("library.db")
    cur=conn.cursor()
    cur.execute("UPDATE BOOK_DETAILS SET BOOK_NAME=?,AUTHOR_NAME=?,YEAR_PUBLISH=? WHERE BOOK_ID=?",(title_edit,author_edit,year_edit,book_id,))
    conn.commit()
    conn.close()

def updateMember(first_name_edit,last_name_edit,address_edit,mob_number_edit,client_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE MEMBERSHIP_DETAILS SET FIRST_NAME=?,LAST_NAME=?,ADDRESS=?, MOBILE_NUMBER=? WHERE CLIENT_ID=?",
                (first_name_edit,last_name_edit,address_edit,mob_number_edit,client_id,))
    conn.commit()
    conn.close()

def deleteBook(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM BOOK_DETAILS WHERE BOOK_ID=?",(book_id,))
    conn.commit()
    conn.close()

def deleteMember(client_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM MEMBERSHIP_DETAILS WHERE CLIENT_ID=?", (client_id,))
    conn.commit()
    conn.close()

def fetchMembershipDetails(client_ID):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MEMBERSHIP_DETAILS WHERE CLIENT_ID=?", (client_ID,))
    rows = cur.fetchone()
    conn.close()
    return rows

def chkIssuedStatusBook(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT ISSUED_IND FROM BOOK_DETAILS WHERE BOOK_ID=?", (book_id,))
    rows=cur.fetchone()
    conn.close()
    return rows

def chkIssuedBookOnClient(client_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT '1' FROM BOOK_DETAILS WHERE ISSUED_CLIENT_ID=?", (client_id,))
    rows = cur.fetchone()
    conn.close()
    return rows

def issueBook(book_id,issued_on_dt,issued_till_dt,issued_clientID):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE BOOK_DETAILS SET ISSUED_IND=?,ISSUED_ON_DT=?,ISSUED_TILL_DT=?,ISSUED_CLIENT_ID=? WHERE BOOK_ID=?",('Y',issued_on_dt,issued_till_dt,issued_clientID,book_id,))
    conn.commit()
    conn.close()

def returnBook(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE BOOK_DETAILS SET ISSUED_IND=?,ISSUED_ON_DT=?,ISSUED_TILL_DT=?,ISSUED_CLIENT_ID=? WHERE BOOK_ID=?",('N','9999-01-01','9999-01-01', '',book_id,))
    conn.commit()
    conn.close()

def chkOverdueBooks(current_dt):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
#Need to include a check on ISSUED_CLIENT_ID ='' as well in this query
    cur.execute("SELECT * FROM BOOK_DETAILS WHERE ISSUED_TILL_DT<?", (current_dt,))
    rows = cur.fetchall()
    conn.close()
    return rows

def totalBooks():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM BOOK_DETAILS")
    count = cur.fetchone()
    conn.close()
    return count

def totalMembers():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM MEMBERSHIP_DETAILS")
    count = cur.fetchone()
    conn.close()
    return count

def totalIssuedBooks():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM BOOK_DETAILS WHERE ISSUED_IND=?",('Y',))
    count = cur.fetchone()
    conn.close()
    return count

def totalOverdueBooks(current_dt):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM BOOK_DETAILS WHERE ISSUED_IND=? AND ISSUED_TILL_DT<?", ('Y',current_dt,))
    count = cur.fetchone()
    conn.close()
    return count

connect()