# robosys_2022
こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているリポジトリです。

このリポジトリには

* 講義で扱った plus,test.bash

* 自分で作成した calclator.py, check_calc.bash

が含まれています

## リポジトリの概要 
plus

* 標準入力から読み込んだ数字の和を求めることができます。

calculator.py

* pythonを用いて、四則演算ができます。

# リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$git clone https://github.com/IkuoShige/robosys2022.git
$cd robosys2022/
```


# plus
![test](https://github.com/IkuoShige/robosys2022/actions/workflows/test.yml/badge.svg)

## 機能

標準入力から読み込んだ数字の和を求める

## 使い方
以下が実行例です

```
$seq 5 | ./plus
```

出力結果は以下のようになります
```
15
```

# calculator.py

![calc](https://github.com/IkuoShige/robosys2022/actions/workflows/calc.yml/badge.svg)

## 機能

 pythonを用いて、四則演算を行う
 * 数式がどんなに長くても計算することが可能

## 使い方

以下のコマンドで実行が可能

```
$./calculator.py
```

その後、標準入力が求められるので数式を打ち込む

"1 + 1" は例
```
$1 + 1
```

出力結果は以下のようになる

```
2.0
```


# テスト環境
* Ubuntu 20.04.5 LTS

* Python
    3.7~3.10

# LICENSE

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Ikuo Shige
