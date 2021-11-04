import pandas
from src import data_file as DF
from src.getSample import get_sample
from src.writeFile import write_file
def get_data(samples=1000, data_file=DF):
    """
    データをcsvファイルに書き込む
    """
    datas=get_sample(samples).replace("\"",'',-1)
    #datas.pop()#最後の改行を取り除く
    print("data:"+data_file)
    
    with open(data_file ,"w") as f:
        for data in datas:
            f.write(data)
            pass
if __name__=='__main__':
    get_data()
    get_data(samples=50,data_file='output/hypothesis.csv')