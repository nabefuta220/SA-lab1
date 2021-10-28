"""
母集団から小さなサイズのサンプルを取り出す
"""
import pandas as pd
import random as rd
from .getSample import get_data
def get_small_sample(size,population:pd):
    return population.sample(n=size)

