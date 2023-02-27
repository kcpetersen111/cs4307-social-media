def Create(db, usr, password):
    cur = db.cursor()
    # Create a user
    cur.execute("""
        INSERT INTO users VALUES
        (
            ?,
            ?
        );""", [usr, password])
    # print(res.fetchone())
    print ("built a user")

def ListUsers(db):
    cur = db.cursor()
    res = cur.execute ("""
        SELECT userID FROM users;             
    """)
    
    for x in res.fetchall():
        print(x)