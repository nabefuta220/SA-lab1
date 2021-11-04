from typing import List, Tuple

import numpy as np
import pandas as pd
from pandas.io.pytables import Term
from scipy import stats

from src.getSample import get_data


def linked_phothesis(data:pd.DataFrame,index:List[str],significance_level : float)->Tuple[bool,float]:
    """
    対応がつけられたデータについて、両側検定によって、2つの量的データに差があるか判定する

    
    Parameters
    ----------
    data : pandas.Dataframe
        検定を行う標本

    index : [str,str]
        比較したい量的データ
    significance_level :float
        有意水準

    Returns
    ------
    res: bool
        2つの量的データに差があるか
        Trueならば 2つの量的データに差がないとはいえない
        Falseならば2つの量的データに差がないと言える
    prob: float
        有意確率の値
    """
    #データを抽出する
    ndata=data[index].diff(axis=1).dropna(axis=1)
    
    # 1標本の検定を行う
    t,p=stats.ttest_1samp(ndata, 0)
    p=p[0]
    accept = p >(significance_level/2)
    print(f"{index[0]} vs {index[1]}: \n t-value : {t[0]} \n p-value : {p} \n -> {'accepted' if accept else 'rejected'}")

    return (accept,p)


    
if __name__=='__main__':
    data=get_data(data_file='output/hypothesis.csv')
    data_column=data.select_dtypes(include='number').columns
    print("linked hyothesis:\n")
    #2科目を抽出する
    for i in range(len(data_column)):
        for j in range(i+1,len(data_column)):
            linked_phothesis(data,[data_column[i],data_column[j]],0.05)
