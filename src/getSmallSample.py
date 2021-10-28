"""
母集団から小さなサイズのサンプルを取り出す
"""
import pandas as pd
from .writeFile import write_file
def get_small_sample(size,population:pd, save_as=""):
    data=population.sample(n=size)
    if save_as!="":
        write_file(data,save_as)
    return data
