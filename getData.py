import csv
import requests

URL='http://roycekimmons.com/system/generate_data.php?dataset=exams&n=1000'
write_file='data.csv'

if __name__=='__main__':
    res=requests.get(URL)
    print(res)
    
    datas=res.text.replace("\"",'',-1).split("\n")
    datas.pop()#最後の改行を取り除く
    with open (write_file,'w') as f:
        writer = csv.writer(f)
        for data in datas:
            writer.writerow(data.split(','))
