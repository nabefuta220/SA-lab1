import pandas
from src import data_file as DF
from src.getSample import get_sample
from src.writeFile import write_file
def get_data(samples:int =1000, data_file:str=DF):
    """
    データをcsvファイルに書き込む

    Parameters
    ----------
    samples : int , defalt = 1000
        取得する標本数
    data_file : str , defalt = src.data_file
        書き込むcsvファイル
    """
    datas=get_sample(samples).replace("\"",'',-1)
    print("data:"+data_file)
    
    with open(data_file ,"w") as f:
        for data in datas:
            f.write(data)
            pass
if __name__=='__main__':
    get_data()
    get_data(samples=50,data_file='output/hypothesis.csv')