import mysql
from mysql import connector

from DBUtil import DBUtil

dbutil = DBUtil()
cursor = dbutil.getDBConnection()
cursor.execute("select event_id,ticket_price from events where event_name='Concert'")
rows = cursor.fetchone()
if rows:
    event_id, ticket_price = rows
    print(event_id,ticket_price)
