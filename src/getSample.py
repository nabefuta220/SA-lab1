"""URLからn個分のデータを取得する"""
import pandas as pd
import requests

from . import URL
from . import data_file as DF


def get_sample(n:int=1000)->str:
    """
    URLからn個分のデータを取得する
    
    Parameters
    ----------
    n : int , defalt=1000
        取得するデータの個数
    
    Returns
    -------
    str : str
        取得したデータ(生のテキストファイル)
    """
    res=requests.get(f"{URL}&n={n}")
    print(res)
    print(res.text[:200])
    return res.text


def get_data(data_file:str=DF)->pd.DataFrame:
    """
    データファイルからpandasファイルに変換する

    Parameters
    ----------
    data_file : str , defalt = data_file
        取得したいデータのパス

    Returns
    -------
    data : pandas.Dataframe
        データ
    """
    csv_input = pd.read_csv(filepath_or_buffer=data_file,  sep=",")
    return csv_input
