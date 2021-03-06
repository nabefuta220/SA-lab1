"""
中心極限定理によって、点推定を行う
"""
import pandas as pd

from src.getSmallSample import get_small_sample


def CLT(popuation:pd.DataFrame,samples:int,sets:int)->pd.DataFrame:
	"""
	中心極限定理によって、母集団の平均と標準偏差を推定する

	Parameters
    ----------
	popuation : pandas.Dataframe
		母集団のデータ
	samples : int
		1回で取得する標本数
	sets : int
		サンプルを取得する回数

	Returns
	--------
	res: pandas.Dataframe
		各量的データと[平均、分散]のデータフレーム
	"""

	#すべての平均を取得
	means=[get_small_sample(samples,popuation,f"output/CLT/sample_{i}.csv").mean(numeric_only=True) for i in range(sets)]

	#結合して転置する
	small_datas=pd.concat(means,axis=1).T

	#平均、分散の計算(平均は標本の平均値、分散は、標本の分散にサンプル数をかけたもの)
	mean=small_datas.mean(numeric_only=True)
	var=small_datas.var(numeric_only=True,ddof=0)*samples
	
	res=pd.concat([mean,var],axis=1).T
	res.index=['ave','var']
	return res
