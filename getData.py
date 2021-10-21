import csv
import requests
from  src import URL,data_file
from src.getSample import get_sample
if __name__=='__main__':

    
    datas=get_sample(1000).replace("\"",'',-1).split("\n")
    datas.pop()#最後の改行を取り除く
    with open (data_file,'w') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow(data.split(','))
