_factorial:
	BeginFunc 36 (n) ;
	_tmp0 = 1 ;
	_tmp1 = n < _tmp0 ;
	_tmp2 = n == _tmp0 ;
	_tmp3 = _tmp1 || _tmp2 ;
	IfZ _tmp3 Goto _L0 ;
	_tmp4 = 1 ;
	Return _tmp4 ;
_L0:
	_tmp5 = 1 ;
	_tmp6 = n - _tmp5 ;
	PushParam _tmp6 ;
	_tmp7 = LCall _factorial ;
	PopParams 4 ;
	_tmp8 = n * _tmp7 ;
	Return _tmp8 ;
	EndFunc ;
main:
	BeginFunc 48 () ;
	_tmp9 = 1 ;
	n = _tmp9 ;
_L1:
	_tmp10 = 15 ;
	_tmp11 = n < _tmp10 ;
	_tmp12 = n == _tmp10 ;
	_tmp13 = _tmp11 || _tmp12 ;
	IfZ _tmp13 Goto _L2 ;
	_tmp14 = "Factorial(" ;
	PushParam _tmp14 ;
	LCall _PrintString ;
	PopParams 4 ;
	PushParam n ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp15 = ") = " ;
	PushParam _tmp15 ;
	LCall _PrintString ;
	PopParams 4 ;
	PushParam n ;
	_tmp16 = LCall _factorial ;
	PopParams 4 ;
	PushParam _tmp16 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp17 = "\n" ;
	PushParam _tmp17 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp18 = 1 ;
	_tmp19 = n + _tmp18 ;
	n = _tmp19 ;
	Goto _L1 ;
_L2:
	EndFunc ;
