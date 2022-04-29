main:
	BeginFunc 48 () ;
	_tmp0 = 4 ;
	_tmp1 = 1 ;
	_tmp2 = _tmp0 < _tmp1 ;
	IfZ _tmp2 Goto _L0 ;
	_tmp3 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp3 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L0:
	_tmp4 = 1 ;
	_tmp5 = _tmp4 + _tmp0 ;
	_tmp6 = 4 ;
	_tmp7 = _tmp5 * _tmp6 ;
	PushParam _tmp7 ;
	_tmp8 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp8) = _tmp0 ;
	_tmp9 = _tmp8 + _tmp6 ;
	x = _tmp9 ;
	_tmp10 = *(x + -4) ;
	PushParam _tmp10 ;
	LCall _PrintInt ;
	PopParams 4 ;
	EndFunc ;
