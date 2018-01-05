import mysql.connector

conn_00 = mysql.connector.connect(user="root", password="1234#qwer", database="test_00")
conn_01 = conn_00.cursor()

# conn_01.execute("create table user(id VARCHAR (20) PRIMARY KEY ,name VARCHAR (20))")
# conn_01.execute("insert into USER (id,NAME ) VALUES (%s,%s)" , [1, "Jason Morata"])
# conn_00.commit()
# conn_01.close()


conn_01.execute("select * from USER where id = %s", (1,))
value_00 = conn_01.fetchall()
print(value_00)
conn_00.commit()
conn_01.close()
