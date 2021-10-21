import csv
import requests
from  src import URL,data_file

if __name__=='__main__':
    res=requests.get(URL)
    print(res)
    
    datas=res.text.replace("\"",'',-1).split("\n")
    datas.pop()#最後の改行を取り除く
    with open (data_file,'w') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow(data.split(','))
