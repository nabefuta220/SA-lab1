from src.getSample import get_data
from src.testContingency import test_contingency

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

