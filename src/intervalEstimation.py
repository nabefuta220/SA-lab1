"""区間推定を行う"""
import pandas as pd
from scipy import stats

from src.getSmallSample import get_small_sample


def interval_estimation(popuation:pd.DataFrame,samples:int,confidence_level:float)->pd.DataFrame:
	"""
	区間推定によって、標本平均と信頼度に応じた信頼区間(両側)を計算する

	Parameters
	----------
	
	popuation : pandas.Dataframe
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

	std_err=stats.sem(data_c)

	res=pd.DataFrame(stats.t.interval(alpha=confidence_level,df=samples-1,loc=ave,scale=std_err))
	res.index=['down','up']
	res.columns=ave.index

	return res
	