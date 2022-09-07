#!/usr/bin/perl
# トップ画面 2004/01/20 由來

use utf8;
use Encode qw(decode_utf8);
binmode(STDOUT, ':encoding(utf8)');

require './_config.cgi';
RequireFile('inc-func.cgi');
RequireFile('inc-version.cgi');

Turn();

GetQuery();
GetCookie();
SetCookieSession();
DataRead();

$username=$Q{nm} ? $Q{nm} : $COOKIE{USERNAME};
$password=$Q{pw} ? $Q{pw} : $COOKIE{PASSWORD};
$lform="";
if (!$MOBILE)
	{
	$lform.=GetTagA(l('【新規店舗オープン】<small>残り %1 名様</small>', $MAX_USER - $DTusercount),"action.cgi?key=new") if $MAX_USER>$DTusercount;
	$lform.=l('【新規店舗オープン】<small>現在満員</small>') if $MAX_USER<=$DTusercount;
	$lform.=($MAX_MOVE_USER>$DTusercount)?(l('<small>（移転：残り%1名様）</small>',($MAX_MOVE_USER-$DTusercount))):(l('<small>（移転：現在満員）</small>')) if $MOVETOWN_ENABLE;
	$lform.="<br>";
	}
$DISP{MENU} =~ s/#SKINNEW#/$lform/;
$DISP{MENU} =~ s/#SKINNAME#/$username/;
$DISP{MENU} =~ s/#SKINPW#/$password/;
$DISP{MENU} =~ s/#SKINCOMMENT#/$TITLE_COMMENT/;

$DT={};
$DT->{id}=-1;
$GUEST_USER=1;
RequireFile('inc-html-top.cgi') if (!$MOBILE);

$DISP{BOTTOM} =~ s/#SKINVER#/$BASE_VERSION/;
$DISP{BOTTOM} =~ s/#SKINEDIT#/$ITEM_VERSION/;
$DISP{BOTTOM} =~ s/#SKINMAIL#/$ADMIN_EMAIL/;

OutSkin();
exit;

sub GetCookie
{
	$cookiebundle = decode_utf8($ENV{HTTP_COOKIE});
	foreach(split(/\s*;\s*/,$cookiebundle))
	{
		@_=split(/=/);
		$COOKIE{$_[0]}=$_[1];
		next if $_[0] ne 'shop';
		foreach(split(/,/,$_[1]))
		{
			@_=split(/:/);
			$COOKIE{$_[0]}=$_[1];
		}
	}
}
