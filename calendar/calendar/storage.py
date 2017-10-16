import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, task_massage, zagolovok, status, created FROM calendar
"""

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_URL_BY_MASSEGE = SQL_SELECT_ALL+ " WHERE task_massage="

SQL_SELECT_URL_BY_ZAGOLOVOK = SQL_SELECT_ALL + " WHERE zagolovok="

SQL_SELECT_URL_BY_STATUS = SQL_SELECT_ALL + " WHERE status="

SQL_INSERT_TASK = """
INSERT INTO calendar (status, zagolovok, task_massage) VALUES (?)
"""

SQL_UPDATE_MASSAGE = """
    APDATE calendar SET task_massage=? WHERE id=?
"""
SQL_UPDATE_STATUS = """
    APDATE calendar SET status? WHERE id=?
"""
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect(db_name=None):
	if db_name is None:
		db_name = ':memory:'

	conn = sqlite3.connect(db_name)
	return conn

def initialize(conn, creation_shema):
    with conn, open(creation_shema) as f:
        conn.executescript(f.read())

def print_task(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()

def new_task(conn):
    if not task_massage:
        return
    with conn:
        found = find_task(conn, task_massage)
        if found:
            return found.get('task_massage')

        cursor = conn.execute(SQL_INSERT_TASK, (task_massage, zagolovok))
        pk = cursor.lastrowid
        conn.execute(SQL_UPDATE_MASSAGE, (task_massage, zagolovok))

        return task_massage

def mod_task(conn, pk):
    with conn:
        conn.execute(SQL_UPDATE_MASSAGE, (task_massage, pk))
def finish_task(conn, short_url):
    with conn:
        conn.execute(SQL_UPDATE_STATUS, (status, pk))

def repeat_task(conn, ):
    with conn:
        conn.execute(SQL_UPDATE_STATUS, (status, pk))

def find_task(conn, zagolovok):
    with conn:
        cursor = conn.execute(SQL_SELECT_ZAD_BY_ZAGOLOVOK, (zagolovok, task_massage, status,))
        return cursor.fetchone()
