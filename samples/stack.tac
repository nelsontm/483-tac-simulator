_Stack.Init:
	BeginFunc 56 (this) ;
	_tmp0 = 100 ;
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
	*(this + 8) = _tmp9 ;
	_tmp10 = 0 ;
	*(this + 4) = _tmp10 ;
	_tmp11 = 3 ;
	_tmp12 = *(this) ;
	_tmp13 = *(_tmp12 + 4) ;
	PushParam _tmp11 ;
	PushParam this ;
	ACall _tmp13 ;
	PopParams 8 ;
	EndFunc ;
_Stack.Push:
	BeginFunc 60 (this, i) ;
	_tmp14 = *(this + 8) ;
	_tmp15 = *(this + 4) ;
	_tmp16 = 0 ;
	_tmp17 = _tmp15 < _tmp16 ;
	_tmp18 = *(_tmp14 + -4) ;
	_tmp19 = _tmp15 < _tmp18 ;
	_tmp20 = _tmp19 == _tmp16 ;
	_tmp21 = _tmp17 || _tmp20 ;
	IfZ _tmp21 Goto _L1 ;
	_tmp22 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp22 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L1:
	_tmp23 = 4 ;
	_tmp24 = _tmp23 * _tmp15 ;
	_tmp25 = _tmp14 + _tmp24 ;
	*(_tmp25) = i ;
	_tmp26 = *(this + 4) ;
	_tmp27 = 1 ;
	_tmp28 = _tmp26 + _tmp27 ;
	*(this + 4) = _tmp28 ;
	EndFunc ;
_Stack.Pop:
	BeginFunc 76 (this) ;
	_tmp29 = *(this + 8) ;
	_tmp30 = *(this + 4) ;
	_tmp31 = 1 ;
	_tmp32 = _tmp30 - _tmp31 ;
	_tmp33 = 0 ;
	_tmp34 = _tmp32 < _tmp33 ;
	_tmp35 = *(_tmp29 + -4) ;
	_tmp36 = _tmp32 < _tmp35 ;
	_tmp37 = _tmp36 == _tmp33 ;
	_tmp38 = _tmp34 || _tmp37 ;
	IfZ _tmp38 Goto _L2 ;
	_tmp39 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp39 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L2:
	_tmp40 = 4 ;
	_tmp41 = _tmp40 * _tmp32 ;
	_tmp42 = _tmp29 + _tmp41 ;
	_tmp43 = *(_tmp42) ;
	val = _tmp43 ;
	_tmp44 = *(this + 4) ;
	_tmp45 = 1 ;
	_tmp46 = _tmp44 - _tmp45 ;
	*(this + 4) = _tmp46 ;
	Return val ;
	EndFunc ;
_Stack.NumElems:
	BeginFunc 4 (this) ;
	_tmp47 = *(this + 4) ;
	Return _tmp47 ;
	EndFunc ;
VTable Stack =
	_Stack.Init,
	_Stack.Push,
	_Stack.Pop,
	_Stack.NumElems,
; 
main:
	BeginFunc 136 () ;
	_tmp48 = 12 ;
	PushParam _tmp48 ;
	_tmp49 = LCall _Alloc ;
	PopParams 4 ;
	_tmp50 = Stack ;
	*(_tmp49) = _tmp50 ;
	s = _tmp49 ;
	_tmp51 = *(s) ;
	_tmp52 = *(_tmp51) ;
	PushParam s ;
	ACall _tmp52 ;
	PopParams 4 ;
	_tmp53 = 3 ;
	_tmp54 = *(s) ;
	_tmp55 = *(_tmp54 + 4) ;
	PushParam _tmp53 ;
	PushParam s ;
	ACall _tmp55 ;
	PopParams 8 ;
	_tmp56 = 7 ;
	_tmp57 = *(s) ;
	_tmp58 = *(_tmp57 + 4) ;
	PushParam _tmp56 ;
	PushParam s ;
	ACall _tmp58 ;
	PopParams 8 ;
	_tmp59 = 4 ;
	_tmp60 = *(s) ;
	_tmp61 = *(_tmp60 + 4) ;
	PushParam _tmp59 ;
	PushParam s ;
	ACall _tmp61 ;
	PopParams 8 ;
	_tmp62 = *(s) ;
	_tmp63 = *(_tmp62 + 12) ;
	PushParam s ;
	_tmp64 = ACall _tmp63 ;
	PopParams 4 ;
	PushParam _tmp64 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp65 = " " ;
	PushParam _tmp65 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp66 = *(s) ;
	_tmp67 = *(_tmp66 + 8) ;
	PushParam s ;
	_tmp68 = ACall _tmp67 ;
	PopParams 4 ;
	PushParam _tmp68 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp69 = " " ;
	PushParam _tmp69 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp70 = *(s) ;
	_tmp71 = *(_tmp70 + 8) ;
	PushParam s ;
	_tmp72 = ACall _tmp71 ;
	PopParams 4 ;
	PushParam _tmp72 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp73 = " " ;
	PushParam _tmp73 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp74 = *(s) ;
	_tmp75 = *(_tmp74 + 8) ;
	PushParam s ;
	_tmp76 = ACall _tmp75 ;
	PopParams 4 ;
	PushParam _tmp76 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp77 = " " ;
	PushParam _tmp77 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp78 = *(s) ;
	_tmp79 = *(_tmp78 + 12) ;
	PushParam s ;
	_tmp80 = ACall _tmp79 ;
	PopParams 4 ;
	PushParam _tmp80 ;
	LCall _PrintInt ;
	PopParams 4 ;
	EndFunc ;
