#!/usr/local/bin/perl
# �g�b�v��� 2004/01/20 �R��

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
	$lform.=GetTagA('�y�V�K�X�܃I�[�v���z<small>�c��'.($MAX_USER-$DTusercount).'���l</small>',"action.cgi?key=new") if $MAX_USER>$DTusercount;
	$lform.='�y�V�K�X�܃I�[�v���z<small>���ݖ���</small>' if $MAX_USER<=$DTusercount;
	$lform.=($MAX_MOVE_USER>$DTusercount)?('<small>�i�ړ]�F�c��'.($MAX_MOVE_USER-$DTusercount).'���l�j</small>'):('<small>�i�ړ]�F���ݖ����j</small>') if $MOVETOWN_ENABLE;
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
	foreach(split(/\s*;\s*/,$ENV{HTTP_COOKIE}))
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
