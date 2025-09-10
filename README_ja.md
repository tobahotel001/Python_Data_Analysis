# Python_Data_Analysis

## プロジェクト概要
このプロジェクトは、ローカルの TXT/JSON データを読み込み、クレンジングした後、MySQL データベースに保存し、日次売上データを可視化することを目的としています。

---

## ファイル構成
pandas&mysql/nodb_ver/
├── data_viz.ipynb          # 可視化用 Notebook / データ可視化 Notebook
├── data_viz.py             # データ可視化モジュール
├── file_define.ipynb       # データ読み込み Notebook
├── file_define.py          # Reader クラスとデータクレンジング
├── main.ipynb              # 実行用 Notebook
├── README.ipynb            # プロジェクト説明
├── sql_handle.ipynb        # データベース操作 Notebook
├── sql_handle.py           # データベース操作モジュール
└── data/
    ├── february_sales.json
    └── january_sales.txt

---

## 依存関係のインストール

仮想環境の使用を推奨：

```powershell
# Anaconda
conda create -n pandas_mysql python=3.12
conda activate pandas_mysql

# または venv
python -m 

Python ライブラリをインストール：
pip install pandas matplotlib pymysql注意：MySQL がインストール済みで、接続可能であることを確認してください。

使用方法
1. データ読み込みとクレンジング
from file_define import TxtFileReader, JsonFileReader
import pandas as pd

txt_reader = TxtFileReader("data/january_sales.txt")
json_reader = JsonFileReader("data/february_sales.json")

df_txt = txt_reader.read_data()
df_json = json_reader.read_data()

df = pd.concat([df_txt, df_json], ignore_ind
2. MySQL にデータをインポートefrom sql_handle import mysql_connection, create_database, use_database, create_sales_table, insert_data

# パスワードは自分の MySQL に合わせて変更してください
conn = mysql_connection(password="YOUR_PASSWORD")
create_database(conn, "test_db")
use_database(conn, "test_db")
create_sales_table(conn)
insert_data(conn, df)
conn.
3. データ可視化
from data_viz import plot_sales_by_day

plot_sales_by_day(df

注意点

. file_define.py の Reader クラスは、自動的にデータクレンジングを行います

. データベースにインポートする前に、欠損値や異常値がないことを確認してください

. Jupyter Notebook での実行を推奨します)
close()
x=True)

venv venv
.\venv\Scripts\activate
