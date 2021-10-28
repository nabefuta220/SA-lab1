from src.getSample import get_data
from src.getSmallSample import get_small_sample

if __name__ == "__main__":
    data=get_data()
    for i in range(2):
        print(get_small_sample(10,data,f"output/sample{i}.csv"))
    
    