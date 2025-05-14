import mysql.connector



def connectToServer(): 
    connection = mysql.connector.connect(user='jinfengp',
                                     password='234083608',
                                     host='10.8.37.226',
                                     database='jinfengp_db')
    return connection

def askInput():
    connection = connectToServer()
    role = input("Login as Teacher [1] or Login as Student [2]: ")
    if int(role)==1:
        tid = input("Enter your Teacher ID: ")
        teacherSignIn(tid,connection)
    elif int(role)==2:
        sid = input("Enter your Student ID: ")
        studentSignIn(sid,connection)


def teacherSignIn(id,c): #WORK IN PROGRESS
    cursor = c.cursor()
    cursor.close()
    c.close()

def studentSignIn(id,c):
    cursor = c.cursor()
    query = 'call boowomp('+id+')'
    cursor.execute(query)
    printStudentSchedule(cursor)
    cursor.close()
    c.close()


def printStudentSchedule(list):
    for row in list:
        print("Period: " + str(row[3]))
        print("Course: " + str(row[1]))
        print("Room:" + str(row[2]))
        print("Teacher: " + str(row[4])+ " " + str(row[5]) + "\n")


askInput()