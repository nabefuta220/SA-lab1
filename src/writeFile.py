"""
データをcsvファイルに書き込む
"""
import pandas as pd
import csv

def write_file(datas:pd,file):  
    datas.to_csv(file,index=False)
    return