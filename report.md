# 統計分析法　第一回レポート

## 準備:データを取得する

演習データは、`requests.get()`メソッドによって取得した。

そのときに、URLの末端の`n=1000`の部分を変更することで取得する標本数を変更できるため、関数の引数で取得する標本数を変更できるようにした。

また、そのときに返されるデータには、値がダブルクォートで囲まれているため、`replace()`メソッドでダブルフォートを削除し、加工がしやすいように、csvファイルにまとめた。

取得したデータ: [datas](output/data.csv)

## 実行環境

python3.9.7

- pipenv

(これ以降のモジュールは`pipenv update`でダウンロードできます)

- requests
- pandas
- matplotlib
- cogapp
- scipy

## 1 量的データの基本統計量

### task 1-1:母集団の分布を確認する

方針: データを取得したファイルから、量的データを取り出し、それぞれの値について、`matplotlib.pyplot`の`hist`でヒストグラムを作成する。

結果:

数学のスコア: ![math](output/math%20score_distribute.png)

読解のスコア　:![read](output/reading%20score_distribute.png)

書きのスコア: ![write](output/writing%20score_distribute.png)

### task 1-2:母集団の基本統計量を調べる

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
math score       66.125
reading score    69.696
writing score    68.340
dtype: float64
var:
math score       224.163375
reading score    220.105584
writing score    240.182400
dtype: float64
std:
math score       14.972087
reading score    14.835956
writing score    15.497819
dtype: float64
corr:
               math score  reading score  writing score
math score       1.000000       0.824112       0.811148
reading score    0.824112       1.000000       0.953334
writing score    0.811148       0.953334       1.000000

```
<!-- [[[end]]] -->

### task 1-3:母平均の推定

標本データは`pandas.sample()`メソッドによって、抽出した。

#### 点推定

中心極限定理によって推測し、(サンプル数を取得する回数を1とするとそのまま点推定になる)標本平均の平均、標本平均の分散はそれぞれ`pandas.mean()`、`pandas.var(ddof=0)`メソッドによって行った。

#### 区間推定

`scipy.stats.sem()`メソッドによって標準誤差を算出し、、`scipy.stats.t.interval(alpha,df,loc,scale)`
によって、信頼度が`alpha`、自由度が`df`,平均が`loc`,標準誤差が`scale`のときの区間の上限と下限を求めた。

今回は、1回で取得する標本数を20、区間推定で標本を取得する数を1回、信頼度を95%にして推定を行った。

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
ave       63.25          66.25           63.9
var        0.00           0.00            0.0

samples:20, confience_level:0.95
interval:
      math score  reading score  writing score
down   59.313921      67.135722      66.885626
up     74.086079      80.964278      81.014374

```
<!-- [[[end]]] -->

## 2 仮説検定

### 今回使うデータについて

今回は、`## 準備:データを取得する`のデータを取得する数を引数で指定できることを活かして、`##1`とは別の50個のデータを標本として使用した。

検定に使用した標本

[仮説検定](output/hypothesis.csv)

### task 2-1:質的データの検定

#### 科目平均の差に意味があるかの検定

帰無仮説は`各科目の平均の差が0`である。また、それに対する対立仮説は`各科目の平均の差が0ではない`である。

今回は科目の得点のデータが50個ずつあることからデータの対応がある。そのため有意確率については、`ave + t x stderr = 0`となるようなt値が自由度49での両側検定での値とする。

有意水準は5%とする。つまり、有意確率が5%より低ければ、帰無仮説は却下され、各科目の平均の差があると言える。

また、有意確率の計算については、調べたい変数を抽出したあと、`scipy.stats.ttest_rel()`メソッドによって行った。

#### 異なる学生グループの科目平均の差に意味があるかの検定

今回は、性別で学生をグループ分けを行った。

帰無仮説は`両グループの各科目の平均の差が0`である。また、それに対する対立仮説は`両グループの各科目の平均の差が0ではない`である。

今回は科目の平均のデータが、それぞれのグループによって異なるため、データの対応はない。そのため有意確率については、両グループの分散が等しいものと仮定して、`(両グループの平均の差) + t x (両グループを使った標準誤差) = 0 `となるようなt値が自由度:両グループの自由度の和での両側検定の値とする。ただし、両グループの分散が等しいとするには、F検定を行う必要があるが、今回は省略する。

有意水準は5%とする。つまり、有意確率が5%より低ければ、帰無仮説は却下され、各科目の平均の差があると言える。

また、有意確率の計算については、調べたい変数を抽出したあと、`scipy.stats.ttest_ind()`メソッドによって行った。


結果:

<!-- [[[cog
import cog
file="output/task2-1.txt"
cog.outl("\n```bash")
with open(file,"r") as f:
    cog.outl(f.read())
cog.outl("```")
    ]]] -->

```bash
$pipenv run python3 task2-1.py
linked hyothesis:

math score vs reading score: 
 t-value : -1.7608103862858517 
 p-value : 0.08451037527725584 
 -> accepted
math score vs writing score: 
 t-value : -1.2739378465778306 
 p-value : 0.2086949194755527 
 -> accepted
reading score vs writing score: 
 t-value : 0.7587842494663274 
 p-value : 0.45161626129468035 
 -> accepted
unlinked hyothesis:

['female' 'male']
female vs male:

(math score):
 t-value : -0.91697562022924
 p-value : 0.3637398641045435 
-> accepted 
(reading score):
 t-value : 2.265435460829317
 p-value : 0.028036093614298416 
-> rejected 
(writing score):
 t-value : 2.810455251081373
 p-value : 0.007139682124466801 
-> rejected 

```
<!-- [[[end]]] -->

全学生の科目平均の差については、いずれも帰無仮説が採択されたことより、科目平均の差の意味はあるとは言えない。

一方で、男女別の科目平均の差については、数学については帰無仮説が採択されたが、読みと書きについては帰無仮説が棄却されたことより、数学については男女別の平均の差に意味があるとは言えないが、読みと書きについては、(t値が正であったことから、)男子のほうが有意に高い理由があると言える。

### task2-2 : 名義データについて、関係があるかを検定する

今回は、標本数が50のため、期待度数が小さくなる可能性がある。そのため、イエーツの補正を用いる。
