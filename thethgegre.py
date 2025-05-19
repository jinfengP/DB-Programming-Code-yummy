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
        action = input("See Schedule [1] or Select Class [2]: ")
        teacherSignIn(tid,connection,action)
    elif int(role)==2:
        sid = input("Enter your Student ID: ")
        action = input("See Schedule [1] or Select Class [2] or View Overall [3]: ")
        studentSignIn(sid,connection,action)
    else:
        print("Invalid Option!")


def teacherSignIn(id,c,act):
    act=int(act)
    cursor = c.cursor()
    if act==1:
        query = 'call teacher_boowomp('+id+');'
        cursor.execute(query)
        printTeacherSchedule(cursor)
    elif act==2:
        print('WIP')
    else:
        print("Invalid Option!")
    cursor.close()
    c.close()

def studentSignIn(id,c,act):
    act=int(act)
    cursor = c.cursor()
    if act==1:
        query = 'call boowomp('+id+');'
        cursor.execute(query)
        printStudentSchedule(cursor)
    elif act==2:
        query = 'call boowomp('+id+');'
        cursor.execute(query)     
        i=1
        for row in cursor:
            print("Period " + str(row[3]) + " - " + str(row[1]) + " - " + str(row[2]) + " [" + str(i) + "]")
            i+=1
        input("Which class do you want to view?: ")
    elif act==3:
        print('WIP')
    else:
        print("Invalid Option!")
    cursor.close()
    c.close()


def printStudentSchedule(list):
    print("")
    for row in list:
        print("Period: " + str(row[3]))
        print("Course: " + str(row[1]))
        print("Room:" + str(row[2]))
        print("Teacher: " + str(row[4])+ " " + str(row[5]) + "\n")

def printTeacherSchedule(list):
    print("")
    for row in list:
        print("Period: " + str(row[2]))
        print("Offering ID: " + str(row[0]))
        print("Course: " + str(row[3]))
        print("Room: " + str(row[5]) + "\n")

askInput()