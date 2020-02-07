import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='CS485',
                             password='WinonaState',
                             db='CS485',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * from Students"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
            print ("Student ID: " + str(result['StudentID'])) # convert the integer ID into a string before concatenating
            print ("First Name: " + result['FirstName'])
            print ("Last Name: " + result['LastName'])
            print ("Age: " + str(result['Age'])) # convert the integer Age into a string before concatenating
            print ("")
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
