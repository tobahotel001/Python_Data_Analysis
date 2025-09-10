#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 为了创建抽象类，从python内置模块abc导入ABC类和 abstactmethod装饰器
from abc import ABC, abstractmethod
# 为了整理数据，导入第三方库pandas
import pandas as pd

# 创建一个ABC的子类，定义为数据读取的抽象类
class FileReader(ABC):
    # 使用abstractmethod声明下面的方法为抽象方法
    @abstractmethod
    # read_data方法无法实例化必须通过子类的改写才能实例化
    def read_data(self):
        pass

# 定义一个读取txt文件的子类,通过read_data方法实现txt的读取功能
class TxtFileReader(FileReader):
    # 初始化txt读取器的属性,接收一个参数 data_path，表示要读取的文件路径
    def __init__(self, data_path):
        self.data_path = data_path
        
    # 改写父类的读取文件的抽象方法
    def read_data(self):
        # 使用pd.read_csv方法读取txt文件的数据(未加入数据清洗和补缺流程)
        df = pd.read_csv(self.data_path, header = None, names = ["date", "order_id", "money", "province"])
        return df

# 定义一个读取json文件的子类,通过read_data方法实现json文件的读取功能
class JsonFileReader(FileReader):
    # 初始化json读取器的属性，接收一个data_path参数表示要读取文件的路径
    def __init__(self, data_path):
        self.data_path = data_path

    # 改写父类读取文件的抽象方法
    def read_data(self):
        df = pd.read_json(self.data_path)
        return df

if __name__ == "__main__":
    txt_file_reader = TxtFileReader("data/january_sales.txt")
    
    try:
        print(txt_file_reader.read_data())
    except Exception as e:
        print("读取文件失败：", e)
    
    json_file_reader = JsonFileReader("data/february_sales.json")
    try:
        print(json_file_reader.read_data())
    except Exception as e:
        print("读取文件失败：", e)



        
        




        
    
    


# In[ ]:




