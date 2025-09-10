## 日本語版 README_ja

```markdown
# pandas&mysql/nodb_ver

## プロジェクト概要
このプロジェクトは、ローカルの TXT/JSON データを読み込み、クレンジングした後、MySQL データベースに保存し、日次売上データを可視化することを目的としています。

---

## ファイル構成
pandas&mysql/nodb_ver/
├── data_viz.ipynb          # 可视化用 Notebook / 可視化用 Notebook
├── data_viz.py             # 数据可视化模块 / データ可視化モジュール
├── file_define.ipynb       # 数据读取 Notebook / データ読み込み Notebook
├── file_define.py          # Reader 类和数据清洗 / Reader クラスとデータクレンジング
├── main.ipynb              # 主 Notebook / 実行用 Notebook
├── README.ipynb            # 项目说明 / プロジェクト説明
├── sql_handle.ipynb        # 数据库操作 Notebook / データベース操作 Notebook
├── sql_handle.py           # 数据库操作模块 / データベース操作モジュール
└── data/
    ├── february_sales.json
    └── januar


---

## 依存関係のインストール

仮想環境の使用を推奨：

```powershell
# Anaconda
conda create -n pandas_mysql python=3.12
conda activate pandas_mysql

# または venv
python -m venv venv
.\venv\Scripts\activate

Python ライブラリをインストール：
pip install pandas matplotlib pymysql
注意：MySQL がインストール済みで、接続可能であることを確認してください。

使い方
1. データ読み込みとクレンジング
from file_define import TxtFileReader, JsonFileReader
import pandas as pd

txt_reader = TxtFileReader("data/january_sales.txt")
json_reader = JsonFileReader("data/february_sales.json")

df_txt = txt_reader.read_data()
df_json = json_reader.read_data()

df = pd.concat([df_txt, df_json], ignore_in
d2. MySQL にデータをインポート
from sql_handle import mysql_connection, create_database, use_database, create_sales_table, insert_data

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
file_define.py の Reader クラスは、自動的にデータクレンジングを行います。
データベースにインポートする前に、欠損値や異常値がないことを確認してください。
Jupyter Notebook での実行を推奨します。)
close()
ex=True)



y_sales.txt

