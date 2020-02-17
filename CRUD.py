import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', password='', db='tkinter')
mycursor= conn.cursor()
print('database connected')

#######Insert Query#########
#sql = "INSERT INTO student ( student_ID,student_name,student_phone,student_email) VALUES (%s, %s, %s, %s)"
#val = ("04","noman","98343","hdgsb")
#mycursor.execute(sql, val)


#######Update Query#########
#sql = "UPDATE student SET student_name = 'shafat' WHERE student_ID = '04'"
#mycursor.execute(sql)


#######View Query###########
#sql="Select * from student"
#mycursor.execute(sql)
#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)


########Delete Query#########

sql="Delete from student where student_ID=04"
mycursor.execute(sql)

conn.commit()


print("inserted successfully")