import uuid

def Create(db, usr, pd):
    cur = db.cursor()
    # Create a user
    usrID = str(uuid.uuid4())
    cur.execute("""
        INSERT INTO users VALUES
        (
            ?,
            ?,
            ?
        );""", [usrID, usr, pd])
    # print(res.fetchone())
    print ("built a user")

def ListUsers(db):
    cur = db.cursor()
    res = cur.execute ("""
        SELECT userID, name FROM users;             
    """)
    
    for x in res.fetchall():
        print(x)

def Login(db, usr, pd):
    cur = db.cursor()
    res = cur.execute("""
    SELECT 
        userID
    FROM
        users
    WHERE
        name = ? AND
         password = ?;
    """, [usr, pd])
    return res.fetchone()[0]
    