main:
	BeginFunc 56 () ;
	_tmp0 = 5 ;
	_tmp1 = 0 ;
	_tmp2 = _tmp1 - _tmp0 ;
	_tmp3 = 1 ;
	_tmp4 = _tmp2 < _tmp3 ;
	IfZ _tmp4 Goto _L0 ;
	_tmp5 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp5 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L0:
	_tmp6 = 1 ;
	_tmp7 = _tmp6 + _tmp2 ;
	_tmp8 = 4 ;
	_tmp9 = _tmp7 * _tmp8 ;
	PushParam _tmp9 ;
	_tmp10 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp10) = _tmp2 ;
	_tmp11 = _tmp10 + _tmp8 ;
	arr = _tmp11 ;
	_tmp12 = "How did I get here?\n" ;
	PushParam _tmp12 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
