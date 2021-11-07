from typing import List, Tuple

import numpy as np
from numpy.core.fromnumeric import var
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
    (res,t_value)
    res: bool
        2つの量的データに差があるか
        Trueならば 2つの量的データに差がないとはいえない
        Falseならば2つの量的データに差がないと言える
    prob: float
        t-統計量
    """
    #データを抽出する
    ndata=data[index].diff(axis=1).dropna(axis=1)
    
    # 1標本の検定を行う
    t,p=stats.ttest_1samp(ndata, 0)
    p=p[0]
    accept = p >(significance_level/2)
    print(f"{index[0]} vs {index[1]}: \n t-value : {t[0]} \n p-value : {p} \n -> {'accepted' if accept else 'rejected'}")

    return (accept,t)

def unlinked_phothesis(data:pd.DataFrame,varable: str,index:List[str],significance_level : float)->Tuple[bool,float]:
    """
    対応がないデータについて、両側検定によって、2つのグループのデータに差があるか判定する

    
    Parameters
    ----------
    data : pandas.Dataframe
        検定を行う標本
    varable : str
        比較したいデータの変数
    index : [str,str]
        比較する標本の値
    significance_level :float
        有意水準

    Returns
    ------
    res: bool
        2つの量的データに差があるか
        Trueならば 2つの量的データに差がないとはいえない
        Falseならば2つの量的データに差がないと言える
    prob: float
        t-統計量
    """
    #データを抽出する
    indexs=data.select_dtypes(include='number').columns
    data1 = data[data[varable]== index[0]].select_dtypes(include='number')
    data2 = data[data[varable]== index[1]].select_dtypes(include='number')



    if len(data1)==0:  
        raise KeyError(index[0])
    if len(data2)==0:  
        raise KeyError(index[1])
    
    t_value,prob=stats.ttest_ind(data1,data2)
    print(t_value)
    print(prob)
    res=pd.DataFrame([t_value,[True if i > significance_level else False for i in prob]])
    res.columns=indexs
    res.index=['t_value','accepted']
    print(res)
    print(f"{index[0]} vs {index[1]}:\n")
    for j,i in enumerate(indexs):
        print(f"({i}):\n t-value : {t_value[j]}\n p-value : {prob[j]} \n-> {'accepted' if res.loc['accepted',i] else 'rejected'} ")
    return res

    
if __name__=='__main__':
    data=get_data(data_file='output/hypothesis.csv')
    data_column=data.select_dtypes(include='number').columns

    print("linked hyothesis:\n")
    #2科目を抽出する
    for i in range(len(data_column)):
        for j in range(i+1,len(data_column)):
            linked_phothesis(data,[data_column[i],data_column[j]],0.05)
    print("unlinked hyothesis:\n")
    unlinked_phothesis(data,'parental level of education',['high school', 'some college'],0.05)