# �ݒ�t�@�C�� 2005/01/06 �R��
# ���̃t�@�C���̃p�[�~�b�V������ݒ肷��K�v�͓��ɂ���܂���B�ݒ肷��Ȃ�644�Ȃǂłn�j�B

#-----------------------
# ���͂��߂ɂ���ݒ�
#-----------------------
$MASTER_PASSWORD	='';			# �Ǘ��p�X���[�h
$ADMIN_EMAIL		='';			# �Ǘ��҃��[���A�h���X

$HTML_TITLE	='�X�̐�������';		# �X�̐�������

$TOWN_TITLE	='����';			# �X�̖��́i�S�p�Q�������炢�ŒZ���j
						# ��ɂȂ��ĊX�̖��̂�ς����Ƃ��́C�Ǘ�����
						# �u�������^�j���C���v�{�^���������K�v������܂��B


#-----------------------
# ���X�̐ݒ�
#-----------------------
$TOWN_CODE	='uron';			# �X�̃R�[�h�i���ʋL���j
						# ���p�p��������10�����ȓ��œK���ɐݒ肵�܂��傤�B
						# ���̊X�Ɠ����R�[�h�ɂȂ�Ȃ��悤�ɁB

$TITLE_COMMENT	='';				# ���O�C����ʂɍڂ���R�����g�B�^�O�g���܂��B

$HOME_PAGE	='../index.html';		# �u�z�[���v�̃����N��

$MOVETOWN_ENABLE	=0;			# �ړ]�@�\�̗L���� 1:�L�� 0:����
						# �T�[�o�[��socket�ɑΉ����ĂȂ��ƈړ]�@�\�͎g���܂���B


#------------------------
# ��{�I�ȃQ�[���ݒ�
#------------------------
$MAX_USER	=50;				# �V���J�X�ő吔�F���܂�傫�����Ă͂����܂���B
$MAX_MOVE_USER	=55;				# �ړ]�ő吔�i������ړ]���Ă����ꍇ�̎󂯓���\���j

$EXPIRE_TIME	=3600*24*7;			# �o�c�ҕs�݊���(�b)
						# ���̊��Ԃ����ƃA�N�Z�X���Ȃ��ƃf�[�^����������܂��B

$ONE_DAY_TIME		=3600*36;		# ���Z�T�C�N��(�b)
$DATE_REVISE_TIME	=3600*6;		# ���Z���������炷�b��(-3600��1���ԑO�|��)

$MAX_STOCK_TIME		=72*60*60;		# �ő厝������(�b)

$LIMIT_EXP	=3600;				# �n���x�̍��v�l���~�b�g�i10�{�̐��l���w��j
						# 3600����360%������B0�ɂ���Ə���Ȃ��B

$REQUEST_LIMIT		=48*60*60;		# �u�˗����v�̈˗����L���Ȏ���(�b)
$REQUEST_CAPACITY	=1;			# �����Ɉ˗��ł��鐔

$HouseMax	=5;				# �u�Z��v�ɕۊǂł�����F
						# 5 �Ƃ���ƁC���ꂼ��̃A�C�e�����q�ɍő吔��5�{�܂ŕۊǂł���B

$MAX_BOX	=5;				# �莆�̑��M�ő吔
$BOX_STOCK_TIME	=48*60*60;			# �莆���L���Ȏ���(�b)

@DIGNITY=(					# �݈ʂ̖��O�B�E�ɍs���قǒn�ʂ������Ȃ�܂��B
	"����","�m��","�q��","����","���","����","���"
	);
@DIG_POINT=(					# �K�v�Ȏ݈ʃ|�C���g�B��ƑΉ������Ă��������B
	0,1,2,4,8,16,32
	);
$DIG_FORGUILD=16;				# �M���h�����ɕK�v�Ȏ݈ʃ|�C���g

$BAL_NAME	='�o���o���X';			# �����m�o�b�̖��O
$BAL_JOB	='�R��';			# �����m�o�b�̐E��


#-------------------------------
# �p��Ɋւ���ݒ� : �Q�[�����ɏo�Ă���p�����C�ɕύX�ł��܂��B
#-------------------------------

@term=(
	'\\',			#�O�ɂ���ʉݒP��
	'',			#��ɂ���ʉݒP��
	'�~',			#���{��\�L�����ꍇ�̒ʉݒP�ʁi���ʂȂǂŎg���j
	'�T��������',		#�����}�C�i�X���i���ʂŎg���j

);


#-------------------------------
# �A�N�Z�X�̐����Ɋւ���ݒ�
#-------------------------------
$NEW_SHOP_ADMIN		=0;			# �V�K�I�[�v������ 0:��� 1:�Ǘ��҂̂�
						# 1 �ɂ���ƊǗ���ʂ��炵���X���J���Ȃ��Ȃ�܂��B

$NEW_SHOP_KEYWORD	='';			# �V�K�X�܃I�[�v���ɕK�v�ȃL�[���[�h
						# �L�[���[�h��ݒ肷��ƁC���̌��t��m��Ȃ��ƊJ�X�ł��Ȃ��Ȃ�܂��B

$NEW_SHOP_BLOCKIP	=1;			# 1�œ���IP�ɂ��A���o�^(�X��̍ēo�^���܂�)��j�~
$CHECK_IP		=1;			# ����IP��USER_AGENT�̃A�N�Z�X�������I�ɐ������� 1:�������� 0:�������Ȃ�
@NG_SHOP_NAME		=qw(�Ǘ� �x 11 12 aa http ?);	# �X�ܖ��Ƃ��Ďg�p�ł��Ȃ�����(�X�y�[�X�ŋ�؂�)

$NEW_OTHERTOWN_BLOCK	=0;			# 1 �ŊX�O���[�v�S�̂ŏd���o�^�����o�B
						# �X�O���[�v�S�̂�1�����X�����ĂȂ��Ȃ�܂��B



#********************** ��ʓI�Ȑݒ荀�ڂ͂����܂łł� **********************



#--------------------------------------------------------------------
# �摜�Ɋւ���ݒ� �F �摜�������ւ�����C����ȏꏊ�ɒu���l�����B
#--------------------------------------------------------------------
$IMAGE_URL		='./image';		# �摜�f�B���N�g���̂���ꏊ�i�A�h���X�j
						# CGI���ʃT�[�o�[�ƂȂ�Ƃ���ł͕ύX�̕K�v����B
$IMAGE_DIR		='./image';		# �摜�f�B���N�g���i�T�[�o�[�̃t���p�X�j
						# nifty �Ȃǂ̓���ȃT�[�o�[�ł͕ύX�̕K�v����B

$ICON_NUMBER		=25;			# �X����A�C�R���̐�
$ICON_SIZE		='WIDTH=48 HEIGHT=48';	# ��A�C�R���̃T�C�Y

$IMAGE_EXT		='.png';		# �摜�g���q

$COMMON_URL		='../common';		# �O���[�o���f�[�^�f�B���N�g���i�M���h���j
						# CGI���ʃT�[�o�[�ƂȂ�Ƃ���ł͕ύX�̕K�v����B
$COMMON_DIR		='../common';		# �O���[�o���f�[�^�f�B���N�g���i�T�[�o�[�̃t���p�X�j
						# nifty �Ȃǂ̓���ȃT�[�o�[�ł͕ύX�̕K�v����B

#---------------------------------------------------------
# ���x�ȃQ�[���o�����X�ݒ� �F �o�����X���n�m�����l�����B
#---------------------------------------------------------
$UPDATE_TIME		=60*5;			# �ŒZ�X�V�T�C�N��(�b)

$PROFIT_DAY_COUNT	=3;			# �_���v�Z�̍ۍl������ߋ��̏����v�i���j
$SALE_SPEED		=12;			# ����s���{��(inc-item-data.cgi�ł̐ݒ��1�Ƃ���)
$POP_DOWN_RATE	=5;				# ���݂̐l�C�ɉ����Ă̏㉺��

$EXP_DOWN_POINT		=5;			# ���Z���Ɍ�������n���x�|�C���g(1%==10)
$EXP_DOWN_RATE		=60;			# ���Z���Ɍ�������n���x����(6%==60)
						# ��:���݂̏n���x50%�̏ꍇ�A�Œ��0.5%��50%��6%��3%�A���킹��3.5%����


#---------------------------------------------------------
# �ׂ����\���ݒ� �F �ނ�݂ɕύX����ƌ��h��������܂��B
#---------------------------------------------------------
$TOP_RANKING_PAGE_ROWS	=5;			# �u�g�b�v�v�����L���O�\������
$MAIN_LOG_PAGE_ROWS	=10;			# �u�X�����v�ŋ߂̏o�����\������
$SHOP_PAGE_ROWS		=5;			# �u���X�v�X�ܕ\������
$RANKING_PAGE_ROWS	=10;			# �����L���O�\������
$LIST_PAGE_ROWS_PC	=25;			# �e�탊�X�g�\�������i�ʏ�j
$LIST_PAGE_ROWS_MOBILE	=5;			# �e�탊�X�g�\�������i�g�сj



#********************** �����艺�̐ݒ�͂Ȃ�ׂ����̂܂܂� **********************

$DATA_DIR		='./data';
$LOG_DIR		=$DATA_DIR.'/log';
$ITEM_DIR		=$DATA_DIR.'/item';
$SESSION_DIR		=$DATA_DIR.'/session';
$BACKUP_DIR		=$DATA_DIR.'/backup';
$TEMP_DIR		=$DATA_DIR.'/temp';
$SUBDATA_DIR		=$DATA_DIR.'/subdata';

$COTEMP_DIR		=$COMMON_DIR.'/temp';

$INCLUDE_DIR		='../program';
$AUTOLOAD_DIR		=$INCLUDE_DIR.'/plug';
$TOWN_DIR		=$INCLUDE_DIR.'/town';
$JCODE_FILE		=$INCLUDE_DIR.'/jcode.pl';
$CUSTOM_DIR		='./custom';

$DIR_PERMISSION		=0777;
$TZ_JST			=60*60*9;

$FILE_EXT		='.cgi';

$COMMIT_FILE		='commit';
$LASTTIME_FILE		='lasttime';
$LOCK_FILE		='lockfile';
$DATA_FILE		='play';
$LOG_FILE		='log';
$BBS_FILE		='treelog';
$BOX_FILE		='box';
$GUILDBAL_FILE		='guildbal';
$GUILD_FILE		='guild';
$ERROR_COUNT_FILE	='errorcnt';

$LOG_ERROR_FILE		='error';
$LOG_DELETESHOP_FILE	='delete';
$LOG_MOVESHOP_FILE	='moveshop';
$LOG_LOGIN_FILE		='login';
$LOG_DEBUG_FILE		='debug';
$LOG_MARK_FILE		='mark';
$LOG_SIZE_MAX		=30000;

$PASSWORD_CRYPT	=1;
$CHAR_SHIFT_JIS		=0;

$AUTO_UNLOCK_TIME		=60;
$SESSION_TIMEOUT_TIME		=3600;
$LOG_EXPIRE_TIME		=3600*36;
$PASSWORD_HASH_EXPIRE_TIME	=60*15;

$BACKUP_TIME		=3600;
$BACKUP		=3;
@BACKUP_FILES		=(
		$LOG_FILE.'0',
		$LOG_FILE.'1',
		$LOG_FILE.'2',
		$GUILDBAL_FILE,
		$DATA_FILE,
			);

# �Z�p�Ҍ����f�o�b�O�p 
$DEBUG_MOBILE		=0;			# 1�Ōg�ђ[�������Œ�
$DEBUG_LOG_ENABLE	=0;			# 1��item::DebugLog()��event::DebugLog()��L����

# set umask
umask(~$DIR_PERMISSION & 0777);
require './_config-local.cgi' if -e './_config-local.cgi';

sub RequireFile
{
	my $customfile="$CUSTOM_DIR/$_[0]";
	require $customfile,return if -e $customfile;
	my $fname="$INCLUDE_DIR/$_[0]";
	OutError('�t�@�C����������܂��� - '.$fname) unless -e $fname;
	require $fname;
}
1;
