"""
データをcsvファイルに書き込む
"""
import pandas as pd
import csv
import os

def write_file(datas:pd,file):  
    os.makedirs(os.path.dirname(file), exist_ok=True)
    datas.to_csv(file,index=False)
    return