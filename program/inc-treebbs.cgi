use utf8;
# 掲示板設定ファイル 2003/09/25 由來

# 掲示板の表示設定をカスタマイズできます。

$p_tree = 10;		# 1ページに表示するトピックの数
$max = 50;		# 最大保持記事数（トピックの数ではなく記事数）

$new_time = 24;						# 新着記事と判断する時間
$newmark ='<b><font color="#FF0000">&lt;-</font></b>';	# 新着記事マーク

$adminname = "★管理者";	# 管理者権限で投稿したときの名前

# 発言種類の設定
@KIND=("(選択)","連絡","質問","回答","参考","依頼","意見","感想","取引","解決","その他");
@VALUE=("","連絡","<SPAN>質問</SPAN>","回答","参考","<SPAN>依頼</SPAN>","<b>意見</b>","感想","<BIG>取引</BIG>","<b>解決</b>","");

1;
