"""
検定を行う
"""


def linked_phothesis(data:pd.DataFrame,index:List[str],significance_level : float)->Tuple[bool,float]:
    """
    対応がつけられたデータについて、両側検定によって、2つの量的データに差があるか判定する

    
    Parameters
    ----------
    data : pandas.Dataframe
        検定を行う標本

    index : [str,str]
        比較したい量的データ
    significance_level :float
        有意水準

    Returns
    ------
    accepted: bool
        2つの量的データに差があるか
        True ならば2つの量的データに差があるとはいえない
        Falseならば2つの量的データに差があると言える
    prob: float
        t-統計量
    """
    #データを抽出する
    data1=data[index[0]]
    data2=data[index[1]]
    
    #対応がある2変数の検定を行う
    t,p=stats.ttest_rel(data1,data2)

    accept = p >significance_level
    print(f"{index[0]} vs {index[1]}: \n t-value : {t} \n p-value : {p} \n -> {'accepted' if accept else 'rejected'}")

    return (accept,t)

def unlinked_phothesis(data:pd.DataFrame,varable: str,index:List[str],significance_level : float)->pd.DataFrame:
    """
    対応がないデータについて、両側検定によって、2つのグループのデータに差があるか判定する

    Parameters
    ----------
    data : pandas.Dataframe
        検定を行う標本
    varable : str
        比較したいデータの変数
    index : [str,str]
        比較する標本の値
    significance_level :float
        有意水準

    Returns
    ------
    res: pandas.DataFrame
        各量的データとt統計量、差があるかをまとめたもの
        indexは次の通り:

        accepted: bool
            2つの量的データに差があるか
            Trueならば 2つの量的データに差があるとはいえない
            Falseならば2つの量的データに差があると言える
        prob: float
            t-統計量

        columnはdataのcolumnのうち、量的データであるもの

    Raises
    ------
    KeyError
        indexの値がvarableにないとき
    """
    #データを抽出する
    indexs=data.select_dtypes(include='number').columns
    data1 = data[data[varable]== index[0]].select_dtypes(include='number')
    data2 = data[data[varable]== index[1]].select_dtypes(include='number')

    #データが存在しているか確認する
    if len(data1)==0:  
        raise KeyError(index[0])
    if len(data2)==0:  
        raise KeyError(index[1])
    
    #対応がない2変数の検定を行う
    t_value,prob=stats.ttest_ind(data1,data2)

    #仮説を採択するか判断する
    res=pd.DataFrame([t_value,[True if i > significance_level else False for i in prob]])
    res.columns=indexs
    res.index=['t_value','accepted']

    print(f"{index[0]} vs {index[1]}:\n")
    for j,i in enumerate(indexs):
        print(f"({i}):\n t-value : {t_value[j]}\n p-value : {prob[j]} \n-> {'accepted' if res.loc['accepted',i] else 'rejected'} ")
    return res
