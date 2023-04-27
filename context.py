# import datetime
import time
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
        timeStamp, context, data, postID
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
        );""", [usr, cont, time.time(), ' '.join(data), postID])
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

def Comment(db, usr, cont, postId, msg):
    cur = db.cursor()
    comId = str(uuid.uuid4())
    res = cur.execute("""
        INSERT INTO comment VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        );      
        """,[usr,cont,postId,comId,msg, time.time()]) 
    
    # not done yet
def SeePost(db,pid):
    cur = db.cursor()
    res = cur.execute("""
        SELECT 
            timeStamp, context, data, postID
        FROM post
        WHERE post.postId = ?;   
        """, [pid])
    # Prints off the post before the comments
    for x in res.fetchall():
        print(x)
    print()
    res = cur.execute("""
        SELECT 
            users.name, comment.data, comment.timeStamp
        FROM post
        JOIN comment ON comment.postId = post.postId 
        JOIN users ON comment.userID = users.userID
        WHERE post.postId = ?;   
        """, [pid])
    for x in res.fetchall():
        print("User:",x[0],"\nMessage:",x[1],"\nTimestamp:",x[2])
        print()
             
def followAll(db,userId, userCont, otherName):
    cur = db.cursor()
    
    cur.execute("""
        INSERT INTO follows 
            SELECT u1.userID, ?, u2.userID, a.context
            FROM users as u1
            join users as u2 on u2.name = ?
            join accounts as a on a.userID = u2.userID
            WHERE u1.userID = ?
            ;     
    """, [userCont, otherName, userId])
    db.commit()