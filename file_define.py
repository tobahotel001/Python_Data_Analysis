#!/usr/bin/env python
# coding: utf-8

# In[5]:

# 抽象クラスを作成するために、Python標準モジュールabcからABCクラスとabstractmethodデコレータをインポート
from abc import ABC, abstractmethod
# データ整形のため、サードパーティライブラリpandasをインポート
import pandas as pd

# ABCのサブクラスを作成し、データ読み込みの抽象クラスとして定義
class FileReader(ABC):
    # abstractmethodを使って下記のメソッドを抽象メソッドとして宣言
    @abstractmethod
    # read_dataメソッドはインスタンス化できず、サブクラスでオーバーライドする必要がある
    def read_data(self):
        pass

# txtファイルを読み込むサブクラスを定義し、read_dataメソッドでtxtの読み込み機能を実装
class TxtFileReader(FileReader):
    # txtリーダーの属性を初期化、data_pathパラメータで読み込むファイルのパスを受け取る
    def __init__(self, data_path):
        self.data_path = data_path
        
    # 親クラスの抽象メソッドをオーバーライド
    def read_data(self):
        # pd.read_csvを使ってtxtファイルのデータを読み込む（データクレンジングや欠損補完は未実施）
        df = pd.read_csv(self.data_path, header=None, names=["date", "order_id", "money", "province"])
        return df

# jsonファイルを読み込むサブクラスを定義し、read_dataメソッドでjsonの読み込み機能を実装
class JsonFileReader(FileReader):
    # jsonリーダーの属性を初期化、data_pathパラメータで読み込むファイルのパスを受け取る
    def __init__(self, data_path):
        self.data_path = data_path

    # 親クラスの抽象メソッドをオーバーライド
    def read_data(self):
        df = pd.read_json(self.data_path)
        return df

if __name__ == "__main__":
    txt_file_reader = TxtFileReader("data/january_sales.txt")
    
    try:
        print(txt_file_reader.read_data())
    except Exception as e:
        print("ファイルの読み込みに失敗しました：", e)
    
    json_file_reader = JsonFileReader("data/february_sales.json")
    try:
        print(json_file_reader.read_data())
    except Exception as e:
        print("ファイルの読み込みに失敗しました：", e)





