
from src.CLT import CLT
from src.getSample import get_data
from src.intervalEstimation import interval_estimation

import argparse

def input_data():
	arg=argparse.ArgumentParser()
	arg.add_argument("samples",help="一度の取得するサンプル数",type=int)
	arg.add_argument("sets",help="取得する回数",type=int)
	arg.add_argument("CL",help="信頼度(0 ~ 1)",type=float)
	parse=arg.parse_args()

	return (parse.samples,parse.sets,parse.CL)

if __name__ == "__main__":
	data=get_data()
	
	samples,sets,CL=input_data()

	print(f"samples:{samples}, sets:{sets}")
	print(f"CLT:\n{CLT(data,samples,sets)}\n")

	print(f"samples:{samples}, confience_level:{CL}")
	print(f"interval:\n{interval_estimation(data,samples,CL)}")

