#!/usr/bin/env python
# coding: utf-8

# サードパーティライブラリのインポート
import pandas as pd
import pymysql

# MySQL接続モジュール
def mysql_connection(host="localhost", port=3306, user="root", password="", database=None, autocommit=True):
    """MySQLに接続し、接続オブジェクトを返す"""
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            autocommit=autocommit
        )
    except Exception as e:
        print("接続に失敗しました", e)
        return None
        
    return conn

def create_database(conn, db_name):
    """データベースを作成（日本語や絵文字をサポート）"""
    cursor = conn.cursor()
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    )

def use_database(conn, db_name):
    """使用するデータベースを選択"""
    conn.select_db(db_name)

def create_sales_table(conn):
    """sales_dataテーブルを作成"""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS sales_data")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_data(
            date DATE,
            order_id VARCHAR(20),
            money FLOAT,
            province VARCHAR(20)
        )
    """)

def insert_data(conn, df):
    """sales_dataテーブルにDataFrameのデータを挿入"""
    cursor = conn.cursor()
    insert_sql = "INSERT INTO sales_data(date, order_id, money, province) VALUES(%s, %s, %s, %s)"
    data_tuples = [tuple(row) for row in df.values]
    cursor.executemany(insert_sql, data_tuples)

def read_sales_data(conn):
    """sales_dataテーブルから全データを取得し、DataFrameに変換"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales_data")
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    return df

if __name__ == "__main__":
    # パスワードはご自身で設定してください
    mysql_connection(password="ここにパスワードを設定")
