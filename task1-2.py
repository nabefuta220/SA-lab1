from src.getSample import get_data

if __name__ == "__main__":
    data=get_data()
    mean=data.mean(numeric_only=True)       #平均
    var=data.var(numeric_only=True,ddof=0)  #分散
    std=data.std(numeric_only=True,ddof=0)  #標準偏差
    corr=data.corr()                        #相関係数
    
    print(f"mean:\n{mean}")
    print(f"var:\n{var}")
    print(f"std:\n{std}")
    print(f"corr:\n{corr}")
