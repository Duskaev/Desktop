import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, task_massage, FROM calendar
"""

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_URL_BY_MASSEGE = SQL_SELECT_ALL+ " WHERE task_massage=?"

SQL_INSERT_NAME = """
    INSERT INTO calendar (task_name) VALUES (?)
"""

SQL_UPDATE_SHORT_START_TIME = """
    APDATE calendar SET time_task_start=? WHERE id=?
"""

SQL_UPDATE_SHORT_STOP_TIME = """
    APDATE calendar SET time_task_stop=? WHERE id=?
"""


def connect(db_name=None):
	if db_name is None:
		db_name = ':memory:'

	conn = sqlite3.connect(db_name)
#магия
	return conn

def initialize(conn, creation_shema):
    with conn, open(creation_shema) as f:
        conn.executescript(f.read())
#запускает БД

def print_task(conn, url, domain=''):
    """выводит список задач"""

def new_task(conn):
	"""Новая задача"""

def mod_task(conn, pk):
	"""редактировать задачу"""

def finish_task(conn, short_url):
	"""завершить задачу""""

def repeat_task(conn, ):
    """Начать задачу заново"""
