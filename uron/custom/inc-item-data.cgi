# うどん＆そば版アイテムデータ 2005/01/06 由來

# このファイルはアイテムデータの定義ファイルです。
# 好きなようにカスタマイズできます。詳細はマニュアルをご覧ください。

@@DEFINE
	version	05-01-06(URon)		#★商品データバージョン表記
					# 最後の「URon」はうどん＆そば版であることを示します。
					# もしあなたが独自アイテムを目玉にした商人物語を製作なら，
					# この記号を変えるのがよいでしょう。

	scale	碗			#★デフォルトの数え単位
	type0	全			#全アイテムの集合
	type1	人材
	type2	陸產品
	type3	海產品
	type4	烏龍麵
	type5	蕎麥麵
	type6	工具
	
	job	agri		農業		#★職業コードは英小文字10文字以内
	job	fish		漁業
	job	temp		天婦羅屋
	job	udon		烏龍麵屋
	job	soba		蕎麥麵屋
	job	man		人力仲介
	job	black		黑道
	
	# 職業別時間短縮用変数設定
	set job_agri_time_rate		1.5	#★職業についていると1.5倍早くなる
	set job_fish_time_rate		1.5
	set job_temp_time_rate		1.5
	set job_udon_time_rate		1.5
	set job_soba_time_rate		1.5
	set job_man_time_rate		2
	set job_black_time_rate		2

	MaxMoney	999999999	#★最大資金
	
	set NewShopMoney	200000					#初期資金 (@@FUNCNEWにて使用)
	set NewShopTime		24*60*60				#初期持時間(秒) (@@FUNCNEWにて使用)
	set NewShopItem		攻略本:1	#初期所持商品 (@@FUNCNEWにて使用) 書式 商品名:個数:商品名:個数:...
	
	TimeEditShowcase	10m		#★展示架操作時間
	TimeShopping		20m		#★仕入時間(旧SOLD OUTとの互換性確保。今は使用せず)
	TimeSendItem		20m		#★アイテム仕入/送信時間(基本)
	TimeSendItemPlus	20s		#★アイテム仕入/送信時間(1個辺りの追加時間)
	TimeSendMoney		20m		#★資金送信時間(基本)
	TimeSendMoneyPlus	100000		#★入金所要時間計算用金額(この金額につきTimeSendMoney時間を消費)
	
	CostShowcase1		0		#★展示架1個時維持費
	CostShowcase2		1000	#展示架2個時維持費
	CostShowcase3		2000	#展示架3個時維持費
	CostShowcase4		4000	#展示架4個時維持費
	CostShowcase5		8000	#展示架5個時維持費
	CostShowcase6		16000	#展示架6個時維持費
	CostShowcase7		32000	#展示架7個時維持費
	CostShowcase8		64000	#展示架8個時維持費
	
	ItemUseTimeRate		0.5		#★アイテム使用時時間計算補正倍率(@USE内time,exptimeに有効)
	

#------ ここからアイテム定義 ---------------------------------


@@ITEM
	no		1
	type	人材
	code	man-free
	name	臨時工
	info	有潛能的人才
	scale	人
	price	5000
	cost	100
	limit	5/5
	plus	2h
	pop	1d
	flag	noshowcase|norequest|human
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人力仲介	times/job_man_time_rate
		scale	人
		action	從事農業
		name	從事農業
		info	臨時工開始從事農業了
		okmsg	臨時工成為農夫了
			use		1	臨時工
			get		1	農夫
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人力仲介	times/job_man_time_rate
		scale	人
		action	從事漁業
		name	從事漁業
		info	臨時工開始從事漁業了
		okmsg	臨時工成為漁夫了
			use		1	臨時工
			get		1	漁夫
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人力仲介	times/job_man_time_rate
		scale	人
		action	開始修行
		name	進行成為天婦羅師傅的修行
		info	臨時工開始進行成為天婦羅師傅的修行了
		okmsg	臨時工成為天婦羅師傅了
			use		1	臨時工
			get		1	天婦羅師傅
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人力仲介	times/job_man_time_rate
		scale	人
		action	開始修行
		name	進行成為烏龍麵師傅的修行
		info	臨時工開始進行成為烏龍麵師傅的修行了
		okmsg	臨時工成為烏龍麵師傅了
			use		1	臨時工
			use		10	小麥粉
			get		1	烏龍麵師傅
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人力仲介	times/job_man_time_rate
		scale	人
		action	開始修行
		name	進行成為蕎麥麵師傅的修行
		info	臨時工開始進行成為蕎麥麵師傅的修行了
		okmsg	臨時工成為蕎麥麵師傅了
			use		1	臨時工
			use		10	蕎麥粉
			get		1	蕎麥麵師傅
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		人力仲介	times/job_man_time_rate
		scale	人
		action	從事便利屋
		name	從事便利屋
		info	臨時工開始從事便利屋的工作了
		okmsg	臨時工成為便利屋了
			use		1	臨時工
			get		1	便利屋
			get		10	店力	20%
	@@use
		time	4h
		job		人力仲介	times/job_man_time_rate
		scale	回
		action	工作
		name	發傳單賺取資金
		info	稍微賺點錢
		param	7000
		func	_local_
			$DT->{money}+=$USE->{param1}*$count;
			my $ret='賺到'.GetMoneyString($USE->{param1}*$count).'了';
			if (rand(1000)<200)
			{
			UseItem(1,1,$ITEM[1]->{name}.'厭倦打工而離開商店了');
			}
			WriteLog(0,$DT->{id},"去打工了，$ret");
			WriteLog(3,0,$DT->{shopname}."的臨時工開始打工了");
			return $ret;
		_local_
	@@use
		time	9h
		job		人力仲介	times/job_man_time_rate
		scale	回
		action	工作
		name	在便利商店賺取資金
		info	稍微努力一點賺錢
		param	20000
		func	_local_7
	@@USE
		time	6h
		action	成為人力仲介
		arg		nocount
		name	成為人力仲介
		info	利用自身的經驗，成為人力仲介。
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是人力仲介了') if ($DT->{job} eq 'man');
			$DT->{job} = 'man';
			$ret="成為人力仲介了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		2
	type	人材
	code	man-nou
	name	農夫
	info	也擅長飼養牲畜。
	scale	人
	price	30000
	cost	1000
	limit	3/0.5
	plus	1d
	pop	1d
	flag	noshowcase|human
	@@USE
		time	3h
		exp		1%
		exptime	1h
		price	20000
		job		農業	times/job_agri_time_rate
		scale	反
		action	取得田地
		name	取得田地
		info	尋找並購買良好的田地
		okmsg	馬上找到了可以收割的田地，甚至還有一些堆肥。
			get		1	待收割的田地
			get		100	堆肥
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	反
		action	進行耕作並且播種
		name	進行耕作並且播種
		info	對田地施肥犁田，並且種植作物
		okmsg	對田地施肥犁田，並且種植作物了
			use		1	耕作前的田地
			use		100	堆肥
			get		1	耕作後的田地
			get		10	店力	10%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	進行收割
		name	收穫蔥
		info	去蔥田裡進行收割
		func	lostman
		param	50
		ngmsg	沒有收穫任何東西..
			use		1	待收割的田地
			get		100	蔥	50%	收穫了蔥
			get		10	玉米	50%	也撿到了一些玉米
			get		1	抽獎卷	01%	在田地裡撿到抽獎卷了
			get		1	鵝	05%	抓到一隻入侵田地的野鵝
			get		1	耕作前的田地
			get		10	店力	10%
		funcb	_local_
			# 1/20の確率で収穫量が2倍になる
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='本次大豐收<br>獲得了新的田地';
			return 0;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	進行收割
		name	收穫小麥
		info	去小麥田裡進行收割
		func	lostman
		param	50
		ngmsg	沒有收穫任何東西..
			use		1	待收割的田地
			get		40	小麥粉	50%	收穫了小麥，並且磨成了粉
			get		10	唐辛子	50%	也撿到了一些唐辛子
			get		1	抽獎卷	01%	在田地裡撿到抽獎卷了
			get		1	鵝	05%	抓到一隻入侵田地的野鵝
			get		1	耕作前的田地
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='本次大豐收<br>獲得了新的田地';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	進行收割
		name	收割蕎麥
		info	去そば田裡進行收割
		func	lostman
		param	50
		ngmsg	沒有收穫任何東西..
			use		1	待收割的田地
			get		40	蕎麥粉	50%	收穫了蕎麥，並且磨成了粉
			get		20	唐辛子	50%	也撿到了一些唐辛子
			get		1	抽獎卷	01%	在田地裡撿到抽獎卷了
			get		1	豬	05%	抓到一隻入侵田地的野豬
			get		1	耕作前的田地
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='本次大豐收<br>獲得了新的田地';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	進行收割
		name	收穫大豆
		info	去大豆田裡進行收割
		func	lostman
		param	50
		ngmsg	沒有收穫任何東西..
			use		1	待收割的田地
			get		40	大豆	50%	收穫了大豆
			get		30	蔥	50%	也撿到了一些蔥
			get		1	抽獎卷	01%	在田地裡撿到抽獎卷了
			get		1	豬	05%	抓到一隻入侵田地的野豬
			get		1	耕作前的田地
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='本次大豐收<br>獲得了新的田地';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		action	進行收割
		name	收穫玉米
		info	去玉米田裡進行收割
		func	lostman
		param	50
		ngmsg	沒有收穫任何東西..
			use		1	待收割的田地
			get		27	玉米	50%	收穫了玉米
			get		20	大豆	50%	也撿到了一些大豆
			get		1	抽獎卷	01%	在田地裡撿到抽獎卷了
			get		1	鵝	05%	抓到一隻入侵田地的野鵝
			get		1	耕作前的田地
			get		10	店力	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='本次大豐收<br>獲得了新的田地';
			return 0;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		arg		nocount
		action	照顧
		name	照顧雞
		info	如果你準備了足夠的飼料，你可以在清理雞舍後餵雞
		param	2
			need		1	雞
		func	_local_
			my $val=$USE->{param1}*$count;
			my $ret="";
			my $niwatori=$DT->{item}[20-1];
			my $toumorokosi=$DT->{item}[17-1];

			if ($niwatori*$count>$toumorokosi)
			{
			AddItem(58,$count,);
			$ret='看來雞的飼料不夠了，所以只打掃了雞舍。';
			WriteLog(0,$DT->{id},$ret);
			}
			else
			{
			$val*=$DT->{item}[20-1];
			$val=int(rand($val) * 2)+1;
			AddItem(9,$val,);
			AddItem(58,$count,);
			UseItem(17,$niwatori*$count,'給每隻雞餵了'.$count.'個玉米');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(20,$usecount,$ITEM[20]->{name}.'吃飽後，就升天了。') if $usecount;
			
			$ret='獲得了'.$val.'個雞蛋';
			WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	次
		action	讓母雞孵蛋
		name	將雞蛋孵化
		info	讓母雞孵蛋，使雞蛋孵化
		func	lostman
		param	50
		okmsg	孵化的準備已經完成了
			need		1	雞
			use		5	雞蛋
			get		5	等待孵化的雞蛋
			get		10	店力	10%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	隻
		action	照顧
		name	照顧農場的鵝
		info	餵食鵝充足的食物
		func	lostman
		param	50
		ngmsg	還沒來得及拿到鵝肝，鵝就已經升天了……
		okmsg	得到了高級的鵝肝
			use		1	鵝
			use		10	玉米
			get		48	鵝肝	50%
			get		10	店力	15%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		農業	times/job_agri_time_rate
		scale	回
		arg		nocount
		action	照顧
		name	照顧農場的豬
		info	如果準備了足夠的飼料可以餵豬，然後帶牠們去山裡散步。
		param	1
			need		1	豬
		func	_local_
			my $val=$USE->{param1}*$count;
			my $ret="";
			my $buta=$DT->{item}[22-1];
			my $daizu=$DT->{item}[16-1];

			if ($buta*$count*5>$daizu)
			{
			AddItem(58,$count*2,);
			$ret='因為飼料不足，所以只進行了豬欄的打掃';
			WriteLog(0,$DT->{id},$ret);
			}
			else
			{
			$val*=$DT->{item}[22-1];
			$val=int(rand($val) * 3)+1;
			AddItem(18,$val,);
			AddItem(58,$count,);
			UseItem(16,$buta*$count*5,'給每頭豬餵食了'.($count*5).'kg的大豆');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(22,$usecount,$ITEM[22]->{name}.'往深山裡跑走了') if $usecount;
			
			$ret='帶吃飽的豬去山上散步，豬發現了'.$val.'個松露';
			WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@USE
		time	6h
		action	成為農業專門家
		scale	回
		arg		nocount
		name	成為農業專門家
		info	利用自身的經驗，成為農業專門家
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是農業專門家了') if ($DT->{job} eq 'agri');
			$DT->{job} = 'agri';
			$ret="成為農業專門家了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		3
	type	人材
	code	man-gyo
	name	漁夫
	info	需要誘餌才能釣到大魚
	scale	人
	price	30000
	cost	1000
	limit	3/0.5
	plus	1d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	4.5h
		exp		1%
		exptime	1.5h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	去釣魚
		name	去釣魚
		info	在附近的海岸釣魚
		ngmsg	什麼魚都沒釣到..
			get		10	黃線狹鱈	50%	釣到了黃線狹鱈
			get		2	狗母魚	50%	釣到了狗母魚
			get		100	蝦	60%	捕到了蝦
			get		40	海帶芽	50%	順便採到了一些海帶芽
			get		1	鵝	02%	救了一隻溺水的鵝
			get		10	店力	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	出海捕魚
		name	出海捕魚
		info	搭船出海捕魚
		func	lostman
		param	50
		ngmsg	什麼魚都沒釣到..
			use		50	蝦
			get		8	黃線狹鱈	30%	釣到了黃線狹鱈
			get		8	狗母魚	50%	釣到了狗母魚
			get		10	鰹魚	50%	釣到了鰹魚
			get		2	鱘魚	30%	釣到了大隻的鱘魚
			get		1	豬	02%	救了一隻溺水的豬
			get		10	店力	20%
	@@USE
		time	2h
		exp		1%
		exptime	1h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	製作
		name	製作明太子
		info	將黃線狹鱈的魚卵進行加工，做成明太子
		func	lostman
		param	50
		ngmsg	製作明太子失敗，材料都浪費了..
		okmsg	做好明太子了
			use		1	黃線狹鱈
			use		5	唐辛子
			get		20	明太子	80%
			get		10	店力	10%
	@@USE
		time	2h
		exp		1%
		exptime	1h
		job		漁業	times/job_fish_time_rate
		scale	回
		action	取得
		name	取得魚子醬
		info	從鱘魚裡面將魚子醬取出
		func	lostman
		param	50
		ngmsg	這隻鱘魚是公的啦‥
		okmsg	取得魚子醬了
			use		1	鱘魚
			get		40	魚子醬	60%
			get		10	店力	10%
	@@USE
		time	6h
		action	成為漁業專門家
		scale	回
		arg		nocount
		name	成為漁業專門家
		info	利用自身的經驗，成為漁業專門家
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是漁業專門家了') if ($DT->{job} eq 'fish');
			$DT->{job} = 'fish';
			$ret="成為漁業專門家了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		4
	type	人材
	code	man-ten
	name	天婦羅師傅
	info	可以料理炸豆皮或魚板
	scale	人
	price	30000
	cost	1000
	limit	3/0.5
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job	天婦羅屋	times/job_temp_time_rate
		scale	回
		action	製作
		name	製作炸豆皮
		info	由大豆做成豆腐，然後加工成炸豆皮。
		ngmsg	製作炸豆皮失敗，材料都浪費了..
			use		10	大豆
			get		100	炸豆皮	80%	做好炸豆皮了
			get		10	店力	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		天婦羅屋	times/job_temp_time_rate
		scale	回
		action	製作
		name	製作魚板
		info	製作魚板
		ngmsg	製作魚板失敗，材料都浪費了..
			use		4	黃線狹鱈
			get		100	魚板	80%	做好魚板了
			get		10	店力	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		天婦羅屋	times/job_temp_time_rate
		scale	回
		action	製作
		name	製作圓形天婦羅
		info	製作圓形天婦羅
		func	lostman
		param	50
		ngmsg	製作圓形天婦羅失敗，材料都浪費了..
			use		2	狗母魚
			get		60	圓形天婦羅	80%	做好圓形天婦羅了
			get		10	店力	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		天婦羅屋	times/job_temp_time_rate
		scale	回
		action	製作
		name	製作炸蝦天婦羅
		info	製作炸蝦天婦羅
		func	lostman
		param	50
		ngmsg	製作炸蝦天婦羅失敗，材料都浪費了..
			use		20	蝦
			use		2	小麥粉
			use		10	雞蛋
			get		50	炸蝦天婦羅	80%	做好炸蝦天婦羅了
			get		10	店力	20%
	@@USE
		time	6h
		action	成為天婦羅師傅
		arg		nocount
		name	成為天婦羅師傅
		info	利用自身的經驗，成為天婦羅師傅
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是天婦羅師傅了') if ($DT->{job} eq 'temp');
			$DT->{job} = 'temp';
			$ret="成為天婦羅師傅了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		5
	type	人材
	code	man-udon
	name	烏龍麵師傅
	info	每種烏龍麵各準備一碗，開發新的烏龍麵吧！
	scale	人
	price	30000
	cost	1000
	limit	3/0.3
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作清湯烏龍麵
		info	製作清湯烏龍麵
		ngmsg	製作清湯烏龍麵失敗，材料都浪費了..
			use		3	小麥粉
			use		2	蔥
			use		2	魚板
			use		40	乾淨的碗
			get		40	清湯烏龍麵	80%	做好清湯烏龍麵了
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作海帶芽烏龍麵
		info	製作海帶芽烏龍麵
		ngmsg	製作海帶芽烏龍麵失敗，材料都浪費了..
			use		3	小麥粉
			use		2	蔥
			use		5	海帶芽
			use		32	乾淨的碗
			get		30	海帶芽烏龍麵	90%	做好海帶芽烏龍麵了
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作豆皮烏龍麵
		info	製作豆皮烏龍麵
		ngmsg	製作豆皮烏龍麵失敗，材料都浪費了..
			use		3	小麥粉
			use		2	蔥
			use		10	炸豆皮
			use		25	乾淨的碗
			get		25	豆皮烏龍麵	80%	做好豆皮烏龍麵了
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作天婦羅烏龍麵
		info	製作天婦羅烏龍麵
		ngmsg	製作天婦羅烏龍麵失敗，材料都浪費了..
			use		3	小麥粉
			use		2	蔥
			use		10	圓形天婦羅
			use		20	乾淨的碗
			get		20	天婦羅烏龍麵	80%	做好天婦羅烏龍麵了
			get		10	店力	10%
	@@USE
		time	2h
		exp	2%
		exptime	40m
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作炸蝦烏龍麵
		info	製作炸蝦烏龍麵
		ngmsg	製作炸蝦烏龍麵失敗，材料都浪費了..
			use		5	小麥粉
			use		5	蔥
			use		20	炸蝦天婦羅
			use		20	乾淨的碗
			get		20	炸蝦烏龍麵	80%	做好炸蝦烏龍麵了
			get		20	店力	10%
	@@USE
		time	20m
		exp	0%
		exptime	10m
		job	烏龍麵屋	times/job_udon_time_rate
		scale	組
		action	製作
		name	製作烏龍麵三昧
		info	製作烏龍麵三昧
		okmsg	做好烏龍麵三昧了
			needexp		20%
			use		10	豆皮烏龍麵
			use		10	天婦羅烏龍麵
			use		10	炸蝦烏龍麵
			get		10	烏龍麵三昧
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作魚子醬烏龍麵
		info	製作魚子醬烏龍麵
		func	lostman
		param	50
		ngmsg	製作魚子醬烏龍麵失敗，材料都浪費了..
			needexp		40%
			use		3	小麥粉
			use		1	鰹魚
			use		2	魚子醬
			use		8	乾淨的碗
			get		8	魚子醬烏龍麵	80%	做好魚子醬烏龍麵了
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作松露烏龍麵
		info	製作松露烏龍麵
		func	lostman
		param	50
		ngmsg	製作松露烏龍麵失敗，材料都浪費了..
			needexp		40%
			use		3	小麥粉
			use		1	鰹魚
			use		2	松露
			use		8	乾淨的碗
			get		10	松露烏龍麵	60%	做好松露烏龍麵了
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job		烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作鵝肝烏龍麵
		info	製作鵝肝烏龍麵
		func	lostman
		param	50
		ngmsg	製作鵝肝烏龍麵失敗，材料都浪費了..
			needexp		40%
			use		3	小麥粉
			use		1	鰹魚
			use		2	鵝肝
			use		6	乾淨的碗
			get		6	鵝肝烏龍麵	80%	做好鵝肝烏龍麵了
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作博多烏龍麵
		info	製作博多烏龍麵
		func	lostman
		param	50
		ngmsg	製作博多烏龍麵失敗，材料都浪費了..
			needexp		60%
			use		5	小麥粉
			use		1	豬
			use		2	明太子
			use		6	乾淨的碗
			get		6	博多烏龍麵	80%	做好博多烏龍麵了
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		烏龍麵屋	times/job_udon_time_rate
		scale	回
		action	製作
		name	製作原創烏龍麵
		info	製作原創烏龍麵
		ngmsg	製作原創烏龍麵失敗，材料都浪費了..
			needexp		80%
			need		1	原創烏龍麵食譜
			use		5	小麥粉
			use		1	鰹魚
			use		1	鵝
			use		5	唐辛子
			use		3	乾淨的碗
			get		5	原創烏龍麵	40%	做好原創烏龍麵了
			get		10	店力	20%
		func	_local_
			my $ret="";
			$DT->{user}->{udoncnt}+=1;
			if (rand(1000)<100)
			{
				UseItem(@@ITEMNO"烏龍麵師傅",1,"<br>工作完成後，烏龍麵師傅默默離去了");
			}
			if ((rand(1000)<100)&&($DT->{user}->{udoncnt}>50))
			{
				$DT->{user}->{udoncnt}=0;
				UseItem(@@ITEMNO"原創烏龍麵食譜",1,"<br>原創烏龍麵食譜無意間被點燃，然後就燒毀了");
				WriteLog(0,$DT->{id},"失去原創烏龍麵食譜了");
				WriteLog(2,0,$DT->{shopname}."好像不小心把原創烏龍麵食譜燒了。");
			}
			return $ret;
		_local_
	@@USE
		time	6h
		exp		1%
		exptime	4h
		job		烏龍麵屋	times/job_udon_time_rate
		action	烏龍麵要叫什麼名字呢
		name	開發原創烏龍麵
		info	為全心全意創造的原創烏龍麵命名
		arg		nocount|message30
		okmsg	在忘記之前將食譜記下來吧。
			use		1	清湯烏龍麵
			use		1	海帶芽烏龍麵
			use		1	豆皮烏龍麵
			use		1	天婦羅烏龍麵
			use		1	炸蝦烏龍麵
			use		1	魚子醬烏龍麵
			use		1	松露烏龍麵
			use		1	鵝肝烏龍麵
			use		1	博多烏龍麵
			get		1	原創烏龍麵
			get		1	原創烏龍麵食譜
		func	_local_
			# 原創烏龍麵を製作
			main::OutError('請輸入名稱') if !$USE->{arg}->{message};
			my $ret;
			$ret='原創烏龍麵【'.$USE->{arg}->{message}.'】製作完成了';	
			WriteLog(3,0,$DT->{shopname}."的特製烏龍麵「".$USE->{arg}->{message}."」完成了。");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{udon}=$USE->{arg}->{message};
			return $ret;
		_local_
	@@USE
		time	6h
		action	成為烏龍麵師傅
		arg		nocount
		name	成為烏龍麵師傅
		info	利用自身的經驗，成為烏龍麵師傅
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是烏龍麵師傅了') if ($DT->{job} eq 'udon');
			$DT->{job} = 'udon';
			$ret="成為烏龍麵師傅了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		6
	type	人材
	code	man-soba
	name	蕎麥麵師傅
	info	每種蕎麥麵各準備一碗，開發新的蕎麥麵吧！
	scale	人
	price	30000
	cost	1000
	limit	3/0.3
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作清湯蕎麥麵
		info	製作清湯蕎麥麵
		ngmsg	製作清湯蕎麥麵失敗，材料都浪費了..
			use		3	蕎麥粉
			use		2	蔥
			use		2	魚板
			use		40	乾淨的碗
			get		40	清湯蕎麥麵	80%	做好清湯蕎麥麵了
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作海帶芽蕎麥麵
		info	製作海帶芽蕎麥麵
		ngmsg	製作海帶芽蕎麥麵失敗，材料都浪費了..
			use		3	蕎麥粉
			use		2	蔥
			use		5	海帶芽
			use		32	乾淨的碗
			get		30	海帶芽蕎麥麵	90%	做好海帶芽蕎麥麵了
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作豆皮蕎麥麵
		info	製作豆皮蕎麥麵
		ngmsg	製作豆皮蕎麥麵失敗，材料都浪費了..
			use		3	蕎麥粉
			use		2	蔥
			use		10	炸豆皮
			use		25	乾淨的碗
			get		25	豆皮蕎麥麵	80%	做好豆皮蕎麥麵了
			get		10	店力	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作天婦羅蕎麥麵
		info	製作天婦羅蕎麥麵
		ngmsg	製作天婦羅蕎麥麵失敗，材料都浪費了..
			use		3	蕎麥粉
			use		2	蔥
			use		10	圓形天婦羅
			use		20	乾淨的碗
			get		20	天婦羅蕎麥麵	80%	做好天婦羅蕎麥麵了
			get		10	店力	10%
	@@USE
		time	2h
		exp	2%
		exptime	40m
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作炸蝦蕎麥麵
		info	製作炸蝦蕎麥麵
		ngmsg	製作炸蝦蕎麥麵失敗，材料都浪費了..
			use		5	蕎麥粉
			use		5	蔥
			use		20	炸蝦天婦羅
			use		20	乾淨的碗
			get		20	炸蝦蕎麥麵	80%	做好炸蝦蕎麥麵了
			get		20	店力	10%
	@@USE
		time	20m
		exp	0%
		exptime	10m
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	組
		action	製作
		name	製作蕎麥麵三昧
		info	製作蕎麥麵三昧
		okmsg	蕎麥麵三昧做好了
			needexp		20%
			use		10	豆皮蕎麥麵
			use		10	天婦羅蕎麥麵
			use		10	炸蝦蕎麥麵
			get		10	蕎麥麵三昧
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作魚子醬蕎麥麵
		info	製作魚子醬蕎麥麵
		func	lostman
		param	50
		ngmsg	製作魚子醬蕎麥麵失敗，材料都浪費了..
			needexp		40%
			use		3	蕎麥粉
			use		1	鰹魚
			use		2	魚子醬
			use		8	乾淨的碗
			get		8	魚子醬蕎麥麵	80%	做好魚子醬蕎麥麵了
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作松露蕎麥麵
		info	製作松露蕎麥麵
		func	lostman
		param	50
		ngmsg	製作松露蕎麥麵失敗，材料都浪費了..
			needexp		40%
			use		3	蕎麥粉
			use		1	鰹魚
			use		2	松露
			use		8	乾淨的碗
			get		10	松露蕎麥麵	60%	做好松露蕎麥麵了
			get		10	店力	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作鵝肝蕎麥麵
		func	lostman
		param	50
		info	製作鵝肝蕎麥麵
		ngmsg	製作鵝肝蕎麥麵失敗，材料都浪費了..
			needexp		40%
			use		3	蕎麥粉
			use		1	鰹魚
			use		2	鵝肝
			use		6	乾淨的碗
			get		6	鵝肝蕎麥麵	80%	做好鵝肝蕎麥麵了
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作博多蕎麥麵
		info	製作博多蕎麥麵
		func	lostman
		param	50
		ngmsg	製作博多蕎麥麵失敗，材料都浪費了..
			needexp		60%
			use		5	蕎麥粉
			use		1	豬
			use		2	明太子
			use		6	乾淨的碗
			get		6	博多蕎麥麵	80%	做好博多蕎麥麵了
			get		10	店力	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		蕎麥麵屋	times/job_soba_time_rate
		scale	回
		action	製作
		name	製作原創蕎麥麵
		info	製作原創蕎麥麵
		ngmsg	製作原創蕎麥麵失敗，材料都浪費了..
			needexp		80%
			need		1	原創蕎麥麵食譜
			use		5	蕎麥粉
			use		1	鰹魚
			use		1	鱘魚
			use		15	雞蛋
			use		3	乾淨的碗
			get		5	原創蕎麥麵	40%	做好原創蕎麥麵了
			get		10	店力	30%
		func	_local_
			my $ret="";
			$DT->{user}->{sobacnt}+=1;
			if (rand(1000)<100)
			{
				UseItem(@@ITEMNO"蕎麥麵師傅",1,"<br>工作完成後，蕎麥麵師傅默默離去了");
			}
			if ((rand(1000)<100)&&($DT->{user}->{sobacnt}>50))
			{
				$DT->{user}->{sobacnt}=0;
				UseItem(@@ITEMNO"原創蕎麥麵食譜",1,"<br>原創蕎麥麵食譜無意間被點燃，然後就燒毀了");
				WriteLog(0,$DT->{id},"失去原創蕎麥麵食譜了");
				WriteLog(2,0,$DT->{shopname}."好像不小心把原創蕎麥麵食譜燒了。");
			}
			return $ret;
		_local_
	@@USE
		time	6h
		exp		1%
		exptime	4h
		job		蕎麥麵屋	times/job_soba_time_rate

		action	蕎麥麵要叫什麼名字呢
		name	開發原創蕎麥麵
		info	為全心全意創造的原創蕎麥麵命名
		arg		nocount|message30
		okmsg	在忘記之前將食譜記下來吧。
			use		1	清湯蕎麥麵
			use		1	海帶芽蕎麥麵
			use		1	豆皮蕎麥麵
			use		1	天婦羅蕎麥麵
			use		1	炸蝦蕎麥麵
			use		1	魚子醬蕎麥麵
			use		1	松露蕎麥麵
			use		1	鵝肝蕎麥麵
			use		1	博多蕎麥麵
			get		1	原創蕎麥麵
			get		1	原創蕎麥麵食譜
		func	_local_
			# 原創蕎麥麵を製作
			main::OutError('請輸入名稱') if !$USE->{arg}->{message};
			my $ret;
			$ret='原創蕎麥麵【'.$USE->{arg}->{message}.'】製作完成了';	
			WriteLog(3,0,$DT->{shopname}."的特製蕎麥麵「".$USE->{arg}->{message}."」完成了。");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{soba}=$USE->{arg}->{message};
			return $ret;
		_local_
	@@USE
		time	6h
		action	成為蕎麥麵師傅
		arg		nocount
		name	成為蕎麥麵師傅
		info	利用自身的經驗，成為蕎麥麵師傅
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是蕎麥麵師傅了') if ($DT->{job} eq 'soba');
			$DT->{job} = 'soba';
			$ret="成為蕎麥麵師傅了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		7
	type	人材
	code	man-benri
	name	便利屋
	info	擅長製作展示架和洗碗
	scale	人
	price	30000
	cost	1000
	limit	5/0.5
	plus	2h
	pop		3d
	flag	noshowcase|human
	@@USE
		time	1h
		job		人力仲介	times/job_man_time_rate
		scale	回
		action	施工
		price	0
		name	將展示架改為1個
		info	將展示架改為1個
		arg		nocount
		param	1
		func	_local_
			# ★展示架数変更
			#   param1 変更後の棚数
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="展示架已經改成$DT->{showcasecount}個了";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."的展示架已經變成$DT->{showcasecount}個了");
			
			return $ret;
		_local_
	@@USE
		time	2h
		job		人力仲介	times/job_man_time_rate
		price	10000
		name	將展示架改為2個
		info	將展示架改為2個
		func	_local_1
		arg		nocount
		param	2
	@@USE
		time	4h
		job		人力仲介	times/job_man_time_rate
		price	50000
		name	將展示架改為3個
		info	將展示架改為3個
		func	_local_1
		arg		nocount
		param	3
			need	2	便利屋
	@@USE
		time	6h
		job		人力仲介	times/job_man_time_rate
		price	100000
		name	將展示架改為4個
		info	將展示架改為4個
		func	_local_1
		arg		nocount
		param	4
			need	2	便利屋
	@@USE
		time	10h
		job		人力仲介	times/job_man_time_rate
		price	200000
		name	將展示架改為5個
		info	將展示架改為5個
		func	_local_1
		arg		nocount
		param	5
			need	3	便利屋
	@@USE
		time	12h
		job		人力仲介	times/job_man_time_rate
		price	500000
		name	將展示架改為6個
		info	將展示架改為6個
		func	_local_1
		arg		nocount
		param	6
			need	3	便利屋
	@@USE
		time	14h
		job		人力仲介	times/job_man_time_rate
		price	1000000
		name	將展示架改為7個
		info	將展示架改為7個
		func	_local_1
		arg		nocount
		param	7
			need	4	便利屋
	@@USE
		time	16h
		job		人力仲介	times/job_man_time_rate
		price	2000000
		name	將展示架改為8個
		info	將展示架改為8個
		func	_local_1
		arg		nocount
		param	8
			need	5	便利屋
	@@USE
		time	30m
		exp		1%
		exptime	10m
		job		人力仲介	times/job_man_time_rate
		scale	回
		action	清洗
		name	將碗洗乾淨
		info	將髒掉的碗洗乾淨
		func	lostman
		param	10
		ngmsg	全部的碗都被打破了‥
			use		10	髒掉的碗
			get		10	乾淨的碗	90%	碗變得亮晶晶了
			get		10	店力	02%
	@@USE
		time	1h
		exp		1%
		exptime	30m
		job		人力仲介	times/job_man_time_rate
		scale	回
		action	使用
		name	使用洗碗機將碗洗乾淨
		info	將髒掉的碗用洗碗機洗乾淨
		func	lostman
		param	50
		ngmsg	全部的碗都被打破了‥
			need		1	洗碗機
			use		50	髒掉的碗
			get		50	乾淨的碗	95%	碗變得亮晶晶了
			get		10	店力	05%
	@@use
		time	10h
		exp		5%
		exptime	6h
		job		人力仲介	times/job_man_time_rate
		action	投放廣告
		name	在[新聞]上投放廣告
		info	請填寫下面的表格並點選按鈕<br>在[新聞]上投放廣告
		param	300
		arg		nocount|message100
			use	1	便利屋
		func	_local_
			main::OutError('請輸入廣告文宣') if !$USE->{arg}->{message};
			my $ret;
			my $up=int($USE->{param1}*(2-$DT->{rank}/5000));
			$DT->{rank}+=$up;
			$DT->{rank}=10000 if $DT->{rank}>10000;

			$ret='在[新聞]上頭放廣告，人氣提升了'.int($up/100)."%";
			WriteLog(2,0,"【廣告】".$USE->{arg}{message});
			WriteLog(0,$DT->{id},$ret);	
			return $ret;
		_local_
	@@USE
		time	6h
		action	取下招牌
		arg		nocount
		name	取下招牌
		info	將專門職業的招牌拿下來
		func	_local_
			my $ret="";
			main::OutError('無法卸下專門職業的招牌') if ($DT->{job} eq '');
			$DT->{money}+=30000;
			$DT->{job}='';	
			$ret='卸下招牌後，獲得了30000的慰問金';
			WriteLog(0,$DT->{id},"拿下招牌並且接受了慰問金");
			WriteLog(3,0,$DT->{shopname}."卸下專門職業的招牌後，商店街自治會發給了慰問金");
			return $ret;
		_local_

@@ITEM
	no		8
	type	人材
	code	man-black
	name	黑道小弟
	info	使用店力來進行地下工作
	scale	人
	price	50000
	cost	2500
	limit	2/0.2
	plus	2d
	flag	noshowcase|human
	@@use
		time	6h
		exp	5%
		exptime	4h
		job		黑道	times/job_black_time_rate
		scale	回
		action	招募夥伴
		name	招募夥伴
		info	夥伴會來的機率只有50%
		ngmsg	夥伴沒有來呢
		okmsg	成功招募夥伴了
		arg		nocount
			get		1	黑道小弟	50%
	@@use
		time	1h
		exp	1%
		exptime	30m
		job		黑道	times/job_black_time_rate
		scale	回
		action	製作
		name	製作暗黑烏龍麵
		info	盡量使用擁有的材料做成烏龍麵
		func	lostman
		param	50
		ngmsg	暗黑烏龍麵製作失敗了‥
			use		10	髒掉的碗
			get		10	暗黑烏龍麵	95%	做好暗黑烏龍麵了
			get		10	店力	07%
	@@use
		time	1h
		exp	1%
		exptime	30m
		job		黑道	times/job_black_time_rate
		scale	回
		action	製作
		name	製作暗黑蕎麥麵
		info	盡量使用擁有的材料做成蕎麥麵
		func	lostman
		param	50
		ngmsg	暗黑蕎麥麵製作失敗了‥
			use		10	髒掉的碗
			get		10	暗黑蕎麥麵	95%	做好暗黑蕎麥麵了
			get		10	店力	07%
	@@use
		time	4h
		exp	5%
		exptime	2h
		job		黑道	times/job_black_time_rate
		scale	回
		action	執行
		name	執行替換作戰
		info	偷偷把其他店鋪展示架的商品換成其他商品
		arg		target|nocount
			use		1	黑道小弟
			use		50	暗黑烏龍麵
			use		50	暗黑蕎麥麵
			use		10	店力
		func	_local_
		# ★すり替え作戦を実行する
			my $cnt=int(rand(100))+1;
			my $ret="因為替換作戰失敗的關係，店裡的人氣下降了";
			if(rand(1000)<900)
			{
				if($DTS->{item}[@@ITEMNO"警報器"-1])
				{
					if(rand(1000)<200)
					{
					$DTS->{showcase}[0]=57; # 暗黑蕎麥麵のアイテム番号
					$DTS->{price}[0]=20; # 暗黑蕎麥麵の価格
					$DTS->{item}[@@ITEMNO"暗黑蕎麥麵"-1]+=$cnt;
					$DTS->{item}[@@ITEMNO"暗黑蕎麥麵"-1]=2000 if $DTS->{item}[$itemno2-1]>2000;
					$ret="替換作戰成功了";
					$DTS->{item}[@@ITEMNO"警報器"-1]--;
					WriteLog(2,0,$DTS->{shopname}."展示架的商品被換成暗黑蕎麥麵，生氣的店長將警報器弄壞了");
					}
					elsif(rand(1000)<700)
					{
					$DT->{rank}-=int($DT->{rank}/3);
					$DTS->{item}[@@ITEMNO"警報器"-1]--;
					WriteLog(3,0,"入侵".$DTS->{shopname}."後，".$DT->{shopname}."的黑道小弟雖然破壞了警報器，但最後還是被逮捕了");
					}
					else
					{
					$DT->{rank}-=int($DT->{rank}/3);
					WriteLog(3,0,$DTS->{shopname}."的警報器響了，想進行入侵的".$DT->{shopname}."的黑道小弟被逮捕了");
					}
				}
				else
				{
				$DTS->{showcase}[0]=45; # 暗黑烏龍麵のアイテムナンバー
				$DTS->{price}[0]=20; # 暗黑烏龍麵の価格
				$DTS->{item}[@@ITEMNO"暗黑烏龍麵"-1]+=$cnt;
				$DTS->{item}[@@ITEMNO"暗黑烏龍麵"-1]=2000 if $DTS->{item}[$itemno-1]>2000;
				$ret="替換作戰成功了";
				WriteLog(2,0,$DTS->{shopname}."展示架的商品被換成暗黑烏龍麵了");
				}
			}
			else
			{
			$ret="替換作戰失敗了";
			WriteLog(3,0,"不知為何，出現在".$DTS->{shopname}."中的黑道小弟什麼都沒做就離開了。");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			_local_
	@@use
		time	4h
		exp	10%
		job		黑道	times/job_black_time_rate
		scale	回
		action	進行偷竊
		name	進行偷竊
		info	有警報器的商店危險了！？
		arg		target|nocount
			use		50	店力
		func	_local_
			# ★万引き作戦（成功時はイベントと同じメッセージを出力）
			
			my $ret="偷竊失敗，店裡的人氣下降了";
			if(rand(1000)<700)
			{
				if($DTS->{item}[@@ITEMNO"警報器"-1])
				{
					$DT->{rank}-=int($DT->{rank}/2);
					if(rand(1000)<700)
					{
						$DTS->{item}[@@ITEMNO"警報器"-1]--;
						WriteLog(3,0,$DT->{shopname}."的黑道小弟想去".$DTS->{shopname}."偷竊，雖然將$ITEM[@@ITEMNO"警報器"]->{name}破壊，但最後還是被逮捕了。");
					}
					else
					{
						WriteLog(3,0,$DT->{shopname}."的黑道小弟想去".$DTS->{shopname}."偷竊失敗了。");
					}
				}
				else
				{
					my $manbiki_count=0;
					foreach my $idx (0..$DTS->{showcasecount}-1)
					{
						my $itemno=$DTS->{showcase}[$idx];
						if($itemno)
						{
							my $cnt=int($DTS->{item}[$itemno-1]/4);
							$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
							$DTS->{item}[$itemno-1]-=$cnt;
							$DT->{item}[$itemno-1]+=$cnt;
							$manbiki_count+=$cnt*$DTS->{price}[$idx];
						}
					}
					$ret="成功進行偷竊了";
					$ret="黑道小弟改變了主意，停止了入室行竊。" if !$manbiki_count;
					WriteLog(2,0,$DTS->{shopname}."被偷了總價大概".GetMoneyString($manbiki_count)."的財物。") if $manbiki_count;
					WriteLog(2,0,"闖進".$DTS->{shopname}."的小偷什麼都沒拿就逃走了。") if !$manbiki_count;
				}
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/3);
				WriteLog(3,0,$DT->{shopname}."的黑道小弟想去".$DTS->{shopname}."偷竊但失敗了。");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
	@@use
		time	10h
		exp	10%
		job		黑道	times/job_black_time_rate
		scale	回
		action	散佈謠言
		name	散佈店鋪的謠言
		info	散佈流言蜚語，降低其他店舖的人氣
		arg		target|nocount
			use		1	黑道小弟
			use		100	店力
		func	_local_
			# ★悪い噂を流す作戦
			my $ret;
			if(rand(1000)<750)
			{
				$DTS->{rank}-=int($DTS->{rank}/4);
				$ret='散佈'.$DTS->{shopname}.'謠言的作戰成功了。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DTS->{shopname}.'因為謠言的關係人氣下降了。');
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/2);
				$ret='散佈'.$DTS->{shopname}.'謠言的作戰失敗了。';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."的黑道小弟策畫散佈".$DTS->{shopname}.'的謠言。');
			}
			return $ret;
			_local_
	@@use
		time	2h
		exp	10%
		job		黑道	times/job_black_time_rate
		action	解放
		name	將店力解放
		info	將店力全部解放，使店的人氣上升
		arg		nocount
		func	_local_
			main::OutError('店力沒有100以上沒辦法進行解放') if ($DT->{item}[@@ITEMNO"店力"-1]<100);
			my $ret="";
			my $power;
			my $cnt=$DT->{item}[@@ITEMNO"店力"-1];
			$power=$DT->{item}[@@ITEMNO"店力"-1]*3;
			my $up=int($power*(2-$DT->{rank}/5000));

			$DT->{rank}+=$up;
			$DT->{rank}=10000 if $DT->{rank}>10000;
			$ret="全部的店力被解放了（人気提升".int($up/100)."%）";
			UseItem(@@ITEMNO"店力",$cnt);
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."將全部的店力解放了。");
			return $ret;
			_local_
	@@USE
		time	0m
		action	進行時間操作
		scale	回
		name	進行時間操作
		info	如果你成功了，可以讓時光倒流！
			use		2	黑道小弟
		arg		nocount
		func	_local_
			# ★持ち時間増加
			my $ret;
			my $cnt=int(rand(6))+1;

			if(rand(1000)<100)
			{
				$ret='時間操作失敗了';
				WriteLog(3,0,$DT->{shopname}.'的黑道小弟似乎在進行時間操作的時候失敗了。');
				AddItem(8,1,'有1位黑道小弟從時空裂縫中回來了');
				WriteLog(0,$DT->{id},'的時間操作失敗了');
			}
			else
			{
				$DT->{time}-=3600*($cnt);
				$DT->{user}->{black}+=1;
				$ret='時間操作成功了　（＋'.($cnt).'時間）';
				WriteLog(3,0,$DT->{shopname}.'的黑道小弟似乎進行了時間操作。');
				WriteLog(0,$DT->{id},'因為時間操作的結果，持有時間增加了');
			}					
			return $ret;
		_local_
	@@USE
		time	6h
		action	成為地下工作的專家
		arg		nocount
		name	成為地下工作的專家
		info	利用自身的經驗，成為黑道
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('目前已經是黑道了') if ($DT->{job} eq 'black');
			$DT->{job} = 'black';
			$ret="成為黑道了";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		9
	type	陸產品
	code	riku-tamagoa
	name	雞蛋
	info	是一種營養豐富的食物
	scale	個
	price	100
	cost	10
	limit	5000/50
	base	2500/10000
	plus	5h
	pop	40m
	point	20%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	雞蛋
			get		10	堆肥	15%	做成優質堆肥了

@@ITEM
	no		10
	type	陸產品
	code	riku-tamagob
	name	等待孵化的雞蛋
	info	是一種營養豐富的食物
	scale	個
	price	100
	cost	50
	limit	50/0
	pop	10d
	funct	_local_
		my($ITEM,@DT)=@_;
		my $gabirth_per_day=3;  # 1日に鵝が3羽産まれるような確率(?)の設定
		my $nibirth_per_day=30;  # 1日に雞が30羽産まれるような確率(?)の設定
		my $val          =1;  # 一度に産まれる基本数

		my $gabirth_rate=$gabirth_per_day && (86400/$gabirth_per_day); # 0で割るのを阻止
		my $nibirth_rate=$nibirth_per_day && (86400/$nibirth_per_day);
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"等待孵化的雞蛋"-1];
			if(rand($gabirth_rate)<$TIMESPAN) # 1店舗につき「1日に$gabirth_per_day回」の確率で条件が真になる(ハズ…)
			{
				UseItemSub(@@ITEMNO"等待孵化的雞蛋",$val,$DT);
				AddItemSub(@@ITEMNO"鵝",$val,$DT);
				WriteLog(0,$DT->{id},'天啊！雞蛋竟然孵出了鵝');
			}
			if(rand($nibirth_rate)<$TIMESPAN)
			{
				UseItemSub(@@ITEMNO"等待孵化的雞蛋",$val,$DT);
				AddItemSub(@@ITEMNO"雞",$val,$DT);
			}
		}
	_local_ 

@@ITEM
	no		11
	type	陸產品
	code	riku-age
	name	炸豆皮
	info	這是一種通常被認為是狐狸喜愛的食物。
	scale	枚
	price	300
	cost	10
	limit	10000/10
	base	500/2000
	plus	5h
	pop	40m
	point	20%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	炸豆皮
			get		10	堆肥	20%	做成優質堆肥了

@@ITEM
	no		12
	type	陸產品
	code	riku-negi
	name	蔥
	info	烏龍麵和蕎麥麵不可缺少的調味料。
	scale	把
	price	200
	limit	5000/10
	base	500/2000
	plus	3h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	蔥
			get		10	堆肥	25%	做成優質堆肥了

@@ITEM
	no		13
	type	陸產品
	code	riku-komugi
	name	小麥粉
	info	製作烏龍麵和天婦羅的材料
	scale	kg
	price	500
	cost	10
	limit	1000/10
	base	500/1000
	plus	4h
	pop	4h
	point	30%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	小麥粉
			get		10	堆肥	30%	做成優質堆肥了

@@ITEM
	no		14
	type	陸產品
	code	riku-soba
	name	蕎麥粉
	info	製作蕎麥麵的材料
	scale	kg
	price	500
	cost	10
	limit	1000/10
	base	500/1000
	plus	4h
	pop	4h
	point	30%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	蕎麥粉
			get		10	堆肥	30%	做成優質堆肥了

@@ITEM
	no		15
	type	陸產品
	code	riku-tougarasi
	name	唐辛子
	info	用於調味博多名產『明太子』
	scale	kg
	price	800
	limit	1000/10
	base	500/1000
	plus	-1d
	pop	5h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	唐辛子
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		16
	type	陸產品
	code	riku-daizu
	name	大豆
	info	其中一種加工品是『炸豆皮』喔
	scale	kg
	price	400
	limit	1500/20
	base	1000/2000
	plus	-1d
	pop	5h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	大豆
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		17
	type	陸產品
	code	riku-toukibi
	name	玉米
	info	它也可以做為家畜的飼料
	scale	kg
	price	600
	limit	1000/10
	base	500/1000
	plus	-1d
	pop	4h
	point	50%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	玉米
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		18
	type	陸產品
	code	riku-toryuhu
	name	松露
	info	一種罕見的蘑菇
	scale	個
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	松露
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		19
	type	陸產品
	code	riku-foagura
	name	鵝肝
	info	肥鵝的肝臟
	scale	個
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	鵝肝
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		20
	type	陸產品
	code	riku-niwatori
	name	雞
	info	需要飼料來生雞蛋。
	scale	隻
	price	5000
	limit	30/3
	base	30/300
	plus	1d
	pop	10d
	@@USE
		time	30m
		action	交換
		scale	回
		name	與鵝交換
		info	到繁殖場將把雞換成鵝
		okmsg	獲得了鵝
			use		2	雞
			get		1	鵝
	@@USE
		time	30m
		action	交換
		scale	回
		name	與豬交換
		info	到繁殖場將把雞換成豬
		okmsg	獲得了豬
			use		3	雞
			get		1	豬

@@ITEM
	no		21
	type	陸產品
	code	riku-gatyou
	name	鵝
	info	需要飼料來讓牠變胖
	scale	隻
	price	7500
	limit	20/2
	base	20/200
	plus	-1d
	pop	10d

@@ITEM
	no		22
	type	陸產品
	code	riku-buta
	name	豬
	info	如果好好照顧牠的話，可能會報答你的恩惠。
	scale	頭
	price	10000
	limit	20/2
	plus	1d
	pop	10d

@@ITEM
	no		23
	type	海產品
	code	umi-ebi
	name	蝦
	info	附近海域的蝦，肉質緊實
	scale	尾
	price	100
	limit	5000/20
	base	1000/4000
	plus	3h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	蝦
			get		10	堆肥	25%	做成優質堆肥了

@@ITEM
	no		24
	type	海產品
	code	umi-wakame
	name	海帶芽
	info	富含礦物質的海帶芽
	scale	kg
	price	200
	limit	2500/10
	base	100/2000
	plus	4h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	海帶芽
			get		10	堆肥	30%	做成優質堆肥了

@@ITEM
	no		25
	type	海產品
	code	umi-kama
	name	魚板
	info	粉紅色的魚板
	scale	條
	price	300
	limit	1500/10
	plus	4h
	pop	90m
	point	30%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	魚板
			get		10	堆肥	30%	做成優質堆肥了

@@ITEM
	no		26
	type	海產品
	code	umi-maruten
	name	圓形天婦羅
	info	魚漿製成，厚厚的圓形天婦羅
	scale	枚
	price	500
	limit	1000/10
	plus	6h
	pop	150m
	point	50%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	圓形天婦羅
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		27
	type	海產品
	code	umi-ebiten
	name	炸蝦天婦羅
	info	油炸的炸蝦天婦羅
	scale	個
	price	600
	limit	1000
	plus	-1h
	pop	180m
	point	50%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	炸蝦天婦羅
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		28
	type	海產品
	code	umi-suke
	name	黃線狹鱈
	info	可以製成魚板的魚，卵也可以加工。
	scale	尾
	price	1000
	limit	1000/10
	base	500/5000
	plus	5h
	pop	9h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	黃線狹鱈
			get		10	堆肥	50%	做成優質堆肥了

@@ITEM
	no		29
	type	海產品
	code	umi-eso
	name	狗母魚
	info	魚漿可以做成天婦羅的魚
	scale	尾
	price	2000
	limit	500/5
	base	250/5000
	plus	7h
	pop	18h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	狗母魚
			get		10	堆肥	50%	做成優質堆肥了

@@ITEM
	no		32
	type	海產品
	code	umi-katuo
	name	鰹魚
	info	製作高級烏龍麵（蕎麥麵）湯頭的必備品
	scale	尾
	price	2000
	limit	500
	base	250/5000
	plus	-1m
	pop	18h
	point	200%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	鰹魚
			get		10	堆肥	50%	做成優質堆肥了

@@ITEM
	no		33
	type	海產品
	code	umi-tyouzame
	name	鱘魚
	info	它是一種被稱為海中珍寶的魚。
	scale	尾
	price	8000
	limit	100
	base	250/5000
	plus	-1m
	pop	4d
	point	200%
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	鱘魚
			get		10	堆肥	80%	做成優質堆肥了

@@ITEM
	no		30
	type	海產品
	code	umi-mentai
	name	明太子
	info	將黃線狹鱈的魚卵與唐辛子汁醃製，是博多名產之一
	scale	kg
	price	3000
	limit	300
	base	50/200
	plus	-1d
	pop	12h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	明太子
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		31
	type	海產品
	code	umi-kyabia
	name	魚子醬
	info	珍貴到被稱為黑色鑽石，鱘魚的卵。
	scale	kg
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	放入堆肥
		name	放入堆肥
		info	把舊食物放入堆肥中，做成堆肥
		ngmsg	堆肥製作失敗了
			use		1	魚子醬
			get		10	堆肥	35%	做成優質堆肥了

@@ITEM
	no		34
	type	烏龍麵
	code	udon-su
	name	清湯烏龍麵
	info	深受饕客喜愛的簡單烏龍麵
	price	500
	limit	1000/0
	pop	75m
	point	40%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	非常好吃
			use		1	清湯烏龍麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		35
	type	烏龍麵
	code	udon-wakame
	name	海帶芽烏龍麵
	info	猶如閃亮亮頭髮的健康烏龍麵
	price	600
	limit	1000/0
	pop	90m
	point	50%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	非常好吃
			use		1	海帶芽烏龍麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		36
	type	烏龍麵
	code	udon-kitune
	name	豆皮烏龍麵
	info	搭配味道濃郁炸豆腐的烏龍麵
	price	800
	limit	1000/0
	pop	120m
	point	60%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	非常好吃
			use		1	豆皮烏龍麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		37
	type	烏龍麵
	code	udon-maruten
	name	天婦羅烏龍麵
	info	搭配圓形天婦羅的烏龍麵
	price	1000
	limit	1000/0
	pop	120m
	point	75%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	非常好吃
			use		1	天婦羅烏龍麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		38
	type	烏龍麵
	code	udon-ebiten
	name	炸蝦烏龍麵
	info	搭配兩隻炸蝦的烏龍麵
	price	2000
	limit	500/0
	pop	240m
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	非常好吃
			use		1	炸蝦烏龍麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		39
	type	烏龍麵
	code	udon-zanmai
	name	烏龍麵三昧
	info	搭配三種推薦配料的烏龍麵
	scale	組
	price	5000
	limit	200
	pop	8h
	point	500%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	非常好吃
			use		1	烏龍麵三昧
			get		3	髒掉的碗
			get		10	店力	30%

@@ITEM
	no		40
	type	烏龍麵
	code	udon-kyabia
	name	魚子醬烏龍麵
	info	世界三大美味烏龍麵之一
	price	7500
	limit	120/0
	pop	12h
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	出乎意料的好吃
			use		1	魚子醬烏龍麵
			get		1	髒掉的碗
			get		10	店力	50%

@@ITEM
	no		41
	type	烏龍麵
	code	udon-toryuhu
	name	松露烏龍麵
	info	世界三大美味烏龍麵之一
	price	8000
	limit	120/0
	pop	13h
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	出乎意料的好吃
			use		1	松露烏龍麵
			get		1	髒掉的碗
			get		10	店力	50%

@@ITEM
	no		42
	type	烏龍麵
	code	udon-foagura
	name	鵝肝烏龍麵
	info	世界三大美味烏龍麵之一
	price	10000
	limit	100/0
	pop	15h
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	出乎意料的好吃
			use		1	鵝肝烏龍麵
			get		1	髒掉的碗
			get		10	店力	50%

@@ITEM
	no		43
	type	烏龍麵
	code	udon-hakata
	name	博多烏龍麵
	info	博多風的特製烏龍麵
	price	20000
	limit	50
	pop	25h
	point	200%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	出乎意料的好吃
			use		1	博多烏龍麵
			get		1	髒掉的碗
			get		10	店力	70%

@@ITEM
	no		44
	type	烏龍麵
	code	udon-origi
	name	原創烏龍麵
	info	灌注靈魂所製作的原創烏龍麵
	price	50000
	limit	20/0
	pop	60h
	point	200%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	像夢一般美味
			use		1	原創烏龍麵
			get		1	髒掉的碗
			get		20	店力	50%

@@ITEM
	no		45
	type	烏龍麵
	code	udon-yami
	name	暗黑烏龍麵
	info	黑道小弟製作的難吃烏龍麵
	price	100
	limit	5000/0
	pop	1h
	point	-10%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的烏龍麵
		okmsg	即使奉承也不好吃
			use		1	暗黑烏龍麵
			get		1	髒掉的碗

@@ITEM
	no		46
	type	蕎麥麵
	code	soba-kake
	name	清湯蕎麥麵
	info	深受饕客喜愛的簡單蕎麥麵
	price	500
	limit	1000/0
	pop	75m
	point	40%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	非常好吃
			use		1	清湯蕎麥麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		47
	type	蕎麥麵
	code	soba-wakame
	name	海帶芽蕎麥麵
	info	猶如閃亮亮頭髮的健康蕎麥麵
	price	600
	limit	1000/0
	pop	90m
	point	50%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	非常好吃
			use		1	海帶芽蕎麥麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		48
	type	蕎麥麵
	code	soba-kitune
	name	豆皮蕎麥麵
	info	搭配味道濃郁炸豆腐的蕎麥麵
	price	800
	limit	1000/0
	pop	120m
	point	60%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	非常好吃
			use		1	豆皮蕎麥麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		49
	type	蕎麥麵
	code	soba-maruten
	name	天婦羅蕎麥麵
	info	搭配圓形天婦羅的蕎麥麵
	price	1000
	limit	1000/0
	pop	120m
	point	75%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	非常好吃
			use		1	天婦羅蕎麥麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		50
	type	蕎麥麵
	code	soba-ebiten
	name	炸蝦蕎麥麵
	info	搭配兩隻炸蝦的蕎麥麵
	price	2000
	limit	500/0
	pop	240m
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	非常好吃
			use		1	炸蝦蕎麥麵
			get		1	髒掉的碗
			get		10	店力	20%

@@ITEM
	no		51
	type	蕎麥麵
	code	soba-zanmai
	name	蕎麥麵三昧
	info	搭配三種推薦配料的蕎麥麵
	scale	組
	price	5000
	limit	200
	pop	8h
	point	500%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	非常好吃
			use		1	蕎麥麵三昧
			get		3	髒掉的碗
			get		10	店力	30%

@@ITEM
	no		52
	type	蕎麥麵
	code	soba-kyabia
	name	魚子醬蕎麥麵
	info	世界三大美味蕎麥麵之一
	price	7500
	limit	120/0
	pop	12h
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	出乎意料的好吃
			use		1	魚子醬蕎麥麵
			get		1	髒掉的碗
			get		10	店力	50%

@@ITEM
	no		53
	type	蕎麥麵
	code	soba-toryuhu
	name	松露蕎麥麵
	info	世界三大美味蕎麥麵之一
	price	8000
	limit	120/0
	pop	13h
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	出乎意料的好吃
			use		1	松露蕎麥麵
			get		1	髒掉的碗
			get		10	店力	50%

@@ITEM
	no		54
	type	蕎麥麵
	code	soba-foagura
	name	鵝肝蕎麥麵
	info	世界三大美味蕎麥麵之一
	price	10000
	limit	100/0
	pop	15h
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	出乎意料的好吃
			use		1	鵝肝蕎麥麵
			get		1	髒掉的碗
			get		10	店力	50%

@@ITEM
	no		55
	type	蕎麥麵
	code	soba-hakata
	name	博多蕎麥麵
	info	博多風的特製蕎麥麵
	price	20000
	limit	50
	pop	25h
	point	200%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	出乎意料的好吃
			use		1	博多蕎麥麵
			get		1	髒掉的碗
			get		10	店力	70%

@@ITEM
	no		56
	type	蕎麥麵
	code	soba-origi
	name	原創蕎麥麵
	info	灌注靈魂所製作的原創蕎麥麵
	price	50000
	limit	20/0
	pop	60h
	point	200%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	像夢一般美味
			use		1	原創蕎麥麵
			get		1	髒掉的碗
			get		20	店力	50%

@@ITEM
	no		57
	type	蕎麥麵
	code	soba-yami
	name	暗黑蕎麥麵
	info	黑道小弟製作的難吃蕎麥麵
	price	100
	limit	5000/0
	pop	1h
	point	-10%
	@@USE
		time	5m
		action	食用
		name	食用
		info	食用熱騰騰的蕎麥麵
		okmsg	即使奉承也不好吃
			use		1	暗黑蕎麥麵

@@ITEM
	no		58
	type	工具
	code	tool-tikara
	name	店力
	info	在緊急情況下它可能會顯示出它的真正價值[店的力量]
	scale	力
	price	0
	limit	1000/0
	pop		0
	flag	noshowcase|norequest|notrash
	@@use
		time	10m
		scale	回
		action	沐浴
		name	沐浴
		info	用祈禱沐浴在店力中
		arg		nocount
			use		500	店力
		func	_local_
			my $ret='沐浴在店力中祈禱後似乎有股神秘的力量';

			if ((rand(1000)<20) && !$DT->{item}[@@ITEMNO"原創烏龍麵食譜"-1])
			{
				AddItem(@@ITEMNO"原創烏龍麵食譜",1,"突然颳起一陣風吹來了張紙片，天啊！竟然是某間店的「原創烏龍麵食譜」");
				WriteLog(0,$DT->{id},'得到原創烏龍麵食譜了');
			}
			elsif((rand(1000)<20) && !$DT->{item}[@@ITEMNO"原創蕎麥麵食譜"-1])
			{
				AddItem(@@ITEMNO"原創蕎麥麵食譜",1,"突然颳起一陣風吹來了張紙片，天啊！竟然是某間店的「原創蕎麥麵食譜」");
				WriteLog(0,$DT->{id},'得到原創蕎麥麵食譜了');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"豬"-1]<=10))
			{
				AddItem(@@ITEMNO"豬",10,"一群野生的豬衝進了店裡");
				WriteLog(0,$DT->{id},'得到豬了');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"鵝"-1]<=10))
			{
				AddItem(@@ITEMNO"鵝",10,"一群野生的鵝衝進了店裡");
				WriteLog(0,$DT->{id},'得到鵝了');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"唐辛子"-1]<=500))
			{
				AddItem(@@ITEMNO"唐辛子",500,"遠房親戚寄了一小包唐辛子。");
				WriteLog(0,$DT->{id},'得到唐辛子了');
			}
			elsif((rand(1000)<100) && $DT->{item}[@@ITEMNO"雞"-1] && ($DT->{item}[@@ITEMNO"雞蛋"-1]<=2700))
			{
				AddItem(@@ITEMNO"雞蛋",$DT->{item}[@@ITEMNO"雞"-1]*10,"飼っている雞が一斉に雞蛋を10個ずつ産みました");
				WriteLog(0,$DT->{id},'得到雞蛋了');
			}
			elsif((rand(1000)<100) && $DT->{item}[@@ITEMNO"豬"-1] && ($DT->{item}[@@ITEMNO"松露"-1]<=50))
			{
				AddItem(@@ITEMNO"松露",$DT->{item}[@@ITEMNO"豬"-1]*5,"飼養的豬隻竟然，嘴巴裡都含著5個松露");
				WriteLog(0,$DT->{id},'得到松露了');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"黑道小弟"-1]<2))
			{
				AddItem(@@ITEMNO"黑道小弟",1,"黑道小弟偷偷的溜進店裡後說，請雇用他吧");
				WriteLog(0,$DT->{id},'得到黑道小弟了');
			}
			elsif((rand(1000)<20) && $DT->{user}->{udon} && ($DT->{user}->{udon}ne'唐努拉烏龍麵') && ($DT->{user}->{udon}ne'超級厲害ＵＤＯＮ'))
			{
				if (rand(1000)<500)
				{
					$ret.='<br>突然腦中閃過，開發的原創烏龍麵的名稱變成「唐努拉烏龍麵」了<br>';
					$DT->{user}->{udon}='唐努拉烏龍麵';
				}
				else
				{
					$ret.='<br>突然腦中閃過，開發的原創烏龍麵的名稱變成「超級厲害ＵＤＯＮ」了<br>';
					$DT->{user}->{udon}='超級厲害ＵＤＯＮ';
				}
				WriteLog(0,$DT->{id},'原創烏龍麵名稱修改完成了');
				WriteLog(3,0,$DT->{shopname}.'的店長沐浴在店力之下，原創烏龍麵的名稱變更了');
			}
			elsif((rand(1000)<20) && $DT->{user}->{soba} && ($DT->{user}->{soba}ne'愛的脫離貧窮蕎麥麵') && ($DT->{user}->{soba}ne'滑頭鬼蕎麥麵'))
			{
				if (rand(1000)<500)
				{
					$ret.='<br>突然腦中閃過，開發的原創蕎麥麵的名稱變成「愛的脫離貧窮蕎麥麵」了<br>';
					$DT->{user}->{soba}='愛的脫離貧窮蕎麥麵';
				}
				else
				{
					$ret.='<br>突然腦中閃過，開發的原創蕎麥麵的名稱變成「滑頭鬼蕎麥麵」了<br>';
					$DT->{user}->{soba}='滑頭鬼蕎麥麵';
				}
				WriteLog(0,$DT->{id},'原創蕎麥麵名稱修改完成了');
				WriteLog(3,0,$DT->{shopname}.'的店長沐浴在店力之下，原創蕎麥麵的名稱變更了');
			}
			else
			{
				$ret.='<br>店力使得能量增幅，可以活動的時間增加了';
				my $cnt=int(rand(6))+5;
				$DT->{time}-=3600*($cnt);
				$ret.='（＋'.($cnt).'時間）<br>';
				WriteLog(0,$DT->{id},'沐浴在店力中祈禱後，持有的時間增加了');
			}
			return $ret;
		_local_

@@ITEM
	no		59
	type	工具
	code	tool-huku
	name	抽獎卷
	info	可以用5張抽獎卷抽1次獎
	scale	枚
	price	0
	limit	1000/0
	pop		0
	@@USE
		time	5m
		action	抽獎
		name	抽獎
		info	用收到的抽獎卷進行抽獎
		scale	回
			use		5	抽獎卷
		func	_local_
			# ★福引き
			my $ret;
			my $hit1=0; #手に入る特等景品の個数
			my $hit2=0; #手に入る1等景品の個数
			my $hit3=0; #手に入る2等景品の個数
			my $hit4=0; #手に入る3等景品の個数
			my $hit5=0; #手に入る4等景品の個数
			my $hit6=0; #手に入る5等景品の個数
			my $hit7=0; #手に入る残念賞の個数

			foreach(1..$count)
			{
				if(rand(1000)<1)
				{
					$hit1+=1;
				}
				elsif(rand(1000)<3)
				{
					$hit2+=1;
				}
				elsif(rand(1000)<10)
				{
					$hit3+=1;
				}
				elsif(rand(1000)<50)
				{
					$hit4+=1;
				}
				elsif(rand(1000)<100)
				{
					$hit5+=1;
				}
				elsif(rand(1000)<200)
				{
					$hit6+=1;
				}
			}
			$hit7=$count-($hit1+$hit2+$hit3+$hit4+$hit5+$hit6);
			AddItem(83,$hit1,'天啊！抽中了'.$hit1.'次特獎的招財貓') if ($hit1>=1);
			AddItem(82,$hit2,'天啊！抽中了'.$hit2.'次頭獎的汽車') if ($hit2>=1);
			AddItem(80,$hit3,'抽中了'.$hit3.'次二獎的洗碗機') if ($hit3>=1);
			AddItem(79,$hit4,'抽中了'.$hit4.'次三獎的腳踏車') if ($hit4>=1);
			AddItem(67,$hit5,'抽中了'.$hit5.'次四獎的攻略本') if ($hit5>=1);
			AddItem(66,$hit6,'抽中了'.$hit6.'次五獎的商品券') if ($hit6>=1);
			AddItem(64,$hit7,'抽到'.$hit7.'次安慰獎乾淨的碗') if ($hit7>=1);
			$ret='抽獎什麼都沒中';
			$ret='抽到獎品了' if ($hit7<$count);
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		60
	type	工具
	code	tool-udon
	name	原創烏龍麵食譜
	info	記載著原創烏龍麵的製作方法
	scale	枚
	price	0
	limit	1/0
	pop		0
	@@USE
		time	1m
		action	閱讀
		name	閱讀食譜
		info	為了忘記原創烏龍麵的材料與製作方法的時候
		scale	回
		arg		nocount
		ngmsg	【原創烏龍麵的製作方法】<br>材料<br>・小麥粉<br>・鰹魚<br>・鵝<br>・唐辛子<br>・乾淨的碗<br><br>做法<br><b>&nbsp;&nbsp;秘密</b>
	@@USE
		time	4h
		job		烏龍麵屋	times/job_udon_time_rate
		action	重新命名為
		name	修改原創烏龍麵的名稱
		info	修改原創烏龍麵的名稱
		arg		nocount|message30
		func	_local_
			# 原創烏龍麵の名前を変える
			main::OutError('請先開發原創烏龍麵') if !$DT->{user}->{udon};
			main::OutError('請輸入名稱') if !$USE->{arg}->{message};
			my $ret;
			$ret='原創蕎麥麵的名稱變成【'.$USE->{arg}->{message}.'】了';	
			WriteLog(3,0,$DT->{shopname}."改變原創烏龍麵的名稱了");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{udon}=$USE->{arg}->{message};
			return $ret;
		_local_

@@ITEM
	no		61
	type	工具
	code	tool-soba
	name	原創蕎麥麵食譜
	info	記載著原創蕎麥麵的製作方法
	scale	枚
	price	0
	limit	1/0
	pop		0
	@@USE
		time	1m
		action	閱讀
		name	閱讀食譜
		info	為了忘記原創蕎麥麵的材料與製作方法的時候
		scale	回
		arg		nocount
		ngmsg	【原創蕎麥麵的製作方法】<br>材料<br>・蕎麥粉<br>・鰹魚<br>・鱘魚<br>・魚卵<br>・乾淨的碗<br><br>做法<br><b>&nbsp;&nbsp;秘密</b>
	@@USE
		time	4h
		job		蕎麥麵屋	times/job_soba_time_rate
		action	重新命名為
		name	修改原創蕎麥麵的名稱
		info	修改原創蕎麥麵的名稱
		arg		nocount|message30
		func	_local_
			main::OutError('請先開發原創蕎麥麵') if !$DT->{user}->{soba};
			main::OutError('請輸入名稱') if !$USE->{arg}->{message};
			my $ret;
			$ret='原創蕎麥麵的名稱變成【'.$USE->{arg}->{message}.'】了';	
			WriteLog(3,0,$DT->{shopname}."改變原創蕎麥麵的名稱了");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{soba}=$USE->{arg}->{message};
			return $ret;
		_local_

@@ITEM
	no		62
	type	工具
	code	tool-taihi
	name	堆肥
	info	田地的肥料
	scale	kg
	price	5
	cost	0
	limit	5000/1000
	base	100/20000
	plus	20m
	pop		20m
	point	10%

@@ITEM
	no		63
	type	工具
	code	tool-yogore
	name	髒掉的碗
	info	使用過的碗
	scale	個
	price	10
	cost	0
	limit	10000/0
	pop		0

@@ITEM
	no		64
	type	工具
	code	tool-kirei
	name	乾淨的碗
	info	洗乾淨的碗
	scale	個
	price	50
	cost	10
	limit	3000/2000
	base	10000/100000
	plus	1h
	pop	10d

@@ITEM
	no		65
	type	工具
	code	tool-takara
	name	彩卷
	info	夢想快速致富...
	scale	枚
	price	1000
	cost	10
	limit	100/20
	plus	3h
	pop		2h
	flag	noshowcase|norequest

@@ITEM
	no		66
	type	工具
	code	tool-syou
	name	商品券
	info	可以換成想要的物品
	scale	枚
	price	5000
	cost	10
	limit	500/0
	pop		0
	@@USE
		time	10m
		action	交換
		scale	回
		name	交換堆肥
		info	將商品券換成想要的物品
		okmsg	獲得了堆肥
			use		1	商品券
			get		250	堆肥
	@@USE
		time	10m
		action	交換
		scale	回
		name	交換乾淨的碗
		info	將商品券換成想要的物品
		okmsg	獲得了乾淨的碗
			use		1	商品券
			get		100	乾淨的碗
	@@USE
		time	10m
		action	交換
		scale	回
		name	交換攻略本
		info	將商品券換成想要的物品
		okmsg	獲得了攻略本
			use		2	商品券
			get		1	攻略本
	@@USE
		time	10m
		action	交換
		scale	回
		name	交換警報器
		info	將商品券換成想要的物品
		okmsg	獲得了警報器
			use		40	商品券
			get		1	警報器
	@@USE
		time	10m
		action	交換
		scale	回
		name	交換汽車
		info	將商品券換成想要的物品
		okmsg	獲得了汽車
			use		100	商品券
			get		1	汽車
	@@USE
		time	10m
		action	交換
		scale	回
		name	交換招財貓
		info	將商品券換成想要的物品
		okmsg	獲得了招財貓
			use		200	商品券
			get		1	招財貓
	@@use
		time	10m
		scale	枚
		action	換錢
		name	換錢
		info	商品券
		param	500,2500
			use		1	商品券
		func	_local_
			my $ret;
			if (rand(1000)<300)
			{
				$DT->{money}+=$USE->{param1}*$count;
				$ret='金券行的大叔好像會買的樣子<br>';
				$ret.='換到'.GetMoneyString($USE->{param1}*$count).'了';
			}
			else
			{
			$DT->{money}+=$USE->{param2}*$count;
			$ret='換到'.GetMoneyString($USE->{param2}*$count).'了';
			}
			WriteLog(0,$DT->{id},"將商品券換成了錢");
			return $ret;
		_local_

@@ITEM
	no		67
	type	工具
	code	tool-hint
	name	攻略本
	info	<b>注意！有★符號的提示看了之後，攻略本會被刪除</b>
	scale	本
	price	10000
	cost	10
	limit	5/0
	pop		0
	flag	noshowcase|norequest
	@@USE
		time	1m
		action	閱讀提示
		name	新手入門
		info	如果您不知道先做什麼可以閱讀提示
		arg		nocount
		ngmsg	（可以閱讀「圖書館」內的資料）<br><br>從市場或商店街招募農民或漁夫。<br>（如果都沒有的話，可以先招募臨時工再轉職成農夫或漁夫）<br>漁夫可以馬上開始捕魚。<br>農夫可以取得田地後進行收割。<br>收穫後的田地會變回「耕作前的田地」，可以再進行耕作，1反需要堆肥100kg<br>隨著時間的流逝，「耕作後的田地」會變成「待收割的田地」。
	@@USE
		time	10m
		action	閱讀提示
		name	★臨時工的秘密
		info	針對想從事人力仲介的人
		arg		nocount
		ngmsg	・想要進行烏龍麵師傅修行的話，需要臨時工和小麥粉。<br>・想要進行蕎麥麵師傅修行的話，需要臨時工和蕎麥粉。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★農夫的秘密
		info	從事農業的方法
		arg		nocount
		ngmsg	・用飼料飼養動物。雞和鵝的飼料是玉米，豬的飼料是大豆。<br>・當你有幾個雞蛋時，可以讓母雞孵蛋，讓牠們孵化。<br>（等待孵化的雞蛋，隨著時間的推移，牠們會慢慢長成成雞。）<br>・也可以使用雞，將其換成鵝或豬。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★漁夫的秘密
		info	從事漁業的方法
		arg		nocount
		ngmsg	・如果有足夠的蝦，可以去釣魚。<br>・準備黃線狹鱈和唐辛子，可以做成明太子。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★天婦羅師傅的秘密
		info	從事天婦羅屋的方法
		arg		nocount
		ngmsg	・可以用大豆做炸豆皮。<br>・黃線狹鱈可以做成魚板。<br>・狗母魚可以做成圓形天婦羅。<br>・準備蝦、小麥粉和雞蛋，可以做成炸蝦天婦羅。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★烏龍麵師傅的秘密
		info	從事烏龍麵屋的方法
		arg		nocount
		ngmsg	・可以做的烏龍麵，按標準價格升序排列為「清湯烏龍麵」「海帶芽烏龍麵」「豆皮烏龍麵」<br>「天婦羅烏龍麵」「炸蝦烏龍麵」「烏龍麵三昧」「魚子醬烏龍麵」「松露烏龍麵」「鵝肝烏龍麵」<br>「博多烏龍麵」「原創烏龍麵」共11種。<br>・清湯烏龍麵材料是小麥粉、蔥、魚板還有乾淨的碗（製作烏龍麵的基本）。<br>・烏龍麵三昧是將指定的三種配料組合做成的。<br>・許多高檔烏龍麵料理都需要鰹魚。<br>・博多烏龍麵是豚骨風味的，上面有博多特產海鮮加工品。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★蕎麥麵師傅的秘密
		info	從事蕎麥麵屋的方法
		arg		nocount
		ngmsg	・可以做的蕎麥麵，按標準價格升序排列為「清湯蕎麥麵」「海帶芽蕎麥麵」「豆皮蕎麥麵」<br>「天婦羅蕎麥麵」「炸蝦蕎麥麵」「蕎麥麵三昧」「魚子醬蕎麥麵」「松露蕎麥麵」「鵝肝蕎麥麵」<br>「博多蕎麥麵」「原創蕎麥麵」共11種。<br>・清湯蕎麥麵的材料是蕎麥粉、蔥、魚板還有乾淨的碗（製作蕎麥麵的基本）。<br>・蕎麥麵三昧是將指定的三種配料組合做成的。<br>・許多高檔蕎麥麵料理都需要鰹魚。<br>・博多蕎麥麵是豚骨風味的，上面有博多特產海鮮加工品。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★便利屋的秘密
		info	從事人力仲介的方法
		arg		nocount
		ngmsg	・臨時工可以成為人力仲介，便利屋可以使得各種作業時間縮短。<br>・獲得洗碗機的話，可以在短時間內將髒掉的碗洗乾淨。<br>・取下專門職業招牌的話，商店街自治會會發給慰問金。
			use		1	攻略本
	@@USE
		time	10m
		action	閱讀提示
		name	★黑道小弟的秘密
		info	從事黑道的方法
		arg		nocount
		ngmsg	・如果有一定數量髒掉的碗的話，可以製作暗黑烏龍麵和暗黑蕎麥麵。<br>・在暗黑烏龍麵和暗黑蕎麥麵很多的時候，如果有一點店力，可以進行替換作戰。<br>・散佈謠言需要100的店力。<br>・有2名黑道小弟時，在店力有100的情況下可以進行時間操作。<br>（通過時間操作，可用時間會隨機增加）
			use		1	攻略本
	@@USE
		time	1m
		action	閱讀提示
		name	關於展示架
		info	這是展示架擴增與維護費的說明
		arg		nocount
		ngmsg	想變更展示架數量時，可以使用便利屋。<br>但是，便利屋1人只能將展示架變成２個，<br>如果還要增加更多的話，需要的便利屋數量也會更多。<br>展示架的維護費，會隨著數量增加而變多。
	@@USE
		time	1m
		action	閱讀提示
		name	關於店力
		info	店力相關的說明
		arg		nocount
		ngmsg	店力（店的力量），可以透過採取等生產性行動<br>以及吃烏龍麵和蕎麥麵獲得。<br>黑道小弟或招財貓需要使用這種力量。
	@@USE
		time	1m
		action	閱讀提示
		name	關於原創烏龍麵（蕎麥麵）
		info	原創烏龍麵（蕎麥麵）製作方法的說明
		arg		nocount
		ngmsg	除了烏龍麵（蕎麥麵）三昧以及原創烏龍麵（蕎麥麵）以外，需要準備全部種類的烏龍麵（蕎麥麵）各一碗，<br>烏龍麵（蕎麥麵）師傅似乎可以開發原創烏龍麵（蕎麥麵）。<br>原創烏龍麵（蕎麥麵）可以指定自己想要的名稱。<br>在櫥窗（展示架1）販售時，這個名字會在排行榜上顯示。
	@@USE
		time	1m
		action	閱讀提示
		name	關於髒掉的碗
		info	髒掉的碗相關的說明
		arg		nocount
		ngmsg	烏龍麵或蕎麥麵販售後，倉庫裡會產生髒掉的碗。<br>（從其他店舖裡購買的話，不會退還空碗）<br>但是，暗黑烏龍麵和暗黑蕎麥麵是例外<br>一般人會說「好，好難吃啊！」一怒之下把碗砸碎。
	@@USE
		time	1m
		action	閱讀提示
		name	關於攻略本
		info	攻略本獲得方法與相關的說明
		arg		nocount
		ngmsg	攻略本可以透過商品券交換得到。<br>商品券為決算時可能得到的獎品。<br>另外，攻略本也可能在抽獎時抽到。<br>在市場購物時可能會獲得抽獎卷。
	@@use
		time	10m
		scale	冊
		action	換成錢
		name	換成錢
		info	將攻略本拿去金券行換成錢
		param	1000,5000
			use		1	攻略本
		func	_local_
			my $ret;
			if (rand(1000)<300)
			{
				$DT->{money}+=$USE->{param1}*$count;
				$ret='金券行的大叔好像會買的樣子<br>';
				$ret.='換到'.GetMoneyString($USE->{param1}*$count).'了';
			}
			else
			{
			$DT->{money}+=$USE->{param2}*$count;
			$ret='換到'.GetMoneyString($USE->{param2}*$count).'了';
			}
			WriteLog(0,$DT->{id},"將攻略本換成錢了");
			return $ret;
		_local_

@@ITEM
	no		68
	type	工具
	code	tool-paintr
	name	紅色顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		69
	type	工具
	code	tool-paintb
	name	藍色顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		70
	type	工具
	code	tool-painto
	name	橘色顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		71
	type	工具
	code	tool-painty
	name	黃色顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		72
	type	工具
	code	tool-paintg
	name	綠顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		73
	type	工具
	code	tool-paintp
	name	粉紅色顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		74
	type	工具
	code	tool-painte
	name	紫色顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		75
	type	工具
	code	tool-paintk
	name	黒顏料
	info	（沒辦法使用的道具。請丟棄）
	scale	罐
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		76
	type	工具
	code	tool-hatakea
	name	耕作前的田地
	info	施予充足的的肥料吧
	scale	反
	price	5000
	limit	40/2
	plus	1d
	pop		2d
	flag	noshowcase|onlysend

@@ITEM
	no		77
	type	工具
	code	tool-hatakeb
	name	耕作後的田地
	info	過一段時間就可以收割了
	scale	反
	price	10000
	limit	20/0
	pop		1d
	flag	noshowcase|onlysend
	funct	_local_
		my($ITEM,@DT)=@_;
		my $birth_per_day=40;  # 1日に待收割的田地が40になる確率の設定
		my $val          =1;  # 一度に待收割的田地になる基本数
		
		my $birth_rate=$birth_per_day && (86400/$birth_per_day); # 0で割るのを阻止
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"耕作後的田地"-1];
			if(rand($birth_rate)<$TIMESPAN) # 1店舗につき「1日に$birth_per_day回」の確率で条件が真になる(ハズ…)
			{
				UseItemSub(@@ITEMNO"耕作後的田地",$val,$DT);
				AddItemSub(@@ITEMNO"待收割的田地",$val,$DT);
			}
		}
	_local_ 

@@ITEM
	no		78
	type	工具
	code	tool-hatakec
	name	待收割的田地
	info	可以期待各式各樣的收穫
	scale	反
	price	20000
	limit	20/0
	pop		1d
	flag	noshowcase|onlysend

@@ITEM
	no		79
	type	工具
	code	tool-ziten
	name	腳踏車
	info	讓購物更輕鬆
	scale	台
	price	30000
	cost	1000
	limit	1/0.5
	plus	10d
	pop		3d
	flag	noshowcase|onlysend

@@ITEM
	no		80
	type	工具
	code	tool-syokki
	name	洗碗機
	info	可以快速完成洗碗
	scale	台
	price	100000
	cost	3000
	limit	1/0.8
	plus	10d
	pop		10d
	flag	noshowcase|onlysend

@@ITEM
	no		81
	type	工具
	code	tool-keihou
	name	警報器
	info	為了店鋪安全...
	scale	台
	price	200000
	cost	5000
	limit	1/0.5
	plus	10d
	pop		20d
	flag	noshowcase|onlysend

@@ITEM
	no		82
	type	工具
	code	tool-kuruma
	name	汽車
	info	讓購物更輕鬆
	scale	台
	price	500000
	cost	5000
	limit	1/0.3
	plus	10d
	pop	30d
	flag	noshowcase|onlysend

@@ITEM
	no		83
	type	工具
	code	tool-neko
	name	招財貓
	info	店裡的守護神
	scale	尊
	price	1000000
	cost	1000
	limit	1/0.2
	plus	10d
	pop		50d
	flag	noshowcase|onlysend
	@@use
		time	3m
		scale	回
		action	膜拜
		name	膜拜
		info	為了生意興隆，膜拜招財貓
			use		1	店力
		func	_local_
			my $val=$count;
			my $ret="";
			
			if($count>=50)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'店主昏倒，被救護車抬走了。');
				WriteLog(2,0,'一次拜了'.$count.'回招財貓，不一定是理智的。');
				$ret="..當醒來時躺在病床上";
			}
			elsif($count>=20)
			{
				$ret='膜拜太多次引起貧血 要等'.$count.'回合後才可以膜拜。';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='膜拜招財貓後，感覺今天生意不錯。';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_

@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto
	startfunc	loto
	info		彩卷抽選

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		luckyneko
	info		招財貓的財運
	startfunc	_local_(200)
		my($hitproba)=@_;
		
		foreach my $DT (@main::DT)
		{
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"招財貓")
			{			
			if ($DT->{item}[@@ITEMNO"招財貓"-1])
			{
				$DT->{item}[@@ITEMNO"招財貓"-1]=0;
				my $up=int(1000*(2-$DT->{rank}/5000));
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				WriteLog(2,0,$DT->{shopname}."的招財貓給店裡帶來的好運飛上天了。");
				WriteLog(0,$DT->{id},"招財貓不可思議的力量，使店裡的人氣上升".int($up/100)."%了");			}
			}		
			}
		}
		return 0;
	_local_

@@EVENT
	start		100%
	basetime	0h
	plustime	0h
	code		yogoredon
	info		髒掉的碗的惡臭
	startfunc	_local_(500)
		my($hitproba)=@_;
		
		foreach my $DT (@main::DT)
		{
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"髒掉的碗")
			{			
			if ($DT->{item}[@@ITEMNO"髒掉的碗"-1]>=1000)
			{
				my $down=int($DT->{rank}/5);
				$DT->{rank}-=$down;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}."髒掉的碗散發出難聞的氣味，店裡的人氣下降了。");
				WriteLog(0,$DT->{id},"因為髒掉的碗的關係，店裡的人氣下降".int($down/100)."%了");			}
			}		
			}
		}
		return 0;
	_local_

# 原創烏龍麵で人気アップ
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		udonpop
	info		原創烏龍麵人氣沸騰
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if rand(1000)>200;
			if ($_->{user}->{udon}&&($_->{user}->{udon} ne 'n'))
			{
			my $up=int(300*(2-$_->{rank}/5000));
			$_->{rank}+=$up;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'特製烏龍麵「'.$_->{user}->{udon}.'」成了街上熱門話題，店前坐滿了滿懷期待的顧客。') ;
			}
		}
		return 0;
	_local_

# 原創蕎麥麵で人気アップ
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		sobapop
	info		原創蕎麥麵人氣沸騰
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if rand(1000)>200;
			if ($_->{user}->{soba}&&($_->{user}->{soba} ne 'n'))
			{
			my $up=int(300*(2-$_->{rank}/5000));
			$_->{rank}+=$up;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'特製蕎麥麵「'.$_->{user}->{soba}.'」成了街上熱門話題，店前坐滿了滿懷期待的顧客。') ;
			}
		}
		return 0;
	_local_

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		syokkiarai
	info		洗碗機的壽命
	startfunc	_local_(100)
		my($hitproba)=@_;
		
		foreach my $DT (@DT)
		{			
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"洗碗機")
			{
				if ($DT->{item}[@@ITEMNO"洗碗機"-1]==1)					{
				$DT->{item}[@@ITEMNO"洗碗機"-1]=0;
				WriteLog(2,0,$DT->{shopname}."的洗碗機壞掉了。");
				WriteLog(0,$DT->{id},"丟棄了壞掉的洗碗機。");
				}
			}
			}
		}
		return 0;
	_local_

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		haisya
	info		爛車
	startfunc	_local_(100)
		my($hitproba)=@_;
		
		foreach my $DT (@DT)
		{			
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"汽車")
			{
				if ($DT->{item}[@@ITEMNO"汽車"-1]==1)	{
				$DT->{item}[@@ITEMNO"汽車"-1]=0;
				WriteLog(2,0,$DT->{shopname}."的汽車因為多次故障所以進行報廢了。");
				WriteLog(0,$DT->{id},"對汽車進行了報廢");
				}
			}
			}
		}
		return 0;
	_local_

#祝福イベントを大売り出しイベントに変更
@@event
	start		20%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	商店街開始進行大特賣了。
	endmsg		大特賣結束了。
	info		商店街很熱鬧，買氣提升了。
	func		_local_
		my $time=$TIMESPAN;
		$time=10*3600 if $time>10*3600; # 最大10%制限
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		udon-boom
	startmsg	烏龍麵似乎是街頭的熱潮。
	endmsg		烏龍麵熱潮結束了。
	info		烏龍麵越來越受歡迎。
		param	清湯烏龍麵			pop/1.5
		param	海帶芽烏龍麵			pop/1.5
		param	豆皮烏龍麵			pop/1.5
		param	天婦羅烏龍麵			pop/1.5
		param	炸蝦烏龍麵			pop/2
		param	烏龍麵三昧			pop/2
		param	魚子醬烏龍麵			pop/2
		param	松露烏龍麵			pop/2
		param	鵝肝烏龍麵		pop/2
		param	博多烏龍麵			pop/2
		param	原創烏龍麵		pop/2

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		soba-boom
	startmsg	蕎麥麵似乎是街頭的熱潮。
	endmsg		蕎麥麵熱潮結束了。
	info		蕎麥麵越來越受歡迎了。
		param	清湯蕎麥麵			pop/1.5
		param	海帶芽蕎麥麵			pop/1.5
		param	豆皮蕎麥麵			pop/1.5
		param	天婦羅蕎麥麵			pop/1.5
		param	炸蝦蕎麥麵			pop/2
		param	蕎麥麵三昧			pop/2
		param	魚子醬蕎麥麵			pop/2
		param	松露蕎麥麵			pop/2
		param	鵝肝蕎麥麵			pop/2
		param	博多蕎麥麵			pop/2
		param	原創蕎麥麵			pop/2

@@EVENT
	start		5%
	basetime	9h
	plustime	16h
	code		plusup-katuo
	group		sui
	startmsg	鰹魚豐收了。
	endmsg		鰹魚的流通量回到平常的水準了。
	info		鰹魚的流通量增加了。
		param	鰹魚				plus=300

@@EVENT
	start		1%
	basetime	6h
	plustime	18h
	code		plusup-tyouzame
	group		sui
	startmsg	一大群鱘魚被沖上海灘。
	endmsg		鱘魚的流通量回到平常的水準了。
	info		鱘魚的流通量增加了。
		param	鱘魚			plus=500

# 低資金優先でギルド未加盟店に資金援助イベント
@@EVENT
	start		30%
	code		getmoney
	info		資金援助
	startfunc	_local_(100000)
		my($money)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;

			if ($_->{guild} eq '')
			{
			$_->{money}+=$money;
			$_->{money}=$main::MAX_MONEY if $_->{money}>$main::MAX_MONEY;
			return (0,"商店街自治會發給".$_->{shopname}.'共'.GetMoneyString($money).'的補助金');
			}
		}
		return 0;
	_local_

# 上位優先で万引きイベント
@@EVENT
	start		100% #old50%
	basetime	0h		#★持続系のイベントではないので時間は0。
	plustime	0h
	code		manbiki
	info		偷竊
	startfunc	_local_(400,200)
		#★実はこの関数がイベントの本体になってる
		my($hitproba,$breakproba)=@_;
		#狙われる確率,ロボット破壊確率
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"警報器"-1])
			{
				return (0,$DT->{shopname}.'有人企圖入室行竊，但被制止了。') if rand(1000)>$breakproba;
				
				$DT->{item}[@@ITEMNO"警報器"-1]--;
				return (0,$DT->{shopname}.'有人企圖入室行竊，'.$ITEM[@@ITEMNO"警報器"]->{name}.'被破壊了。');
			}
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/10);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'被偷了相當於總額'.GetMoneyString($count).'的商品。') if $count;
			return (0,'闖入'.$DT->{shopname}.'的小偷什麼都沒拿就逃走了。');
		}
		return 0;
	_local_

@@EVENT
	start		30% #old15%
	basetime	0h
	plustime	0h
	code		goutou
	info		強盜
	startfunc	_local_(700)
		#★実はこの関数がイベントの本体になってる
		my($hitproba)=@_;
		#狙われる確率
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"警報器"-1])
			{
				$DT->{item}[@@ITEMNO"警報器"-1]--;
				return (0,$DT->{shopname}.'有強盜闖入，'.$ITEM[@@ITEMNO"警報器"]->{name}.'被破壞了。');
			}
			
			$DT->{rank}-=int($DT->{rank}/5);
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/4);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'被搶了相當於總額'.GetMoneyString($count).'的商品。') if $count;
			return (0,'闖入'.$DT->{shopname}.'的強盜什麼都沒拿就逃走了。');
		}
		return 0;
	_local_

@@EVENT
	start		15%
	basetime	0h
	plustime	0h
	code		blacktime
	info		時間漩渦
	startfunc	_local_(700)
		my($hitproba)=@_;
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{user}->{black}>10)
			{
				my $blackcnt=int($DT->{user}->{black}/10);
				my $cnt=int(rand(10))+$blackcnt;
				$cnt=12 if $cnt>12;
				$DT->{time}+=3600*$cnt;
				$DT->{user}->{black}=0;
				WriteLog(0,$DT->{id},'的時間被時間漩渦吸收了　－'.$cnt.'小時');
				return (0,'由於重複操作時間的關係，產生了時間漩渦，'.$DT->{shopname}.'的時間被吸收了。');
			}
		}
		return 0;
	_local_

# 下位優先で人気アップイベント
@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		getpop
	info		人気アップ
	startfunc	_local_(1000)
		my($pop)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{rank}+=$pop;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,'雜誌上介紹了'.$_->{shopname}.'，人氣提升了。');
		}
		return 0;
	_local_

@@FUNCEVENT
######################################################################
# ★彩卷イベント
# usage:  loto
# return: 0 固定
######################################################################
sub loto
{
	WriteLog(2,0,"彩卷的開獎開始了。");
	foreach my $DT (@main::DT)
	{
		my $count=$DT->{item}[65-1];
		$DT->{item}[65-1]=0;
		my $hit1=0;
		my $hit2=0;
		my $hit3=0;
		my $hit4=0;
		my $hit5=0;
		next if !$count;
		
		foreach(1..$count)
		{
			my $rnd=rand(6096454);
			my $hit=0;
			
			if ($rnd<152411) {$hit=5;$hit5++;}
			elsif ($rnd<10000) {$hit=4;$hit4++;}
			elsif ($rnd<216) {$hit=3;$hit3++;}
			elsif ($rnd<6) {$hit=2;$hit2++;}
			elsif ($rnd<1) {$hit=1;$hit1++;}
			
			if($hit)
			{
				my $getmoney=(0,1000000000,150000000,5000000,100000,10000)[$hit];
				
				$DT->{moneystock}+=$getmoney;
				$DT->{money}=$main::MAX_MONEY if $DT->{money}>$main::MAX_MONEY;
			}
		}
		my $hitlog=5;
		$hitlog=1;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."抽中了頭獎".GetMoneyString(1000000000)."！") if $hit1>0;
		$hitlog=2;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."抽中了二獎".GetMoneyString(150000000)."$hit2次") if $hit2>0;
		$hitlog=3;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."抽中了三獎".GetMoneyString(5000000)."$hit3次") if $hit3>0;
		$hitlog=4;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."抽中了四獎".GetMoneyString(100000)."$hit4次") if $hit4>0;
		my $hitlog=5;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."抽中了五獎".GetMoneyString(10000)."$hit5次") if $hit5>0;
	}
	return 0;
}

@@FUNCINIT
#腳踏車を持っている場合，買い物に必要な時間を3/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if (($DT->{item}[@@ITEMNO"腳踏車"-1])&&(!$DT->{item}[@@ITEMNO"汽車"-1]));

#汽車を持っている場合，買い物に必要な時間を1/4にする。
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4) if $DT->{item}[@@ITEMNO"汽車"-1];

@@FUNCITEM
######################################################################
# ★人材が店を去る
######################################################################
sub lostman
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,'<br>工作結束後'.$ITEM[$itemno]->{name}.'默默離去了');
	}
	return "";
}

@@FUNCUPDATE
sub UpdateResetBefore #決算直前の処理(関数名固定)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#賞品授与
		my @TOP123=(
			[
				['商品券',	[[@@ITEMNO "商品券", 5],			],],
				['商品券',	[[@@ITEMNO "商品券", 4],			],],
				['商品券',	[[@@ITEMNO "商品券", 3],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 5],		],],
				['商品防竊',	[[@@ITEMNO "警報器", 1],		],],
				['肥料一卡車',[[@@ITEMNO "堆肥", 1000],	],],
				['食器',[[@@ITEMNO "乾淨的碗", 500],	],],
			],
			[
				['商品券',	[[@@ITEMNO "商品券", 3],			],],
				['商品券',	[[@@ITEMNO "商品券", 2],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 3],		],],
				['食器',[[@@ITEMNO "乾淨的碗", 300],	],],
			],
			[
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 2],		],],
				['商品券',	[[@@ITEMNO "商品券", 2],			],],
				['商品券',	[[@@ITEMNO "商品券", 1],			],],
				['食器',[[@@ITEMNO "乾淨的碗", 200],	],],
			],
			[
				['商品券',	[[@@ITEMNO "商品券", 2],			],],
				['商品券',	[[@@ITEMNO "商品券", 1],			],],
				['抽獎卷',	[[@@ITEMNO "抽獎卷", 1],		],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"輝煌勝利的") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"可惜第二名的") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"第三名獲勝的") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"只有".($i+1)."名") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."，收到商店街自治會贈送的".$getitem[0]."了。";
			WriteLog(2,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,"作為".$head."獎品，獲得".$ITEM->{name}." ".$itemnocount[1].$ITEM->{scale}."了。",1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"但是由於超過了最大持有數量，".$cnt.$ITEM->{scale}."被丟棄了",1) if $cnt;
			}
		}
	}
}

@@FUNCNEW

# @@DEFINE Set NewShopMoney NewShopTime NewShopItem の処理
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

# $DEFINE_FUNCNEW_NOLOG=1 を設定すると，システム側の最近の出来事新装開店メッセージを抑制します。
$DEFINE_FUNCNEW_NOLOG=1;
WriteLog(1,0,0,$DT->{shopname}."拉著一輛拖車，出現在城鎮上了。",1);

# その他，新装開店時に独自の処理を追加できます。

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # 移転時刻を記録

$DT->{item}[67-1]=1;	# 攻略本をプレゼント
if($DT->{job} eq 'man')
{
	# 人力仲介(man)には移転消費時間の1/2を返還
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'轉移時間大概是'.GetTime2HMS($DT->{_MoveTownTime}).'會完成',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'原始轉移街道送了餞別禮，得到'.GetMoneyString(GetUserDataEx($DT,'_so_present_money')).'了',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # 滞在期間1日に付き\5000を餞別として資金へ
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} を削除
}

@@FUNCBUY
# package item です。
# 
# $item::BUY を利用できます。$item::BUY の構造はマニュアルの @@ITEM funcb をご覧ください。
# 商品毎の処理は @@ITEM funcb を利用してください。

if($BUY->{whole})
{
	# 市場からの仕入の場合，\500000に付き1枚の抽獎卷を進呈する。
	my $price=$BUY->{num}*$BUY->{price};
	my $count=int $price/500000;
	
	$count=AddItemSub(@@ITEMNO"抽獎卷",$count,$BUY->{dt}) if $count;
	WriteLog(0,$BUY->{dt}{id},'收到來自市場的抽獎卷'.$count.'枚了') if $count;
}

@@END #定義終了宣言(以降コメント扱い)


