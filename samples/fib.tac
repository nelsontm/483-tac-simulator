_fib:
	BeginFunc 68 (base) ;
	_tmp0 = 1 ;
	_tmp1 = base < _tmp0 ;
	_tmp2 = base == _tmp0 ;
	_tmp3 = _tmp1 || _tmp2 ;
	IfZ _tmp3 Goto _L0 ;
	Return base ;
	Goto _L1 ;
_L0:
	_tmp4 = 0 ;
	f0 = _tmp4 ;
	_tmp5 = 1 ;
	f1 = _tmp5 ;
	_tmp6 = 2 ;
	i = _tmp6 ;
_L2:
	_tmp7 = i < base ;
	_tmp8 = i == base ;
	_tmp9 = _tmp7 || _tmp8 ;
	IfZ _tmp9 Goto _L3 ;
	_tmp10 = f0 + f1 ;
	f2 = _tmp10 ;
	f0 = f1 ;
	f1 = f2 ;
	_tmp11 = 1 ;
	_tmp12 = i + _tmp11 ;
	i = _tmp12 ;
	Goto _L2 ;
_L3:
	Return f2 ;
_L1:
	EndFunc ;
main:
	BeginFunc 56 () ;
	_tmp13 = "\nThis program computes Fibonacci numbers (slowly..." ;
	PushParam _tmp13 ;
	LCall _PrintString ;
	PopParams 4 ;
_L4:
	_tmp14 = 1 ;
	IfZ _tmp14 Goto _L5 ;
	_tmp15 = "\nEnter the fibonacci number you want: (-1 to qui..." ;
	PushParam _tmp15 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp16 = LCall _ReadInteger ;
	n = _tmp16 ;
	_tmp17 = 1 ;
	_tmp18 = 0 ;
	_tmp19 = _tmp18 - _tmp17 ;
	_tmp20 = n == _tmp19 ;
	IfZ _tmp20 Goto _L6 ;
	Goto _L5 ;
_L6:
	_tmp21 = "Fib(" ;
	PushParam _tmp21 ;
	LCall _PrintString ;
	PopParams 4 ;
	PushParam n ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp22 = ") = " ;
	PushParam _tmp22 ;
	LCall _PrintString ;
	PopParams 4 ;
	PushParam n ;
	_tmp23 = LCall _fib ;
	PopParams 4 ;
	PushParam _tmp23 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp24 = "\n" ;
	PushParam _tmp24 ;
	LCall _PrintString ;
	PopParams 4 ;
	Goto _L4 ;
_L5:
	_tmp25 = "Goodbye!\n" ;
	PushParam _tmp25 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
