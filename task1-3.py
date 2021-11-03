
from src.CLT import CLT
from src.getSample import get_data
from src.intervalEstimation import interval_estimation

sample_data=10


if __name__ == "__main__":
	data=get_data()
	

	print(f"CLT:\n{CLT(data,20,10)}")

	print(f"range:\n{interval_estimation(data,20,0.95)}")

