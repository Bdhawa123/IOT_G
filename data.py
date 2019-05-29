import MySQLdb
import mysql.connector
import datetime, serial



mydb = mysql.connector.connect(host ="localhost",user = "root",passwd="root", database="tempdb")
mycursor = mydb.cursor()

def showifitsworking():
	print("Please work")
	if mydb:
		print("connector working")
	else:
		print("Connector not working")
		
#	mycursor.execute("SHOW TABLES")		
#	for x in mycursor:
#		print(x)


#INSERT INTO THE DATABASE
def insert_db(val):
	Statement = "INSERT INTO MOTION_SENSOR(STATE,TIME,DATE) VALUES(%s,%s,%s)"
	
	curr_date = str(datetime.date.today()) 	#date
	current = datetime.datetime.now()		
	curr_time = str(current.hour)+":"+str(current.minute)		#time
	
	
	values = (val,curr_time,curr_date)	
	
	if mydb:
		mycursor.execute(Statement,values)
		mydb.commit() 	
		print(mycursor.rowcount,"records inserted")
		
	else:
		print("Connection error")
		







	 
	
	