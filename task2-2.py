from typing import List
from src.getSample import get_data
import pandas as pd
from scipy import stats

def test_contingency(data:pd.DataFrame,index:List[str],significance_level : float):
    """
    イエーツの補正を加えてχ二乗検定を用いて、表に偏りがないか判定する

    Paramters
    ---------
    data:pandas.DataFrame
        検定を行う標本
    index: [str,str]
        関係があるか調べたい変数
    significance_level :float
        有意水準

    Returns
    -------
    chi_value : float
        χ二乗値
    accepted : bool
        2つの変数に関係があるか
        Trueならば 2つの変数に関係があるとは言えない
        Falseならば2つの変数に関係があると言える
    """
    #クロス表を作る
    data1=pd.crosstab(data[index[0]],data[index[1]])

    #イエーツの補正を加え、χ二乗検定を行う
    chi_value,p,_,_=stats.chi2_contingency(data1)
    accepted=True if p >significance_level else False
    print(f"{index[0]} & {index[1]}:\nchi_vale : {chi_value} \nprob : {p}\n->{'accepted' if accepted else 'rejected'}")
    return (chi_value,accepted)

if __name__=='__main__':
    data=get_data(data_file='output/hypothesis.csv')
    #変数を取得する
    data_column=data.select_dtypes(include='object').columns
    exclude=['gender','test preparation course']

    #2変数を抽出する
    for i in range(len(data_column)):
        if data_column[i] in exclude:
            continue
        for j in range(i+1,len(data_column)):
            if data_column[j] in exclude:
                continue
            test_contingency(data,[data_column[i],data_column[j]],0.05)

