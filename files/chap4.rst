文字の表現
################

1行目の文章です。
2行目の文章です。

丸竹夷二　押御池　姉三六角　蛸錦　四綾仏高　松万五条　雪駄ちゃらちゃら　魚の棚　六条　三哲　通りすぎ　七 越えれば　八九条　条東寺で　とどめさす

*斜体*

- :ref:`ロロノア・ゾロ <onigiri>`

``コードサンプル``

:フィールドリスト１: 説明文その1
:フィールドリスト２: 説明文その2
:フィールドリスト３: 説明文その3

| このように先頭に "|" を書くと
| ラインブロックになり、
| 改行を含めて、書いたとおりに表示します。

ここは通常の文章です。次の行はリテラルコードブロックです。 ::

   ここからリテラルコードブロックです。
   リテラルコードブロック部分の改行は、
   ソースコードの内容がそのまま反映されます。
   入力した文字はそのまま表示されます。箇条書きをしようとしても

   - あああ
   - いいい

   のように、書いたとおりに表示します。
   ここでリテラルコードブロックは終了です。

ここから通常の文章です。

- リストの 1 つ目です。
- リストは先頭に "・" がつきます。
- リストでも
  改行は Sphinx 任せです。


#. 富士
#. 鷹
#. なすび

- 親リストの 1 つめ

   - 子リストの 1 つめ
   - 子リストの 2 つめ
   - 子リストの 3 つめ

- 親リストの 2 つめ

#. 番号付き親リストの 1 つめ

   #. 番号付き子リストの 1 つめ
   #. 番号付き子リストの 2 つめ
   #. 番号付き子リストの 3 つめ

#. 番号付き親リストの 2 つめ

a. 番号の代わりに英小文字を使用したリストの 1 つ目です。
#. リストの番号は a. b. c. ・・・ になります。
#. 改行は
   やっぱり Sphinx 任せです。

A. 番号の代わりに英大文字を使用したリストの 1 つ目です。
#. リストの番号は A. B. C. ・・・ になります。
#. 改行は
   やっぱり Sphinx 任せです。

〇〇〇 を入力後 :guilabel:`OK` をクリックします。

- :guilabel:`list` ボタン ：登録されている内容を一覧表示します。
- :guilabel:`search` ボタン ：入力した文字列をキーワードにしてドキュメント内を検索します。

:command:`ls` コマンド

スタックは :abbr:`LIFO (last-in, first-out)` 構造です。

nginx のメインの設定ファイルは :file:`/etc/nginx/nginx.conf` です。

サンプルのテキストファイルをダウンロードするには :download:`ここをクリック <./explain.txt>` します。

新しくテキストファイルを作成するには" :menuselection:`ファイル(F) --> 新規作成(N)` "の順に操作します。

処理を中断するときは :kbd:`Esc` を押します。

二次方程式の一般形は 「 :math:`ax^2 + bx + c = 0` 」 です。

Gauss積分は 「 :math:`\displaystyle\int_{-\infty}^\infty dx\,\mathrm{e}^{-ax^2} = \sqrt{\dfrac{\pi}{a}}` 」 です。

.. _onigiri:

鬼斬りを表示
------------

.. image:: ./image.png
  :scale: 70%
  :align: center


Sphinx の日本ユーザー会のサイトは https://sphinx-users.jp/index.html です。

Sphinx の日本ユーザー会のサイトは `ここをクリック <https://sphinx-users.jp/index.html>`_ します。

このサイトについて :doc:`./chap3`

+-------+------+---------+
| A     | B    | A and B |
+-------+------+---------+
| False | うおe| False   |
+-------+------+---------+
| True  | Fals | Flase   |
+-------+------+---------+
| False | True | False   |
+-------+------+---------+
| True  | True | True    |
+-------+------+---------+

====== ====== =======
A      B      A and B
False  うおe  False
True   False  False
False  True   False
True   True   True
====== ====== =======

.. csv-table::

   "A", "B", "A and B"
   "False", "False", "False"
   "True", "False", "False"
   "False", "True", "False"
   "True", "True", "True"

.. list-table:: 各年代の伝説的アニメ
  :widths: 1, 1, 1
  :header-rows: 1

  * - 2011年
    - 2012年
    - 2015年
  * - まどマギ
    - 中二恋
    - Charlotte

+-----+-------+-------+--------+
|     | A     | B     | Result |
+-----+-------+-------+--------+
| and | False | False | False  |
+     +-------+-------+        +
|     | True  | False |        |
+     +-------+-------+        +
|     | False | True  |        |
+     +-------+-------+--------+
|     | True  | True  | True   |
+-----+-------+-------+--------+
| or  | False | False | False  |
+     +-------+-------+--------+
|     | True  | False | True   |
+     +-------+-------+        +
|     | False | True  |        |
+     +-------+-------+        +
|     | True  | True  |        |
+-----+-------+-------+--------+

.. csv-table::
   :widths: 1, 1, 2

   "A", "B", "A and B"
   "False", "False", "False"
   "True", "False", "False"
   "False", "True", "False"
   "True", "True", "True"

+-------+-------+---------+
| A     | B     | A and B |
+=======+=======+=========+
| False | False | False   |
+-------+-------+---------+
| True  | False | Flase   |
+-------+-------+---------+
| False | True  | False   |
+-------+-------+---------+
| True  | True  | True    |
+-------+-------+---------+

.. code-block::

   public class HelloWorld{
      public static void main(String[] args){
        System.out.println("hello, world");
      }
   }

.. code-block:: java
  :linenos:

   public class HelloWorld{
      public static void main(String[] args){
        System.out.println("hello, world");
      }
   }

.. literalinclude:: ./chapter2/uo.jl
  :language: julia
  :emphasize-lines: 3, 5

"c:\\windows" ディレクトリーです。

なんだ、かんだ

----

あーだ、こーだ

.. attention:: 如月アテンション

  attentionの中にtは3回登場します。

:math:`\displaystyle\int\dd[3]{x}`

.. math::
  :nowrap:

  \begin{align}
    \int_{-\infty}^\infty\dd{x}\mathrm{e}^{-ax^2} = \sqrt{\dfrac{\pi}{a}} \label{eq:uo}
  \end{align}


式 :math:`\ref{eq:uo}` がGauss積分。