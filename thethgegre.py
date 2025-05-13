import mysql.connector



def connectToServer(): 
    connection = mysql.connector.connect(user='jinfengp',
                                     password='234083608',
                                     host='10.8.37.226',
                                     database='jinfengp_db')
    return connection

def askInput():
    id = input("Enter Student ID: ")
    query = "call boowomp("+id+")"
    return query

def yummers():
    connection = connectToServer()
    query = askInput()
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print("Period: " + str(row[3]))
        print("Course: " + str(row[1]))
        print("Room:" + str(row[2]))
        print("Teacher: " + str(row[4])+ " " + str(row[5]) + "\n")
    cursor.close()
    connection.close()



yummers()