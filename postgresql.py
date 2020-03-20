import psycopg2
import sys
from helpers import DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME
from sqlalchemy import create_engine 

def pgConnect():
	#Define our connection string
	conn_string = f"host={DB_HOST} dbname={DB_NAME} user={DB_USERNAME} password={DB_PASSWORD}"
 
	# print the connection string we will use to connect
	print(f"Connecting to database\n	->{conn_string}")
 
	# get a connection, if a connect cannot be made an exception will be raised here
	try: 
		connection = psycopg2.connect(conn_string)
	
	except:
		print('Bad connection')

	return connection
    #print(connection)
    #return conn
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	#cursor = conn.cursor()
	#print("Connected!\n")

    #return cursor
 
def pgEngine():
	engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}')
	return engine

if __name__ == "__main__":
	pgConnect()