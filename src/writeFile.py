"""
データをcsvファイルに書き込む
"""
import csv
import os

import pandas as pd


def write_file(datas:pd.DataFrame,file:str):  
    """
    データをscvファイルに保存する

    Parameters
    ----------
    datas : pandas.Dataframe
        データ
    file : str
        保存するファイルのパス
    """
    os.makedirs(os.path.dirname(file), exist_ok=True)
    datas.to_csv(file,index=False)

