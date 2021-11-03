from src.getSample import get_data

if __name__ == "__main__":
    data=get_data()
    mean=data.mean(numeric_only=True)
    var=data.var(numeric_only=True,ddof=0) 
    std=data.std(numeric_only=True,ddof=0)
    corr=data.corr()
    print(f"mean:\n{mean}")#平均
    print(f"var:\n{var}")#分散
    print(f"std:\n{std}")#標準偏差
    print(f"corr:\n{corr}")#相関係数
    
