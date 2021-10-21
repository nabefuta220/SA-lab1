"""URLからn個分のデータを取得する"""
from . import URL

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
    return res.text