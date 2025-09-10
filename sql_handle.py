#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 导入第三方库
import pandas as pd
import pymysql

# 连接MySQL模块
def mysql_connection(host = "localhost", port= 3306, user= "root", password = "", database = None, autocommit = True):
    """连接到MySQL，并返回连接对象"""
    try:
        conn = pymysql.connect(host = host, port = port,user = user,password = password,database = database,autocommit = autocommit)

    except Exception as e:
        print("bad connnection", e)
        return None

    return conn

def create_database(conn, db_name):
    """创建数据库，支持中文和表情符号"""
    cursor = conn.cursor()
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci" 
    )

def use_database(conn, db_name):
    """选择需要使用的数据库"""
    conn.select_db(db_name)

def create_sales_table(conn):
    """创建sales_data表"""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS sales_data" )
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_data(
        date DATE,
        order_id VARCHAR(20),
        money float,
        province VARCHAR(20)
        )
    """)

def insert_data(conn, df):
    """向sales_data表里面插入df数据"""
    cursor = conn.cursor()
    insert_sql = "INSERT INTO sales_data(date, order_id, money, province) VALUES(%s, %s, %s, %s)"
    data_tuples = [tuple(row) for row in df.values]
    cursor.executemany(insert_sql, data_tuples)

def read_sales_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales_data")
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns = columns)
    return df

if __name__ =="__main__":
    mysql_connection(password = "19720924")


# In[ ]:




