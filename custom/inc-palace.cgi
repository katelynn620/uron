use utf8;
# 宮殿設定ファイル 2003/07/19 由來

# 王様の依頼内容をカスタマイズできます。
# 「依頼文章」，「依頼するアイテム番号」，「個数」の順に記入します。
# 種類はこの要領で増やすことができます。

($msg[0],$itemno[0],$count[0])=('余は，いまグルメに凝っていてな。珍味を食したいと思っておるのじゃ。',18,150);
($msg[1],$itemno[1],$count[1])=('余は，いまグルメに凝っていてな。珍味を食したいと思っておるのじゃ。',19,120);
($msg[2],$itemno[2],$count[2])=('余は，いまグルメに凝っていてな。珍味を食したいと思っておるのじゃ。',31,120);
($msg[3],$itemno[3],$count[3])=('ずっと食べたいと思っているのじゃが，この身では博多には行けぬ。',43,20);
($msg[4],$itemno[4],$count[4])=('ずっと食べたいと思っているのじゃが，この身では博多には行けぬ。',55,20);
($msg[5],$itemno[5],$count[5])=('我が国には，その日の食べ物すらままならない子供たちがおるのじゃ。',45,2000);
($msg[6],$itemno[6],$count[6])=('我が国には，その日の食べ物すらままならない子供たちがおるのじゃ。',57,2000);

#記述例 ($msg[7],$itemno[7],$count[7])=('セリフ',10,100);

# 王様と面会するのに必要な点数(低いと面会を拒否)
# 初心者がいきなり使命を達成しようとすると危険。ある程度高く設定すべし。
$deny_point=20000;

1;
