import pymysql.cursors
import os
from multiprocessing import Process

def insert():
    connection = pymysql.connect(host='10.221.75.136',
                                 user='zm',
                                 password='0123456789',
                                 database='test',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        for _ in range(50):
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                for _ in range(0, 10000):
                    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            print('{} 开始commit'.format(os.getpid()))
            connection.commit()


p_list = []
for _ in range(8):
    p =Process(target=insert, args=())
    p.start()
    p_list.append(p)

for p in p_list:
    p.join()
