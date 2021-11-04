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

`pandas.mean()`メソッドで平均を、`pandas.var(ddof=0)`メソッドで分散を、`pandas.std(ddof=0)`メソッドで標準偏差を、`pandas.corr()`メソッド相関係数をそれぞれ計算した。

結果:

<!-- [[[cog
import cog
file="output/task1-2.txt"
cog.outl("\n```bash")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]] -->

```bash
$pipenv run python3 task1-2.py
mean:
math score       67.185
reading score    70.398
writing score    69.023
dtype: float64
var:
math score       234.848775
reading score    214.631596
writing score    234.904471
dtype: float64
std:
math score       15.324777
reading score    14.650310
writing score    15.326594
dtype: float64
corr:
               math score  reading score  writing score
math score       1.000000       0.826605       0.820362
reading score    0.826605       1.000000       0.952643
writing score    0.820362       0.952643       1.000000

```
<!-- [[[end]]] -->

### task 3:母平均の推定

標本データは`pandas.sample()`メソッドによって、抽出した。

点推定については、中心極限定理によって推測し、(サンプル数を取得する回数を1とするとそのまま点推定になる)標本平均の平均、標本平均の分散はそれぞれ`pandas.mean()`、`pandas.var(ddof=0)`メソッドによって行った。

また、区間推定については、`scipy.stats.sem()`メソッドによって標準誤差を算出し、、`scipy.stats.t.interval(alpha,df,loc,scale)`
によって、信頼度が`alpha`、自由度が`df`,平均が`loc`,標準誤差が`scale`のときの区間の上限と下限を求めた。

推定に使用したファイル:

[点推定](output/CLT)

[区間推定](output/IE.csv)

結果:

<!-- [[[cog
import cog
file="output/task1-3.txt"
cog.outl("\n```bash")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]] -->

```bash
$pipenv run python3 task1-3.py 20 1 0.95
samples:20, sets:1
CLT:
     math score  reading score  writing score
ave       65.35          70.55          69.35
var        0.00           0.00           0.00

samples:20, confience_level:0.95
interval:
      math score  reading score  writing score
down   54.090344      60.353603      57.624823
up     69.009656      72.646397      71.775177

```
<!-- [[[end]]] -->
