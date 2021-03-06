import MySQLdb
import mysql.connector
import datetime, serial



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



mydb = mysql.connector.connect(host ="localhost",user = "root",passwd="root", database="tempdb")
mycursor = mydb.cursor()

device ="/dev/ttyACM0"
#device ="/dev/ttyAMA0"
arduino = serial.Serial(device,9600)
print("This should be working in a way")
while(1):
	if (arduino.in_waiting>0):
		line = arduino.readline()
		print(int(line))
		if(int(line)==1):
			print("motion detected")
			insert_db("ON")
		else:
			print("motion turned off")
			insert_db("OFF")


	
	
