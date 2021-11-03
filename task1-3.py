import numpy as np
import pandas as pd
from pandas.core.tools import numeric
from scipy import stats

from src.getSample import get_data
from src.getSmallSample import get_small_sample


def CLT(popuation:pd,samples:int,sets:int):
	"""
	中心極限定理によって、母集団の平均と標準偏差を推定する

	Parameters
	----
	
	popuation : pandas
		母集団のデータ
	
	samples : int
		1回で取得する標本数
	
	sets:int
		サンプルを取得する回数


	returns
	------
	res: pandas
		各量的データと[平均、分散]のデータフレーム
	"""

	#すべての平均を取得
	means=[get_small_sample(samples,popuation,f"output/CLT_{i}.csv").mean(numeric_only=True) for i in range(sets)]

	#結合して転置する
	small_datas=pd.concat(means,axis=1).T

	#平均、分散の計算(平均は標本の平均値、分散は、標本の分散にサンプル数をかけたもの)
	mean=small_datas.mean(numeric_only=True)
	var=small_datas.var(numeric_only=True,ddof=0)*samples
	

	res=pd.concat([mean,var],axis=1).T
	res.index=['ave','var']
	return res

def interval_estimation(popuation:pd,samples:int,confidence_level:float):
	"""
	区間推定によって、標本平均と信頼度に応じた信頼区間(両側)を計算する

	Parameters
	----
	
	popuation : pandas
		母集団のデータ
	
	samples : int
		1回で取得する標本数
	
	confidence_level:float
		信頼度


	returns
	------
	res: pandas
		各量的データと信頼区間のデータフレーム
	"""
	#データを取得する
	data=get_small_sample(samples,popuation,f"output/IE.csv")
	#平均を求める
	ave=data.mean(numeric_only=True) 
	
	#誤差を求める	
	#数値データのみを取り出す
	data_c=data.select_dtypes(include='number')
	data_c=np.array(data_c)
	std_err=stats.sem(data_c)
	#print(std_err)

	res=pd.DataFrame(stats.t.interval(alpha=confidence_level,df=samples-1,loc=ave,scale=std_err))
	res.index=['down','up']
	res.columns=ave.index

	return res
	


sample_data=10
if __name__ == "__main__":
	data=get_data()
	
	print(f"CLT:\n{CLT(data,20,10)}")

	print(f"range:\n{interval_estimation(data,20,0.95)}")

	
	
	