#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 模块化可视功能
import matplotlib.pyplot as plt
import pandas as pd

def plot_sales_by_day(df):
    grouped = df.groupby("date")["money"].sum().sort_index()

    plt.figure(figsize = (10, 6))
    grouped.plot(kind = "bar", color = "skyblue")
    plt.title("Daily Sales")
    plt.xlabel("DATE")
    plt.ylabel("SALES")
    plt.tight_layout()
    plt.show()

