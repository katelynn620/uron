# �X�^�b�t���[�� 2005/03/30 �R��
#
# �e�풘�쌠�\���p�ł��B�V���ȑf�ށE�v���O������g�ݍ��ލۂɁC�����ɒǉ����܂��傤�B
# HTML�̒m��������΁C���悤���܂˂łł���Ǝv���܂��B
#
# �X�^�b�t���[���ւ̃����N���O������C�ڗ����Ȃ����Ă͂����܂���B
# ���쌠�\���͖ڗ��悤�K�؂ɍs���K�v������C�����ӂ�Ɩ@�I���ɂȂ�ꍇ������܂��B

DataRead();
CheckUserPass(1);
OutError("�p�X���[�h�R��̊댯������̂ŕ\�����~���܂��B") if $Q{u};
$MENUSAY=GetMenuTag('town','[�X�ē�]');
$disp.="<BIG>���J���X�^�b�t���[��</BIG><br><br>";
$disp.=$TB.$TR.$TD.GetTagImgKao("�ē��l","guide").$TD;
$disp.='�Q�[���̊e�����ɂ��Ă̒��쌠�́C���ꂼ�ꉺ�L�̕��X�ɋA�����܂��B<br>';
$disp.='�Ȃ��C�f�ނ��Q�[�����璼�ڎ��o���ė��p���Ȃ��ł��������B'.$TRE.$TBE;
$disp.="<br>".$TBT.$TRT.$TD;

# ----------- �������牺�����낢�돑��������B-----------------------------

$disp.=<<"HTML";
<SPAN>����E����</SPAN> �F �R�� ... <A HREF="http://akimono.org/" target="_blank">���l����</A>
<br><br>
<SPAN>����</SPAN> �F MU �l ... <A HREF="http://mutoys.com/" target="_blank">MUTOYS</A>
<br><br>
<SPAN>���ǂ񂻂Ύd�l����</SPAN> �F ���~�R �l ... <A HREF="http://rumiko.cside.tv/index.htm" target="_blank">SOLD OUT �ԊO�n</A>
<br><br>
<SPAN>���S�E�W���u�C���X�g</SPAN> �F ���� �l ... <A HREF="http://www2.holon.dyndns.org/~musou/" target="_blank">�ǎ��̉� ��������</A>
<br><br>
<SPAN>�A�C�R���i�ǉ��j</SPAN> �F ���� �l �E �A�V�� �l
<br><br>
<SPAN>�}�b�v�E�L����</SPAN> �F �݂삱 �l ... <A HREF="http://sweetpunch.or.tv/akimono1/index.html" target="_blank"> �r�������� �o��������</A>
<br><br>
<SPAN>���y</SPAN> �F ���� �l ... <A HREF="http://www.tam-music.com/" target="_blank">�s�`�l �l�������� �e������������</A>
HTML

# ----------- �����܂ŁB�Ō�́uHTML�v�������Ȃ��悤���ӁB-----------------

require "skin.pl" if -e "skin.pl";
$disp.=$TRE.$TBE;
OutSkin();
1;
