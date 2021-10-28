# 統計分析法　第一回レポート

## 準備:データを取得する

data: [datas](output/data.csv)

## 1 量的データの基本統計量

### task1-1:母集団の分布を確認する

方針: データを取得したファイルから、量的データを取り出し、それぞれの値について、`matplotlib.pyplot`の`hist`でヒストグラムを作成する。

結果:

数学のスコア: ![math](img/math%20score_distribute.png)

読解のスコア　:![read](img/reading%20score_distribute.png)

書きのスコア: ![write](img/writing%20score_distribute.png)

### task 2:母集団の基本統計量を調べる

方針：ライブラリをもちいて計算する

<!-- 



[[[cog
import cog
file="output/task1-2.txt"
cog.outl("\n```text")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]]-->

```text
>>pipenv run python3.9 task1-2.py
mean:
math score       66.264
reading score    69.332
writing score    68.165
dtype: float64
var:
math score       225.746050
reading score    203.607383
writing score    222.308083
dtype: float64
std:
math score       15.024848
reading score    14.269106
writing score    14.909999
dtype: float64
corr:
               math score  reading score  writing score
math score       1.000000       0.797156       0.783433
reading score    0.797156       1.000000       0.949532
writing score    0.783433       0.949532       1.000000

```
<!-- [[[end]]] -->
