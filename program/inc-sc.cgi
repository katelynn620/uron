# ÂñIº¿¯ 2005/01/06 RÒ

my $showcasecount=$DT->{showcasecount};

$disp.="<BIG>ÂñIF»Ý$showcasecountÂFÛï ".GetMoneyString($SHOWCASE_COST[$showcasecount-1])."</BIG><br><br>";

my $usertaxrate=GetUserTaxRate($DT,$DTTaxrate);

$disp.=$TB;
if(!$MOBILE)
{
	my @taxmode=('','(ÆÅ)','({Å)');
	$disp.=$TR;
	$disp.=$TDB."INo.";
	$disp.=$TDB."¤i¼";
	$disp.=$TDB."l";
	$disp.=$TDB."W¿i";
	$disp.=$TDB."pÅ".$taxmode[$DT->{taxmode}+0];
	$disp.=$TDB."ÝÉ";
	$disp.=$TDB."¡úã";
	$disp.=$TDB."Oúã";
	$disp.=$TD;
	$disp.=$TRE;
}
else
{
	$tdh_pr{$MOBILE}="l:";
	$tdh_sp{$MOBILE}="W:";
	$tdh_tx{$MOBILE}="Å:";
	$tdh_st{$MOBILE}="ÝÉ:";
	$tdh_ts{$MOBILE}="{:";
	$tdh_ys{$MOBILE}="ð:";
}

for(my $cnt=0; $cnt<$DT->{showcasecount}; $cnt++)
{
	my $itemno=$DT->{showcase}[$cnt];
	my $ITEM=$ITEM[$itemno];
	my $scale=$ITEM->{scale};
	my $stock=$itemno ? $DT->{item}[$itemno-1]:0;

	$disp.=$TR.$TD."<SPAN>I".($cnt+1)."</SPAN>";
	$disp.=$TD;
	$disp.="<A HREF=\"action.cgi?key=item&$USERPASSURL&no=$itemno&sc=".($cnt+1)."&pr=".$DT->{price}[$cnt]."&bk=$Q{key}\">" if $stock;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name};
	$disp.="</A>" if $stock;
	
	if($itemno)
	{
		my($taxrate,$tax)=GetSaleTax($itemno,1,$DT->{price}[$cnt],$usertaxrate);
		$disp.=$TD.$tdh_pr{$MOBILE}.GetMoneyString($DT->{price}[$cnt]);
		$disp.=$TD.$tdh_sp{$MOBILE}.GetMoneyString($ITEM->{price});
		$disp.=$TD.$tdh_tx{$MOBILE}.GetMoneyString($tax)." (Å¦".$taxrate."%)";
		$disp.=$TD.$tdh_st{$MOBILE}.$stock.$scale;
		$disp.=$TD.$tdh_ts{$MOBILE}.($DT->{itemtoday}{$itemno}+0).$scale;
		$disp.=$TD.$tdh_ys{$MOBILE}.($DT->{itemyesterday}{$itemno}+0).$scale;
		$disp.=$TD.'<A HREF="action.cgi?key=sc-s&'.$USERPASSURL.'&item=0&no='.$cnt.'&bk=sc">Âñ~</A>';
	}
	else
	{
		$disp.=$TD.$TD.$TD.$TD.$TD.$TD;
	}
	$disp.=$TRE;
}
$disp.=$TBE;
1;
