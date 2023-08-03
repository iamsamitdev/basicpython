import pymysql.cursors


# Function connect db and return conection
def getConnection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='pythontestdb',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )


# print(getConnection())
