from src.getSample import get_data
import pandas as pd
from scipy import stats


if __name__=='__main__':
    data=get_data(data_file='output/hypothesis.csv')
    data_column=data.select_dtypes(include='object').columns
    print(data_column)


    #クロス表を作る
    data1=pd.crosstab(data['race/ethnicity'],data['lunch'])
    print(data1)

    #イエーツの補正を加え、χ二乗検定を行う
    t,p,_,_=stats.chi2_contingency(data1)
    print(t,p)
