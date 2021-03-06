import matplotlib.pyplot as plt

from src.getSample import get_data

if __name__=='__main__':
    df=get_data()
    
    scales=['math score','reading score','writing score']
    data=df[scales]
    for i in scales:
        fig = plt.figure()
        plt.title(f"{i}")
        plt.hist(data[i])
        fig.savefig(f"output/{i}_distribute.png")