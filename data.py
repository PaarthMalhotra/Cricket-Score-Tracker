def insert_match_Details(value):
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="vasu",
        database = "cricket"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO Match_Details(Team1,Team2,Format,Total_Over,Inning_1,Inning_2,Win ) values(%s,%s,%s,%s,0,0,'None')"
    mycursor.execute(sql,value)
    mydb.commit()


def Identify_Over(info):
    if info == 'ODI':
        return 50
    elif info =='T20':
        return 20
    elif info == 'Test':
        return 90
    elif info == 'Friendly':
        return 1
    else:
        return 20

def get_id():

    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vasu",
        database="cricket"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM MATCH_DETAILS"
    mycursor.execute(sql)

    result = mycursor.fetchall()
    return result[-1][0]


def update_score_inning1(score_1,id):
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="vasu",
        database = "cricket"
    )

    mycursor = mydb.cursor()

    sql = f"UPDATE MATCH_DETAILS SET INNING_1 = INNING_1+{score_1}  WHERE ID = {id} "
    mycursor.execute(sql)
    mydb.commit()


def update_score_inning2(score_2,id):
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        password="vasu",
        database = "cricket"
    )

    mycursor = mydb.cursor()

    sql = f"UPDATE MATCH_DETAILS SET INNING_2 = INNING_2+{score_2} WHERE ID = {id} "
    mycursor.execute(sql)
    mydb.commit()