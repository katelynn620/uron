# �V�K�J�X�J�X�^�}�C�Y�p 2004/01/20 �R��

# �V�K�J�X���̒��ӎ����̕\���Ȃǂ��J�X�^�}�C�Y�ł��܂��B
# �������C������x��HTML�̒m���ƃv���O�����̗������K�v�ł��B

$disp.=<<"HTML";
<BIG>���͂��߂�</BIG><br><br>
$TB$TR
$TD$image[0]$TD
���̃Q�[���́C�u���E�U�Ńv���C�ł���o�c�V�~�����[�V�����q�o�f�ł��B<br>
�Q������O�ɁC�}���قŃ��[����v���C���@���悭�ǂ�ł��������B
$TRE$TBE
<hr width=500 noshade size=1>
HTML

$i_rand=int(rand($ICON_NUMBER))+1;
$disp.="<BIG>���V�K�X�܃I�[�v���F�c��".($MAX_USER-$DTusercount)."���l</BIG><br>";
$disp.=<<"HTML";
<small>�o�^��<b>�P�l�P�X��</b>�̂�</small><br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="new">
<INPUT TYPE=HIDDEN NAME=admin VALUE="$Q{admin}">
<TABLE>
  <TR>
    <TD>
<SPAN>���O</SPAN>�F<INPUT TYPE=TEXT NAME=name> ���p�S�pOK<BR>
<SPAN>�X��</SPAN>�F<INPUT TYPE=TEXT NAME=sname> ���p�S�pOK<BR>

<SPAN>�A�C�R��</SPAN>�F<SELECT NAME=icon>
<OPTION value="$i_rand" selected>�����_��</OPTION>
HTML

foreach my $i(1..$ICON_NUMBER)
	{
	$disp.=qq|<OPTION value="$i">�摜$i</OPTION>|;
	}

$disp.=<<"HTML";
</SELECT> 
<input type="button" value="�A�C�R���ꗗ" onclick="javascript:window.open('action.cgi?key=icon','_blank','width=450,height=380,scrollbars')">
<br>
<SPAN>�p�X���[�h</SPAN>�F<INPUT TYPE=PASSWORD maxlength=12 NAME=pass1> ���p�p���̂�<BR>
<SPAN>�p�X���[�h������x</SPAN>�F<INPUT TYPE=PASSWORD maxlength=12 NAME=pass2><BR>
HTML

$disp.="<SPAN>�o�X�L�[���[�h</SPAN>�F<INPUT TYPE=TEXT NAME=newkey><BR>" if ($NEW_SHOP_KEYWORD);

$disp.=<<"HTML";
<center><INPUT TYPE=SUBMIT VALUE="�o�^"></center>
</TD></TR>
</TABLE>
<small>���r�炵�Ƌ^����悤�Ȗ��O�͔����܂��傤�B<br>
���p�X���[�h�͑��l�������ł��Ȃ��悤�Ȃ��̂��B</small>
</FORM>
HTML
1;
