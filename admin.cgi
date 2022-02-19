#!/usr/local/bin/perl
# �Ǘ����C�� 2005/03/30 �R��

require './_config.cgi';
GetQuery();
RequireFile("inc-makeitem.cgi") if $Q{key} eq "makeitem";

($MYDIR,$MYNAME)=($ENV{SCRIPT_NAME}=~/^.*\/([^\/]+)\/([^\/]+)$/); # ���t�@�C����/�f�B���N�g����
@log=();

OutError('�Ǘ��҃p�X���[�h���ݒ肳��Ă��܂���') if $MASTER_PASSWORD eq '';
OutError('�Ǘ��҃��[���A�h���X���ݒ肳��Ă��܂���') if $ADMIN_EMAIL eq '';
OutError('�X�R�[�h���ݒ肳��Ă��܂���') if ($MOVETOWN_ENABLE && !$TOWN_CODE);
OutError('$DATA_DIR �̐ݒ�s�ǁC�������́C$DATA_DIR �f�B���N�g�����쐬����Ă��܂���') if !-e $DATA_DIR;
OutError('$SESSION_DIR $TEMP_DIR $LOG_DIR $BACKUP_DIR $SUBDATA_DIR �ӂ�̐ݒ肪�ُ�ł�') if $SESSION_DIR eq '' || $TEMP_DIR eq '' || $LOG_DIR eq '' || $BACKUP_DIR eq '' || $SUBDATA_DIR eq '';

$checkdatadir=' �f�B���N�g�� '.$DATA_DIR.' �̃p�[�~�b�V�������������Ă�������';

if($Q{admin} ne $MASTER_PASSWORD)
{
	$disp.=<<"HTML";
	<FORM ACTION="$MYNAME" METHOD="POST">
	<TABLE cellspacing="0" cellpadding="1" bgcolor="#6B6599" border="0">
	<TBODY><TR vAlign=center align=middle><TD>
	<TABLE cellspacing="0" cellpadding="5" width="700" border="0">
	<TBODY><TR><TD width="80" bgcolor="#ABA5FF" align="center">
	<FONT color="#FFFFFF"><small>for Admin</small></FONT></TD>
	<TD align="center" bgcolor="#DBD5FF" colspan="2">�Ǘ��҃p�X���[�h 
	<INPUT TYPE=PASSWORD size=8 NAME=admin> <INPUT TYPE=SUBMIT VALUE="�Ǘ����j���[��"> 
	... <small><A HREF="http://akimono.org/">���l����</A></small>
	</TD></TR></TBODY></TABLE></TD></TR></TBODY></TABLE></FORM>
HTML
}
elsif($Q{mode} ne "")
{
	RequireFile("inc-admin-func.cgi");
}
else
{
	RequireFile("inc-admin.cgi");
}

OutHeader();
foreach(@log)
{
	$_="<b>$_</b>" if substr($_,0,1) eq ' ';
	print $_."<br>";
}
print $disp;
print <<"HTML" if scalar(@log);
	<hr noshade size=1>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�Ǘ����j���[�֖߂�">
	</FORM>
HTML
print "</center></BODY>";
print "</HTML>";
exit;


sub OutHeader
{
print "Cache-Control: no-cache, must-revalidate\n";
print "Pragma: no-cache\n";
print "Content-type: text/html; charset=Shift_JIS\n\n";
print <<STR;
<HTML><HEAD>
<Style Type="text/css">
<!--
A:link   { font-weight: bold; text-decoration:none}
A:visited{ font-weight: bold; text-decoration:none}
A:hover  { font-weight: bold; text-decoration:underline;}
FORM {margin: 2pt;}
BODY,TR,TD,TH { font-family:"MS UI Gothic"; font-size:11pt; }
BIG { font-weight: bold; font-size:11pt; color:#664499 ;}
SPAN { font-weight: bold; font-size:11pt; color:#bb44bb ;}
input,select,textarea{color:#000000;background-color:#FFFFFF;border:1 #5f5f8c solid}
input.button{color:#000000;background-color:#FFFFFF;border:1 #5f5f8c solid}
hr 	{color:#666666;}
-->
</Style>
<TITLE>$HTML_TITLE:�Ǘ���</TITLE>
</HEAD><BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#6050cc" VLINK="#6050cc" ALINK="#FF0000">
<center>
<BIG>���l���� $HTML_TITLE �Ǘ���</BIG><br><br>
STR
}

sub GetQuery
{
	my($q,@q,$key,$val);
	$q="";
	
	if($ENV{'REQUEST_METHOD'} eq "POST")
	{
		read(STDIN,$q,$ENV{'CONTENT_LENGTH'});
	}
	$q.="&".$ENV{'QUERY_STRING'};

	@q=split(/&/,$q);
	foreach (@q)
	{
		($key,$val)=split(/=/);
		$val =~ tr/\?/ /;
		$val =~ tr/+/ /;
		$val =~ s/\t/ /g;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2",$1)/eg;
		$val =~ s/"/ /g;
		$val =~ s/'/ /g;
		$val =~ s/,/ /g;
		$val =~ s/[\r\n]//g;
		$Q{$key}=$val;
	}
	if($Q{u} ne '')
	{
		$Q{nm}="";
		$Q{pw}="";
		$Q{ss}="";
		($Q{nm},$Q{pw},$Q{ss})=split(/[!:]/,$Q{u},3);
	}
}

sub OutError
{
	print "Cache-Control: no-cache, must-revalidate\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html; charset=Shift_JIS\n\n";
	print "<HTML><HEAD><TITLE>�Ǘ����j���[</TITLE></HEAD>";
	print "<BODY>";
	print $_[0]."<br>";
	print '<font color=red><b>�}�j���A�����Q�Ƃ��Đ������ݒ肵�ĉ�����</b></font>' if !$_[1];
	print qq|<FORM ACTION="$MYNAME" METHOD="POST"><INPUT TYPE=HIDDEN NAME=admin VALUE="$Q{admin}">|;
	print qq|<INPUT TYPE="SUBMIT" VALUE="�Ǘ����j���[�֖߂�"></FORM>|;
	print "</BODY>";
	print "</HTML>";
	exit;
}

sub GetFileList
{
	opendir(DIR,$_[0]);
	my @list=map{$_[0]."/".$_}grep(/$_[1]/ && !/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	
	return @list;
}

