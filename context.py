import datetime
import uuid

def Create(db, usr, cont):
    cur = db.cursor()
    cur.execute("""
        INSERT INTO accounts VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?
        );""", [usr, cont, "I don't", "know what", "this is for"])
    print ("created ", cont)

def SwitchContext(db, usr, cont):
    cur = db.cursor()
    res = cur.execute("""
    SELECT 
        context
    FROM
        accounts
    WHERE
        userID = ? AND
        context = ?;
    """, [usr, cont])
    try:
        return res.fetchone()[0]
    except:
        return None

def SeeFeed(db, usr, cont):
    cur = db.cursor()
    res = cur.execute("""
    SELECT 
        timeStamp, context, data
    FROM
        follows JOIN post ON 
            toUserID = userID AND
            toContext = context
    WHERE
        fromUserID = ? AND
        fromContext = ?
    ORDER BY
        timeStamp DESC
    LIMIT
        10;
    """, [usr, cont])

    for x in res.fetchall():
        print(x)

def Post(db, usr, cont, data):
    postID = str(uuid.uuid4())
    cur = db.cursor()
    cur.execute("""
        INSERT INTO post VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?
        );""", [usr, cont, datetime.datetime.now(), ' '.join(data), postID])
    print ("posted")

def Follow(db, usr, cont, otherUsr, otherCont):
    cur = db.cursor()
    cur.execute("""
        INSERT INTO follows VALUES
        (
            ?,
            ?,
            ?,
            ?
        );""", [usr, cont, otherUsr,otherCont])
    print ("following ", usr)

def List(db, usr):
    cur = db.cursor()
    res = cur.execute ("""
        SELECT context FROM accounts WHERE userID = ?;             
    """, [usr])
    
    for x in res.fetchall():
        print(x)
