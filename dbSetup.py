#!/usr/bin/env python3
import sqlite3
def Migration():  
    con = sqlite3.connect("social.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        userID TEXT PRIMARY KEY,
        password TEXT
    );""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        userID TEXT,
        context TEXT,
        follows TEXT,
        name TEXT,
        label TEXT,
        PRIMARY KEY (userID, context)
    );""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS follows (
        fromUserID TEXT,
        fromContext TEXT,
        toUserID TEXT,
        toContext TEXT,
        PRIMARY KEY (fromUserID, fromContext, toUserID, toContext)
    );""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS post (
        userID TEXT,
        context TEXT,
        timeStamp DATETIME,
        data TEXT,
        postID TEXT,
        PRIMARY KEY (postID)
    );""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS comment (
        userID TEXT,
        context TEXT,
        postID TEXT,
        commentID TEXT,
        data TEXT,
        timeStamp TEXT,
        PRIMARY KEY (commentID)
    );""")
    
    cur.close()
    return con