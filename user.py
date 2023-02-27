def Create(db, usr, pd):
    cur = db.cursor()
    # Create a user
    cur.execute("""
        INSERT INTO users VALUES
        (
            ?,
            ?
        );""", [usr, pd])
    # print(res.fetchone())
    print ("built a user")

def ListUsers(db):
    cur = db.cursor()
    res = cur.execute ("""
        SELECT userID FROM users;             
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
        userID = ? AND
         password = ?;
    """, [usr, pd])
    return res.fetchone()[0]
    