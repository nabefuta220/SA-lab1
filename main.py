import pandas as pd
from src import data_file
from src.getSample import get_data
from src.getSmallSample import get_small_sample
if __name__=='__main__':
    res=get_data()
    print(res)
    print(get_small_sample(10,res))
    print(res.dtypes)
    pass