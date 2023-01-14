import mysql.connector
import time

from read_csv import read_csv_file_get_list

db = mysql.connector.connect(
    host="192.168.56.200",
    user="",
    password="",
    database="",
    auth_plugin='mysql_native_password'
)

my_cursor = db.cursor()


def create_table():
    create_table_sql = "CREATE TABLE Person " \
                       "(" \
                       "person_id int NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                       "discord VARCHAR(50) NOT NULL UNIQUE, " \
                       "investID VARCHAR(20), farmID VARCHAR(20),"\
                       "nfscID VARCHAR(20), " \
                       "joinDate DATETIME, " \
                       "leftDate DATETIME, " \
                       "isDelete BOOLEAN" \
                       ")"

    my_cursor.execute(create_table_sql)
    my_cursor.execute("DESCRIBE Person")
    for x in my_cursor:
        print(x)


def drop_table():
    pass


def insert_values_example():
    now = time.strftime('%Y-%m-%d %H:%M:%S')

    insert_value_sql = "INSERT INTO Person (discord, investID, farmID, nfscID, joinDate) VALUES (%s,%s,%s,%s,%s)"
    values = [("abc#233", "123", "1245", "3343", now),
              ("xxx#233", "123", "1245", "3343", now),
              ("eee#233", "123", "1245", "3343", now)]

    # my_cursor.execute(insert_value_sql, values)
    my_cursor.executemany(insert_value_sql, values)

    db.commit()


def insert_values_csv(csv_file):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    insert_value_sql = "INSERT INTO Person (discord, investID, farmID, nfscID, joinDate, isDelete) " \
                       "VALUES (%s,%s,%s,%s,%s,%s)"

    csv_values = read_csv_file_get_list(csv_file)

    values = []
    for item in csv_values:
        values.append((item[0], item[1], item[2], None, now, False))

    print(values)
    my_cursor.executemany(insert_value_sql, values)

    db.commit()


def insert_user(name):
    # 先查找用户是否存在
    result = search_db_with_name(name)
    if result == "not exist":
        now = time.strftime('%Y-%m-%d %H:%M:%S')

        insert_value_sql = "INSERT INTO Person (discord, joinDate, isDelete) " \
                           "VALUES (%s,%s,%s)"
        values = (name, now, False)

        my_cursor.execute(insert_value_sql, values)

        db.commit()
        return "add success"
    else:
        return "exist user"


def delete_user(discord):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    sql = "UPDATE Person set leftDate=%s,isDelete=True where discord=%s"

    values = (now, discord)

    my_cursor.execute(sql, values)

    db.commit()


def search_db_with_name(name):
    # print(name)
    sql = "SELECT * FROM Person WHERE discord=%s and not isDelete"
    my_cursor.execute(sql, (name,))
    result = my_cursor.fetchone()
    # print(result)
    if result:
        return result
    else:
        return "not exist"


class HandleDB(object):
    def __init__(self):
        self.db = mysql.connector.connect(
            host="192.168.56.200",
            user="alex",
            password="123456",
            database="mall",
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.db.cursor()

    def get_one_record(self, sql):
        self.conn.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_all_records(self, sql):
        self.conn.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_count(self, sql):
        # self.conn.commit()
        return self.cursor.execute(sql)

    def close_connections(self):
        self.cursor.close()
        self.conn.close()

    def update(self, sql):
        """
        CRUB,
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    # db = mysql.connector.connect(
    #     host="192.168.56.200",
    #     user="",
    #     password="",
    #     database="",
    #     auth_plugin='mysql_native_password'
    # )
    #
    # my_cursor = db.cursor()

    # create_table()
    insert_values_csv('test_id.csv')
    # delete_user('abc#233')
    print(search_db_with_name('克里#7528'))
    insert_user("ddd")

    my_cursor.close()
    db.close()


#
# select_sql('xxx#233')
#
# update_sql = "UPDATE Person set isDelete=True where discord='xxx#233'"
# my_cursor.execute(update_sql)
#
# db.commit()
# select_sql('xxx#233')
#
#
# select_sql_value = "SELECT * FROM Person"
# # my_cursor.execute(select_sql)
# # for item in my_cursor.fetchall():
# #     print(item)
#
