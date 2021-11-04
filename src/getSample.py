"""URLからn個分のデータを取得する"""
from . import URL,data_file as DF
import pandas as pd
import requests
def get_sample(n:int=1000):
    """
    URLからn個分のデータを取得する
    
    Parameters
    ----------
    n : int ,defalt=1000
        取得するデータの個数
    
    Returns
    -------
    str :str
    取得したデータ(生のテキストファイル)
    """
    res=requests.get(f"{URL}&n={n}")
    print(res)
    print(res.text[:200])
    return res.text


def get_data(data_file=DF):
    """
    データファイルからpandasファイルに変換する
    """
    csv_input = pd.read_csv(filepath_or_buffer=data_file,  sep=",")
    return csv_input