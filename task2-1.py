from src.getSample import get_data
from src.phothesis import linked_phothesis, unlinked_phothesis

if __name__=='__main__':
    data=get_data(data_file='output/hypothesis.csv')
    data_column=data.select_dtypes(include='number').columns

    #対応ありの仮説検定
    print("linked hyothesis:\n")
    #2科目を抽出する
    for i in range(len(data_column)):
        for j in range(i+1,len(data_column)):
            linked_phothesis(data,[data_column[i],data_column[j]],0.05)

    #対応なしの仮説検定
    print("unlinked hyothesis:\n")
    #性別でグループ分けする
    target='gender'
    data_column=data[target].unique()
    #2群を抽出する
    for i in range(len(data_column)):
        for j in range(i+1,len(data_column)):
            unlinked_phothesis(data,target,[data_column[i],data_column[j]],0.05)
