# �鉺���ݒ�t�@�C�� 2003/10/08 �R��

# �鉺���̕��i���J�X�^�}�C�Y�ł��܂��B
# �������C�u�̎�@�v�ƁC�ŉ��i�́u���X�X�v�u���݊������̓X�v�̈ʒu�͕ύX�ł��܂���B
# �ꏊ�̔ԍ��́C���̂悤�ɂȂ��Ă��܂��B
#
#   [No.0]  [   �̎�@   ] [No.1]
#   [No.2]  [No.3]  [No.4] [No.5]
#   [No.6]  [No.7]  [No.8] [No.9]
#                 �E
#                 �E
#   [   ���X�X   ] [ �������̓X ]
#   
#  ��No.10�ȉ����`����΁C����ɓ��H�������ĉ��ɐL�΂��܂��B

#  ���L�q���@��
#  �E�u���O�v�C�u�摜�v�C�u�����N�v�C�u�Q�X�g�����ł̃����N�v�̏��ł��B
#  �E�摜�ł́C$i[0]�i�ʏ팚���j�C$i[1]�i�X�܌����j�C$space�i��������ԁj�C$vspace�i�傫�ȋ�ԁj���L���ł��B
#  �E�����N�́C�T�u�v���O�������̂ق��A�h���X���w��\�ł��B�󗓂��ƃ����N������܂���B
#  �E������`���Ȃ��ꏊ�́C���؂Ɖ��߂��܂��B

# --- No.0 �̏ꏊ��` ---

($Pname[0],$Pimage[0],$Plink[0],$Pguest[0])=(
	"���Z��",
	qq|<IMG WIDTH=16 HEIGHT=64 SRC="$IMAGE_URL/map/mapsignslime.png">$i[0]|,
	"slime",
	"slime"
	);

# --- No.1 �̏ꏊ��` ---

# ���؂̂��ߏȗ�

# --- No.2 �̏ꏊ��` ---

($Pname[2],$Pimage[2],$Plink[2],$Pguest[2])=(
	"�˗���",
	qq|$space<IMG WIDTH=16 HEIGHT=64 SRC=\"$IMAGE_URL/map/mapsignrequest.png\">$i[1]|,
	"req",
	"req"
	);

# --- No.3 �̏ꏊ��` ---

($Pname[3],$Pimage[3],$Plink[3],$Pguest[3])=(
	"�s��",
	qq|$space<IMG WIDTH=16 HEIGHT=64 SRC=\"$IMAGE_URL/map/mapsignmarket.png\">$i[1]|,
	"shop-m",
	"shop-m"
	);

# --- No.4 �̏ꏊ��` ---

# ���؂̂��ߏȗ�

# --- No.5 �̏ꏊ��` ---

($Pname[5],$Pimage[5],$Plink[5],$Pguest[5])=(
	"�M���h",
	qq|<IMG WIDTH=16 HEIGHT=64 SRC="$IMAGE_URL/map/mapsignguild.png">$i[0]|,
	"gd",
	"gd"
	);

# --- No.6 �̏ꏊ��` ---

# ���؂̂��ߏȗ�

# --- No.7 �̏ꏊ��` ---

($Pname[7],$Pimage[7],$Plink[7],$Pguest[7])=(
	"���m���ԏ�",
	qq|<IMG WIDTH=16 HEIGHT=64 SRC="$IMAGE_URL/map/mapsignarmy.png">$i[0]|,
	"army",
	""
	);

# --- No.8 �̏ꏊ��` ---

($Pname[8],$Pimage[8],$Plink[8],$Pguest[8])=(
	"�}����",
	qq|$space<IMG WIDTH=112 HEIGHT=80 SRC="$IMAGE_URL/map/house1c.png">|,
	"action.cgi?key=library",
	"action.cgi?key=library"
	);

# --- No.9 �̏ꏊ��` ---

($Pname[9],$Pimage[9],$Plink[9],$Pguest[9])=(
	"�f����",
	qq|<br><br><IMG WIDTH=32 HEIGHT=32 SRC="$IMAGE_URL/map/mapboard.png">|.GetTime2FormatTime((stat($COMMON_DIR.'/treelog.cgi'))[9]+0,1),
	"treebbs",
	""
	);

# --- �ȉ��CNo.10�C11�c�Ƒ��₵�Ă������Ƃ��ł��܂��B


# --- �L�����N�^�[�̃Z���t ---
# ���悤���܂˂ŃJ�X�^�}�C�Y���Ă��������i��

sub CharaDefine
{
@chara=();
	if ($DTevent{rebel})
		{
		$chara[1]=TagChara('��ς��E�E�E�B���R���Ă΂Ȃ��ƁI',"d2");
		$chara[2]=TagChara('�������I�����ɍs������',"d1");
		$chara[5]=TagChara('�̎��|����',"d1")."<br>".TagChara('��C�ɃP�������悤��',"d1");
		return;
		}
my $i=int($NOW_TIME / 3600) % 4;
	if ($i == 0)
		{
		$chara[0]=TagChara("�����̃X���C���܂�������������E�E�E","e1").$vspace.$vspace;
		$chara[4]=$space.TagChara("�H���̍ޗ������ɍs���Ȃ�������B","e2");
		}
	elsif ($i == 1)
		{
		$chara[7]=$vspace.$vspace.TagChara("�}���ق̏��͏d�v�����","b2").$space
			.TagChara("�f���̃`�F�b�N����؂��ˁB�ӂނӂށE�E�E","b1");
		}
	elsif ($i == 2)
		{
		$chara[4]=$vspace.TagChara("�ۂ��ۂ����ċC���������̂��E�E�E","c2");
		$chara[6]=TagChara("�������͂���ς�".$DT[0]->{shopname}."��˂�","c1").$space;
		}
	elsif ($STATE->{safety} < 4000)
		{
		my $lid=$id2idx{$STATE->{leader}};
		$chara[0]=TagChara(($STATE->{leader} ? $DT[$lid]->{name} : $BAL_NAME).'�̖\���ɒf�Ńn���^�[�C�I',"a1")
			.TagChara('�����Ǝs���̈��S���l����[��',"a2");
		}
}
1;

