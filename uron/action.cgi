#!/usr/local/bin/perl
# ���������v���O���� 2003/11/03 �R��

require './_config.cgi';
RequireFile('inc-func.cgi');
GetQuery();
OutError("bad request") if ($Q{key} =~ /inc/ || $Q{key} =~ /[^\w-]/);
$Q{key}||='main';
RequireFile($Q{key}.'.cgi');
exit;
