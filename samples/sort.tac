_ReadArray:
	BeginFunc 128 () ;
	_tmp0 = "How many scores? " ;
	PushParam _tmp0 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp1 = LCall _ReadInteger ;
	numScores = _tmp1 ;
	_tmp2 = 1 ;
	_tmp3 = numScores < _tmp2 ;
	IfZ _tmp3 Goto _L0 ;
	_tmp4 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp4 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L0:
	_tmp5 = 1 ;
	_tmp6 = _tmp5 + numScores ;
	_tmp7 = 4 ;
	_tmp8 = _tmp6 * _tmp7 ;
	PushParam _tmp8 ;
	_tmp9 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp9) = numScores ;
	_tmp10 = _tmp9 + _tmp7 ;
	arr = _tmp10 ;
	_tmp11 = 0 ;
	i = _tmp11 ;
_L1:
	_tmp12 = *(arr + -4) ;
	_tmp13 = i < _tmp12 ;
	IfZ _tmp13 Goto _L2 ;
	_tmp14 = "Enter next number: " ;
	PushParam _tmp14 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp15 = LCall _ReadInteger ;
	num = _tmp15 ;
	_tmp16 = 0 ;
	_tmp17 = i < _tmp16 ;
	_tmp18 = *(arr + -4) ;
	_tmp19 = i < _tmp18 ;
	_tmp20 = _tmp19 == _tmp16 ;
	_tmp21 = _tmp17 || _tmp20 ;
	IfZ _tmp21 Goto _L3 ;
	_tmp22 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp22 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L3:
	_tmp23 = 4 ;
	_tmp24 = _tmp23 * i ;
	_tmp25 = arr + _tmp24 ;
	*(_tmp25) = num ;
	_tmp26 = 1 ;
	_tmp27 = i + _tmp26 ;
	i = _tmp27 ;
	Goto _L1 ;
_L2:
	Return arr ;
	EndFunc ;
_Sort:
	BeginFunc 304 (arr) ;
	_tmp28 = 1 ;
	i = _tmp28 ;
_L4:
	_tmp29 = *(arr + -4) ;
	_tmp30 = i < _tmp29 ;
	IfZ _tmp30 Goto _L5 ;
	_tmp31 = 1 ;
	_tmp32 = i - _tmp31 ;
	j = _tmp32 ;
	_tmp33 = 0 ;
	_tmp34 = i < _tmp33 ;
	_tmp35 = *(arr + -4) ;
	_tmp36 = i < _tmp35 ;
	_tmp37 = _tmp36 == _tmp33 ;
	_tmp38 = _tmp34 || _tmp37 ;
	IfZ _tmp38 Goto _L6 ;
	_tmp39 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp39 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L6:
	_tmp40 = 4 ;
	_tmp41 = _tmp40 * i ;
	_tmp42 = arr + _tmp41 ;
	_tmp43 = *(_tmp42) ;
	val = _tmp43 ;
_L7:
	_tmp44 = 0 ;
	_tmp45 = _tmp44 < j ;
	_tmp46 = _tmp44 == j ;
	_tmp47 = _tmp45 || _tmp46 ;
	IfZ _tmp47 Goto _L8 ;
	_tmp48 = 0 ;
	_tmp49 = j < _tmp48 ;
	_tmp50 = *(arr + -4) ;
	_tmp51 = j < _tmp50 ;
	_tmp52 = _tmp51 == _tmp48 ;
	_tmp53 = _tmp49 || _tmp52 ;
	IfZ _tmp53 Goto _L9 ;
	_tmp54 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp54 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L9:
	_tmp55 = 4 ;
	_tmp56 = _tmp55 * j ;
	_tmp57 = arr + _tmp56 ;
	_tmp58 = *(_tmp57) ;
	_tmp59 = _tmp58 < val ;
	_tmp60 = _tmp58 == val ;
	_tmp61 = _tmp59 || _tmp60 ;
	IfZ _tmp61 Goto _L10 ;
	Goto _L8 ;
_L10:
	_tmp62 = 1 ;
	_tmp63 = j + _tmp62 ;
	_tmp64 = 0 ;
	_tmp65 = _tmp63 < _tmp64 ;
	_tmp66 = *(arr + -4) ;
	_tmp67 = _tmp63 < _tmp66 ;
	_tmp68 = _tmp67 == _tmp64 ;
	_tmp69 = _tmp65 || _tmp68 ;
	IfZ _tmp69 Goto _L11 ;
	_tmp70 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp70 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L11:
	_tmp71 = 4 ;
	_tmp72 = _tmp71 * _tmp63 ;
	_tmp73 = arr + _tmp72 ;
	_tmp74 = 0 ;
	_tmp75 = j < _tmp74 ;
	_tmp76 = *(arr + -4) ;
	_tmp77 = j < _tmp76 ;
	_tmp78 = _tmp77 == _tmp74 ;
	_tmp79 = _tmp75 || _tmp78 ;
	IfZ _tmp79 Goto _L12 ;
	_tmp80 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp80 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L12:
	_tmp81 = 4 ;
	_tmp82 = _tmp81 * j ;
	_tmp83 = arr + _tmp82 ;
	_tmp84 = *(_tmp83) ;
	*(_tmp73) = _tmp84 ;
	_tmp85 = 1 ;
	_tmp86 = j - _tmp85 ;
	j = _tmp86 ;
	Goto _L7 ;
_L8:
	_tmp87 = 1 ;
	_tmp88 = j + _tmp87 ;
	_tmp89 = 0 ;
	_tmp90 = _tmp88 < _tmp89 ;
	_tmp91 = *(arr + -4) ;
	_tmp92 = _tmp88 < _tmp91 ;
	_tmp93 = _tmp92 == _tmp89 ;
	_tmp94 = _tmp90 || _tmp93 ;
	IfZ _tmp94 Goto _L13 ;
	_tmp95 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp95 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L13:
	_tmp96 = 4 ;
	_tmp97 = _tmp96 * _tmp88 ;
	_tmp98 = arr + _tmp97 ;
	*(_tmp98) = val ;
	_tmp99 = 1 ;
	_tmp100 = i + _tmp99 ;
	i = _tmp100 ;
	Goto _L4 ;
_L5:
	EndFunc ;
_PrintArray:
	BeginFunc 80 (arr) ;
	_tmp101 = 0 ;
	i = _tmp101 ;
	_tmp102 = "Sorted results: " ;
	PushParam _tmp102 ;
	LCall _PrintString ;
	PopParams 4 ;
_L14:
	_tmp103 = *(arr + -4) ;
	_tmp104 = i < _tmp103 ;
	IfZ _tmp104 Goto _L15 ;
	_tmp105 = 0 ;
	_tmp106 = i < _tmp105 ;
	_tmp107 = *(arr + -4) ;
	_tmp108 = i < _tmp107 ;
	_tmp109 = _tmp108 == _tmp105 ;
	_tmp110 = _tmp106 || _tmp109 ;
	IfZ _tmp110 Goto _L16 ;
	_tmp111 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp111 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L16:
	_tmp112 = 4 ;
	_tmp113 = _tmp112 * i ;
	_tmp114 = arr + _tmp113 ;
	_tmp115 = *(_tmp114) ;
	PushParam _tmp115 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp116 = " " ;
	PushParam _tmp116 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp117 = 1 ;
	_tmp118 = i + _tmp117 ;
	i = _tmp118 ;
	Goto _L14 ;
_L15:
	_tmp119 = "\n" ;
	PushParam _tmp119 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
main:
	BeginFunc 16 () ;
	_tmp120 = "\nThis program will read in a bunch of numbers and print them\n" ;
	PushParam _tmp120 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp121 = "back out in sorted order.\n\n" ;
	PushParam _tmp121 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp122 = LCall _ReadArray ;
	arr = _tmp122 ;
	PushParam arr ;
	LCall _Sort ;
	PopParams 4 ;
	PushParam arr ;
	LCall _PrintArray ;
	PopParams 4 ;
	EndFunc ;
