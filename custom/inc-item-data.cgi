# ���ǂ񁕂��ΔŃA�C�e���f�[�^ 2005/01/06 �R��

# ���̃t�@�C���̓A�C�e���f�[�^�̒�`�t�@�C���ł��B
# �D���Ȃ悤�ɃJ�X�^�}�C�Y�ł��܂��B�ڍׂ̓}�j���A�����������������B

@@DEFINE
	version	05-01-06(URon)		#�����i�f�[�^�o�[�W�����\�L
					# �Ō�́uURon�v�͂��ǂ񁕂��Δłł��邱�Ƃ������܂��B
					# �������Ȃ����Ǝ��A�C�e����ڋʂɂ������l��������Ȃ�C
					# ���̋L����ς���̂��悢�ł��傤�B

	scale	�t			#���f�t�H���g�̐����P��
	type0	�S			#�S�A�C�e���̏W��
	type1	�l��
	type2	���Y��
	type3	�C�Y��
	type4	���ǂ�
	type5	����
	type6	�c�[��
	
	job	agri		�_��		#���E�ƃR�[�h�͉p������10�����ȓ�
	job	fish		����
	job	temp		�V�Ղ牮
	job	udon		���ǂ�
	job	soba		���Ή�
	job	man		�l�ޔh����
	job	black		���Ƌ�
	
	# �E�ƕʎ��ԒZ�k�p�ϐ��ݒ�
	set job_agri_time_rate		1.5	#���E�Ƃɂ��Ă����1.5�{�����Ȃ�
	set job_fish_time_rate		1.5
	set job_temp_time_rate		1.5
	set job_udon_time_rate		1.5
	set job_soba_time_rate		1.5
	set job_man_time_rate		2
	set job_black_time_rate		2

	MaxMoney	999999999	#���ő厑��
	
	set NewShopMoney	200000					#�������� (@@FUNCNEW�ɂĎg�p)
	set NewShopTime		24*60*60				#����������(�b) (@@FUNCNEW�ɂĎg�p)
	set NewShopItem		�q���g�u�b�N:1	#�����������i (@@FUNCNEW�ɂĎg�p) ���� ���i��:��:���i��:��:...
	
	TimeEditShowcase	10m		#����I���쎞��
	TimeShopping		20m		#���d������(��SOLD OUT�Ƃ̌݊����m�ہB���͎g�p����)
	TimeSendItem		20m		#���A�C�e���d��/���M����(��{)
	TimeSendItemPlus	20s		#���A�C�e���d��/���M����(1�ӂ�̒ǉ�����)
	TimeSendMoney		20m		#���������M����(��{)
	TimeSendMoneyPlus	100000		#���������v���Ԍv�Z�p���z(���̋��z�ɂ�TimeSendMoney���Ԃ�����)
	
	CostShowcase1		0		#����I1���ێ���
	CostShowcase2		1000	#��I2���ێ���
	CostShowcase3		2000	#��I3���ێ���
	CostShowcase4		4000	#��I4���ێ���
	CostShowcase5		8000	#��I5���ێ���
	CostShowcase6		16000	#��I6���ێ���
	CostShowcase7		32000	#��I7���ێ���
	CostShowcase8		64000	#��I8���ێ���
	
	ItemUseTimeRate		0.5		#���A�C�e���g�p�����Ԍv�Z�␳�{��(@USE��time,exptime�ɗL��)
	

#------ ��������A�C�e����` ---------------------------------


@@ITEM
	no		1
	type	�l��
	code	man-free
	name	�t���[�^�[
	info	�\�����߂��l�ނł�
	scale	�l
	price	5000
	cost	100
	limit	5/5
	plus	2h
	pop	1d
	flag	noshowcase|norequest|human
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		�l�ޔh����	times/job_man_time_rate
		scale	�l
		action	�_�Ƃ��n�߂�
		name	�_�Ƃ��n�߂�
		info	�t���[�^�[�͔_�Ƃ��n�߂܂�
		okmsg	�t���[�^�[�͔_�v�ɂȂ�܂���
			use		1	�t���[�^�[
			get		1	�_�v
			get		10	�X��	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		�l�ޔh����	times/job_man_time_rate
		scale	�l
		action	���Ƃ��n�߂�
		name	���Ƃ��n�߂�
		info	�t���[�^�[�͋��Ƃ��n�߂܂�
		okmsg	�t���[�^�[�͋��t�ɂȂ�܂���
			use		1	�t���[�^�[
			get		1	���t
			get		10	�X��	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		�l�ޔh����	times/job_man_time_rate
		scale	�l
		action	�C�s������
		name	�V�Ղ�E�l�̏C�s������
		info	�t���[�^�[�͓V�Ղ�E�l�ɂȂ�C�s�����܂�
		okmsg	�t���[�^�[�͓V�Ղ�E�l�ɂȂ�܂���
			use		1	�t���[�^�[
			get		1	�V�Ղ�E�l
			get		10	�X��	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		�l�ޔh����	times/job_man_time_rate
		scale	�l
		action	�C�s������
		name	���ǂ�E�l�̏C�s������
		info	�t���[�^�[�͂��ǂ�E�l�ɂȂ�C�s�����܂�
		okmsg	�t���[�^�[�͂��ǂ�E�l�ɂȂ�܂���
			use		1	�t���[�^�[
			use		10	������
			get		1	���ǂ�E�l
			get		10	�X��	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		�l�ޔh����	times/job_man_time_rate
		scale	�l
		action	�C�s������
		name	���ΐE�l�̏C�s������
		info	�t���[�^�[�͂��ΐE�l�ɂȂ�C�s�����܂�
		okmsg	�t���[�^�[�͂��ΐE�l�ɂȂ�܂���
			use		1	�t���[�^�[
			use		10	���Ε�
			get		1	���ΐE�l
			get		10	�X��	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		�l�ޔh����	times/job_man_time_rate
		scale	�l
		action	�֗����ɂȂ�
		name	�֗����ɂȂ�
		info	�t���[�^�[�͕֗����ɂȂ�܂�
		okmsg	�t���[�^�[�͕֗����ɂȂ�܂���
			use		1	�t���[�^�[
			get		1	�֗���
			get		10	�X��	20%
	@@use
		time	4h
		job		�l�ޔh����	times/job_man_time_rate
		scale	��
		action	����
		name	�`���V�z��Ŏ����҂�
		info	�����҂��܂��傤
		param	7000
		func	_local_
			$DT->{money}+=$USE->{param1}*$count;
			my $ret=GetMoneyString($USE->{param1}*$count).'�҂��܂���';
			if (rand(1000)<200)
			{
			UseItem(1,1,$ITEM[1]->{name}.'�������҂��Ŕ��ēX������܂���');
			}
			WriteLog(0,$DT->{id},"�o�C�g���C$ret");
			WriteLog(3,0,$DT->{shopname}."�̃t���[�^�[���o�C�g�����悤�ł�");
			return $ret;
		_local_
	@@use
		time	9h
		job		�l�ޔh����	times/job_man_time_rate
		scale	��
		action	����
		name	�R���r�j�Ŏ����҂�
		info	������Ƃ������ǂ��������ȉ҂��ł�
		param	20000
		func	_local_7
	@@USE
		time	6h
		action	�l�ޔh���Ƃ̐��ƂɂȂ�
		arg		nocount
		name	�l�ޔh���Ƃ̐��ƂɂȂ�
		info	���܂ł̌o���𐶂����āC�l�ޔh���Ƃ̐��ƂɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɐl�ޔh���Ƃ̐��Ƃł�') if ($DT->{job} eq 'man');
			$DT->{job} = 'man';
			$ret="�l�ޔh���Ƃ̐��ƂɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		2
	type	�l��
	code	man-nou
	name	�_�v
	info	�ƒ{�������̂����ӂł�
	scale	�l
	price	30000
	cost	1000
	limit	3/0.5
	plus	1d
	pop	1d
	flag	noshowcase|human
	@@USE
		time	3h
		exp		1%
		exptime	1h
		price	20000
		job		�_��	times/job_agri_time_rate
		scale	��
		action	������ɓ����
		name	������ɓ����
		info	�����̂悢����T���čw�����܂�
		okmsg	�����Ɏ��n�ł������Ȕ�����ɓ���C���܂��ɑ͔�������Ă��炢�܂���
			get		1	���n��҂�
			get		100	�͔�
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		action	�k���Ď��A����
		name	�����k���Ď��A����
		info	���ɔ엿��^���čk���C�앨�̎��A���܂�
		okmsg	���͂悭�k����C�앨�̎킪�A�����܂���
			use		1	�k���O�̔�
			use		100	�͔�
			get		1	�悭�k������
			get		10	�X��	10%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		action	���n������
		name	�˂��̎��n������
		info	�˂����ɍs���Ď��n�����܂�
		func	lostman
		param	50
		ngmsg	�������n�ł��܂���ł����d
			use		1	���n��҂�
			get		100	�˂�	50%	�˂������n���܂���
			get		10	�Ƃ����낱��	50%	���łɐH�׍��̂Ƃ����낱��������Ă��܂���
			get		1	�������⏕��	01%	���ŕ������⏕�����E���܂���
			get		1	�����傤	05%	���ɐN�����Ă����쐶�̂����傤�����܂��܂���
			get		1	�k���O�̔�
			get		10	�X��	10%
		funcb	_local_
			# 1/20�̊m���Ŏ��n�ʂ�2�{�ɂȂ�
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='����͂��Ȃ�L��ł���<br>�V����������ɓ���܂���';
			return 0;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		action	���n������
		name	�����̎��n������
		info	�������ɍs���Ď��n�����܂�
		func	lostman
		param	50
		ngmsg	�������n�ł��܂���ł����d
			use		1	���n��҂�
			get		40	������	50%	���������n���C����ɐ������܂���
			get		10	�Ƃ����炵	50%	���łɂƂ����炵������Ă��܂���
			get		1	�������⏕��	01%	���ŕ������⏕�����E���܂���
			get		1	�����傤	05%	���ɐN�����Ă����쐶�̂����傤�����܂��܂���
			get		1	�k���O�̔�
			get		10	�X��	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='����͂��Ȃ�L��ł���<br>�V����������ɓ���܂���';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		action	���n������
		name	���΂̎��n������
		info	���Δ��ɍs���Ď��n�����܂�
		func	lostman
		param	50
		ngmsg	�������n�ł��܂���ł����d
			use		1	���n��҂�
			get		40	���Ε�	50%	���΂����n���C����ɐ������܂���
			get		20	�Ƃ����炵	50%	���łɂƂ����炵������Ă��܂���
			get		1	�������⏕��	01%	���ŕ������⏕�����E���܂���
			get		1	��	05%	���ɐN�����Ă����쐶�̓؂����܂��܂���
			get		1	�k���O�̔�
			get		10	�X��	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='����͂��Ȃ�L��ł���<br>�V����������ɓ���܂���';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		action	���n������
		name	�哤�̎��n������
		info	�哤���ɍs���Ď��n�����܂�
		func	lostman
		param	50
		ngmsg	�������n�ł��܂���ł����d
			use		1	���n��҂�
			get		40	�哤	50%	�哤�����n���܂���
			get		30	�˂�	50%	���łɂ˂�������Ă��܂���
			get		1	�������⏕��	01%	���ŕ������⏕�����E���܂���
			get		1	��	05%	���ɐN�����Ă����쐶�̓؂����܂��܂���
			get		1	�k���O�̔�
			get		10	�X��	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='����͂��Ȃ�L��ł���<br>�V����������ɓ���܂���';
			return 0;
		_local_
@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		action	���n������
		name	�Ƃ����낱���̎��n������
		info	�Ƃ����낱�����ɍs���Ď��n�����܂�
		func	lostman
		param	50
		ngmsg	�������n�ł��܂���ł����d
			use		1	���n��҂�
			get		27	�Ƃ����낱��	50%	�Ƃ����낱�������n���܂���
			get		20	�哤	50%	���łɑ哤������Ă��܂���
			get		1	�������⏕��	01%	���ŕ������⏕�����E���܂���
			get		1	�����傤	05%	���ɐN�����Ă����쐶�̂����傤�����܂��܂���
			get		1	�k���O�̔�
			get		10	�X��	10%
		funcb	_local_
			return 0 if rand(1000)>50;
			
			my $USE=$_[0];
			
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			$USE->{result}->{message}->{resultok}='����͂��Ȃ�L��ł���<br>�V����������ɓ���܂���';
			return 0;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		arg		nocount
		action	���b������
		name	�ɂ�Ƃ�̐��b������
		info	�a���\���ɏ�������΁C�{�ɂ̑|����ɂɂ�Ƃ�ɐH�ׂ����邱�Ƃ��ł��܂�
		param	2
			need		1	�ɂ�Ƃ�
		func	_local_
			my $val=$USE->{param1}*$count;
			my $ret="";
			my $niwatori=$DT->{item}[20-1];
			my $toumorokosi=$DT->{item}[17-1];

			if ($niwatori*$count>$toumorokosi)
			{
			AddItem(58,$count,);
			$ret='�{�̉a������Ȃ��悤�Ȃ̂ŁC�{�ɂ̑|�������ς܂��܂���';
			WriteLog(0,$DT->{id},$ret);
			}
			else
			{
			$val*=$DT->{item}[20-1];
			$val=int(rand($val) * 2)+1;
			AddItem(9,$val,);
			AddItem(58,$count,);
			UseItem(17,$niwatori*$count,'�ɂ�Ƃ�P�H�ɂ��C�Ƃ����낱����'.$count.'�{�H�ׂ����܂���');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(20,$usecount,$ITEM[20]->{name}.'������������C���V���܂���') if $usecount;
			
			$ret='����'.$val.'��ɓ���܂���';
			WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	�Z�b�g
		action	�e���ɗ����������
		name	����z��������
		info	����e���ɕ������C�z�������Ă݂܂�
		func	lostman
		param	50
		okmsg	�z���̏����������܂���
			need		1	�ɂ�Ƃ�
			use		5	��
			get		5	�z����҂�
			get		10	�X��	10%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	�H
		action	���b������
		name	�����傤�̐��b������
		info	�����傤�ɂ����Ղ�a��^���Ă݂܂�
		func	lostman
		param	50
		ngmsg	�t�H�A�O�����Ƃ��O�ɁC�����傤�����V���Ă��܂��܂����d
		okmsg	�����ȃt�H�A�O������ɓ���܂���
			use		1	�����傤
			use		10	�Ƃ����낱��
			get		48	�t�H�A�O��	50%
			get		10	�X��	15%
	@@USE
		time	3h
		exp		1%
		exptime	1h
		job		�_��	times/job_agri_time_rate
		scale	��
		arg		nocount
		action	���b������
		name	�؂̐��b������
		info	�a���\���ɗp�ӂ���΁C�؂ɐH�ׂ����Ă���R�ɎU���ɘA��čs�����Ƃ��ł��܂�
		param	1
			need		1	��
		func	_local_
			my $val=$USE->{param1}*$count;
			my $ret="";
			my $buta=$DT->{item}[22-1];
			my $daizu=$DT->{item}[16-1];

			if ($buta*$count*5>$daizu)
			{
			AddItem(58,$count*2,);
			$ret='�a�����肻���ɂȂ������̂ŁC�؏����̑|�������ς܂��܂���';
			WriteLog(0,$DT->{id},$ret);
			}
			else
			{
			$val*=$DT->{item}[22-1];
			$val=int(rand($val) * 3)+1;
			AddItem(18,$val,);
			AddItem(58,$count,);
			UseItem(16,$buta*$count*5,'��1���ɂ��C�哤��'.($count*5).'kg�H�ׂ����܂���');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(22,$usecount,$ITEM[22]->{name}.'���R���ɓ����Ă����܂���') if $usecount;
			
			$ret='�H��̎U���ɘA��čs�����R�ŁC�؂��g�����t��'.$val.'�����܂���';
			WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@USE
		time	6h
		action	�_�Ƃ̐��ƂɂȂ�
		scale	��
		arg		nocount
		name	�_�Ƃ̐��ƂɂȂ�
		info	���܂ł̌o���𐶂����āC�_�Ƃ̐��ƂɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɔ_�Ƃ̐��Ƃł�') if ($DT->{job} eq 'agri');
			$DT->{job} = 'agri';
			$ret="�_�Ƃ̐��ƂɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		3
	type	�l��
	code	man-gyo
	name	���t
	info	�啨��ނ�ɂ͉a���K�v�ł�
	scale	�l
	price	30000
	cost	1000
	limit	3/0.5
	plus	1d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	4.5h
		exp		1%
		exptime	1.5h
		job		����	times/job_fish_time_rate
		scale	��
		action	�ނ������
		name	�ނ������
		info	�߂��̊C�݂Œނ�����Ă݂܂�
		ngmsg	�މʂ͂���܂���ł����d
			get		10	�����Ƃ�����	50%	�����Ƃ����炪�ނ�܂���
			get		2	����	50%	�������ނ�܂���
			get		100	����	60%	���т�߂܂��܂���
			get		40	�킩��	50%	���łɂ킩�߂��̂�܂���
			get		1	�����傤	02%	�M�ꂩ���Ă��������傤�������܂���
			get		10	�X��	20%
	@@USE
		time	4h
		exp		1%
		exptime	2h
		job		����	times/job_fish_time_rate
		scale	��
		action	���ɏo��
		name	���ɏo��
		info	�D�ɏ���ċ��ɏo�Ă݂܂�
		func	lostman
		param	50
		ngmsg	�މʂ͂���܂���ł����d
			use		50	����
			get		8	�����Ƃ�����	30%	�����Ƃ����炪�ނ�܂���
			get		8	����	50%	�������ނ�܂���
			get		10	����	50%	�������ނ�܂���
			get		2	���傤����	30%	�啨�̂��傤���߂��ނ�܂���
			get		1	��	02%	�M�ꂩ���Ă����؂������܂���
			get		10	�X��	20%
	@@USE
		time	2h
		exp		1%
		exptime	1h
		job		����	times/job_fish_time_rate
		scale	��
		action	���
		name	�h�q�߂񂽂������
		info	�����Ƃ�����̗������H���āC�h�q�߂񂽂������܂�
		func	lostman
		param	50
		ngmsg	�h�q�߂񂽂����Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
		okmsg	�h�q�߂񂽂����ł��܂���
			use		1	�����Ƃ�����
			use		5	�Ƃ����炵
			get		20	�h�q�߂񂽂�	80%
			get		10	�X��	10%
	@@USE
		time	2h
		exp		1%
		exptime	1h
		job		����	times/job_fish_time_rate
		scale	��
		action	��ɓ����
		name	�L���r�A����ɓ����
		info	���傤���߂̂��Ȃ�����L���r�A�����o���܂�
		func	lostman
		param	50
		ngmsg	���傤���߂́��ł����d
		okmsg	�L���r�A����ɓ���܂���
			use		1	���傤����
			get		40	�L���r�A	60%
			get		10	�X��	10%
	@@USE
		time	6h
		action	���Ƃ̐��ƂɂȂ�
		scale	��
		arg		nocount
		name	���Ƃ̐��ƂɂȂ�
		info	���܂ł̌o���𐶂����āC���Ƃ̐��ƂɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɋ��Ƃ̐��Ƃł�') if ($DT->{job} eq 'fish');
			$DT->{job} = 'fish';
			$ret="���Ƃ̐��ƂɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		4
	type	�l��
	code	man-ten
	name	�V�Ղ�E�l
	info	���g���₩�܂ڂ������܂�
	scale	�l
	price	30000
	cost	1000
	limit	3/0.5
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job	�V�Ղ牮	times/job_temp_time_rate
		scale	��
		action	���
		name	���g�������
		info	�哤���瓤�������C����ɖ��g���ɉ��H���܂�
		ngmsg	���g�����Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		10	�哤
			get		100	���g��	80%	���g�����ł��܂���
			get		10	�X��	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		�V�Ղ牮	times/job_temp_time_rate
		scale	��
		action	���
		name	���܂ڂ������
		info	���܂ڂ������܂�
		ngmsg	���܂ڂ����Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		4	�����Ƃ�����
			get		100	���܂ڂ�	80%	���܂ڂ����ł��܂���
			get		10	�X��	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		�V�Ղ牮	times/job_temp_time_rate
		scale	��
		action	���
		name	�ۓV�����
		info	�ۓV�����܂�
		func	lostman
		param	50
		ngmsg	�ۓV���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		2	����
			get		60	�ۓV	80%	�ۓV���ł��܂���
			get		10	�X��	20%
	@@USE
		time	90m
		exp	2%
		exptime	30m
		job		�V�Ղ牮	times/job_temp_time_rate
		scale	��
		action	���
		name	���ѓV�����
		info	���ѓV�����܂�
		func	lostman
		param	50
		ngmsg	���ѓV���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		20	����
			use		2	������
			use		10	��
			get		50	���ѓV	80%	���ѓV���ł��܂���
			get		10	�X��	20%
	@@USE
		time	6h
		action	�V�Ղ���̐��ƂɂȂ�
		arg		nocount
		name	�V�Ղ���̐��ƂɂȂ�
		info	���܂ł̌o���𐶂����āC�V�Ղ���̐��ƂɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɓV�Ղ���̐��Ƃł�') if ($DT->{job} eq 'temp');
			$DT->{job} = 'temp';
			$ret="�V�Ղ���̐��ƂɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		5
	type	�l��
	code	man-udon
	name	���ǂ�E�l
	info	�e�키�ǂ��1�t�������āC�V�������ǂ�̊J�����I
	scale	�l
	price	30000
	cost	1000
	limit	3/0.3
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�����ǂ�����
		info	�����ǂ�����܂�
		ngmsg	�����ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	������
			use		2	�˂�
			use		2	���܂ڂ�
			use		40	���ꂢ�Ș�
			get		40	�����ǂ�	80%	�����ǂ񂪂ł��܂���
			get		10	�X��	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�킩�߂��ǂ�����
		info	�킩�߂��ǂ�����܂�
		ngmsg	�킩�߂��ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	������
			use		2	�˂�
			use		5	�킩��
			use		32	���ꂢ�Ș�
			get		30	�킩�߂��ǂ�	90%	�킩�߂��ǂ񂪂ł��܂���
			get		10	�X��	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	���˂��ǂ�����
		info	���˂��ǂ�����܂�
		ngmsg	���˂��ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	������
			use		2	�˂�
			use		10	���g��
			use		25	���ꂢ�Ș�
			get		25	���˂��ǂ�	80%	���˂��ǂ񂪂ł��܂���
			get		10	�X��	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�ۓV���ǂ�����
		info	�ۓV���ǂ�����܂�
		ngmsg	�ۓV���ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	������
			use		2	�˂�
			use		10	�ۓV
			use		20	���ꂢ�Ș�
			get		20	�ۓV���ǂ�	80%	�ۓV���ǂ񂪂ł��܂���
			get		10	�X��	10%
	@@USE
		time	2h
		exp	2%
		exptime	40m
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	���ѓV���ǂ�����
		info	���ѓV���ǂ�����܂�
		ngmsg	���ѓV���ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		5	������
			use		5	�˂�
			use		20	���ѓV
			use		20	���ꂢ�Ș�
			get		20	���ѓV���ǂ�	80%	���ѓV���ǂ񂪂ł��܂���
			get		20	�X��	10%
	@@USE
		time	20m
		exp	0%
		exptime	10m
		job	���ǂ�	times/job_udon_time_rate
		scale	�Z�b�g
		action	���
		name	���ǂ�O�������
		info	���ǂ�O�������܂�
		okmsg	���ǂ�O�����ł��܂���
			needexp		20%
			use		10	���˂��ǂ�
			use		10	�ۓV���ǂ�
			use		10	���ѓV���ǂ�
			get		10	���ǂ�O��
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�L���r�A���ǂ�����
		info	�L���r�A���ǂ�����܂�
		func	lostman
		param	50
		ngmsg	�L���r�A���ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		40%
			use		3	������
			use		1	����
			use		2	�L���r�A
			use		8	���ꂢ�Ș�
			get		8	�L���r�A���ǂ�	80%	�L���r�A���ǂ񂪂ł��܂���
			get		10	�X��	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�g�����t���ǂ�����
		info	�g�����t���ǂ�����܂�
		func	lostman
		param	50
		ngmsg	�g�����t���ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		40%
			use		3	������
			use		1	����
			use		2	�g�����t
			use		8	���ꂢ�Ș�
			get		10	�g�����t���ǂ�	60%	�g�����t���ǂ񂪂ł��܂���
			get		10	�X��	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job		���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�t�H�A�O�����ǂ�����
		info	�t�H�A�O�����ǂ�����܂�
		func	lostman
		param	50
		ngmsg	�t�H�A�O�����ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		40%
			use		3	������
			use		1	����
			use		2	�t�H�A�O��
			use		6	���ꂢ�Ș�
			get		6	�t�H�A�O�����ǂ�	80%	�t�H�A�O�����ǂ񂪂ł��܂���
			get		10	�X��	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�������ǂ�����
		info	�������ǂ�����܂�
		func	lostman
		param	50
		ngmsg	�������ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		60%
			use		5	������
			use		1	��
			use		2	�h�q�߂񂽂�
			use		6	���ꂢ�Ș�
			get		6	�������ǂ�	80%	�������ǂ񂪂ł��܂���
			get		10	�X��	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job		���ǂ�	times/job_udon_time_rate
		scale	��
		action	���
		name	�I���W�i�����ǂ�����
		info	�I���W�i�����ǂ�����܂�
		ngmsg	�I���W�i�����ǂ���Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		80%
			need		1	�I���W�i�����ǂ񃌃V�s
			use		5	������
			use		1	����
			use		1	�����傤
			use		5	�Ƃ����炵
			use		3	���ꂢ�Ș�
			get		5	�I���W�i�����ǂ�	40%	�I���W�i�����ǂ񂪂ł��܂���
			get		10	�X��	20%
		func	_local_
			my $ret="";
			$DT->{user}->{udoncnt}+=1;
			if (rand(1000)<100)
			{
				UseItem(@@ITEMNO"���ǂ�E�l",1,"<br>�d�����I�������ǂ�E�l���C�ق��ċ����Ă����܂���");
			}
			if ((rand(1000)<100)&&($DT->{user}->{udoncnt}>50))
			{
				$DT->{user}->{udoncnt}=0;
				UseItem(@@ITEMNO"�I���W�i�����ǂ񃌃V�s",1,"<br>�I���W�i�����ǂ񃌃V�s�ɂ�������΂����C�R�₵�Ă��܂��܂���");
				WriteLog(0,$DT->{id},"�I���W�i�����ǂ񃌃V�s�������܂���");
				WriteLog(2,0,$DT->{shopname}."���I���W�i�����ǂ񃌃V�s����������R�₵�Ă��܂����悤�ł��B");
			}
			return $ret;
		_local_
	@@USE
		time	6h
		exp		1%
		exptime	4h
		job		���ǂ�	times/job_udon_time_rate
		action	�Ƃ������O�̂��ǂ�����
		name	�I���W�i�����ǂ���J������
		info	�������߂č��I���W�i�����ǂ�ɖ��O�����܂�
		arg		nocount|message30
		okmsg	�Y��Ȃ������ɍ������������Ă����܂���
			use		1	�����ǂ�
			use		1	�킩�߂��ǂ�
			use		1	���˂��ǂ�
			use		1	�ۓV���ǂ�
			use		1	���ѓV���ǂ�
			use		1	�L���r�A���ǂ�
			use		1	�g�����t���ǂ�
			use		1	�t�H�A�O�����ǂ�
			use		1	�������ǂ�
			get		1	�I���W�i�����ǂ�
			get		1	�I���W�i�����ǂ񃌃V�s
		func	_local_
			# �I���W�i�����ǂ�����
			main::OutError('���O�����Ă�������') if !$USE->{arg}->{message};
			my $ret;
			$ret='�I���W�i�����ǂ�y'.$USE->{arg}->{message}.'�z���������܂���';	
			WriteLog(3,0,$DT->{shopname}."���������ǂ�u".$USE->{arg}->{message}."�v�����������܂����B");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{udon}=$USE->{arg}->{message};
			return $ret;
		_local_
	@@USE
		time	6h
		action	���ǂ���̐��ƂɂȂ�
		arg		nocount
		name	���ǂ���̐��ƂɂȂ�
		info	���܂ł̌o���𐶂����āC���ǂ���̐��ƂɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɂ��ǂ���̐��Ƃł�') if ($DT->{job} eq 'udon');
			$DT->{job} = 'udon';
			$ret="���ǂ���̐��ƂɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		6
	type	�l��
	code	man-soba
	name	���ΐE�l
	info	�e�킻�΂�1�t�������āC�V�������΂̊J�����I
	scale	�l
	price	30000
	cost	1000
	limit	3/0.3
	plus	2d
	pop	3d
	flag	noshowcase|human
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�������΂����
		info	�������΂����܂�
		ngmsg	�������΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	���Ε�
			use		2	�˂�
			use		2	���܂ڂ�
			use		40	���ꂢ�Ș�
			get		40	��������	80%	�������΂��ł��܂���
			get		10	�X��	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�킩�߂��΂����
		info	�킩�߂��΂����܂�
		ngmsg	�킩�߂��΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	���Ε�
			use		2	�˂�
			use		5	�킩��
			use		32	���ꂢ�Ș�
			get		30	�킩�߂���	90%	�킩�߂��΂��ł��܂���
			get		10	�X��	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job		���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	���˂��΂����
		info	���˂��΂����܂�
		ngmsg	���˂��΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	���Ε�
			use		2	�˂�
			use		10	���g��
			use		25	���ꂢ�Ș�
			get		25	���˂���	80%	���˂��΂��ł��܂���
			get		10	�X��	10%
	@@USE
		time	1h
		exp	1%
		exptime	20m
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�ۓV���΂����
		info	�ۓV���΂����܂�
		ngmsg	�ۓV���΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		3	���Ε�
			use		2	�˂�
			use		10	�ۓV
			use		20	���ꂢ�Ș�
			get		20	�ۓV����	80%	�ۓV���΂��ł��܂���
			get		10	�X��	10%
	@@USE
		time	2h
		exp	2%
		exptime	40m
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	���ѓV���΂����
		info	���ѓV���΂����܂�
		ngmsg	���ѓV���΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			use		5	���Ε�
			use		5	�˂�
			use		20	���ѓV
			use		20	���ꂢ�Ș�
			get		20	���ѓV����	80%	���ѓV���΂��ł��܂���
			get		20	�X��	10%
	@@USE
		time	20m
		exp	0%
		exptime	10m
		job		���Ή�	times/job_soba_time_rate
		scale	�Z�b�g
		action	���
		name	���ΎO�������
		info	���ΎO�������܂�
		okmsg	���ΎO�����ł��܂���
			needexp		20%
			use		10	���˂���
			use		10	�ۓV����
			use		10	���ѓV����
			get		10	���ΎO��
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�L���r�A���΂����
		info	�L���r�A���΂����܂�
		func	lostman
		param	50
		ngmsg	�L���r�A���΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		40%
			use		3	���Ε�
			use		1	����
			use		2	�L���r�A
			use		8	���ꂢ�Ș�
			get		8	�L���r�A����	80%	�L���r�A���΂��ł��܂���
			get		10	�X��	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�g�����t���΂����
		info	�g�����t���΂����܂�
		func	lostman
		param	50
		ngmsg	�g�����t���΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		40%
			use		3	���Ε�
			use		1	����
			use		2	�g�����t
			use		8	���ꂢ�Ș�
			get		10	�g�����t����	60%	�g�����t���΂��ł��܂���
			get		10	�X��	20%
	@@USE
		time	3h
		exp	4%
		exptime	1h
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�t�H�A�O�����΂����
		func	lostman
		param	50
		info	�t�H�A�O�����΂����܂�
		ngmsg	�t�H�A�O�����΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		40%
			use		3	���Ε�
			use		1	����
			use		2	�t�H�A�O��
			use		6	���ꂢ�Ș�
			get		6	�t�H�A�O������	80%	�t�H�A�O�����΂��ł��܂���
			get		10	�X��	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�������΂����
		info	�������΂����܂�
		func	lostman
		param	50
		ngmsg	�������΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		60%
			use		5	���Ε�
			use		1	��
			use		2	�h�q�߂񂽂�
			use		6	���ꂢ�Ș�
			get		6	��������	80%	�������΂��ł��܂���
			get		10	�X��	20%
	@@USE
		time	6h
		exp	5%
		exptime	2h
		job	���Ή�	times/job_soba_time_rate
		scale	��
		action	���
		name	�I���W�i�����΂����
		info	�I���W�i�����΂����܂�
		ngmsg	�I���W�i�����΍��Ɏ��s���C�ޗ��𖳑ʂɂ��Ă��܂��܂����d
			needexp		80%
			need		1	�I���W�i�����΃��V�s
			use		5	���Ε�
			use		1	����
			use		1	���傤����
			use		15	��
			use		3	���ꂢ�Ș�
			get		5	�I���W�i������	40%	�I���W�i�����΂��ł��܂���
			get		10	�X��	30%
		func	_local_
			my $ret="";
			$DT->{user}->{sobacnt}+=1;
			if (rand(1000)<100)
			{
				UseItem(@@ITEMNO"���ΐE�l",1,"<br>�d�����I�������ΐE�l���C�ق��ċ����Ă����܂���");
			}
			if ((rand(1000)<100)&&($DT->{user}->{sobacnt}>50))
			{
				$DT->{user}->{sobacnt}=0;
				UseItem(@@ITEMNO"�I���W�i�����΃��V�s",1,"<br>�I���W�i�����΃��V�s�ɂ�������΂����C�R�₵�Ă��܂��܂���");
				WriteLog(0,$DT->{id},"�I���W�i�����΃��V�s�������܂���");
				WriteLog(2,0,$DT->{shopname}."���I���W�i�����΃��V�s����������R�₵�Ă��܂����悤�ł��B");
			}
			return $ret;
		_local_
	@@USE
		time	6h
		exp		1%
		exptime	4h
		job		���Ή�	times/job_soba_time_rate
		action	�Ƃ������O�̂��΂����
		name	�I���W�i�����΂��J������
		info	�������߂č��I���W�i�����΂ɖ��O�����܂�
		arg		nocount|message30
		okmsg	�Y��Ȃ������ɍ������������Ă����܂���
			use		1	��������
			use		1	�킩�߂���
			use		1	���˂���
			use		1	�ۓV����
			use		1	���ѓV����
			use		1	�L���r�A����
			use		1	�g�����t����
			use		1	�t�H�A�O������
			use		1	��������
			get		1	�I���W�i������
			get		1	�I���W�i�����΃��V�s
		func	_local_
			# �I���W�i�����΂����
			main::OutError('���O�����Ă�������') if !$USE->{arg}->{message};
			my $ret;
			$ret='�I���W�i�����΁y'.$USE->{arg}->{message}.'�z���������܂���';	
			WriteLog(3,0,$DT->{shopname}."���������΁u".$USE->{arg}->{message}."�v�����������܂����B");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{soba}=$USE->{arg}->{message};
			return $ret;
		_local_
	@@USE
		time	6h
		action	���΍��̐��ƂɂȂ�
		arg		nocount
		name	���΍��̐��ƂɂȂ�
		info	���܂ł̌o���𐶂����āC���΍��̐��ƂɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɂ��΍��̐��Ƃł�') if ($DT->{job} eq 'soba');
			$DT->{job} = 'soba';
			$ret="���΍��̐��ƂɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		7
	type	�l��
	code	man-benri
	name	�֗���
	info	�I���☥�􂢂Ȃǂ����ӂł�
	scale	�l
	price	30000
	cost	1000
	limit	5/0.5
	plus	2h
	pop		3d
	flag	noshowcase|human
	@@USE
		time	1h
		job		�l�ޔh����	times/job_man_time_rate
		scale	��
		action	��Ƃ���
		price	0
		name	��I��1�ɂ���
		info	��I��1�ɂ���
		arg		nocount
		param	1
		func	_local_
			# ����I���ύX
			#   param1 �ύX��̒I��
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="��I��$DT->{showcasecount}�ɂ��܂���";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."�̒�I��$DT->{showcasecount}�ɂȂ�܂���");
			
			return $ret;
		_local_
	@@USE
		time	2h
		job		�l�ޔh����	times/job_man_time_rate
		price	10000
		name	��I��2�ɂ���
		info	��I��2�ɂ���
		func	_local_1
		arg		nocount
		param	2
	@@USE
		time	4h
		job		�l�ޔh����	times/job_man_time_rate
		price	50000
		name	��I��3�ɂ���
		info	��I��3�ɂ���
		func	_local_1
		arg		nocount
		param	3
			need	2	�֗���
	@@USE
		time	6h
		job		�l�ޔh����	times/job_man_time_rate
		price	100000
		name	��I��4�ɂ���
		info	��I��4�ɂ���
		func	_local_1
		arg		nocount
		param	4
			need	2	�֗���
	@@USE
		time	10h
		job		�l�ޔh����	times/job_man_time_rate
		price	200000
		name	��I��5�ɂ���
		info	��I��5�ɂ���
		func	_local_1
		arg		nocount
		param	5
			need	3	�֗���
	@@USE
		time	12h
		job		�l�ޔh����	times/job_man_time_rate
		price	500000
		name	��I��6�ɂ���
		info	��I��6�ɂ���
		func	_local_1
		arg		nocount
		param	6
			need	3	�֗���
	@@USE
		time	14h
		job		�l�ޔh����	times/job_man_time_rate
		price	1000000
		name	��I��7�ɂ���
		info	��I��7�ɂ���
		func	_local_1
		arg		nocount
		param	7
			need	4	�֗���
	@@USE
		time	16h
		job		�l�ޔh����	times/job_man_time_rate
		price	2000000
		name	��I��8�ɂ���
		info	��I��8�ɂ���
		func	_local_1
		arg		nocount
		param	8
			need	5	�֗���
	@@USE
		time	30m
		exp		1%
		exptime	10m
		job		�l�ޔh����	times/job_man_time_rate
		scale	��
		action	��
		name	���􂢂�����
		info	���ꂽ����􂢂܂�
		func	lostman
		param	10
		ngmsg	����S�������Ă��܂��܂����d
			use		10	���ꂽ��
			get		10	���ꂢ�Ș�	90%	�����s�J�s�J�ɂȂ�܂���
			get		10	�X��	02%
	@@USE
		time	1h
		exp		1%
		exptime	30m
		job		�l�ޔh����	times/job_man_time_rate
		scale	��
		action	�Z�b�g����
		name	�H��􂢋@�Ř��􂢂�����
		info	���ꂽ����H��􂢋@�ɃZ�b�g���܂�
		func	lostman
		param	50
		ngmsg	����S�������Ă��܂��܂����d
			need		1	�H��􂢋@
			use		50	���ꂽ��
			get		50	���ꂢ�Ș�	95%	�����s�J�s�J�ɂȂ�܂���
			get		10	�X��	05%
	@@use
		time	10h
		exp		5%
		exptime	6h
		job		�l�ޔh����	times/job_man_time_rate
		action	�L���𗬂�
		name	[�V��]�ɍL���𗬂�
		info	���̃t�H�[���ɕ�����������Ń{�^�����N���b�N�����<br>[�V��]�ɍL��������܂�
		param	300
		arg		nocount|message100
			use	1	�֗���
		func	_local_
			main::OutError('�L���������L����������') if !$USE->{arg}->{message};
			my $ret;
			my $up=int($USE->{param1}*(2-$DT->{rank}/5000));
			$DT->{rank}+=$up;
			$DT->{rank}=10000 if $DT->{rank}>10000;

			$ret='[�V��]�ɍL���𗬂��Ē��ڂ���C�l�C'.int($up/100)."%�A�b�v";
			WriteLog(2,0,"�y�L���z".$USE->{arg}{message});
			WriteLog(0,$DT->{id},$ret);	
			return $ret;
		_local_
	@@USE
		time	6h
		action	�Ŕ����낷
		arg		nocount
		name	�Ŕ����낷
		info	���E�̊Ŕ����낵�܂�
		func	_local_
			my $ret="";
			main::OutError('���E�̊Ŕ͂������Ă��܂���') if ($DT->{job} eq '');
			$DT->{money}+=30000;
			$DT->{job}='';	
			$ret='�Ŕ����낵�C�ԘJ��\30000���󂯎��܂���';
			WriteLog(0,$DT->{id},"�Ŕ����낵�C�ԘJ�����󂯎��܂���");
			WriteLog(3,0,"���E�̊Ŕ����낵��".$DT->{shopname}."�ɁC���X���ԘJ�����x�����ꂽ�悤�ł�");
			return $ret;
		_local_

@@ITEM
	no		8
	type	�l��
	code	man-black
	name	�u���b�N�H���
	info	���܂����X�͂��g���ė��H������܂�
	scale	�l
	price	50000
	cost	2500
	limit	2/0.2
	plus	2d
	flag	noshowcase|human
	@@use
		time	6h
		exp	5%
		exptime	4h
		job		���Ƌ�	times/job_black_time_rate
		scale	��
		action	���Ԃ��Ă�
		name	���Ԃ��Ă�
		info	���Ԃ�����m����50%�ł�
		ngmsg	���Ԃ͗��܂���ł���
		okmsg	���Ԃ�����Ă��܂���
		arg		nocount
			get		1	�u���b�N�H���	50%
	@@use
		time	1h
		exp	1%
		exptime	30m
		job		���Ƌ�	times/job_black_time_rate
		scale	��
		action	���
		name	�ł��ǂ�����
		info	���肠�킹�̍ޗ��œK���ɂ��ǂ������Ă݂܂�
		func	lostman
		param	50
		ngmsg	�ł��ǂ���Ɏ��s���܂����d
			use		10	���ꂽ��
			get		10	�ł��ǂ�	95%	�ł��ǂ�����܂���
			get		10	�X��	07%
	@@use
		time	1h
		exp	1%
		exptime	30m
		job		���Ƌ�	times/job_black_time_rate
		scale	��
		action	���
		name	�ł��΂����
		info	���肠�킹�̍ޗ��œK���ɂ��΂�����Ă݂܂�
		func	lostman
		param	50
		ngmsg	�ł��΍��Ɏ��s���܂����d
			use		10	���ꂽ��
			get		10	�ł���	95%	�ł��΂����܂���
			get		10	�X��	07%
	@@use
		time	4h
		exp	5%
		exptime	2h
		job		���Ƌ�	times/job_black_time_rate
		scale	��
		action	���s����
		name	����ւ��������s����
		info	���X�̒�I�̏��i���C�������葼�̏��i�Ƃ���ւ��܂�
		arg		target|nocount
			use		1	�u���b�N�H���
			use		50	�ł��ǂ�
			use		50	�ł���
			use		10	�X��
		func	_local_
		# ������ւ��������s����
			my $cnt=int(rand(100))+1;
			my $ret="����ւ����͎��s���C�X�̐l�C��������܂���";
			if(rand(1000)<900)
			{
				if($DTS->{item}[@@ITEMNO"�x��@"-1])
				{
					if(rand(1000)<200)
					{
					$DTS->{showcase}[0]=57; # �ł��΂̃A�C�e���ԍ�
					$DTS->{price}[0]=20; # �ł��΂̉��i
					$DTS->{item}[@@ITEMNO"�ł���"-1]+=$cnt;
					$DTS->{item}[@@ITEMNO"�ł���"-1]=2000 if $DTS->{item}[$itemno2-1]>2000;
					$ret="����ւ����͐������܂���";
					$DTS->{item}[@@ITEMNO"�x��@"-1]--;
					WriteLog(2,0,$DTS->{shopname}."�̒�I�̏��i���ł��΂ɂ���ւ����C�{�����X�傪�x��@���������󂵂܂���");
					}
					elsif(rand(1000)<700)
					{
					$DT->{rank}-=int($DT->{rank}/3);
					$DTS->{item}[@@ITEMNO"�x��@"-1]--;
					WriteLog(3,0,$DTS->{shopname}."�ɐN������".$DT->{shopname}."�̃u���b�N�H������C�x��@��j�󂵂܂��������Ǖ߂܂�܂���");
					}
					else
					{
					$DT->{rank}-=int($DT->{rank}/3);
					WriteLog(3,0,$DTS->{shopname}."�̌x��@���苿���C�N�����Ă���".$DT->{shopname}."�̃u���b�N�H������߂܂�܂���");
					}
				}
				else
				{
				$DTS->{showcase}[0]=45; # �ł��ǂ�̃A�C�e���i���o�[
				$DTS->{price}[0]=20; # �ł��ǂ�̉��i
				$DTS->{item}[@@ITEMNO"�ł��ǂ�"-1]+=$cnt;
				$DTS->{item}[@@ITEMNO"�ł��ǂ�"-1]=2000 if $DTS->{item}[$itemno-1]>2000;
				$ret="����ւ����͐������܂���";
				WriteLog(2,0,$DTS->{shopname}."�̒�I�̏��i���ł��ǂ�ɂ���ւ����܂���");
				}
			}
			else
			{
			$ret="����ւ����͎��s���܂���";
			WriteLog(3,0,$DTS->{shopname}."�Ɍ��ꂽ�u���b�N�H������C�Ȃ������������ɋ����Ă����܂���");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
			_local_
	@@use
		time	4h
		exp	10%
		job		���Ƌ�	times/job_black_time_rate
		scale	��
		action	������������
		name	������������
		info	�x��@�̂���X�͊댯�I�H
		arg		target|nocount
			use		50	�X��
		func	_local_
			# �����������i�������̓C�x���g�Ɠ������b�Z�[�W���o�́j
			
			my $ret="�������͎��s���C���X�̐l�C��������܂���";
			if(rand(1000)<700)
			{
				if($DTS->{item}[@@ITEMNO"�x��@"-1])
				{
					$DT->{rank}-=int($DT->{rank}/2);
					if(rand(1000)<700)
					{
						$DTS->{item}[@@ITEMNO"�x��@"-1]--;
						WriteLog(3,0,$DT->{shopname}."�̃u���b�N�H�����".$DTS->{shopname}."�֖������ɓ���C$ITEM[@@ITEMNO"�x��@"]->{name}��j�󂵂܂��������Ǖ߂܂�܂����B");
					}
					else
					{
						WriteLog(3,0,$DT->{shopname}."�̃u���b�N�H�����".$DTS->{shopname}."�֖������ɓ���܂��������s���܂����B");
					}
				}
				else
				{
					my $manbiki_count=0;
					foreach my $idx (0..$DTS->{showcasecount}-1)
					{
						my $itemno=$DTS->{showcase}[$idx];
						if($itemno)
						{
							my $cnt=int($DTS->{item}[$itemno-1]/4);
							$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
							$DTS->{item}[$itemno-1]-=$cnt;
							$DT->{item}[$itemno-1]+=$cnt;
							$manbiki_count+=$cnt*$DTS->{price}[$idx];
						}
					}
					$ret="�������͐������܂���";
					$ret="�u���b�N�H����͋C���ς���Ė���������߂܂���" if !$manbiki_count;
					WriteLog(2,0,$DTS->{shopname}."�����z".GetMoneyString($manbiki_count)."�̖�������Q�ɑ����܂����B") if $manbiki_count;
					WriteLog(2,0,$DTS->{shopname}."�ɓ������������Ƃ͉�����炸�ɓ����܂����B") if !$manbiki_count;
				}
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/3);
				WriteLog(3,0,$DT->{shopname}."�̃u���b�N�H�����".$DTS->{shopname}."�֖������ɓ���܂��������s���܂����B");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
	@@use
		time	10h
		exp	10%
		job		���Ƌ�	times/job_black_time_rate
		scale	��
		action	�����\�𗬂�
		name	�X�܂̈����\�𗬂�
		info	�����t���Ȃ��\�𗬂��C���X�̐l�C�������܂�
		arg		target|nocount
			use		1	�u���b�N�H���
			use		100	�X��
		func	_local_
			# �������\�𗬂����
			my $ret;
			if(rand(1000)<750)
			{
				$DTS->{rank}-=int($DTS->{rank}/4);
				$ret=$DTS->{shopname}.'�̈����\�𗬂���킪�������܂����B';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DTS->{shopname}.'�̈����\���L�܂�l�C��������܂����B');
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/2);
				$ret=$DTS->{shopname}.'�̈����\�𗬂���킪���s���܂���';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."�̃u���b�N�H�����".$DTS->{shopname}.'�̈����\�𗬂����Ɖ�􂵂Ă����悤�ł��B');
			}
			return $ret;
			_local_
	@@use
		time	2h
		exp	10%
		job		���Ƌ�	times/job_black_time_rate
		action	�������
		name	�X�͂��������
		info	�X�͂����ׂĉ�����C�X�̐l�C���グ�܂�
		arg		nocount
		func	_local_
			main::OutError('�X�͂�100�ȏ�Ȃ��Ɖ���ł��܂���') if ($DT->{item}[@@ITEMNO"�X��"-1]<100);
			my $ret="";
			my $power;
			my $cnt=$DT->{item}[@@ITEMNO"�X��"-1];
			$power=$DT->{item}[@@ITEMNO"�X��"-1]*3;
			my $up=int($power*(2-$DT->{rank}/5000));

			$DT->{rank}+=$up;
			$DT->{rank}=10000 if $DT->{rank}>10000;
			$ret="�X�͂����ׂĉ�����܂����i�l�C".int($up/100)."%�A�b�v�j";
			UseItem(@@ITEMNO"�X��",$cnt);
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."�����ׂĂ̓X�͂�������܂����B");
			return $ret;
			_local_
	@@USE
		time	0m
		action	���ԑ��������
		scale	��
		name	���ԑ��������
		info	��������Ύ��Ԃ����߂���I
			use		2	�u���b�N�H���
		arg		nocount
		func	_local_
			# ���������ԑ���
			my $ret;
			my $cnt=int(rand(6))+1;

			if(rand(1000)<100)
			{
				$ret='���ԑ���͎��s���܂���';
				WriteLog(3,0,$DT->{shopname}.'�̃u���b�N�H������C���ԑ���������������悤�ł��B');
				AddItem(8,1,'�u���b�N�H�����1�l���C����̊���ڂ���߂��Ă��܂���');
				WriteLog(0,$DT->{id},'���ԑ���͎��s���܂���');
			}
			else
			{
				$DT->{time}-=3600*($cnt);
				$DT->{user}->{black}+=1;
				$ret='���ԑ���͐������܂����@�i�{'.($cnt).'���ԁj';
				WriteLog(3,0,$DT->{shopname}.'�̃u���b�N�H������C���ԑ���������Ȃ����悤�ł��B');
				WriteLog(0,$DT->{id},'���ԑ���̌��ʁC�������Ԃ������܂���');
			}					
			return $ret;
		_local_
	@@USE
		time	6h
		action	���H��̃v���ɂȂ�
		arg		nocount
		name	���H��̃v���ɂȂ�
		info	���܂ł̌o���𐶂����āC���H��̃v���t�F�b�V���i���ɂȂ�܂�
			needexp		20%
		func	_local_
			my $ret="";
			main::OutError('���݂��łɗ��H��̃v���t�F�b�V���i���ł�') if ($DT->{job} eq 'black');
			$DT->{job} = 'black';
			$ret="���H��̃v���t�F�b�V���i���ɂȂ�܂���";
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		9
	type	���Y��
	code	riku-tamagoa
	name	��
	info	�h�{���̍����H�i�ł�
	scale	��
	price	100
	cost	10
	limit	5000/50
	base	2500/10000
	plus	5h
	pop	40m
	point	20%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	��
			get		10	�͔�	15%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		10
	type	���Y��
	code	riku-tamagob
	name	�z����҂�
	info	�h�{���̍����H�i�ł�
	scale	��
	price	100
	cost	50
	limit	50/0
	pop	10d
	funct	_local_
		my($ITEM,@DT)=@_;
		my $gabirth_per_day=3;  # 1���ɂ����傤��3�H�Y�܂��悤�Ȋm��(?)�̐ݒ�
		my $nibirth_per_day=30;  # 1���ɂɂ�Ƃ肪30�H�Y�܂��悤�Ȋm��(?)�̐ݒ�
		my $val          =1;  # ��x�ɎY�܂���{��

		my $gabirth_rate=$gabirth_per_day && (86400/$gabirth_per_day); # 0�Ŋ���̂�j�~
		my $nibirth_rate=$nibirth_per_day && (86400/$nibirth_per_day);
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"�z����҂�"-1];
			if(rand($gabirth_rate)<$TIMESPAN) # 1�X�܂ɂ��u1����$gabirth_per_day��v�̊m���ŏ������^�ɂȂ�(�n�Y�c)
			{
				UseItemSub(@@ITEMNO"�z����҂�",$val,$DT);
				AddItemSub(@@ITEMNO"�����傤",$val,$DT);
				WriteLog(0,$DT->{id},'�Ȃ�ƁI�����炪���傤�����܂�܂���');
			}
			if(rand($nibirth_rate)<$TIMESPAN)
			{
				UseItemSub(@@ITEMNO"�z����҂�",$val,$DT);
				AddItemSub(@@ITEMNO"�ɂ�Ƃ�",$val,$DT);
			}
		}
	_local_ 

@@ITEM
	no		11
	type	���Y��
	code	riku-age
	name	���g��
	info	���ɃL�c�l�̍D���Ƃ�����H�i�ł�
	scale	��
	price	300
	cost	10
	limit	10000/10
	base	500/2000
	plus	5h
	pop	40m
	point	20%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	���g��
			get		10	�͔�	20%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		12
	type	���Y��
	code	riku-negi
	name	�˂�
	info	���ǂ�₻�΂ɂ͌������Ȃ��򖡂ł�
	scale	�c
	price	200
	limit	5000/10
	base	500/2000
	plus	3h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�˂�
			get		10	�͔�	25%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		13
	type	���Y��
	code	riku-komugi
	name	������
	info	���ǂ��V�Ղ�̍ޗ��ɂȂ�܂�
	scale	kg
	price	500
	cost	10
	limit	1000/10
	base	500/1000
	plus	4h
	pop	4h
	point	30%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	������
			get		10	�͔�	30%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		14
	type	���Y��
	code	riku-soba
	name	���Ε�
	info	���΂̍ޗ��ɂȂ�܂�
	scale	kg
	price	500
	cost	10
	limit	1000/10
	base	500/1000
	plus	4h
	pop	4h
	point	30%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	���Ε�
			get		10	�͔�	30%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		15
	type	���Y��
	code	riku-tougarasi
	name	�Ƃ����炵
	info	���������w�h�q�߂񂽂��x�̖��t���Ɏg���܂�
	scale	kg
	price	800
	limit	1000/10
	base	500/1000
	plus	-1d
	pop	5h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�Ƃ����炵
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		16
	type	���Y��
	code	riku-daizu
	name	�哤
	info	���H�i�̈�Ɂw���g���x������܂�
	scale	kg
	price	400
	limit	1500/20
	base	1000/2000
	plus	-1d
	pop	5h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�哤
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		17
	type	���Y��
	code	riku-toukibi
	name	�Ƃ����낱��
	info	�ƒ{�̉a�ɂ��Ȃ�܂�
	scale	kg
	price	600
	limit	1000/10
	base	500/1000
	plus	-1d
	pop	4h
	point	50%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�Ƃ����낱��
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		18
	type	���Y��
	code	riku-toryuhu
	name	�g�����t
	info	�߂��炵�����̂��ł�
	scale	��
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�g�����t
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		19
	type	���Y��
	code	riku-foagura
	name	�t�H�A�O��
	info	��傳���������傤�̊̑��ł�
	scale	��
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�t�H�A�O��
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		20
	type	���Y��
	code	riku-niwatori
	name	�ɂ�Ƃ�
	info	�����Y�܂���ɂ͉a���K�v�ł�
	scale	�H
	price	5000
	limit	30/3
	base	30/300
	plus	1d
	pop	10d
	@@USE
		time	30m
		action	��������
		scale	��
		name	�����傤�ƌ�������
		info	�{���ɍs���Č{�������傤�ƌ������܂�
		okmsg	�����傤����ɓ���܂���
			use		2	�ɂ�Ƃ�
			get		1	�����傤
	@@USE
		time	30m
		action	��������
		scale	��
		name	�؂ƌ�������
		info	�{���ɍs���Č{��؂ƌ������܂�
		okmsg	�؂���ɓ���܂���
			use		3	�ɂ�Ƃ�
			get		1	��

@@ITEM
	no		21
	type	���Y��
	code	riku-gatyou
	name	�����傤
	info	�a�������Ղ����đ��点�܂��傤
	scale	�H
	price	7500
	limit	20/2
	base	20/200
	plus	-1d
	pop	10d

@@ITEM
	no		22
	type	���Y��
	code	riku-buta
	name	��
	info	�ʓ|���悭���Ă���ƁC���Ԃ������邩������܂���
	scale	��
	price	10000
	limit	20/2
	plus	1d
	pop	10d

@@ITEM
	no		23
	type	�C�Y��
	code	umi-ebi
	name	����
	info	�v���b�Ɛg�̈������܂����C�ߊC���̂��тł�
	scale	�C
	price	100
	limit	5000/20
	base	1000/4000
	plus	3h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	����
			get		10	�͔�	25%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		24
	type	�C�Y��
	code	umi-wakame
	name	�킩��
	info	�~�l���������Ղ�̊C���ł�
	scale	kg
	price	200
	limit	2500/10
	base	100/2000
	plus	4h
	pop	1h
	point	10%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�킩��
			get		10	�͔�	30%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		25
	type	�C�Y��
	code	umi-kama
	name	���܂ڂ�
	info	�s���N�̂��܂ڂ��ł�
	scale	�{
	price	300
	limit	1500/10
	plus	4h
	pop	90m
	point	30%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	���܂ڂ�
			get		10	�͔�	30%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		26
	type	�C�Y��
	code	umi-maruten
	name	�ۓV
	info	���݂̂���ۓV�ł�
	scale	��
	price	500
	limit	1000/10
	plus	6h
	pop	150m
	point	50%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�ۓV
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		27
	type	�C�Y��
	code	umi-ebiten
	name	���ѓV
	info	�J���b�Ɨg���������т̓V�Ղ�ł�
	scale	�C
	price	600
	limit	1000
	plus	-1h
	pop	180m
	point	50%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	���ѓV
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		28
	type	�C�Y��
	code	umi-suke
	name	�����Ƃ�����
	info	���܂ڂ��̌����ɂȂ鋛�ŁC���͉��H�ł��܂�
	scale	�C
	price	1000
	limit	1000/10
	base	500/5000
	plus	5h
	pop	9h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�����Ƃ�����
			get		10	�͔�	50%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		29
	type	�C�Y��
	code	umi-eso
	name	����
	info	�ۓV�̌����ɂȂ鋛�ł�
	scale	�C
	price	2000
	limit	500/5
	base	250/5000
	plus	7h
	pop	18h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	����
			get		10	�͔�	50%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		32
	type	�C�Y��
	code	umi-katuo
	name	����
	info	�������ǂ�i���΁j�̂������Ɍ������܂���
	scale	�C
	price	2000
	limit	500
	base	250/5000
	plus	-1m
	pop	18h
	point	200%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	����
			get		10	�͔�	50%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		33
	type	�C�Y��
	code	umi-tyouzame
	name	���傤����
	info	�C�̕�ƌĂ΂�鋛�ł�
	scale	�C
	price	8000
	limit	100
	base	250/5000
	plus	-1m
	pop	4d
	point	200%
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	���傤����
			get		10	�͔�	80%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		30
	type	�C�Y��
	code	umi-mentai
	name	�h�q�߂񂽂�
	info	�����Ƃ�����̗����Ƃ����炵�`�ɒЂ����񂾁C���������̂ЂƂł�
	scale	kg
	price	3000
	limit	300
	base	50/200
	plus	-1d
	pop	12h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�h�q�߂񂽂�
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		31
	type	�C�Y��
	code	umi-kyabia
	name	�L���r�A
	info	�����_�C���ƌĂ΂�Ē��d�����C���傤���߂̗��ł�
	scale	kg
	price	2000
	limit	500
	base	50/200
	plus	-1d
	pop	8h
	@@USE
		time	1m
		action	�R���|�X�g�ɓ����
		name	�R���|�X�g�ɓ����
		info	�Â��Ȃ����H�i���R���|�X�g�ɓ���C�͔�����܂�
		ngmsg	�͔���Ɏ��s���܂���
			use		1	�L���r�A
			get		10	�͔�	35%	�㎿�͔̑삪�ł��܂���

@@ITEM
	no		34
	type	���ǂ�
	code	udon-su
	name	�����ǂ�
	info	�ʍD�݂̃V���v�����ǂ�
	price	500
	limit	1000/0
	pop	75m
	point	40%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	�����ǂ�
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		35
	type	���ǂ�
	code	udon-wakame
	name	�킩�߂��ǂ�
	info	���̖т��w���V�[���ǂ�
	price	600
	limit	1000/0
	pop	90m
	point	50%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	�킩�߂��ǂ�
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		36
	type	���ǂ�
	code	udon-kitune
	name	���˂��ǂ�
	info	���̂��݂��񂾖��g������i�̂��ǂ�
	price	800
	limit	1000/0
	pop	120m
	point	60%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	���˂��ǂ�
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		37
	type	���ǂ�
	code	udon-maruten
	name	�ۓV���ǂ�
	info	�H�׉����̂���ۓV���̂������ǂ�
	price	1000
	limit	1000/0
	pop	120m
	point	75%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	�ۓV���ǂ�
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		38
	type	���ǂ�
	code	udon-ebiten
	name	���ѓV���ǂ�
	info	������Ɨg���������т���C�̂������ǂ�
	price	2000
	limit	500/0
	pop	240m
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	���ѓV���ǂ�
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		39
	type	���ǂ�
	code	udon-zanmai
	name	���ǂ�O��
	info	�������߂��ǂ�O��Z�b�g
	scale	�Z�b�g
	price	5000
	limit	200
	pop	8h
	point	500%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	���ǂ�O��
			get		3	���ꂽ��
			get		10	�X��	30%

@@ITEM
	no		40
	type	���ǂ�
	code	udon-kyabia
	name	�L���r�A���ǂ�
	info	���E�O�咿�����ǂ�̂ЂƂ�
	price	7500
	limit	120/0
	pop	12h
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�L���r�A���ǂ�
			get		1	���ꂽ��
			get		10	�X��	50%

@@ITEM
	no		41
	type	���ǂ�
	code	udon-toryuhu
	name	�g�����t���ǂ�
	info	���E�O�咿�����ǂ�̂ЂƂ�
	price	8000
	limit	120/0
	pop	13h
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�g�����t���ǂ�
			get		1	���ꂽ��
			get		10	�X��	50%

@@ITEM
	no		42
	type	���ǂ�
	code	udon-foagura
	name	�t�H�A�O�����ǂ�
	info	���E�O�咿�����ǂ�̂ЂƂ�
	price	10000
	limit	100/0
	pop	15h
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�t�H�A�O�����ǂ�
			get		1	���ꂽ��
			get		10	�X��	50%

@@ITEM
	no		43
	type	���ǂ�
	code	udon-hakata
	name	�������ǂ�
	info	�����̖��̓������ǂ�
	price	20000
	limit	50
	pop	25h
	point	200%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�������ǂ�
			get		1	���ꂽ��
			get		10	�X��	70%

@@ITEM
	no		44
	type	���ǂ�
	code	udon-origi
	name	�I���W�i�����ǂ�
	info	�������߂č�����I���W�i�����ǂ�
	price	50000
	limit	20/0
	pop	60h
	point	200%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	���̂悤�ɔ������������ł�
			use		1	�I���W�i�����ǂ�
			get		1	���ꂽ��
			get		20	�X��	50%

@@ITEM
	no		45
	type	���ǂ�
	code	udon-yami
	name	�ł��ǂ�
	info	�u���b�N�H�����������܂������ǂ�
	price	100
	limit	5000/0
	pop	1h
	point	-10%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��ǂ��H�ׂ܂�
		okmsg	�������ɂ����������Ƃ͂����܂���ł���
			use		1	�ł��ǂ�
			get		1	���ꂽ��

@@ITEM
	no		46
	type	����
	code	soba-kake
	name	��������
	info	�ʍD�݂̃V���v������
	price	500
	limit	1000/0
	pop	75m
	point	40%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	��������
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		47
	type	����
	code	soba-wakame
	name	�킩�߂���
	info	���̖т��w���V�[����
	price	600
	limit	1000/0
	pop	90m
	point	50%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	�킩�߂���
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		48
	type	����
	code	soba-kitune
	name	���˂���
	info	���̂��݂��񂾖��g������i�̂���
	price	800
	limit	1000/0
	pop	120m
	point	60%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	���˂���
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		49
	type	����
	code	soba-maruten
	name	�ۓV����
	info	�H�׉����̂���ۓV���̂�������
	price	1000
	limit	1000/0
	pop	120m
	point	75%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	�ۓV����
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		50
	type	����
	code	soba-ebiten
	name	���ѓV����
	info	������Ɨg���������т���C�̂�������
	price	2000
	limit	500/0
	pop	240m
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	���ѓV����
			get		1	���ꂽ��
			get		10	�X��	20%

@@ITEM
	no		51
	type	����
	code	soba-zanmai
	name	���ΎO��
	info	�������߂��ΎO��Z�b�g
	scale	�Z�b�g
	price	5000
	limit	200
	pop	8h
	point	500%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�ƂĂ��������������ł�
			use		1	���ΎO��
			get		3	���ꂽ��
			get		10	�X��	30%

@@ITEM
	no		52
	type	����
	code	soba-kyabia
	name	�L���r�A����
	info	���E�O�咿�����΂̂ЂƂ�
	price	7500
	limit	120/0
	pop	12h
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�L���r�A����
			get		1	���ꂽ��
			get		10	�X��	50%

@@ITEM
	no		53
	type	����
	code	soba-toryuhu
	name	�g�����t����
	info	���E�O�咿�����΂̂ЂƂ�
	price	8000
	limit	120/0
	pop	13h
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�g�����t����
			get		1	���ꂽ��
			get		10	�X��	50%

@@ITEM
	no		54
	type	����
	code	soba-foagura
	name	�t�H�A�O������
	info	���E�O�咿�����΂̂ЂƂ�
	price	10000
	limit	100/0
	pop	15h
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	�t�H�A�O������
			get		1	���ꂽ��
			get		10	�X��	50%

@@ITEM
	no		55
	type	����
	code	soba-hakata
	name	��������
	info	�����̖��̓�������
	price	20000
	limit	50
	pop	25h
	point	200%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�т����肷��قǔ������������ł�
			use		1	��������
			get		1	���ꂽ��
			get		10	�X��	70%

@@ITEM
	no		56
	type	����
	code	soba-origi
	name	�I���W�i������
	info	�������߂č�����I���W�i������
	price	50000
	limit	20/0
	pop	60h
	point	200%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	���̂悤�ɔ������������ł�
			use		1	�I���W�i������
			get		1	���ꂽ��
			get		20	�X��	50%

@@ITEM
	no		57
	type	����
	code	soba-yami
	name	�ł���
	info	�u���b�N�H�����������܂�������
	price	100
	limit	5000/0
	pop	1h
	point	-10%
	@@USE
		time	5m
		action	�H�ׂ�
		name	�H�ׂ�
		info	�M�X�̂��΂�H�ׂ܂�
		okmsg	�������ɂ����������Ƃ͂����܂���ł���
			use		1	�ł���

@@ITEM
	no		58
	type	�c�[��
	code	tool-tikara
	name	�X��
	info	�����Ƃ����Ƃ��ɐ^���𔭊����邩������Ȃ�[�݂�������]
	scale	��
	price	0
	limit	1000/0
	pop		0
	flag	noshowcase|norequest|notrash
	@@use
		time	10m
		scale	��
		action	���т�
		name	���т�
		info	�F������߂ēX�͂𓪂��痁�тĂ݂܂�
		arg		nocount
			use		500	�X��
		func	_local_
			my $ret='�F�肪�ʂ��ēX�͂��s�v�c�ȗ͂𔭊������悤�ł�';

			if ((rand(1000)<20) && !$DT->{item}[@@ITEMNO"�I���W�i�����ǂ񃌃V�s"-1])
			{
				AddItem(@@ITEMNO"�I���W�i�����ǂ񃌃V�s",1,"�˕��Ŕ��ł������؂���悭����ƁC�Ȃ�ƁI�ǂ����̓X�́u�I���W�i�����ǂ񃌃V�s�v�ł���");
				WriteLog(0,$DT->{id},'�I���W�i�����ǂ񃌃V�s����ɓ���܂���');
			}
			elsif((rand(1000)<20) && !$DT->{item}[@@ITEMNO"�I���W�i�����΃��V�s"-1])
			{
				AddItem(@@ITEMNO"�I���W�i�����΃��V�s",1,"�˕��Ŕ��ł������؂���悭����ƁC�Ȃ�ƁI�ǂ����̓X�́u�I���W�i�����΃��V�s�v�ł���");
				WriteLog(0,$DT->{id},'�I���W�i�����΃��V�s����ɓ���܂���');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"��"-1]<=10))
			{
				AddItem(@@ITEMNO"��",10,"�쐶�̓؏W�c���X�ɔ�э���ł��܂���");
				WriteLog(0,$DT->{id},'�؂���ɓ���܂���');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"�����傤"-1]<=10))
			{
				AddItem(@@ITEMNO"�����傤",10,"�쐶�̂����傤�W�c���X�ɔ�э���ł��܂���");
				WriteLog(0,$DT->{id},'�����傤����ɓ���܂���');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"�Ƃ����炵"-1]<=500))
			{
				AddItem(@@ITEMNO"�Ƃ����炵",500,"�����e�ʂ���Ƃ����炵�̏�������Ă��܂���");
				WriteLog(0,$DT->{id},'�Ƃ����炵����ɓ���܂���');
			}
			elsif((rand(1000)<100) && $DT->{item}[@@ITEMNO"�ɂ�Ƃ�"-1] && ($DT->{item}[@@ITEMNO"��"-1]<=2700))
			{
				AddItem(@@ITEMNO"��",$DT->{item}[@@ITEMNO"�ɂ�Ƃ�"-1]*10,"�����Ă���ɂ�Ƃ肪��Ăɗ���10���Y�݂܂���");
				WriteLog(0,$DT->{id},'������ɓ���܂���');
			}
			elsif((rand(1000)<100) && $DT->{item}[@@ITEMNO"��"-1] && ($DT->{item}[@@ITEMNO"�g�����t"-1]<=50))
			{
				AddItem(@@ITEMNO"�g�����t",$DT->{item}[@@ITEMNO"��"-1]*5,"�����Ă���؂��F�C�g�����t��5�����킦�Ă��܂���");
				WriteLog(0,$DT->{id},'�g�����t����ɓ���܂���');
			}
			elsif ((rand(1000)<100) && ($DT->{item}[@@ITEMNO"�u���b�N�H���"-1]<2))
			{
				AddItem(@@ITEMNO"�u���b�N�H���",1,"�u���b�N�H�������������X�ɓ����Ă��āC�ق��Ăق����ƌ����܂���");
				WriteLog(0,$DT->{id},'�u���b�N�H�������ɓ���܂���');
			}
			elsif((rand(1000)<20) && $DT->{user}->{udon} && ($DT->{user}->{udon}ne'�g���k�����ǂ�') && ($DT->{user}->{udon}ne'�n�C�p�[�O���[�g�t�c�n�m'))
			{
				if (rand(1000)<500)
				{
					$ret.='<br>�ˑR�Ђ�߂��āC�J�������I���W�i�����ǂ�̖��O���u�g���k�����ǂ�v�ɕς��܂���<br>';
					$DT->{user}->{udon}='�g���k�����ǂ�';
				}
				else
				{
					$ret.='<br>�ˑR�Ђ�߂��āC�J�������I���W�i�����ǂ�̖��O���u�n�C�p�[�O���[�g�t�c�n�m�v�ɕς��܂���<br>';
					$DT->{user}->{udon}='�n�C�p�[�O���[�g�t�c�n�m';
				}
				WriteLog(0,$DT->{id},'�I���W�i�����ǂ�̖��O��ύX���܂���');
				WriteLog(3,0,$DT->{shopname}.'�̓X�傪�X�͂𗁂тĂЂ�߂��C�I���W�i�����ǂ�̖��O��ύX�����悤�ł�');
			}
			elsif((rand(1000)<20) && $DT->{user}->{soba} && ($DT->{user}->{soba}ne'���̕n�R�E�o����') && ($DT->{user}->{soba}ne'�ʂ��Ђ��\�o'))
			{
				if (rand(1000)<500)
				{
					$ret.='<br>�ˑR�Ђ�߂��āC�J�������I���W�i�����΂̖��O���u���̕n�R�E�o���΁v�ɕς��܂���<br>';
					$DT->{user}->{soba}='���̕n�R�E�o����';
				}
				else
				{
					$ret.='<br>�ˑR�Ђ�߂��āC�J�������I���W�i�����΂̖��O���u�ʂ��Ђ��\�o�v�ɕς��܂���<br>';
					$DT->{user}->{soba}='�ʂ��Ђ��\�o';
				}
				WriteLog(0,$DT->{id},'�I���W�i�����΂̖��O��ύX���܂���');
				WriteLog(3,0,$DT->{shopname}.'�̓X�傪�X�͂𗁂тĂЂ�߂��C�I���W�i�����΂̖��O��ύX�����悤�ł�');
			}
			else
			{
				$ret.='<br>�X�͂ɂ���Ď��̃G�l���M�[����������C�����ł��鎞�Ԃ������܂���';
				my $cnt=int(rand(6))+5;
				$DT->{time}-=3600*($cnt);
				$ret.='�i�{'.($cnt).'���ԁj<br>';
				WriteLog(0,$DT->{id},'�X�͂𓪂��痁�т����ʁC�������Ԃ������܂���');
			}
			return $ret;
		_local_

@@ITEM
	no		59
	type	�c�[��
	code	tool-huku
	name	�������⏕��
	info	5����1�񒊑I���ł��܂�
	scale	��
	price	0
	limit	1000/0
	pop		0
	@@USE
		time	5m
		action	������������
		name	������������
		info	�W�߂��������⏕���ŕ����������܂�
		scale	��
			use		5	�������⏕��
		func	_local_
			# ��������
			my $ret;
			my $hit1=0; #��ɓ�������i�i�̌�
			my $hit2=0; #��ɓ���1���i�i�̌�
			my $hit3=0; #��ɓ���2���i�i�̌�
			my $hit4=0; #��ɓ���3���i�i�̌�
			my $hit5=0; #��ɓ���4���i�i�̌�
			my $hit6=0; #��ɓ���5���i�i�̌�
			my $hit7=0; #��ɓ���c�O�܂̌�

			foreach(1..$count)
			{
				if(rand(1000)<1)
				{
					$hit1+=1;
				}
				elsif(rand(1000)<3)
				{
					$hit2+=1;
				}
				elsif(rand(1000)<10)
				{
					$hit3+=1;
				}
				elsif(rand(1000)<50)
				{
					$hit4+=1;
				}
				elsif(rand(1000)<100)
				{
					$hit5+=1;
				}
				elsif(rand(1000)<200)
				{
					$hit6+=1;
				}
			}
			$hit7=$count-($hit1+$hit2+$hit3+$hit4+$hit5+$hit6);
			AddItem(83,$hit1,'�Ȃ�ƁI�����̋��̏����L��'.$hit1.'�񓖂���܂���') if ($hit1>=1);
			AddItem(82,$hit2,'�Ȃ�ƁI1���̎����Ԃ�'.$hit2.'�񓖂���܂���') if ($hit2>=1);
			AddItem(80,$hit3,'2���̐H��􂢋@��'.$hit3.'�񓖂���܂���') if ($hit3>=1);
			AddItem(79,$hit4,'3���̎��]�Ԃ�'.$hit4.'�񓖂���܂���') if ($hit4>=1);
			AddItem(67,$hit5,'4���̃q���g�u�b�N��'.$hit5.'�񓖂���܂���') if ($hit5>=1);
			AddItem(66,$hit6,'5���̏��i����'.$hit6.'�񓖂���܂���') if ($hit6>=1);
			AddItem(64,$hit7,'�c�O�܂̂��ꂢ�Ș���'.$hit7.'�񕪂ł�') if ($hit7>=1);
			$ret='�������͂͂���܂���';
			$ret='�������Ōi�i�𓖂Ă܂���' if ($hit7<$count);
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_

@@ITEM
	no		60
	type	�c�[��
	code	tool-udon
	name	�I���W�i�����ǂ񃌃V�s
	info	�I���W�i�����ǂ�̍����������Ă���܂�
	scale	��
	price	0
	limit	1/0
	pop		0
	@@USE
		time	1m
		action	����
		name	���V�s������
		info	�I���W�i�����ǂ�̍ޗ��ƍ�����Y�ꂽ�Ƃ��̂��߂�
		scale	��
		arg		nocount
		ngmsg	�y�I���W�i�����ǂ�̍����z<br>�ޗ�<br>�E������<br>�E����<br>�E�����傤<br>�E�Ƃ����炵<br>�E���ꂢ�Ș�<br><br>����<br><b>�@�@�閧</b>
	@@USE
		time	4h
		job		���ǂ�	times/job_udon_time_rate
		action	�Ƃ������O�ɕς���
		name	�I���W�i�����ǂ�̖��O��ς���
		info	�I���W�i�����ǂ�̖��O��ύX���܂�
		arg		nocount|message30
		func	_local_
			# �I���W�i�����ǂ�̖��O��ς���
			main::OutError('�܂��I���W�i�����ǂ���J�����Ă�������') if !$DT->{user}->{udon};
			main::OutError('���O�����Ă�������') if !$USE->{arg}->{message};
			my $ret;
			$ret='�I���W�i�����ǂ�̖��O���y'.$USE->{arg}->{message}.'�z�ɕύX���܂���';	
			WriteLog(3,0,$DT->{shopname}."���I���W�i�����ǂ�̖��O��ς����悤�ł�");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{udon}=$USE->{arg}->{message};
			return $ret;
		_local_

@@ITEM
	no		61
	type	�c�[��
	code	tool-soba
	name	�I���W�i�����΃��V�s
	info	�I���W�i�����΂̍����������Ă���܂�
	scale	��
	price	0
	limit	1/0
	pop		0
	@@USE
		time	1m
		action	����
		name	���V�s������
		info	�I���W�i�����΂̍ޗ��ƍ�����Y�ꂽ�Ƃ��̂��߂�
		scale	��
		arg		nocount
		ngmsg	�y�I���W�i�����΂̍����z<br>�ޗ�<br>�E���Ε�<br>�E����<br>�E���傤����<br>�E���܂�<br>�E���ꂢ�Ș�<br><br>����<br><b>�@�@�閧</b>
	@@USE
		time	4h
		job		���Ή�	times/job_soba_time_rate
		action	�Ƃ������O�ɕς���
		name	�I���W�i�����΂̖��O��ς���
		info	�I���W�i�����΂̖��O��ύX���܂�
		arg		nocount|message30
		func	_local_
			main::OutError('�܂��I���W�i�����΂��J�����Ă�������') if !$DT->{user}->{soba};
			main::OutError('���O�����Ă�������') if !$USE->{arg}->{message};
			my $ret;
			$ret='�I���W�i�����΂̖��O���y'.$USE->{arg}->{message}.'�z�ɕύX���܂���';	
			WriteLog(3,0,$DT->{shopname}."���I���W�i�����΂̖��O��ς����悤�ł�");
			WriteLog(0,$DT->{id},$ret);
			$DT->{user}->{soba}=$USE->{arg}->{message};
			return $ret;
		_local_

@@ITEM
	no		62
	type	�c�[��
	code	tool-taihi
	name	�͔�
	info	���̔엿�ł�
	scale	kg
	price	5
	cost	0
	limit	5000/1000
	base	100/20000
	plus	20m
	pop		20m
	point	10%

@@ITEM
	no		63
	type	�c�[��
	code	tool-yogore
	name	���ꂽ��
	info	�g������̘��ł�
	scale	��
	price	10
	cost	0
	limit	10000/0
	pop		0

@@ITEM
	no		64
	type	�c�[��
	code	tool-kirei
	name	���ꂢ�Ș�
	info	���ꂢ�ɐ�������ł�
	scale	��
	price	50
	cost	10
	limit	3000/2000
	base	10000/100000
	plus	1h
	pop	10d

@@ITEM
	no		65
	type	�c�[��
	code	tool-takara
	name	�󂭂�
	info	�ꝺ����𖲌��ād
	scale	��
	price	1000
	cost	10
	limit	100/20
	plus	3h
	pop		2h
	flag	noshowcase|norequest

@@ITEM
	no		66
	type	�c�[��
	code	tool-syou
	name	���i��
	info	��]�̏��i�ƌ����ł��܂�
	scale	��
	price	5000
	cost	10
	limit	500/0
	pop		0
	@@USE
		time	10m
		action	��������
		scale	��
		name	�͔�ƌ�������
		info	���i������]�̏��i�ƌ������܂�
		okmsg	�͔����ɓ���܂���
			use		1	���i��
			get		250	�͔�
	@@USE
		time	10m
		action	��������
		scale	��
		name	���ꂢ�Ș��ƌ�������
		info	���i������]�̏��i�ƌ������܂�
		okmsg	���ꂢ�Ș�����ɓ���܂���
			use		1	���i��
			get		100	���ꂢ�Ș�
	@@USE
		time	10m
		action	��������
		scale	��
		name	�q���g�u�b�N�ƌ�������
		info	���i������]�̏��i�ƌ������܂�
		okmsg	�q���g�u�b�N����ɓ���܂���
			use		2	���i��
			get		1	�q���g�u�b�N
	@@USE
		time	10m
		action	��������
		scale	��
		name	�x��@�ƌ�������
		info	���i������]�̏��i�ƌ������܂�
		okmsg	�x��@����ɓ���܂���
			use		40	���i��
			get		1	�x��@
	@@USE
		time	10m
		action	��������
		scale	��
		name	�����Ԃƌ�������
		info	���i������]�̏��i�ƌ������܂�
		okmsg	�����Ԃ���ɓ���܂���
			use		100	���i��
			get		1	������
	@@USE
		time	10m
		action	��������
		scale	��
		name	���̏����L�ƌ�������
		info	���i������]�̏��i�ƌ������܂�
		okmsg	���̏����L����ɓ���܂���
			use		200	���i��
			get		1	���̏����L
	@@use
		time	10m
		scale	��
		action	��������
		name	��������
		info	���i���������V���b�v�Ɉ�������Ă��炢�܂�
		param	500,2500
			use		1	���i��
		func	_local_
			my $ret;
			if (rand(1000)<300)
			{
				$DT->{money}+=$USE->{param1}*$count;
				$ret='�����V���b�v�̂��₶�ɔ����������ꂽ�悤�ł�<br>';
				$ret.=GetMoneyString($USE->{param1}*$count).'�ň�������Ă��炢�܂���';
			}
			else
			{
			$DT->{money}+=$USE->{param2}*$count;
			$ret=GetMoneyString($USE->{param2}*$count).'�ň�������Ă��炢�܂���';
			}
			WriteLog(0,$DT->{id},"���i�����������܂���");
			return $ret;
		_local_

@@ITEM
	no		67
	type	�c�[��
	code	tool-hint
	name	�q���g�u�b�N
	info	<b>���ӁI����̃q���g��ǂނƃq���g�u�b�N�����ł��܂�</b>
	scale	��
	price	10000
	cost	10
	limit	5/0
	pop		0
	flag	noshowcase|norequest
	@@USE
		time	1m
		action	�q���g��ǂ�
		name	���߂Ă̕���
		info	�܂�����������悢�̂��킩��Ȃ��ꍇ�̃q���g�ł�
		arg		nocount
		ngmsg	�i�u�}���فv�����Ă���j<br><br>�_�v�����t��1�l�C�s�ꂩ���ꂩ��w�����Ă݂܂��傤�B<br>�i�ǂ�����Ȃ��ꍇ�́C�t���[�^�[�𔃂��Ĕ_�v�����t�ɂ��Ă��������j<br>���t�̏ꍇ�͂����ɒނ肪�n�߂��܂��B<br>�_�v�͔�����ɓ����ƁC���n�����邱�Ƃ��ł���悤�ɂȂ�܂��B<br>���n�������́u�k���O�̔��v�ɖ߂�C1���ɂ��͔�100kg��<br>�u�悭�k�������v�ɂ��邱�Ƃ��ł��C����ɂ�����x�̎��Ԍo�߂ɂ����<br>�����u���n��҂��v�ɕω����܂��B
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	���t���[�^�[�̔閧
		info	�l�ޔh���Ƃ��ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E���ǂ�E�l�̏C�s������ɂ́C�t���[�^�[�Ə��������K�v�ł��B<br>�E���ΐE�l�̏C�s������ɂ́C�t���[�^�[�Ƃ��Ε����K�v�ł��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	���_�v�̔閧
		info	�_�Ƃ��ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E�G�T�œ�������Ă܂��傤�B�ɂ�Ƃ�Ƃ����傤�̃G�T�͂Ƃ����낱���C�؂̃G�T�͑哤�ł��B<br>�E��������������Ƃ��́C�ɂ�Ƃ�̐e���ɗ���������C�z�������邱�Ƃ��ł��܂��B<br>�i�z����҂��́C���Ԃ��o�߂���Ə����e���ɂȂ�܂��j<br>�E�ɂ�Ƃ���g�p����ƁC�����傤��؂Ǝ�肩���邱�Ƃ��ł��܂��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	�����t�̔閧
		info	���Ƃ��ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E���т���������p�ӂ���ƁC���ɏo����悤�ɂȂ�܂��B<br>�E�����Ƃ�����ƁC�Ƃ����炵����������΁C�h�q�߂񂽂������܂��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	���V�Ղ�E�l�̔閧
		info	�V�Ղ牮���ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E�哤������g������邱�Ƃ��ł��܂��B<br>�E�����Ƃ����炩�炩�܂ڂ������܂��B<br>�E��������ۓV�����܂��B<br>�E���тƏ������C����p�ӂ���΁C���ѓV����邱�Ƃ��ł��܂��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	�����ǂ�E�l�̔閧
		info	���ǂ񉮂��ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E��邱�Ƃ̂ł��邤�ǂ�́C�W�����i�̈������Ɂu�����ǂ�v�u�킩�߂��ǂ�v�u���˂��ǂ�v<br>�u�ۓV���ǂ�v�u���ѓV���ǂ�v�u���ǂ�O���v�u�L���r�A���ǂ�v�u�g�����t���ǂ�v�u�t�H�A�O�����ǂ�v<br>�u�������ǂ�v�u�I���W�i�����ǂ�v��11��ނł��B<br>�E�����ǂ�̍ޗ��́C�������Ƃ˂��C���܂ڂ��Ƃ��ꂢ�Ș��ł��i���ǂ���̊�{�j�B<br>�E���ǂ�O���͓���̂��ǂ�3��ނ��C�Z�b�g�ɂ��邱�Ƃɂ���č��܂��B<br>�E�����Ȃ��ǂ�ɂ͂������K�v�Ȃ��̂������ł��B<br>�E�������ǂ�͓؍����ŁC���锎�������̊C�Y�����H�i���̂��Ă��܂��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	�����ΐE�l�̔閧
		info	���Ή����ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E��邱�Ƃ̂ł��邻�΂́C�W�����i�̈������Ɂu�������΁v�u�킩�߂��΁v�u���˂��΁v<br>�u�ۓV���΁v�u���ѓV���΁v�u���ΎO���v�u�L���r�A���΁v�u�g�����t���΁v�u�t�H�A�O�����΁v<br>�u�������΁v�u�I���W�i�����΁v��11��ނł��B<br>�E�������΂̍ޗ��́C���Ε��Ƃ˂��C���܂ڂ��Ƃ��ꂢ�Ș��ł��i���΍��̊�{�j�B<br>�E���ΎO���͓���̂���3��ނ��C�Z�b�g�ɂ��邱�Ƃɂ���č��܂��B<br>�E�����Ȃ��΂ɂ͂������K�v�Ȃ��̂������ł��B<br>�E�������΂͓؍����ŁC���锎�������̊C�Y�����H�i���̂��Ă��܂��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	���֗����̔閧
		info	�l�ޔh���Ƃ��ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E�t���[�^�[���l�ޔh���̐��ƂɂȂ邱�Ƃɂ���āC�֗����̊e���Ǝ��Ԃ��Z���Ȃ�܂��B<br>�E�H��􂢋@����ɓ����ƁC�Z�����Ԃł�������̉��ꂽ�����􂦂�悤�ɂȂ�܂��B<br>�E���E�̊Ŕ����낷�ƁC���X���ԘJ�����x������܂��B
			use		1	�q���g�u�b�N
	@@USE
		time	10m
		action	�q���g��ǂ�
		name	���u���b�N�H����̔閧
		info	���ƋƂ��ɂ߂Ă݂�������
		arg		nocount
		ngmsg	�E���ꂽ����������x����ƁC�ł��ǂ�ƈł��΂���邱�Ƃ��ł��܂��B<br>�E�ł��ǂ�ƈł��΂��������񑵂��Ă���Ƃ��ɁC�X�͂���������΁C����ւ��������s�ł��܂��B<br>�E�����\�𗬂����߂ɂ́C�X�͂�100�K�v�ł��B<br>�E�u���b�N�H�����2�l���āC����ɓX�͂�100����Ǝ��ԑ�����s�����Ƃ��ł��܂��B<br>�i���ԑ���ɂ���āC�������Ԃ������_���ɑ������܂��j
			use		1	�q���g�u�b�N
	@@USE
		time	1m
		action	�q���g��ǂ�
		name	��I�ɂ���
		info	��I�̑����z�ƈێ���ɂ��Ă̐����ł�
		arg		nocount
		ngmsg	��I�̐���ς���ɂ́C�֗������g���܂��B<br>�������C�֗���1�l�ł͒�I���Q�܂ł������₷���Ƃ��ł����C<br>����ȏ㑝�₵�����Ƃ��ɂ́C�֗����̐��������ƕK�v�ł��B<br>��I�̈ێ���́C�I��������Ǝ���ɂ�����悤�ɂȂ��Ă��܂��B
	@@USE
		time	1m
		action	�q���g��ǂ�
		name	�X�͂ɂ���
		info	�X�͂Ɋւ�������ł�
		arg		nocount
		ngmsg	�X�́i�݂�������j�Ƃ́C���Y�I�ȍs�����Ƃ�����<br>���ǂ�₻�΂�H�ׂ邱�Ƃɂ���Ď�ɂ͂�����̂�<br>�u���b�N�H�������̏����L�ɂ���āC���̗͂��g�p���邱�Ƃ��ł��܂��B
	@@USE
		time	1m
		action	�q���g��ǂ�
		name	�I���W�i�����ǂ�i���΁j�ɂ���
		info	�I���W�i�����ǂ�i���΁j�̍����̐����ł�
		arg		nocount
		ngmsg	���ǂ�i���΁j�O���ƃI���W�i�����ǂ�i���΁j�������S��ނ̂��ǂ�i���΁j��1�t���p�ӂ���ƁC<br>���ǂ�i���΁j�E�l�̓I���W�i�����ǂ�i���΁j���J�����邱�Ƃ��ł���悤�ɂȂ�܂��B<br>�I���W�i�����ǂ�i���΁j�ɂ́C�D���Ȗ��O��t�����܂��B<br>���̖��O�̓V���E�E�C���h�E�i��I1�j�Ŕ̔������Ƃ��ɁC�����L���O���ɕ\������܂��B
	@@USE
		time	1m
		action	�q���g��ǂ�
		name	���ꂽ���ɂ���
		info	���ꂽ���ɂ��Ă̐����ł�
		arg		nocount
		ngmsg	���ǂ�₻�΂������ƁC���ꂽ�����q�ɂɂ��܂��Ă��܂��B<br>�i���X�܂��甃��ꂽ�Ƃ��ɂ́C���͖߂��Ă��܂���j<br>�������C�ł��ǂ�ƈł��΂͗�O��<br>��ʎs�����u�܁C�܂����I�v�Ɠ{���������C����@�������Ă��܂��̂ł��B
	@@USE
		time	1m
		action	�q���g��ǂ�
		name	�q���g�u�b�N�ɂ���
		info	�q���g�u�b�N�̎�ɓ�����Ɋւ�������ł�
		arg		nocount
		ngmsg	�q���g�u�b�N�́C���i���ƌ����ł��܂��B<br>���i���͌��Z���̏ܕi�Ƃ��Ă��炦�邱�Ƃ�����܂��B<br>�܂��C�q���g�u�b�N�͕������̌i�i�œ����邱�Ƃ�����܂��B<br>�������⏕���́C�s��Ŕ�����������Ƃ��炦�邱�Ƃ�����܂��B
	@@use
		time	10m
		scale	��
		action	��������
		name	��������
		info	�q���g�u�b�N�������V���b�v�Ɉ�������Ă��炢�܂�
		param	1000,5000
			use		1	�q���g�u�b�N
		func	_local_
			my $ret;
			if (rand(1000)<300)
			{
				$DT->{money}+=$USE->{param1}*$count;
				$ret='�����V���b�v�̂��₶�ɔ����������ꂽ�悤�ł�<br>';
				$ret.=GetMoneyString($USE->{param1}*$count).'�ň�������Ă��炢�܂���';
			}
			else
			{
			$DT->{money}+=$USE->{param2}*$count;
			$ret=GetMoneyString($USE->{param2}*$count).'�ň�������Ă��炢�܂���';
			}
			WriteLog(0,$DT->{id},"�q���g�u�b�N���������܂���");
			return $ret;
		_local_

@@ITEM
	no		68
	type	�c�[��
	code	tool-paintr
	name	�Ԃ̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		69
	type	�c�[��
	code	tool-paintb
	name	�̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		70
	type	�c�[��
	code	tool-painto
	name	�I�����W�̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		71
	type	�c�[��
	code	tool-painty
	name	���F�̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		72
	type	�c�[��
	code	tool-paintg
	name	�΂̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		73
	type	�c�[��
	code	tool-paintp
	name	�s���N�̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		74
	type	�c�[��
	code	tool-painte
	name	���̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		75
	type	�c�[��
	code	tool-paintk
	name	���̓h��
	info	�i�g�p�ł��Ȃ��A�C�e���ł��B�j�����Ă��������j
	scale	��
	price	10000
	cost	100
	limit	1/0
	pop	1d

@@ITEM
	no		76
	type	�c�[��
	code	tool-hatakea
	name	�k���O�̔�
	info	�엿�������Ղ�^���܂��傤
	scale	��
	price	5000
	limit	40/2
	plus	1d
	pop		2d
	flag	noshowcase|onlysend

@@ITEM
	no		77
	type	�c�[��
	code	tool-hatakeb
	name	�悭�k������
	info	���΂炭����Ǝ��n�ł���悤�ɂȂ�܂�
	scale	��
	price	10000
	limit	20/0
	pop		1d
	flag	noshowcase|onlysend
	funct	_local_
		my($ITEM,@DT)=@_;
		my $birth_per_day=40;  # 1���Ɏ��n��҂���40�ɂȂ�m���̐ݒ�
		my $val          =1;  # ��x�Ɏ��n��҂��ɂȂ��{��
		
		my $birth_rate=$birth_per_day && (86400/$birth_per_day); # 0�Ŋ���̂�j�~
		foreach my $DT (@DT)
		{
			next if !$DT->{item}[@@ITEMNO"�悭�k������"-1];
			if(rand($birth_rate)<$TIMESPAN) # 1�X�܂ɂ��u1����$birth_per_day��v�̊m���ŏ������^�ɂȂ�(�n�Y�c)
			{
				UseItemSub(@@ITEMNO"�悭�k������",$val,$DT);
				AddItemSub(@@ITEMNO"���n��҂�",$val,$DT);
			}
		}
	_local_ 

@@ITEM
	no		78
	type	�c�[��
	code	tool-hatakec
	name	���n��҂�
	info	���낢��Ȏ��n�������҂ł������ł�
	scale	��
	price	20000
	limit	20/0
	pop		1d
	flag	noshowcase|onlysend

@@ITEM
	no		79
	type	�c�[��
	code	tool-ziten
	name	���]��
	info	��������������Ɗy�ɂȂ�܂�
	scale	��
	price	30000
	cost	1000
	limit	1/0.5
	plus	10d
	pop		3d
	flag	noshowcase|onlysend

@@ITEM
	no		80
	type	�c�[��
	code	tool-syokki
	name	�H��􂢋@
	info	�H��􂢂��葁���ł��܂�
	scale	��
	price	100000
	cost	3000
	limit	1/0.8
	plus	10d
	pop		10d
	flag	noshowcase|onlysend

@@ITEM
	no		81
	type	�c�[��
	code	tool-keihou
	name	�x��@
	info	�X�̈��S�΍�Ɂd
	scale	��
	price	200000
	cost	5000
	limit	1/0.5
	plus	10d
	pop		20d
	flag	noshowcase|onlysend

@@ITEM
	no		82
	type	�c�[��
	code	tool-kuruma
	name	������
	info	�����������Ȃ�y�ɂȂ�܂�
	scale	��
	price	500000
	cost	5000
	limit	1/0.3
	plus	10d
	pop	30d
	flag	noshowcase|onlysend

@@ITEM
	no		83
	type	�c�[��
	code	tool-neko
	name	���̏����L
	info	�X�̎��_�ł�
	scale	��
	price	1000000
	cost	1000
	limit	1/0.2
	plus	10d
	pop		50d
	flag	noshowcase|onlysend
	@@use
		time	3m
		scale	��
		action	�q��
		name	�q��
		info	�����ɐ�������āC���̏����L��q�݂܂�
			use		1	�X��
		func	_local_
			my $val=$count;
			my $ret="";
			
			if($count>=50)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'�̓X�傪�C�������āC�~�}�Ԃŉ^�΂�܂����B');
				WriteLog(2,0,'��x��'.$count.'������̏����L��q�ނȂ�āC���C�̍����ł͂���܂���B');
				$ret="�d�C���t������a�@�̃x�b�h�̏�ł���";
			}
			elsif($count>=20)
			{
				$ret='�n�����N�����Ă��܂��܂����@��x��'.$count.'��͔q�݉߂��ł��B';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='���̏����L��q��ŁC�����������������ɂ����C�����܂����B';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_

@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto
	startfunc	loto
	info		�󂭂����I

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		luckyneko
	info		���̏����L�̏��^
	startfunc	_local_(200)
		my($hitproba)=@_;
		
		foreach my $DT (@main'DT)
		{
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"���̏����L")
			{			
			if ($DT->{item}[@@ITEMNO"���̏����L"-1])
			{
				$DT->{item}[@@ITEMNO"���̏����L"-1]=0;
				my $up=int(1000*(2-$DT->{rank}/5000));
				$DT->{rank}+=$up;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				WriteLog(2,0,$DT->{shopname}."�̋��̏����L���C���X�ɍK�^�������炵�V�ɏ����Ă����܂����B");
				WriteLog(0,$DT->{id},"���̏����L�̕s�v�c�ȗ͂ŁC���X�̐l�C��".int($up/100)."%�オ��܂���");			}
			}		
			}
		}
		return 0;
	_local_

@@EVENT
	start		100%
	basetime	0h
	plustime	0h
	code		yogoredon
	info		���ꂽ���̈��L
	startfunc	_local_(500)
		my($hitproba)=@_;
		
		foreach my $DT (@main'DT)
		{
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"���ꂽ��")
			{			
			if ($DT->{item}[@@ITEMNO"���ꂽ��"-1]>=1000)
			{
				my $down=int($DT->{rank}/5);
				$DT->{rank}-=$down;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}."�ɂ��܂��Ă��鉘�ꂽ�����爫�L���������C�X�̐l�C��������܂����B");
				WriteLog(0,$DT->{id},"���ꂽ���̂����ŁC���X�̐l�C��".int($down/100)."%������܂���");			}
			}		
			}
		}
		return 0;
	_local_

# �I���W�i�����ǂ�Ől�C�A�b�v
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		udonpop
	info		�I���W�i�����ǂ�l�C����
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if rand(1000)>200;
			if ($_->{user}->{udon}&&($_->{user}->{udon} ne 'n'))
			{
			my $up=int(300*(2-$_->{rank}/5000));
			$_->{rank}+=$up;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'�������ǂ�u'.$_->{user}->{udon}.'�v���J�ŉ\�ɂȂ�C�X�̑O�͊��҂ɋ���c��܂����q�ł����ς��ł��B') ;
			}
		}
		return 0;
	_local_

# �I���W�i�����΂Ől�C�A�b�v
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		sobapop
	info		�I���W�i�����ΐl�C����
	startfunc	_local_
		foreach(reverse(@DT))
		{
			next if rand(1000)>200;
			if ($_->{user}->{soba}&&($_->{user}->{soba} ne 'n'))
			{
			my $up=int(300*(2-$_->{rank}/5000));
			$_->{rank}+=$up;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'�������΁u'.$_->{user}->{soba}.'�v���l�C�������C�\�𕷂������q���X�̑O�ɍs��������Ă��܂��B') ;
			}
		}
		return 0;
	_local_

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		syokkiarai
	info		�H��􂢋@�̎���
	startfunc	_local_(100)
		my($hitproba)=@_;
		
		foreach my $DT (@DT)
		{			
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"�H��􂢋@")
			{
				if ($DT->{item}[@@ITEMNO"�H��􂢋@"-1]==1)					{
				$DT->{item}[@@ITEMNO"�H��􂢋@"-1]=0;
				WriteLog(2,0,$DT->{shopname}."�̐H��􂢋@���̏Ⴕ���悤�ł��B");
				WriteLog(0,$DT->{id},"�̏Ⴕ���H��􂢋@��p�����܂���");
				}
			}
			}
		}
		return 0;
	_local_

@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		haisya
	info		�p��
	startfunc	_local_(100)
		my($hitproba)=@_;
		
		foreach my $DT (@DT)
		{			
			next if rand(1000)>$hitproba;
			{
			foreach my $itemno (@@ITEMNO"������")
			{
				if ($DT->{item}[@@ITEMNO"������"-1]==1)	{
				$DT->{item}[@@ITEMNO"������"-1]=0;
				WriteLog(2,0,$DT->{shopname}."���̏�̑��������Ԃ�p�Ԃ����悤�ł��B");
				WriteLog(0,$DT->{id},"�����Ԃ�p�Ԃ��܂���");
				}
			}
			}
		}
		return 0;
	_local_

#�j���C�x���g��唄��o���C�x���g�ɕύX
@@event
	start		20%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	���X�X�̑唄��o�����n�܂�܂����B
	endmsg		�唄��o�����I���܂����B
	info		�唄��o���ŏ��X�X�͊��C�ɂ��ӂ�Ă��܂��B
	func		_local_
		my $time=$TIMESPAN;
		$time=10*3600 if $time>10*3600; # �ő�10%����
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		udon-boom
	startmsg	�J�ł͂��ǂ񂪃u�[���̂悤�ł��B
	endmsg		���ǂ�u�[�����I���܂����B
	info		���ǂ�̐l�C�����܂��Ă��܂��B
		param	�����ǂ�			pop/1.5
		param	�킩�߂��ǂ�			pop/1.5
		param	���˂��ǂ�			pop/1.5
		param	�ۓV���ǂ�			pop/1.5
		param	���ѓV���ǂ�			pop/2
		param	���ǂ�O��			pop/2
		param	�L���r�A���ǂ�			pop/2
		param	�g�����t���ǂ�			pop/2
		param	�t�H�A�O�����ǂ�		pop/2
		param	�������ǂ�			pop/2
		param	�I���W�i�����ǂ�		pop/2

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		soba-boom
	startmsg	�J�ł͂��΂��u�[���̂悤�ł��B
	endmsg		���΃u�[�����I���܂����B
	info		���΂̐l�C�����܂��Ă��܂��B
		param	��������			pop/1.5
		param	�킩�߂���			pop/1.5
		param	���˂���			pop/1.5
		param	�ۓV����			pop/1.5
		param	���ѓV����			pop/2
		param	���ΎO��			pop/2
		param	�L���r�A����			pop/2
		param	�g�����t����			pop/2
		param	�t�H�A�O������			pop/2
		param	��������			pop/2
		param	�I���W�i������			pop/2

@@EVENT
	start		5%
	basetime	9h
	plustime	16h
	code		plusup-katuo
	group		sui
	startmsg	�������L���ł��B
	endmsg		�����̗��ʂ�����ɖ߂�܂����B
	info		�����̗��ʗʂ������Ă��܂��B
		param	����				plus=300

@@EVENT
	start		1%
	basetime	6h
	plustime	18h
	code		plusup-tyouzame
	group		sui
	startmsg	���傤���߂̑�Q���l�ɂ����񂹂܂����B
	endmsg		���傤���߂̗��ʂ�����ɖ߂�܂����B
	info		���傤���߂̗��ʗʂ������Ă��܂��B
		param	���傤����			plus=500

# �᎑���D��ŃM���h�������X�Ɏ��������C�x���g
@@EVENT
	start		30%
	code		getmoney
	info		��������
	startfunc	_local_(100000)
		my($money)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;

			if ($_->{guild} eq '')
			{
			$_->{money}+=$money;
			$_->{money}=$main::MAX_MONEY if $_->{money}>$main::MAX_MONEY;
			return (0,"���X���".$_->{shopname}.'��'.GetMoneyString($money).'�̕⏕�����x������܂���');
			}
		}
		return 0;
	_local_

# ��ʗD��Ŗ������C�x���g
@@EVENT
	start		100% #old50%
	basetime	0h		#�������n�̃C�x���g�ł͂Ȃ��̂Ŏ��Ԃ�0�B
	plustime	0h
	code		manbiki
	info		������
	startfunc	_local_(400,200)
		#�����͂��̊֐����C�x���g�̖{�̂ɂȂ��Ă�
		my($hitproba,$breakproba)=@_;
		#�_����m��,���{�b�g�j��m��
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"�x��@"-1])
			{
				return (0,$DT->{shopname}.'�֖�����������܂������j�~����܂����B') if rand(1000)>$breakproba;
				
				$DT->{item}[@@ITEMNO"�x��@"-1]--;
				return (0,$DT->{shopname}.'�֖�����������C'.$ITEM[@@ITEMNO"�x��@"]->{name}.'���j�󂳂�܂����B');
			}
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/10);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'�����z'.GetMoneyString($count).'�����̖�������Q�ɑ����܂����B') if $count;
			return (0,$DT->{shopname}.'�ɓ������������Ƃ́C������炸�ɓ����܂����B');
		}
		return 0;
	_local_

@@EVENT
	start		30% #old15%
	basetime	0h
	plustime	0h
	code		goutou
	info		����
	startfunc	_local_(700)
		#�����͂��̊֐����C�x���g�̖{�̂ɂȂ��Ă�
		my($hitproba)=@_;
		#�_����m��
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"�x��@"-1])
			{
				$DT->{item}[@@ITEMNO"�x��@"-1]--;
				return (0,$DT->{shopname}.'�֋���������C'.$ITEM[@@ITEMNO"�x��@"]->{name}.'���j�󂳂�܂����B');
			}
			
			$DT->{rank}-=int($DT->{rank}/5);
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/4);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'�����z'.GetMoneyString($count).'�����̋�����Q�ɑ����܂����B') if $count;
			return (0,$DT->{shopname}.'�ɓ����������Ƃ́C������炸�ɓ����܂����B');
		}
		return 0;
	_local_

@@EVENT
	start		15%
	basetime	0h
	plustime	0h
	code		blacktime
	info		���̉Q
	startfunc	_local_(700)
		my($hitproba)=@_;
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{user}->{black}>10)
			{
				my $blackcnt=int($DT->{user}->{black}/10);
				my $cnt=int(rand(10))+$blackcnt;
				$cnt=12 if $cnt>12;
				$DT->{time}+=3600*$cnt;
				$DT->{user}->{black}=0;
				WriteLog(0,$DT->{id},'���̉Q�Ɏ��Ԃ��z�����܂�܂����@�|'.$cnt.'����');
				return (0,'�x�d�Ȃ鎞�ԑ���̂��߂Ɏ��̉Q���������C'.$DT->{shopname}.'�̎��Ԃ��z�����񂾂悤�ł��B');
			}
		}
		return 0;
	_local_

# ���ʗD��Ől�C�A�b�v�C�x���g
@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		getpop
	info		�l�C�A�b�v
	startfunc	_local_(1000)
		my($pop)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{rank}+=$pop;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'���G���ŏЉ��C�l�C���オ�����悤�ł��B');
		}
		return 0;
	_local_

@@FUNCEVENT
######################################################################
# ���󂭂��C�x���g
# usage:  loto
# return: 0 �Œ�
######################################################################
sub loto
{
	WriteLog(2,0,"�󂭂��̒��I���s���܂����B");
	foreach my $DT (@main'DT)
	{
		my $count=$DT->{item}[65-1];
		$DT->{item}[65-1]=0;
		my $hit1=0;
		my $hit2=0;
		my $hit3=0;
		my $hit4=0;
		my $hit5=0;
		next if !$count;
		
		foreach(1..$count)
		{
			my $rnd=rand(6096454);
			my $hit=0;
			
			if ($rnd<152411) {$hit=5;$hit5++;}
			elsif ($rnd<10000) {$hit=4;$hit4++;}
			elsif ($rnd<216) {$hit=3;$hit3++;}
			elsif ($rnd<6) {$hit=2;$hit2++;}
			elsif ($rnd<1) {$hit=1;$hit1++;}
			
			if($hit)
			{
				my $getmoney=(0,1000000000,150000000,5000000,100000,10000)[$hit];
				
				$DT->{moneystock}+=$getmoney;
				$DT->{money}=$main'MAX_MONEY if $DT->{money}>$main'MAX_MONEY;
			}
		}
		my $hitlog=5;
		$hitlog=1;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."��1��".GetMoneyString(1000000000)."�𓖂Ă܂����I") if $hit1>0;
		$hitlog=2;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."��2��".GetMoneyString(150000000)."��$hit2�{���Ă܂���") if $hit2>0;
		$hitlog=3;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."��3��".GetMoneyString(5000000)."��$hit3�{���Ă܂���") if $hit3>0;
		$hitlog=4;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."��4��".GetMoneyString(100000)."��$hit4�{���Ă܂���") if $hit4>0;
		my $hitlog=5;
		WriteLog(($hitlog<=3?1:2),0,$DT->{shopname}."��5��".GetMoneyString(10000)."��$hit5�{���Ă܂���") if $hit5>0;
	}
	return 0;
}

@@FUNCINIT
#���]�Ԃ������Ă���ꍇ�C�������ɕK�v�Ȏ��Ԃ�3/4�ɂ���B
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if (($DT->{item}[@@ITEMNO"���]��"-1])&&(!$DT->{item}[@@ITEMNO"������"-1]));

#�����Ԃ������Ă���ꍇ�C�������ɕK�v�Ȏ��Ԃ�1/4�ɂ���B
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4) if $DT->{item}[@@ITEMNO"������"-1];

@@FUNCITEM
######################################################################
# ���l�ނ��X������
######################################################################
sub lostman
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,'<br>�d�����I����'.$ITEM[$itemno]->{name}.'���C�ق��ċ����Ă����܂���');
	}
	return "";
}

@@FUNCUPDATE
sub UpdateResetBefore #���Z���O�̏���(�֐����Œ�)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#�ܕi���^
		my @TOP123=(
			[
				['���i��',	[[@@ITEMNO "���i��", 5],			],],
				['���i��',	[[@@ITEMNO "���i��", 4],			],],
				['���i��',	[[@@ITEMNO "���i��", 3],			],],
				['�������⏕��',	[[@@ITEMNO "�������⏕��", 5],		],],
				['�h�Ɨp�i',	[[@@ITEMNO "�x��@", 1],		],],
				['�엿�g���b�N1�䕪',[[@@ITEMNO "�͔�", 1000],	],],
				['�H��',[[@@ITEMNO "���ꂢ�Ș�", 500],	],],
			],
			[
				['���i��',	[[@@ITEMNO "���i��", 3],			],],
				['���i��',	[[@@ITEMNO "���i��", 2],			],],
				['�������⏕��',	[[@@ITEMNO "�������⏕��", 3],		],],
				['�H��',[[@@ITEMNO "���ꂢ�Ș�", 300],	],],
			],
			[
				['�������⏕��',	[[@@ITEMNO "�������⏕��", 2],		],],
				['���i��',	[[@@ITEMNO "���i��", 2],			],],
				['���i��',	[[@@ITEMNO "���i��", 1],			],],
				['�H��',[[@@ITEMNO "���ꂢ�Ș�", 200],	],],
			],
			[
				['���i��',	[[@@ITEMNO "���i��", 2],			],],
				['���i��',	[[@@ITEMNO "���i��", 1],			],],
				['�������⏕��',	[[@@ITEMNO "�������⏕��", 1],		],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"�݂��ƗD����") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"�ɂ�����2�ʂ�") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"3�ʓ��܂�") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"�W���X�g".($i+1)."�ʂ�") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."�ɂ́C���X����".$getitem[0]."�������܂����B";
			WriteLog(2,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."�ܕi�Ƃ���".$ITEM->{name}."��".$itemnocount[1].$ITEM->{scale}."�l�����܂����B",1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"�������ő及�����ȏゾ�����̂�".$cnt.$ITEM->{scale}."�j�����܂���",1) if $cnt;
			}
		}
	}
}

@@FUNCNEW

# @@DEFINE Set NewShopMoney NewShopTime NewShopItem �̏���
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

# $DEFINE_FUNCNEW_NOLOG=1 ��ݒ肷��ƁC�V�X�e�����̍ŋ߂̏o�����V���J�X���b�Z�[�W��}�����܂��B
$DEFINE_FUNCNEW_NOLOG=1;
WriteLog(1,0,0,$DT->{shopname}."�����A�J�[�������āC���̊X�Ɍ���܂����B",1);

# ���̑��C�V���J�X���ɓƎ��̏�����ǉ��ł��܂��B

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # �ړ]�������L�^

$DT->{item}[67-1]=1;	# �q���g�u�b�N���v���[���g
if($DT->{job} eq 'man')
{
	# �l�ޔh����(man)�ɂ͈ړ]����Ԃ�1/2��Ԋ�
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'�ړ]���Ԃ�������'.GetTime2HMS($DT->{_MoveTownTime}).'�ōς񂾂悤�ł�',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'�ړ]���̊X�����S�ʂƂ���'.GetMoneyString(GetUserDataEx($DT,'_so_present_money')).'�����炢�܂���',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # �؍݊���1���ɕt��\5000���S�ʂƂ��Ď�����
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} ���폜
}

@@FUNCBUY
# package item �ł��B
# 
# $item::BUY �𗘗p�ł��܂��B$item::BUY �̍\���̓}�j���A���� @@ITEM funcb ���������������B
# ���i���̏����� @@ITEM funcb �𗘗p���Ă��������B

if($BUY->{whole})
{
	# �s�ꂩ��̎d���̏ꍇ�C\500000�ɕt��1���̕������⏕����i�悷��B
	my $price=$BUY->{num}*$BUY->{price};
	my $count=int $price/500000;
	
	$count=AddItemSub(@@ITEMNO"�������⏕��",$count,$BUY->{dt}) if $count;
	WriteLog(0,$BUY->{dt}{id},'�s�ꂩ�畟�����⏕����'.$count.'�����炢�܂���') if $count;
}

@@END #��`�I���錾(�ȍ~�R�����g����)


