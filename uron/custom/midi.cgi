# MIDI�̐ݒ�t�@�C�� 2005/03/30 �R��

# -------- �ݒ蕔�� ----------
# MIDI�̃t�@�C������ύX�ł��܂��B
# CGI�ʃT�[�o�[�̂Ƃ���ł́C������ http:// ����n�܂�p�X�Ɏw�肵�܂��B

$MIDI_URL = "midi.mid";

# ----------------------------

$NOMENU=1;
$Q{bk}="none";
print "Content-type: text/html\n\n";

my $bgmtag;

if ($ENV{HTTP_USER_AGENT}=~ /MSIE/ && $ENV{HTTP_USER_AGENT}!~ /Opera/)
	{
	$bgmtag=qq|<BGSOUND src="$MIDI_URL" loop=infinite>|;
	}
	else
	{
	$bgmtag=qq|<EMBED src="$MIDI_URL" width=2 height=2 autostart=true loop=true>|;
	}
print "Content-type: text/html\n\n";
print <<"EOM";
<html lang="ja">
<HEAD>
<TITLE>BGM</TITLE>
$bgmtag
</HEAD>
<BODY>
</HTML>
EOM
exit;
1;