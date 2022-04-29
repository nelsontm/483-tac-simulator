_Matrix.Init:
	BeginFunc 0 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Matrix.Set:
	BeginFunc 0 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Matrix.Get:
	BeginFunc 0 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Matrix.PrintMatrix:
	BeginFunc 68 ;	# live variables = {this}
	_tmp0 = 0 ;	# live variables = {this}
	i = _tmp0 ;	# live variables = {this,_tmp0}
_L0:
	_tmp1 = 10 ;	# live variables = {this,i}
	_tmp2 = i < _tmp1 ;	# live variables = {this,i,_tmp1}
	IfZ _tmp2 Goto _L1 ;	# live variables = {this,i,_tmp2}
	_tmp3 = 0 ;	# live variables = {this,i}
	j = _tmp3 ;	# live variables = {this,i,_tmp3}
_L2:
	_tmp4 = 10 ;	# live variables = {this,i,j}
	_tmp5 = j < _tmp4 ;	# live variables = {this,i,j,_tmp4}
	IfZ _tmp5 Goto _L3 ;	# live variables = {this,i,j,_tmp5}
	_tmp6 = *(this) ;	# live variables = {this,i,j}
	_tmp7 = *(_tmp6 + 8) ;	# live variables = {this,i,j,_tmp6}
	PushParam j ;	# live variables = {this,i,j,_tmp7}
	PushParam i ;	# live variables = {this,i,j,_tmp7}
	PushParam this ;	# live variables = {this,i,j,_tmp7}
	_tmp8 = ACall _tmp7 ;	# live variables = {this,i,j,_tmp7}
	PopParams 12 ;	# live variables = {this,i,j,_tmp8}
	PushParam _tmp8 ;	# live variables = {this,i,j,_tmp8}
	LCall _PrintInt ;	# live variables = {this,i,j}
	PopParams 4 ;	# live variables = {this,i,j}
	_tmp9 = "\t" ;	# live variables = {this,i,j}
	PushParam _tmp9 ;	# live variables = {this,i,j,_tmp9}
	LCall _PrintString ;	# live variables = {this,i,j}
	PopParams 4 ;	# live variables = {this,i,j}
	_tmp10 = 1 ;	# live variables = {this,i,j}
	_tmp11 = j + _tmp10 ;	# live variables = {this,i,j,_tmp10}
	j = _tmp11 ;	# live variables = {this,i,_tmp11}
	Goto _L2 ;	# live variables = {this,i,j}
_L3:
	_tmp12 = "\n" ;	# live variables = {this,i}
	PushParam _tmp12 ;	# live variables = {this,i,_tmp12}
	LCall _PrintString ;	# live variables = {this,i}
	PopParams 4 ;	# live variables = {this,i}
	_tmp13 = 1 ;	# live variables = {this,i}
	_tmp14 = i + _tmp13 ;	# live variables = {this,i,_tmp13}
	i = _tmp14 ;	# live variables = {this,_tmp14}
	Goto _L0 ;	# live variables = {this,i}
_L1:
	EndFunc ;	# live variables = {}
_Matrix.SeedMatrix:
	BeginFunc 180 ;	# live variables = {this}
	_tmp15 = 0 ;	# live variables = {this}
	i = _tmp15 ;	# live variables = {this,_tmp15}
_L4:
	_tmp16 = 5 ;	# live variables = {this,i}
	_tmp17 = i < _tmp16 ;	# live variables = {this,i,_tmp16}
	IfZ _tmp17 Goto _L5 ;	# live variables = {this,i,_tmp17}
	_tmp18 = 0 ;	# live variables = {this,i}
	j = _tmp18 ;	# live variables = {this,i,_tmp18}
_L6:
	_tmp19 = 5 ;	# live variables = {this,i,j}
	_tmp20 = j < _tmp19 ;	# live variables = {this,i,j,_tmp19}
	IfZ _tmp20 Goto _L7 ;	# live variables = {this,i,j,_tmp20}
	_tmp21 = i + j ;	# live variables = {this,i,j}
	_tmp22 = *(this) ;	# live variables = {this,i,j,_tmp21}
	_tmp23 = *(_tmp22 + 4) ;	# live variables = {this,i,j,_tmp21,_tmp22}
	PushParam _tmp21 ;	# live variables = {this,i,j,_tmp21,_tmp23}
	PushParam j ;	# live variables = {this,i,j,_tmp23}
	PushParam i ;	# live variables = {this,i,j,_tmp23}
	PushParam this ;	# live variables = {this,i,j,_tmp23}
	ACall _tmp23 ;	# live variables = {this,i,j,_tmp23}
	PopParams 16 ;	# live variables = {this,i,j}
	_tmp24 = 1 ;	# live variables = {this,i,j}
	_tmp25 = j + _tmp24 ;	# live variables = {this,i,j,_tmp24}
	j = _tmp25 ;	# live variables = {this,i,_tmp25}
	Goto _L6 ;	# live variables = {this,i,j}
_L7:
	_tmp26 = 1 ;	# live variables = {this,i}
	_tmp27 = i + _tmp26 ;	# live variables = {this,i,_tmp26}
	i = _tmp27 ;	# live variables = {this,_tmp27}
	Goto _L4 ;	# live variables = {this,i}
_L5:
	_tmp28 = 2 ;	# live variables = {this}
	_tmp29 = 3 ;	# live variables = {this,_tmp28}
	_tmp30 = 4 ;	# live variables = {this,_tmp28,_tmp29}
	_tmp31 = *(this) ;	# live variables = {this,_tmp28,_tmp29,_tmp30}
	_tmp32 = *(_tmp31 + 4) ;	# live variables = {this,_tmp28,_tmp29,_tmp30,_tmp31}
	PushParam _tmp30 ;	# live variables = {this,_tmp28,_tmp29,_tmp30,_tmp32}
	PushParam _tmp29 ;	# live variables = {this,_tmp28,_tmp29,_tmp32}
	PushParam _tmp28 ;	# live variables = {this,_tmp28,_tmp32}
	PushParam this ;	# live variables = {this,_tmp32}
	ACall _tmp32 ;	# live variables = {this,_tmp32}
	PopParams 16 ;	# live variables = {this}
	_tmp33 = 4 ;	# live variables = {this}
	_tmp34 = 6 ;	# live variables = {this,_tmp33}
	_tmp35 = 2 ;	# live variables = {this,_tmp33,_tmp34}
	_tmp36 = *(this) ;	# live variables = {this,_tmp33,_tmp34,_tmp35}
	_tmp37 = *(_tmp36 + 4) ;	# live variables = {this,_tmp33,_tmp34,_tmp35,_tmp36}
	PushParam _tmp35 ;	# live variables = {this,_tmp33,_tmp34,_tmp35,_tmp37}
	PushParam _tmp34 ;	# live variables = {this,_tmp33,_tmp34,_tmp37}
	PushParam _tmp33 ;	# live variables = {this,_tmp33,_tmp37}
	PushParam this ;	# live variables = {this,_tmp37}
	ACall _tmp37 ;	# live variables = {this,_tmp37}
	PopParams 16 ;	# live variables = {this}
	_tmp38 = 2 ;	# live variables = {this}
	_tmp39 = 3 ;	# live variables = {this,_tmp38}
	_tmp40 = 5 ;	# live variables = {this,_tmp38,_tmp39}
	_tmp41 = *(this) ;	# live variables = {this,_tmp38,_tmp39,_tmp40}
	_tmp42 = *(_tmp41 + 4) ;	# live variables = {this,_tmp38,_tmp39,_tmp40,_tmp41}
	PushParam _tmp40 ;	# live variables = {this,_tmp38,_tmp39,_tmp40,_tmp42}
	PushParam _tmp39 ;	# live variables = {this,_tmp38,_tmp39,_tmp42}
	PushParam _tmp38 ;	# live variables = {this,_tmp38,_tmp42}
	PushParam this ;	# live variables = {this,_tmp42}
	ACall _tmp42 ;	# live variables = {this,_tmp42}
	PopParams 16 ;	# live variables = {this}
	_tmp43 = 0 ;	# live variables = {this}
	_tmp44 = 0 ;	# live variables = {this,_tmp43}
	_tmp45 = 1 ;	# live variables = {this,_tmp43,_tmp44}
	_tmp46 = *(this) ;	# live variables = {this,_tmp43,_tmp44,_tmp45}
	_tmp47 = *(_tmp46 + 4) ;	# live variables = {this,_tmp43,_tmp44,_tmp45,_tmp46}
	PushParam _tmp45 ;	# live variables = {this,_tmp43,_tmp44,_tmp45,_tmp47}
	PushParam _tmp44 ;	# live variables = {this,_tmp43,_tmp44,_tmp47}
	PushParam _tmp43 ;	# live variables = {this,_tmp43,_tmp47}
	PushParam this ;	# live variables = {this,_tmp47}
	ACall _tmp47 ;	# live variables = {this,_tmp47}
	PopParams 16 ;	# live variables = {this}
	_tmp48 = 1 ;	# live variables = {this}
	_tmp49 = 6 ;	# live variables = {this,_tmp48}
	_tmp50 = 3 ;	# live variables = {this,_tmp48,_tmp49}
	_tmp51 = *(this) ;	# live variables = {this,_tmp48,_tmp49,_tmp50}
	_tmp52 = *(_tmp51 + 4) ;	# live variables = {this,_tmp48,_tmp49,_tmp50,_tmp51}
	PushParam _tmp50 ;	# live variables = {this,_tmp48,_tmp49,_tmp50,_tmp52}
	PushParam _tmp49 ;	# live variables = {this,_tmp48,_tmp49,_tmp52}
	PushParam _tmp48 ;	# live variables = {this,_tmp48,_tmp52}
	PushParam this ;	# live variables = {this,_tmp52}
	ACall _tmp52 ;	# live variables = {this,_tmp52}
	PopParams 16 ;	# live variables = {this}
	_tmp53 = 7 ;	# live variables = {this}
	_tmp54 = 7 ;	# live variables = {this,_tmp53}
	_tmp55 = 7 ;	# live variables = {this,_tmp53,_tmp54}
	_tmp56 = *(this) ;	# live variables = {this,_tmp53,_tmp54,_tmp55}
	_tmp57 = *(_tmp56 + 4) ;	# live variables = {this,_tmp53,_tmp54,_tmp55,_tmp56}
	PushParam _tmp55 ;	# live variables = {this,_tmp53,_tmp54,_tmp55,_tmp57}
	PushParam _tmp54 ;	# live variables = {this,_tmp53,_tmp54,_tmp57}
	PushParam _tmp53 ;	# live variables = {this,_tmp53,_tmp57}
	PushParam this ;	# live variables = {this,_tmp57}
	ACall _tmp57 ;	# live variables = {_tmp57}
	PopParams 16 ;	# live variables = {}
	EndFunc ;	# live variables = {}
VTable Matrix =
	_Matrix.Init,
	_Matrix.Set,
	_Matrix.Get,
	_Matrix.PrintMatrix,
	_Matrix.SeedMatrix,
; 
_DenseMatrix.Init:
	BeginFunc 284 ;	# live variables = {this}
	_tmp58 = 10 ;	# live variables = {this}
	_tmp59 = 1 ;	# live variables = {this,_tmp58}
	_tmp60 = _tmp58 < _tmp59 ;	# live variables = {this,_tmp58,_tmp59}
	IfZ _tmp60 Goto _L8 ;	# live variables = {this,_tmp58,_tmp60}
	_tmp61 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {this,_tmp58}
	PushParam _tmp61 ;	# live variables = {this,_tmp58,_tmp61}
	LCall _PrintString ;	# live variables = {this,_tmp58}
	PopParams 4 ;	# live variables = {this,_tmp58}
	LCall _Halt ;	# live variables = {this,_tmp58}
_L8:
	_tmp62 = 1 ;	# live variables = {this,_tmp58}
	_tmp63 = _tmp62 + _tmp58 ;	# live variables = {this,_tmp58,_tmp62}
	_tmp64 = 4 ;	# live variables = {this,_tmp58,_tmp63}
	_tmp65 = _tmp63 * _tmp64 ;	# live variables = {this,_tmp58,_tmp63,_tmp64}
	PushParam _tmp65 ;	# live variables = {this,_tmp58,_tmp64,_tmp65}
	_tmp66 = LCall _Alloc ;	# live variables = {this,_tmp58,_tmp64}
	PopParams 4 ;	# live variables = {this,_tmp58,_tmp64,_tmp66}
	*(_tmp66) = _tmp58 ;	# live variables = {this,_tmp58,_tmp64,_tmp66}
	_tmp67 = _tmp66 + _tmp64 ;	# live variables = {this,_tmp64,_tmp66}
	*(this + 4) = _tmp67 ;	# live variables = {this,_tmp67}
	_tmp68 = 0 ;	# live variables = {this}
	i = _tmp68 ;	# live variables = {this,_tmp68}
_L9:
	_tmp69 = 10 ;	# live variables = {this,i}
	_tmp70 = i < _tmp69 ;	# live variables = {this,i,_tmp69}
	IfZ _tmp70 Goto _L10 ;	# live variables = {this,i,_tmp70}
	_tmp71 = *(this + 4) ;	# live variables = {this,i}
	_tmp72 = 0 ;	# live variables = {this,i,_tmp71}
	_tmp73 = i < _tmp72 ;	# live variables = {this,i,_tmp71,_tmp72}
	_tmp74 = *(_tmp71 + -4) ;	# live variables = {this,i,_tmp71,_tmp72,_tmp73}
	_tmp75 = i < _tmp74 ;	# live variables = {this,i,_tmp71,_tmp72,_tmp73,_tmp74}
	_tmp76 = _tmp75 == _tmp72 ;	# live variables = {this,i,_tmp71,_tmp72,_tmp73,_tmp75}
	_tmp77 = _tmp73 || _tmp76 ;	# live variables = {this,i,_tmp71,_tmp73,_tmp76}
	IfZ _tmp77 Goto _L11 ;	# live variables = {this,i,_tmp71,_tmp77}
	_tmp78 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,i,_tmp71}
	PushParam _tmp78 ;	# live variables = {this,i,_tmp71,_tmp78}
	LCall _PrintString ;	# live variables = {this,i,_tmp71}
	PopParams 4 ;	# live variables = {this,i,_tmp71}
	LCall _Halt ;	# live variables = {this,i,_tmp71}
_L11:
	_tmp79 = 4 ;	# live variables = {this,i,_tmp71}
	_tmp80 = _tmp79 * i ;	# live variables = {this,i,_tmp71,_tmp79}
	_tmp81 = _tmp71 + _tmp80 ;	# live variables = {this,i,_tmp71,_tmp80}
	_tmp82 = 10 ;	# live variables = {this,i,_tmp81}
	_tmp83 = 1 ;	# live variables = {this,i,_tmp81,_tmp82}
	_tmp84 = _tmp82 < _tmp83 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp83}
	IfZ _tmp84 Goto _L12 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp84}
	_tmp85 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {this,i,_tmp81,_tmp82}
	PushParam _tmp85 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp85}
	LCall _PrintString ;	# live variables = {this,i,_tmp81,_tmp82}
	PopParams 4 ;	# live variables = {this,i,_tmp81,_tmp82}
	LCall _Halt ;	# live variables = {this,i,_tmp81,_tmp82}
_L12:
	_tmp86 = 1 ;	# live variables = {this,i,_tmp81,_tmp82}
	_tmp87 = _tmp86 + _tmp82 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp86}
	_tmp88 = 4 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp87}
	_tmp89 = _tmp87 * _tmp88 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp87,_tmp88}
	PushParam _tmp89 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp88,_tmp89}
	_tmp90 = LCall _Alloc ;	# live variables = {this,i,_tmp81,_tmp82,_tmp88}
	PopParams 4 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp88,_tmp90}
	*(_tmp90) = _tmp82 ;	# live variables = {this,i,_tmp81,_tmp82,_tmp88,_tmp90}
	_tmp91 = _tmp90 + _tmp88 ;	# live variables = {this,i,_tmp81,_tmp88,_tmp90}
	*(_tmp81) = _tmp91 ;	# live variables = {this,i,_tmp81,_tmp91}
	_tmp92 = 1 ;	# live variables = {this,i}
	_tmp93 = i + _tmp92 ;	# live variables = {this,i,_tmp92}
	i = _tmp93 ;	# live variables = {this,_tmp93}
	Goto _L9 ;	# live variables = {this,i}
_L10:
	_tmp94 = 0 ;	# live variables = {this}
	i = _tmp94 ;	# live variables = {this,_tmp94}
_L13:
	_tmp95 = 10 ;	# live variables = {this,i}
	_tmp96 = i < _tmp95 ;	# live variables = {this,i,_tmp95}
	IfZ _tmp96 Goto _L14 ;	# live variables = {this,i,_tmp96}
	_tmp97 = 0 ;	# live variables = {this,i}
	j = _tmp97 ;	# live variables = {this,i,_tmp97}
_L15:
	_tmp98 = 10 ;	# live variables = {this,i,j}
	_tmp99 = j < _tmp98 ;	# live variables = {this,i,j,_tmp98}
	IfZ _tmp99 Goto _L16 ;	# live variables = {this,i,j,_tmp99}
	_tmp100 = *(this + 4) ;	# live variables = {this,i,j}
	_tmp101 = 0 ;	# live variables = {this,i,j,_tmp100}
	_tmp102 = i < _tmp101 ;	# live variables = {this,i,j,_tmp100,_tmp101}
	_tmp103 = *(_tmp100 + -4) ;	# live variables = {this,i,j,_tmp100,_tmp101,_tmp102}
	_tmp104 = i < _tmp103 ;	# live variables = {this,i,j,_tmp100,_tmp101,_tmp102,_tmp103}
	_tmp105 = _tmp104 == _tmp101 ;	# live variables = {this,i,j,_tmp100,_tmp101,_tmp102,_tmp104}
	_tmp106 = _tmp102 || _tmp105 ;	# live variables = {this,i,j,_tmp100,_tmp102,_tmp105}
	IfZ _tmp106 Goto _L17 ;	# live variables = {this,i,j,_tmp100,_tmp106}
	_tmp107 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,i,j,_tmp100}
	PushParam _tmp107 ;	# live variables = {this,i,j,_tmp100,_tmp107}
	LCall _PrintString ;	# live variables = {this,i,j,_tmp100}
	PopParams 4 ;	# live variables = {this,i,j,_tmp100}
	LCall _Halt ;	# live variables = {this,i,j,_tmp100}
_L17:
	_tmp108 = 4 ;	# live variables = {this,i,j,_tmp100}
	_tmp109 = _tmp108 * i ;	# live variables = {this,i,j,_tmp100,_tmp108}
	_tmp110 = _tmp100 + _tmp109 ;	# live variables = {this,i,j,_tmp100,_tmp109}
	_tmp111 = *(_tmp110) ;	# live variables = {this,i,j,_tmp110}
	_tmp112 = 0 ;	# live variables = {this,i,j,_tmp111}
	_tmp113 = j < _tmp112 ;	# live variables = {this,i,j,_tmp111,_tmp112}
	_tmp114 = *(_tmp111 + -4) ;	# live variables = {this,i,j,_tmp111,_tmp112,_tmp113}
	_tmp115 = j < _tmp114 ;	# live variables = {this,i,j,_tmp111,_tmp112,_tmp113,_tmp114}
	_tmp116 = _tmp115 == _tmp112 ;	# live variables = {this,i,j,_tmp111,_tmp112,_tmp113,_tmp115}
	_tmp117 = _tmp113 || _tmp116 ;	# live variables = {this,i,j,_tmp111,_tmp113,_tmp116}
	IfZ _tmp117 Goto _L18 ;	# live variables = {this,i,j,_tmp111,_tmp117}
	_tmp118 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,i,j,_tmp111}
	PushParam _tmp118 ;	# live variables = {this,i,j,_tmp111,_tmp118}
	LCall _PrintString ;	# live variables = {this,i,j,_tmp111}
	PopParams 4 ;	# live variables = {this,i,j,_tmp111}
	LCall _Halt ;	# live variables = {this,i,j,_tmp111}
_L18:
	_tmp119 = 4 ;	# live variables = {this,i,j,_tmp111}
	_tmp120 = _tmp119 * j ;	# live variables = {this,i,j,_tmp111,_tmp119}
	_tmp121 = _tmp111 + _tmp120 ;	# live variables = {this,i,j,_tmp111,_tmp120}
	_tmp122 = 0 ;	# live variables = {this,i,j,_tmp121}
	*(_tmp121) = _tmp122 ;	# live variables = {this,i,j,_tmp121,_tmp122}
	_tmp123 = 1 ;	# live variables = {this,i,j}
	_tmp124 = j + _tmp123 ;	# live variables = {this,i,j,_tmp123}
	j = _tmp124 ;	# live variables = {this,i,_tmp124}
	Goto _L15 ;	# live variables = {this,i,j}
_L16:
	_tmp125 = 1 ;	# live variables = {this,i}
	_tmp126 = i + _tmp125 ;	# live variables = {this,i,_tmp125}
	i = _tmp126 ;	# live variables = {this,_tmp126}
	Goto _L13 ;	# live variables = {this,i}
_L14:
	EndFunc ;	# live variables = {}
_DenseMatrix.Set:
	BeginFunc 88 ;	# live variables = {this,x,y,value}
	_tmp127 = *(this + 4) ;	# live variables = {this,x,y,value}
	_tmp128 = 0 ;	# live variables = {x,y,value,_tmp127}
	_tmp129 = x < _tmp128 ;	# live variables = {x,y,value,_tmp127,_tmp128}
	_tmp130 = *(_tmp127 + -4) ;	# live variables = {x,y,value,_tmp127,_tmp128,_tmp129}
	_tmp131 = x < _tmp130 ;	# live variables = {x,y,value,_tmp127,_tmp128,_tmp129,_tmp130}
	_tmp132 = _tmp131 == _tmp128 ;	# live variables = {x,y,value,_tmp127,_tmp128,_tmp129,_tmp131}
	_tmp133 = _tmp129 || _tmp132 ;	# live variables = {x,y,value,_tmp127,_tmp129,_tmp132}
	IfZ _tmp133 Goto _L19 ;	# live variables = {x,y,value,_tmp127,_tmp133}
	_tmp134 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {x,y,value,_tmp127}
	PushParam _tmp134 ;	# live variables = {x,y,value,_tmp127,_tmp134}
	LCall _PrintString ;	# live variables = {x,y,value,_tmp127}
	PopParams 4 ;	# live variables = {x,y,value,_tmp127}
	LCall _Halt ;	# live variables = {x,y,value,_tmp127}
_L19:
	_tmp135 = 4 ;	# live variables = {x,y,value,_tmp127}
	_tmp136 = _tmp135 * x ;	# live variables = {x,y,value,_tmp127,_tmp135}
	_tmp137 = _tmp127 + _tmp136 ;	# live variables = {y,value,_tmp127,_tmp136}
	_tmp138 = *(_tmp137) ;	# live variables = {y,value,_tmp137}
	_tmp139 = 0 ;	# live variables = {y,value,_tmp138}
	_tmp140 = y < _tmp139 ;	# live variables = {y,value,_tmp138,_tmp139}
	_tmp141 = *(_tmp138 + -4) ;	# live variables = {y,value,_tmp138,_tmp139,_tmp140}
	_tmp142 = y < _tmp141 ;	# live variables = {y,value,_tmp138,_tmp139,_tmp140,_tmp141}
	_tmp143 = _tmp142 == _tmp139 ;	# live variables = {y,value,_tmp138,_tmp139,_tmp140,_tmp142}
	_tmp144 = _tmp140 || _tmp143 ;	# live variables = {y,value,_tmp138,_tmp140,_tmp143}
	IfZ _tmp144 Goto _L20 ;	# live variables = {y,value,_tmp138,_tmp144}
	_tmp145 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {y,value,_tmp138}
	PushParam _tmp145 ;	# live variables = {y,value,_tmp138,_tmp145}
	LCall _PrintString ;	# live variables = {y,value,_tmp138}
	PopParams 4 ;	# live variables = {y,value,_tmp138}
	LCall _Halt ;	# live variables = {y,value,_tmp138}
_L20:
	_tmp146 = 4 ;	# live variables = {y,value,_tmp138}
	_tmp147 = _tmp146 * y ;	# live variables = {y,value,_tmp138,_tmp146}
	_tmp148 = _tmp138 + _tmp147 ;	# live variables = {value,_tmp138,_tmp147}
	*(_tmp148) = value ;	# live variables = {value,_tmp148}
	EndFunc ;	# live variables = {}
_DenseMatrix.Get:
	BeginFunc 92 ;	# live variables = {this,x,y}
	_tmp149 = *(this + 4) ;	# live variables = {this,x,y}
	_tmp150 = 0 ;	# live variables = {_tmp149,x,y}
	_tmp151 = x < _tmp150 ;	# live variables = {_tmp149,_tmp150,x,y}
	_tmp152 = *(_tmp149 + -4) ;	# live variables = {_tmp149,_tmp150,_tmp151,x,y}
	_tmp153 = x < _tmp152 ;	# live variables = {_tmp149,_tmp150,_tmp151,_tmp152,x,y}
	_tmp154 = _tmp153 == _tmp150 ;	# live variables = {_tmp149,_tmp150,_tmp151,_tmp153,x,y}
	_tmp155 = _tmp151 || _tmp154 ;	# live variables = {_tmp149,_tmp151,_tmp154,x,y}
	IfZ _tmp155 Goto _L21 ;	# live variables = {_tmp149,_tmp155,x,y}
	_tmp156 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {_tmp149,x,y}
	PushParam _tmp156 ;	# live variables = {_tmp149,_tmp156,x,y}
	LCall _PrintString ;	# live variables = {_tmp149,x,y}
	PopParams 4 ;	# live variables = {_tmp149,x,y}
	LCall _Halt ;	# live variables = {_tmp149,x,y}
_L21:
	_tmp157 = 4 ;	# live variables = {_tmp149,x,y}
	_tmp158 = _tmp157 * x ;	# live variables = {_tmp149,_tmp157,x,y}
	_tmp159 = _tmp149 + _tmp158 ;	# live variables = {_tmp149,_tmp158,y}
	_tmp160 = *(_tmp159) ;	# live variables = {_tmp159,y}
	_tmp161 = 0 ;	# live variables = {_tmp160,y}
	_tmp162 = y < _tmp161 ;	# live variables = {_tmp160,_tmp161,y}
	_tmp163 = *(_tmp160 + -4) ;	# live variables = {_tmp160,_tmp161,_tmp162,y}
	_tmp164 = y < _tmp163 ;	# live variables = {_tmp160,_tmp161,_tmp162,_tmp163,y}
	_tmp165 = _tmp164 == _tmp161 ;	# live variables = {_tmp160,_tmp161,_tmp162,_tmp164,y}
	_tmp166 = _tmp162 || _tmp165 ;	# live variables = {_tmp160,_tmp162,_tmp165,y}
	IfZ _tmp166 Goto _L22 ;	# live variables = {_tmp160,_tmp166,y}
	_tmp167 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {_tmp160,y}
	PushParam _tmp167 ;	# live variables = {_tmp160,_tmp167,y}
	LCall _PrintString ;	# live variables = {_tmp160,y}
	PopParams 4 ;	# live variables = {_tmp160,y}
	LCall _Halt ;	# live variables = {_tmp160,y}
_L22:
	_tmp168 = 4 ;	# live variables = {_tmp160,y}
	_tmp169 = _tmp168 * y ;	# live variables = {_tmp160,_tmp168,y}
	_tmp170 = _tmp160 + _tmp169 ;	# live variables = {_tmp160,_tmp169}
	_tmp171 = *(_tmp170) ;	# live variables = {_tmp170}
	Return _tmp171 ;	# live variables = {_tmp171}
	EndFunc ;	# live variables = {}
VTable DenseMatrix =
	_DenseMatrix.Init,
	_DenseMatrix.Set,
	_DenseMatrix.Get,
	_Matrix.PrintMatrix,
	_Matrix.SeedMatrix,
; 
_SparseItem.Init:
	BeginFunc 0 ;	# live variables = {d,y,next,this}
	*(this + 4) = d ;	# live variables = {d,y,next,this}
	*(this + 8) = y ;	# live variables = {y,next,this}
	*(this + 12) = next ;	# live variables = {next,this}
	EndFunc ;	# live variables = {}
_SparseItem.GetNext:
	BeginFunc 4 ;	# live variables = {this}
	_tmp172 = *(this + 12) ;	# live variables = {this}
	Return _tmp172 ;	# live variables = {_tmp172}
	EndFunc ;	# live variables = {}
_SparseItem.GetY:
	BeginFunc 4 ;	# live variables = {this}
	_tmp173 = *(this + 8) ;	# live variables = {this}
	Return _tmp173 ;	# live variables = {_tmp173}
	EndFunc ;	# live variables = {}
_SparseItem.GetData:
	BeginFunc 4 ;	# live variables = {this}
	_tmp174 = *(this + 4) ;	# live variables = {this}
	Return _tmp174 ;	# live variables = {_tmp174}
	EndFunc ;	# live variables = {}
_SparseItem.SetData:
	BeginFunc 0 ;	# live variables = {val,this}
	*(this + 4) = val ;	# live variables = {val,this}
	EndFunc ;	# live variables = {}
VTable SparseItem =
	_SparseItem.Init,
	_SparseItem.GetNext,
	_SparseItem.GetY,
	_SparseItem.GetData,
	_SparseItem.SetData,
; 
_SparseMatrix.Init:
	BeginFunc 112 ;	# live variables = {this}
	_tmp175 = 10 ;	# live variables = {this}
	_tmp176 = 1 ;	# live variables = {_tmp175,this}
	_tmp177 = _tmp175 < _tmp176 ;	# live variables = {_tmp175,_tmp176,this}
	IfZ _tmp177 Goto _L23 ;	# live variables = {_tmp175,_tmp177,this}
	_tmp178 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {_tmp175,this}
	PushParam _tmp178 ;	# live variables = {_tmp175,_tmp178,this}
	LCall _PrintString ;	# live variables = {_tmp175,this}
	PopParams 4 ;	# live variables = {_tmp175,this}
	LCall _Halt ;	# live variables = {_tmp175,this}
_L23:
	_tmp179 = 1 ;	# live variables = {_tmp175,this}
	_tmp180 = _tmp179 + _tmp175 ;	# live variables = {_tmp175,_tmp179,this}
	_tmp181 = 4 ;	# live variables = {_tmp175,_tmp180,this}
	_tmp182 = _tmp180 * _tmp181 ;	# live variables = {_tmp175,_tmp180,_tmp181,this}
	PushParam _tmp182 ;	# live variables = {_tmp175,_tmp181,_tmp182,this}
	_tmp183 = LCall _Alloc ;	# live variables = {_tmp175,_tmp181,this}
	PopParams 4 ;	# live variables = {_tmp175,_tmp181,_tmp183,this}
	*(_tmp183) = _tmp175 ;	# live variables = {_tmp175,_tmp181,_tmp183,this}
	_tmp184 = _tmp183 + _tmp181 ;	# live variables = {_tmp181,_tmp183,this}
	*(this + 4) = _tmp184 ;	# live variables = {_tmp184,this}
	_tmp185 = 0 ;	# live variables = {this}
	i = _tmp185 ;	# live variables = {_tmp185,this}
_L24:
	_tmp186 = 10 ;	# live variables = {i,this}
	_tmp187 = i < _tmp186 ;	# live variables = {i,_tmp186,this}
	IfZ _tmp187 Goto _L25 ;	# live variables = {i,_tmp187,this}
	_tmp188 = *(this + 4) ;	# live variables = {i,this}
	_tmp189 = 0 ;	# live variables = {i,_tmp188,this}
	_tmp190 = i < _tmp189 ;	# live variables = {i,_tmp188,_tmp189,this}
	_tmp191 = *(_tmp188 + -4) ;	# live variables = {i,_tmp188,_tmp189,_tmp190,this}
	_tmp192 = i < _tmp191 ;	# live variables = {i,_tmp188,_tmp189,_tmp190,_tmp191,this}
	_tmp193 = _tmp192 == _tmp189 ;	# live variables = {i,_tmp188,_tmp189,_tmp190,_tmp192,this}
	_tmp194 = _tmp190 || _tmp193 ;	# live variables = {i,_tmp188,_tmp190,_tmp193,this}
	IfZ _tmp194 Goto _L26 ;	# live variables = {i,_tmp188,_tmp194,this}
	_tmp195 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp188,this}
	PushParam _tmp195 ;	# live variables = {i,_tmp188,_tmp195,this}
	LCall _PrintString ;	# live variables = {i,_tmp188,this}
	PopParams 4 ;	# live variables = {i,_tmp188,this}
	LCall _Halt ;	# live variables = {i,_tmp188,this}
_L26:
	_tmp196 = 4 ;	# live variables = {i,_tmp188,this}
	_tmp197 = _tmp196 * i ;	# live variables = {i,_tmp188,_tmp196,this}
	_tmp198 = _tmp188 + _tmp197 ;	# live variables = {i,_tmp188,_tmp197,this}
	_tmp199 = 0 ;	# live variables = {i,_tmp198,this}
	*(_tmp198) = _tmp199 ;	# live variables = {i,_tmp198,_tmp199,this}
	_tmp200 = 1 ;	# live variables = {i,this}
	_tmp201 = i + _tmp200 ;	# live variables = {i,_tmp200,this}
	i = _tmp201 ;	# live variables = {_tmp201,this}
	Goto _L24 ;	# live variables = {i,this}
_L25:
	EndFunc ;	# live variables = {}
_SparseMatrix.Find:
	BeginFunc 100 ;	# live variables = {x,y,this}
	_tmp202 = *(this + 4) ;	# live variables = {x,y,this}
	_tmp203 = 0 ;	# live variables = {x,y,_tmp202}
	_tmp204 = x < _tmp203 ;	# live variables = {x,y,_tmp202,_tmp203}
	_tmp205 = *(_tmp202 + -4) ;	# live variables = {x,y,_tmp202,_tmp203,_tmp204}
	_tmp206 = x < _tmp205 ;	# live variables = {x,y,_tmp202,_tmp203,_tmp204,_tmp205}
	_tmp207 = _tmp206 == _tmp203 ;	# live variables = {x,y,_tmp202,_tmp203,_tmp204,_tmp206}
	_tmp208 = _tmp204 || _tmp207 ;	# live variables = {x,y,_tmp202,_tmp204,_tmp207}
	IfZ _tmp208 Goto _L27 ;	# live variables = {x,y,_tmp202,_tmp208}
	_tmp209 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {x,y,_tmp202}
	PushParam _tmp209 ;	# live variables = {x,y,_tmp202,_tmp209}
	LCall _PrintString ;	# live variables = {x,y,_tmp202}
	PopParams 4 ;	# live variables = {x,y,_tmp202}
	LCall _Halt ;	# live variables = {x,y,_tmp202}
_L27:
	_tmp210 = 4 ;	# live variables = {x,y,_tmp202}
	_tmp211 = _tmp210 * x ;	# live variables = {x,y,_tmp202,_tmp210}
	_tmp212 = _tmp202 + _tmp211 ;	# live variables = {y,_tmp202,_tmp211}
	_tmp213 = *(_tmp212) ;	# live variables = {y,_tmp212}
	elem = _tmp213 ;	# live variables = {y,_tmp213}
_L28:
	_tmp214 = 0 ;	# live variables = {y,elem}
	_tmp215 = elem == _tmp214 ;	# live variables = {y,elem,_tmp214}
	_tmp216 = 0 ;	# live variables = {y,elem,_tmp215}
	_tmp217 = _tmp215 == _tmp216 ;	# live variables = {y,elem,_tmp215,_tmp216}
	IfZ _tmp217 Goto _L29 ;	# live variables = {y,elem,_tmp217}
	_tmp218 = *(elem) ;	# live variables = {y,elem}
	_tmp219 = *(_tmp218 + 8) ;	# live variables = {y,elem,_tmp218}
	PushParam elem ;	# live variables = {y,elem,_tmp219}
	_tmp220 = ACall _tmp219 ;	# live variables = {y,elem,_tmp219}
	PopParams 4 ;	# live variables = {y,elem,_tmp220}
	_tmp221 = _tmp220 == y ;	# live variables = {y,elem,_tmp220}
	IfZ _tmp221 Goto _L30 ;	# live variables = {y,elem,_tmp221}
	Return elem ;	# live variables = {elem}
_L30:
	_tmp222 = *(elem) ;	# live variables = {y,elem}
	_tmp223 = *(_tmp222 + 4) ;	# live variables = {y,elem,_tmp222}
	PushParam elem ;	# live variables = {y,elem,_tmp223}
	_tmp224 = ACall _tmp223 ;	# live variables = {y,_tmp223}
	PopParams 4 ;	# live variables = {y,_tmp224}
	elem = _tmp224 ;	# live variables = {y,_tmp224}
	Goto _L28 ;	# live variables = {y,elem}
_L29:
	_tmp225 = 0 ;	# live variables = {}
	Return _tmp225 ;	# live variables = {_tmp225}
	EndFunc ;	# live variables = {}
_SparseMatrix.Set:
	BeginFunc 152 ;	# live variables = {x,y,value,this}
	_tmp226 = *(this) ;	# live variables = {x,y,value,this}
	_tmp227 = *(_tmp226 + 20) ;	# live variables = {x,y,value,_tmp226,this}
	PushParam y ;	# live variables = {x,y,value,_tmp227,this}
	PushParam x ;	# live variables = {x,y,value,_tmp227,this}
	PushParam this ;	# live variables = {x,y,value,_tmp227,this}
	_tmp228 = ACall _tmp227 ;	# live variables = {x,y,value,_tmp227,this}
	PopParams 12 ;	# live variables = {x,y,value,_tmp228,this}
	elem = _tmp228 ;	# live variables = {x,y,value,_tmp228,this}
	_tmp229 = 0 ;	# live variables = {x,y,value,elem,this}
	_tmp230 = elem == _tmp229 ;	# live variables = {x,y,value,elem,_tmp229,this}
	_tmp231 = 0 ;	# live variables = {x,y,value,elem,_tmp230,this}
	_tmp232 = _tmp230 == _tmp231 ;	# live variables = {x,y,value,elem,_tmp230,_tmp231,this}
	IfZ _tmp232 Goto _L31 ;	# live variables = {x,y,value,elem,_tmp232,this}
	_tmp233 = *(elem) ;	# live variables = {value,elem}
	_tmp234 = *(_tmp233 + 16) ;	# live variables = {value,elem,_tmp233}
	PushParam value ;	# live variables = {value,elem,_tmp234}
	PushParam elem ;	# live variables = {elem,_tmp234}
	ACall _tmp234 ;	# live variables = {_tmp234}
	PopParams 8 ;	# live variables = {}
	Goto _L32 ;	# live variables = {}
_L31:
	_tmp235 = 16 ;	# live variables = {x,y,value,this}
	PushParam _tmp235 ;	# live variables = {x,y,value,_tmp235,this}
	_tmp236 = LCall _Alloc ;	# live variables = {x,y,value,this}
	PopParams 4 ;	# live variables = {x,y,value,_tmp236,this}
	_tmp237 = SparseItem ;	# live variables = {x,y,value,_tmp236,this}
	*(_tmp236) = _tmp237 ;	# live variables = {x,y,value,_tmp236,_tmp237,this}
	elem = _tmp236 ;	# live variables = {x,y,value,_tmp236,this}
	_tmp238 = *(this + 4) ;	# live variables = {x,y,value,elem,this}
	_tmp239 = 0 ;	# live variables = {x,y,value,elem,_tmp238,this}
	_tmp240 = x < _tmp239 ;	# live variables = {x,y,value,elem,_tmp238,_tmp239,this}
	_tmp241 = *(_tmp238 + -4) ;	# live variables = {x,y,value,elem,_tmp238,_tmp239,_tmp240,this}
	_tmp242 = x < _tmp241 ;	# live variables = {x,y,value,elem,_tmp238,_tmp239,_tmp240,_tmp241,this}
	_tmp243 = _tmp242 == _tmp239 ;	# live variables = {x,y,value,elem,_tmp238,_tmp239,_tmp240,_tmp242,this}
	_tmp244 = _tmp240 || _tmp243 ;	# live variables = {x,y,value,elem,_tmp238,_tmp240,_tmp243,this}
	IfZ _tmp244 Goto _L33 ;	# live variables = {x,y,value,elem,_tmp238,_tmp244,this}
	_tmp245 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {x,y,value,elem,_tmp238,this}
	PushParam _tmp245 ;	# live variables = {x,y,value,elem,_tmp238,_tmp245,this}
	LCall _PrintString ;	# live variables = {x,y,value,elem,_tmp238,this}
	PopParams 4 ;	# live variables = {x,y,value,elem,_tmp238,this}
	LCall _Halt ;	# live variables = {x,y,value,elem,_tmp238,this}
_L33:
	_tmp246 = 4 ;	# live variables = {x,y,value,elem,_tmp238,this}
	_tmp247 = _tmp246 * x ;	# live variables = {x,y,value,elem,_tmp238,_tmp246,this}
	_tmp248 = _tmp238 + _tmp247 ;	# live variables = {x,y,value,elem,_tmp238,_tmp247,this}
	_tmp249 = *(_tmp248) ;	# live variables = {x,y,value,elem,_tmp248,this}
	_tmp250 = *(elem) ;	# live variables = {x,y,value,elem,_tmp249,this}
	_tmp251 = *(_tmp250) ;	# live variables = {x,y,value,elem,_tmp249,_tmp250,this}
	PushParam _tmp249 ;	# live variables = {x,y,value,elem,_tmp249,_tmp251,this}
	PushParam y ;	# live variables = {x,y,value,elem,_tmp251,this}
	PushParam value ;	# live variables = {x,value,elem,_tmp251,this}
	PushParam elem ;	# live variables = {x,elem,_tmp251,this}
	ACall _tmp251 ;	# live variables = {x,elem,_tmp251,this}
	PopParams 16 ;	# live variables = {x,elem,this}
	_tmp252 = *(this + 4) ;	# live variables = {x,elem,this}
	_tmp253 = 0 ;	# live variables = {x,elem,_tmp252}
	_tmp254 = x < _tmp253 ;	# live variables = {x,elem,_tmp252,_tmp253}
	_tmp255 = *(_tmp252 + -4) ;	# live variables = {x,elem,_tmp252,_tmp253,_tmp254}
	_tmp256 = x < _tmp255 ;	# live variables = {x,elem,_tmp252,_tmp253,_tmp254,_tmp255}
	_tmp257 = _tmp256 == _tmp253 ;	# live variables = {x,elem,_tmp252,_tmp253,_tmp254,_tmp256}
	_tmp258 = _tmp254 || _tmp257 ;	# live variables = {x,elem,_tmp252,_tmp254,_tmp257}
	IfZ _tmp258 Goto _L34 ;	# live variables = {x,elem,_tmp252,_tmp258}
	_tmp259 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {x,elem,_tmp252}
	PushParam _tmp259 ;	# live variables = {x,elem,_tmp252,_tmp259}
	LCall _PrintString ;	# live variables = {x,elem,_tmp252}
	PopParams 4 ;	# live variables = {x,elem,_tmp252}
	LCall _Halt ;	# live variables = {x,elem,_tmp252}
_L34:
	_tmp260 = 4 ;	# live variables = {x,elem,_tmp252}
	_tmp261 = _tmp260 * x ;	# live variables = {x,elem,_tmp252,_tmp260}
	_tmp262 = _tmp252 + _tmp261 ;	# live variables = {elem,_tmp252,_tmp261}
	*(_tmp262) = elem ;	# live variables = {elem,_tmp262}
_L32:
	EndFunc ;	# live variables = {}
_SparseMatrix.Get:
	BeginFunc 48 ;	# live variables = {x,y,this}
	_tmp263 = *(this) ;	# live variables = {x,y,this}
	_tmp264 = *(_tmp263 + 20) ;	# live variables = {x,y,_tmp263,this}
	PushParam y ;	# live variables = {x,y,_tmp264,this}
	PushParam x ;	# live variables = {x,_tmp264,this}
	PushParam this ;	# live variables = {_tmp264,this}
	_tmp265 = ACall _tmp264 ;	# live variables = {_tmp264}
	PopParams 12 ;	# live variables = {_tmp265}
	elem = _tmp265 ;	# live variables = {_tmp265}
	_tmp266 = 0 ;	# live variables = {elem}
	_tmp267 = elem == _tmp266 ;	# live variables = {elem,_tmp266}
	_tmp268 = 0 ;	# live variables = {elem,_tmp267}
	_tmp269 = _tmp267 == _tmp268 ;	# live variables = {elem,_tmp267,_tmp268}
	IfZ _tmp269 Goto _L35 ;	# live variables = {elem,_tmp269}
	_tmp270 = *(elem) ;	# live variables = {elem}
	_tmp271 = *(_tmp270 + 12) ;	# live variables = {elem,_tmp270}
	PushParam elem ;	# live variables = {elem,_tmp271}
	_tmp272 = ACall _tmp271 ;	# live variables = {_tmp271}
	PopParams 4 ;	# live variables = {_tmp272}
	Return _tmp272 ;	# live variables = {_tmp272}
	Goto _L36 ;	# live variables = {}
_L35:
	_tmp273 = 0 ;	# live variables = {}
	Return _tmp273 ;	# live variables = {_tmp273}
_L36:
	EndFunc ;	# live variables = {}
VTable SparseMatrix =
	_SparseMatrix.Init,
	_SparseMatrix.Set,
	_SparseMatrix.Get,
	_Matrix.PrintMatrix,
	_Matrix.SeedMatrix,
	_SparseMatrix.Find,
; 
main:
	BeginFunc 84 ;	# live variables = {}
	_tmp274 = "Dense Rep \n" ;	# live variables = {}
	PushParam _tmp274 ;	# live variables = {_tmp274}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp275 = 8 ;	# live variables = {}
	PushParam _tmp275 ;	# live variables = {_tmp275}
	_tmp276 = LCall _Alloc ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp276}
	_tmp277 = DenseMatrix ;	# live variables = {_tmp276}
	*(_tmp276) = _tmp277 ;	# live variables = {_tmp276,_tmp277}
	m = _tmp276 ;	# live variables = {_tmp276}
	_tmp278 = *(m) ;	# live variables = {m}
	_tmp279 = *(_tmp278) ;	# live variables = {m,_tmp278}
	PushParam m ;	# live variables = {m,_tmp279}
	ACall _tmp279 ;	# live variables = {m,_tmp279}
	PopParams 4 ;	# live variables = {m}
	_tmp280 = *(m) ;	# live variables = {m}
	_tmp281 = *(_tmp280 + 16) ;	# live variables = {m,_tmp280}
	PushParam m ;	# live variables = {m,_tmp281}
	ACall _tmp281 ;	# live variables = {m,_tmp281}
	PopParams 4 ;	# live variables = {m}
	_tmp282 = *(m) ;	# live variables = {m}
	_tmp283 = *(_tmp282 + 12) ;	# live variables = {m,_tmp282}
	PushParam m ;	# live variables = {m,_tmp283}
	ACall _tmp283 ;	# live variables = {_tmp283}
	PopParams 4 ;	# live variables = {}
	_tmp284 = "Sparse Rep \n" ;	# live variables = {}
	PushParam _tmp284 ;	# live variables = {_tmp284}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp285 = 8 ;	# live variables = {}
	PushParam _tmp285 ;	# live variables = {_tmp285}
	_tmp286 = LCall _Alloc ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp286}
	_tmp287 = SparseMatrix ;	# live variables = {_tmp286}
	*(_tmp286) = _tmp287 ;	# live variables = {_tmp286,_tmp287}
	m = _tmp286 ;	# live variables = {_tmp286}
	_tmp288 = *(m) ;	# live variables = {m}
	_tmp289 = *(_tmp288) ;	# live variables = {m,_tmp288}
	PushParam m ;	# live variables = {m,_tmp289}
	ACall _tmp289 ;	# live variables = {m,_tmp289}
	PopParams 4 ;	# live variables = {m}
	_tmp290 = *(m) ;	# live variables = {m}
	_tmp291 = *(_tmp290 + 16) ;	# live variables = {m,_tmp290}
	PushParam m ;	# live variables = {m,_tmp291}
	ACall _tmp291 ;	# live variables = {m,_tmp291}
	PopParams 4 ;	# live variables = {m}
	_tmp292 = *(m) ;	# live variables = {m}
	_tmp293 = *(_tmp292 + 12) ;	# live variables = {m,_tmp292}
	PushParam m ;	# live variables = {m,_tmp293}
	ACall _tmp293 ;	# live variables = {_tmp293}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
  _PrintInt:
	  subu $sp, $sp, 8	# decrement sp to make space to save ra,fp
	  sw $fp, 8($sp)	# save fp
	  sw $ra, 4($sp)	# save ra
	  addiu $fp, $sp, 8	# set up new fp
	  lw $a0, 4($fp)	# fill a from $fp+4
	# LCall _PrintInt
	  li $v0, 1
	  syscall
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp		# pop callee frame off stack
	  lw $ra, -4($fp)	# restore saved ra
	  lw $fp, 0($fp)	# restore saved fp
	  jr $ra		# return from function

  _ReadInteger:
	  subu $sp, $sp, 8	# decrement sp to make space to save ra,fp
	  sw $fp, 8($sp)	# save fp
	  sw $ra, 4($sp)	# save ra
	  addiu $fp, $sp, 8	# set up new fp
	  li $v0, 5
	  syscall
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp		# pop callee frame off stack
	  lw $ra, -4($fp)	# restore saved ra
	  lw $fp, 0($fp)	# restore saved fp
	  jr $ra		# return from function


  _PrintBool:
	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp
	  sw $fp, 8($sp)        # save fp
	  sw $ra, 4($sp)        # save ra
	  addiu $fp, $sp, 8     # set up new fp
	  lw $a0, 4($fp)        # fill a from $fp+4
	  li $v0, 4
	  beq $a0, $0, PrintBoolFalse
	  la $a0, _PrintBoolTrueString
	  j PrintBoolEnd
  PrintBoolFalse:
 	  la $a0, _PrintBoolFalseString
  PrintBoolEnd:
	  syscall
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp         # pop callee frame off stack
	  lw $ra, -4($fp)       # restore saved ra
	  lw $fp, 0($fp)        # restore saved fp
	  jr $ra                # return from function

      .data			# create string constant marked with label
      _PrintBoolTrueString: .asciiz "true"
      .text

      .data			# create string constant marked with label
      _PrintBoolFalseString: .asciiz "false"
      .text

  _PrintString:
	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp
	  sw $fp, 8($sp)        # save fp
	  sw $ra, 4($sp)        # save ra
	  addiu $fp, $sp, 8     # set up new fp
	  lw $a0, 4($fp)        # fill a from $fp+4
	  li $v0, 4
	  syscall
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp         # pop callee frame off stack
	  lw $ra, -4($fp)       # restore saved ra
	  lw $fp, 0($fp)        # restore saved fp
	  jr $ra                # return from function

  _Alloc:
	  subu $sp, $sp, 8      # decrement sp to make space to save ra,fp
	  sw $fp, 8($sp)        # save fp
	  sw $ra, 4($sp)        # save ra
	  addiu $fp, $sp, 8     # set up new fp
	  lw $a0, 4($fp)        # fill a from $fp+4
	  li $v0, 9
	  syscall
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp         # pop callee frame off stack
	  lw $ra, -4($fp)       # restore saved ra
	  lw $fp, 0($fp)        # restore saved fp
	  jr $ra                # return from function

  _Halt:
	  li $v0, 10
	  syscall
	# EndFunc


  _StringEqual:
	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp
	  sw $fp, 8($sp)        # save fp
	  sw $ra, 4($sp)        # save ra
	  addiu $fp, $sp, 8     # set up new fp
	  lw $a0, 4($fp)        # fill a from $fp+4
	  lw $a1, 8($fp)        # fill a from $fp+8
	  beq $a0,$a1,Lrunt10
  Lrunt12:
	  lbu  $v0,($a0)
	  lbu  $a2,($a1)
	  bne $v0,$a2,Lrunt11
	  addiu $a0,$a0,1
	  addiu $a1,$a1,1
	  bne $v0,$0,Lrunt12
      li  $v0,1
      j Lrunt10
  Lrunt11:
	  li  $v0,0
  Lrunt10:
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp         # pop callee frame off stack
	  lw $ra, -4($fp)       # restore saved ra
	  lw $fp, 0($fp)        # restore saved fp
	  jr $ra                # return from function



  _ReadLine:
	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp
	  sw $fp, 8($sp)        # save fp
	  sw $ra, 4($sp)        # save ra
	  addiu $fp, $sp, 8     # set up new fp
	  li $a0, 101
	  li $v0, 9
	  syscall
	  addi $a0, $v0, 0
	  li $v0, 8
	  li $a1,101 
	  syscall
	  addiu $v0,$a0,0       # pointer to begin of string
  Lrunt21:
	  lb $a1,($a0)          # load character at pointer
	  addiu $a0,$a0,1       # forward pointer
	  bnez $a1,Lrunt21      # loop until end of string is reached
	  lb $a1,-2($a0)        # load character before end of string
	  li $a2,10             # newline character	  bneq $a1,$a2,Lrunt20  # do not remove last character if not newline
	  sb $0,-2($a0)         # Add the terminating character in its place
  Lrunt20:
	# EndFunc
	# (below handles reaching end of fn body with no explicit return)
	  move $sp, $fp         # pop callee frame off stack
	  lw $ra, -4($fp)       # restore saved ra
	  lw $fp, 0($fp)        # restore saved fp
	  jr $ra                # return from function
