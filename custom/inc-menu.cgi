# ���j���[�ݒ�t�@�C�� 2005/03/30 �R��

# ���j���[�ɕ\�������郊�X�g��ݒ�ł��܂��B
# �ŏ��̈�s���u���j���[���ږ��v�C
# ���̍s����́u�T�u���j���[���v�C�u�v���O�������v�ł��B
#   ���v���O�������ɂ̓A�h���X���w��\�ł��B

my @MENU=(
	# �Q�X�g�����̏ꍇ�̃��j���[
	['�X�ē�',[
		['���i',	'town'],
		['�V��',	'log'],
		['�}����',	'action.cgi?key=library',	"_blank"],
	]],

	# �ȉ��v���C���[�����̏ꍇ�̃��j���[
	['���X',[
		['�X��',	'main'],
		['�q��',	'stock'],
		['���|��',	'sweep'],
		['���x',	'balance'],
		['�葱',	'other'],
		['LogOut',	'index.cgi'],
	]],
	['���',[
		['�s��',	'shop-m'],
		['���X�ʂ�',	'shop-a'],
		['�˗���',	'req'],
		['�{�a',	'palace'],
	]],
	['���',[
		['���i',	'town'],
		['�V��',	'log'],
		['�a��',	'orilist'],
		['�}����',	'action.cgi?key=library',	"_blank"],
	]],
	['�{��',[
		['�̎�@',	'lord'],
		['�M���h',	'gd'],
		['���Z��',	'slime'],
		['�b����',	'army'],
		['�Z��n',	'hometown'],
	]],
	['��',[
		['�X�֋�',	'letter'],
		['��z��',	'dwarf'],
		['�f���� '.GetTime2FormatTime((stat($COMMON_DIR.'/treelog.cgi'))[9]+0,1),	'treebbs'],
		['wis',	'wis'],
	]],
);

# �ȉ��̓v���O�����ł��B�ҏW����ɂ͋Z�p���K�v�ł��B------------------------------

my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $nextday=$now+$ONE_DAY_TIME-($now % $ONE_DAY_TIME);
$DISP{MENU} =~ s/#SKINMENUTITLE#/$TOWN_TITLE/;

if($USER && $USER ne 'soldoutadmin')
	{
	$DISP{MENU} =~ s/#SKINJOB#/GetTagImgJob($DT->{job},$DT->{icon})/e;
	my $i;
	my $MENUMSG;
	my $file=GetPath($SUBDATA_DIR,$DT->{id}."-wis");
	$MENUMSG.=<<"STR";
<i id="lay"></i>
<SCRIPT LANGUAGE="JavaScript">
<!--
menudata=[
STR
	$MENUMSG.="'";
	$MENUMSG.=(-e $file) ? WisRead($file) : "<BIG>������</BIG> &gt; <small>".LoginMember()."</small>";
	$MENUMSG.="',";
	foreach(1..$#MENU)
		{
		my $msg=@{$MENU[$_]}[0];
		my @list=@{@{$MENU[$_]}[1]};
		$i.=qq|<A href="javascript:mymenu($_)">�y$msg�z</A> |;
		$MENUMSG.="'";
		$MENUMSG.="<BIG>$msg</BIG> &gt; ";
		foreach my $sublist(@list)
			{
			my @SUBMENU=@{$sublist};
			$MENUMSG.=(($SUBMENU[1] =~ /\./) ? GetTagA("[".$SUBMENU[0]."]",$SUBMENU[1],0,$SUBMENU[2]) : GetMenuTag($SUBMENU[1],"[".$SUBMENU[0]."]"));
			}
		$MENUMSG.=qq|<A href="javascript:mymenu(0)">�y�~�z</A> |;
		$MENUMSG.="',";
		}
	$MENUMSG.=<<"STR";
];
function mymenu(i){
document.getElementById("lay").innerHTML = menudata[i];
}
mymenu(0);
// -->
</SCRIPT>
STR
	$i.=qq|<A HREF="action.cgi?key=bgm&$USERPASSURL&mode=$Q{key}" target="_top">[��]</a> |;
	$i.='[���񌈎Z '.GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME).' �܂ł���'.GetTime2HMS(int(($nextday-$now)/60)*60+59).']';
	$DISP{MENU} =~ s/#SKINMENU#/$i/;
	$DISP{MENU} =~ s/#SKINMENUSUB#/$MENUMSG/;
	}
	else
	{
	$DISP{MENU} =~ s/#SKINTITLE#/$HTML_TITLE/;
	$DISP{MENU} =~ s/#SKINJOB#/GetTagImgJob("guest",0)/e;
	my $i;
	my $MENUMSG;
	my $msg=@{$MENU[0]}[0];
	my @list=@{@{$MENU[0]}[1]};
	$MENUMSG.=qq|<BIG>$msg</BIG> > |;
	foreach my $sublist(@list)
		{
		my @SUBMENU=@{$sublist};
		$MENUMSG.=(($SUBMENU[1] =~ /\./) ? GetTagA("[".$SUBMENU[0]."]",$SUBMENU[1],0,"_blank") : GetMenuTag($SUBMENU[1],"[".$SUBMENU[0]."]"));
		}
	$i.=($MYNAME eq 'index.cgi')? qq|<A HREF="$HOME_PAGE" TARGET=_top>[�z�[��]</A> | : qq|<A HREF="index.cgi" TARGET=_top>[�g�b�v]</A> |;
	$i.='[���񌈎Z '.GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME).' �܂ł���'.GetTime2HMS(int(($nextday-$now)/60)*60+59).']';
	$DISP{MENU} =~ s/#SKINMENU#/$i/;
	$DISP{MENU} =~ s/#SKINMENUSUB#/$MENUMSG/;
	}
print $DISP{MENU};
1;


sub LoginMember
{
my $logmemb="";
my $i=0;
foreach(@DT)
	{
	next if ($_->{lastlogin} < $NOW_TIME - 120);
	$logmemb .= "�C ".$_->{shopname};
	$i++;
	$logmemb .= "�ق�", last if ($i > 3);
	}
$logmemb = substr($logmemb,3) if ($logmemb);
$logmemb = "�Ȃ�" if !$logmemb;
return $logmemb
}

sub WisRead
{
	my ($file)=@_;
	open(IN,$file) or return;
	read(IN,my $buf,-s $file);
	close(IN);
	unlink $file;
	return $buf;
}

