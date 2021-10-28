import csv
import requests
from  src import URL,data_file as DF
from src.getSample import get_sample

def get_data(samples=1000, data_file=DF):
    datas=get_sample(samples).replace("\"",'',-1).split("\n")
    datas.pop()#最後の改行を取り除く
    with open (data_file,'w') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow(data.split(','))
if __name__=='__main__':

    
    get_data()