"""
データをcsvファイルに書き込む
"""
import pandas as pd
import csv

def write_file(datas:pd,file):  
    with open (file,'w') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow(data.split(','))