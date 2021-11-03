# 統計分析法　第一回レポート

## 準備:データを取得する

data: [datas](output/data.csv)

## 1 量的データの基本統計量

### task1-1:母集団の分布を確認する

方針: データを取得したファイルから、量的データを取り出し、それぞれの値について、`matplotlib.pyplot`の`hist`でヒストグラムを作成する。

結果:

数学のスコア: ![math](output/math%20score_distribute.png)

読解のスコア　:![read](output/reading%20score_distribute.png)

書きのスコア: ![write](output/writing%20score_distribute.png)

### task 2:母集団の基本統計量を調べる

方針：`pandas`のライブラリをもちいて計算する。

平均は、`mean()`メソッドで、分散は、`var()`メソッドで、標準偏差は`std()`メソッドで、相関係数は`corr()`メソッドでそれぞれ求めることができる

<!-- [[[cog
import cog
file="output/task1-2.txt"
cog.outl("\n```bash")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]] -->

```bash
$pipenv run python3.9 task1-2.py
mean:
math score       66.694
reading score    69.316
writing score    68.184
dtype: float64
var:
math score       224.002366
reading score    199.457602
writing score    223.996140
dtype: float64
std:
math score       14.966709
reading score    14.122946
writing score    14.966501
dtype: float64
corr:
               math score  reading score  writing score
math score       1.000000       0.807585       0.799522
reading score    0.807585       1.000000       0.953226
writing score    0.799522       0.953226       1.000000

```
<!-- [[[end]]] -->

### task 3:母平均の推定

#### サンプルの選び方について

`pandas.sample()`メソッドによって、サンプルを抽出した。



