"""
母集団から小さなサイズのサンプルを取り出す
"""
import pandas as pd

from .writeFile import write_file


def get_small_sample(size:int,population:pd.DataFrame, save_as:str="")->pd.DataFrame:
    """
    標本を取り、それをファイルに保存する

    Parameters
    ----------
    size : int
        標本を取る数
    population : pandas.Dataframe
        母集団
    save_as : str , defalt = ""
        取得した標本を保存する先
        何も指定していない場合は保存しない

    Returns
    -------
    data : pandas.Dataframe
        取得した標本
    """
    data=population.sample(n=size)
    if save_as!="":
        write_file(data,save_as)
    return data
