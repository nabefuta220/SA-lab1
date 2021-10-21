import pandas as pd
from src import data_file

if __name__=='__main__':
    df = pd.read_csv(data_file)
    print(df)