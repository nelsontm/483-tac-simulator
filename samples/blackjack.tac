_Random.Init:
	BeginFunc 0 ;	# live variables = {this,seedVal}
	*(this + 4) = seedVal ;	# live variables = {this,seedVal}
	EndFunc ;	# live variables = {}
_Random.GenRandom:
	BeginFunc 40 ;	# live variables = {this}
	_tmp0 = 15625 ;	# live variables = {this}
	_tmp1 = *(this + 4) ;	# live variables = {this,_tmp0}
	_tmp2 = 10000 ;	# live variables = {this,_tmp0,_tmp1}
	_tmp3 = _tmp1 % _tmp2 ;	# live variables = {this,_tmp0,_tmp1,_tmp2}
	_tmp4 = _tmp0 * _tmp3 ;	# live variables = {this,_tmp0,_tmp3}
	_tmp5 = 22221 ;	# live variables = {this,_tmp4}
	_tmp6 = _tmp4 + _tmp5 ;	# live variables = {this,_tmp4,_tmp5}
	_tmp7 = 65536 ;	# live variables = {this,_tmp6}
	_tmp8 = _tmp6 % _tmp7 ;	# live variables = {this,_tmp6,_tmp7}
	*(this + 4) = _tmp8 ;	# live variables = {this,_tmp8}
	_tmp9 = *(this + 4) ;	# live variables = {this}
	Return _tmp9 ;	# live variables = {_tmp9}
	EndFunc ;	# live variables = {}
_Random.RndInt:
	BeginFunc 16 ;	# live variables = {this,max}
	_tmp10 = *(this) ;	# live variables = {this,max}
	_tmp11 = *(_tmp10 + 4) ;	# live variables = {this,max,_tmp10}
	PushParam this ;	# live variables = {this,max,_tmp11}
	_tmp12 = ACall _tmp11 ;	# live variables = {max,_tmp11}
	PopParams 4 ;	# live variables = {max,_tmp12}
	_tmp13 = _tmp12 % max ;	# live variables = {max,_tmp12}
	Return _tmp13 ;	# live variables = {_tmp13}
	EndFunc ;	# live variables = {}
VTable Random =
	_Random.Init,
	_Random.GenRandom,
	_Random.RndInt,
; 
_Deck.Init:
	BeginFunc 40 ;	# live variables = {this}
	_tmp14 = 52 ;	# live variables = {this}
	_tmp15 = 1 ;	# live variables = {this,_tmp14}
	_tmp16 = _tmp14 < _tmp15 ;	# live variables = {this,_tmp14,_tmp15}
	IfZ _tmp16 Goto _L0 ;	# live variables = {this,_tmp14,_tmp16}
	_tmp17 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {this,_tmp14}
	PushParam _tmp17 ;	# live variables = {this,_tmp14,_tmp17}
	LCall _PrintString ;	# live variables = {this,_tmp14}
	PopParams 4 ;	# live variables = {this,_tmp14}
	LCall _Halt ;	# live variables = {this,_tmp14}
_L0:
	_tmp18 = 1 ;	# live variables = {this,_tmp14}
	_tmp19 = _tmp18 + _tmp14 ;	# live variables = {this,_tmp14,_tmp18}
	_tmp20 = 4 ;	# live variables = {this,_tmp14,_tmp19}
	_tmp21 = _tmp19 * _tmp20 ;	# live variables = {this,_tmp14,_tmp19,_tmp20}
	PushParam _tmp21 ;	# live variables = {this,_tmp14,_tmp20,_tmp21}
	_tmp22 = LCall _Alloc ;	# live variables = {this,_tmp14,_tmp20}
	PopParams 4 ;	# live variables = {this,_tmp14,_tmp20,_tmp22}
	*(_tmp22) = _tmp14 ;	# live variables = {this,_tmp14,_tmp20,_tmp22}
	_tmp23 = _tmp22 + _tmp20 ;	# live variables = {this,_tmp20,_tmp22}
	*(this + 8) = _tmp23 ;	# live variables = {this,_tmp23}
	EndFunc ;	# live variables = {}
_Deck.Shuffle:
	BeginFunc 336 ;	# live variables = {this,gRnd}
	_tmp24 = 0 ;	# live variables = {this,gRnd}
	*(this + 4) = _tmp24 ;	# live variables = {this,gRnd,_tmp24}
_L1:
	_tmp25 = *(this + 4) ;	# live variables = {this,gRnd}
	_tmp26 = 52 ;	# live variables = {this,gRnd,_tmp25}
	_tmp27 = _tmp25 < _tmp26 ;	# live variables = {this,gRnd,_tmp25,_tmp26}
	IfZ _tmp27 Goto _L2 ;	# live variables = {this,gRnd,_tmp27}
	_tmp28 = *(this + 8) ;	# live variables = {this,gRnd}
	_tmp29 = *(this + 4) ;	# live variables = {this,gRnd,_tmp28}
	_tmp30 = 0 ;	# live variables = {this,gRnd,_tmp28,_tmp29}
	_tmp31 = _tmp29 < _tmp30 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp30}
	_tmp32 = *(_tmp28 + -4) ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp30,_tmp31}
	_tmp33 = _tmp29 < _tmp32 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp30,_tmp31,_tmp32}
	_tmp34 = _tmp33 == _tmp30 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp30,_tmp31,_tmp33}
	_tmp35 = _tmp31 || _tmp34 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp31,_tmp34}
	IfZ _tmp35 Goto _L3 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp35}
	_tmp36 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,gRnd,_tmp28,_tmp29}
	PushParam _tmp36 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp36}
	LCall _PrintString ;	# live variables = {this,gRnd,_tmp28,_tmp29}
	PopParams 4 ;	# live variables = {this,gRnd,_tmp28,_tmp29}
	LCall _Halt ;	# live variables = {this,gRnd,_tmp28,_tmp29}
_L3:
	_tmp37 = 4 ;	# live variables = {this,gRnd,_tmp28,_tmp29}
	_tmp38 = _tmp37 * _tmp29 ;	# live variables = {this,gRnd,_tmp28,_tmp29,_tmp37}
	_tmp39 = _tmp28 + _tmp38 ;	# live variables = {this,gRnd,_tmp28,_tmp38}
	_tmp40 = *(this + 4) ;	# live variables = {this,gRnd,_tmp39}
	_tmp41 = 1 ;	# live variables = {this,gRnd,_tmp39,_tmp40}
	_tmp42 = _tmp40 + _tmp41 ;	# live variables = {this,gRnd,_tmp39,_tmp40,_tmp41}
	_tmp43 = 13 ;	# live variables = {this,gRnd,_tmp39,_tmp42}
	_tmp44 = _tmp42 % _tmp43 ;	# live variables = {this,gRnd,_tmp39,_tmp42,_tmp43}
	*(_tmp39) = _tmp44 ;	# live variables = {this,gRnd,_tmp39,_tmp44}
	_tmp45 = *(this + 4) ;	# live variables = {this,gRnd}
	_tmp46 = 1 ;	# live variables = {this,gRnd,_tmp45}
	_tmp47 = _tmp45 + _tmp46 ;	# live variables = {this,gRnd,_tmp45,_tmp46}
	*(this + 4) = _tmp47 ;	# live variables = {this,gRnd,_tmp47}
	Goto _L1 ;	# live variables = {this,gRnd}
_L2:
_L4:
	_tmp48 = *(this + 4) ;	# live variables = {this,gRnd}
	_tmp49 = 0 ;	# live variables = {this,gRnd,_tmp48}
	_tmp50 = _tmp49 < _tmp48 ;	# live variables = {this,gRnd,_tmp48,_tmp49}
	IfZ _tmp50 Goto _L5 ;	# live variables = {this,gRnd,_tmp50}
	_tmp51 = *(this + 4) ;	# live variables = {this,gRnd}
	_tmp52 = *(gRnd) ;	# live variables = {this,gRnd,_tmp51}
	_tmp53 = *(_tmp52 + 8) ;	# live variables = {this,gRnd,_tmp51,_tmp52}
	PushParam _tmp51 ;	# live variables = {this,gRnd,_tmp51,_tmp53}
	PushParam gRnd ;	# live variables = {this,gRnd,_tmp53}
	_tmp54 = ACall _tmp53 ;	# live variables = {this,gRnd,_tmp53}
	PopParams 8 ;	# live variables = {this,gRnd,_tmp54}
	r = _tmp54 ;	# live variables = {this,gRnd,_tmp54}
	_tmp55 = *(this + 4) ;	# live variables = {this,gRnd,r}
	_tmp56 = 1 ;	# live variables = {this,gRnd,r,_tmp55}
	_tmp57 = _tmp55 - _tmp56 ;	# live variables = {this,gRnd,r,_tmp55,_tmp56}
	*(this + 4) = _tmp57 ;	# live variables = {this,gRnd,r,_tmp57}
	_tmp58 = *(this + 8) ;	# live variables = {this,gRnd,r}
	_tmp59 = *(this + 4) ;	# live variables = {this,gRnd,r,_tmp58}
	_tmp60 = 0 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59}
	_tmp61 = _tmp59 < _tmp60 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp60}
	_tmp62 = *(_tmp58 + -4) ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp60,_tmp61}
	_tmp63 = _tmp59 < _tmp62 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp60,_tmp61,_tmp62}
	_tmp64 = _tmp63 == _tmp60 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp60,_tmp61,_tmp63}
	_tmp65 = _tmp61 || _tmp64 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp61,_tmp64}
	IfZ _tmp65 Goto _L6 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp65}
	_tmp66 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,gRnd,r,_tmp58,_tmp59}
	PushParam _tmp66 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp66}
	LCall _PrintString ;	# live variables = {this,gRnd,r,_tmp58,_tmp59}
	PopParams 4 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59}
	LCall _Halt ;	# live variables = {this,gRnd,r,_tmp58,_tmp59}
_L6:
	_tmp67 = 4 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59}
	_tmp68 = _tmp67 * _tmp59 ;	# live variables = {this,gRnd,r,_tmp58,_tmp59,_tmp67}
	_tmp69 = _tmp58 + _tmp68 ;	# live variables = {this,gRnd,r,_tmp58,_tmp68}
	_tmp70 = *(_tmp69) ;	# live variables = {this,gRnd,r,_tmp69}
	temp = _tmp70 ;	# live variables = {this,gRnd,r,_tmp70}
	_tmp71 = *(this + 8) ;	# live variables = {this,gRnd,r,temp}
	_tmp72 = *(this + 4) ;	# live variables = {this,gRnd,r,temp,_tmp71}
	_tmp73 = 0 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72}
	_tmp74 = _tmp72 < _tmp73 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp73}
	_tmp75 = *(_tmp71 + -4) ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp73,_tmp74}
	_tmp76 = _tmp72 < _tmp75 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp73,_tmp74,_tmp75}
	_tmp77 = _tmp76 == _tmp73 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp73,_tmp74,_tmp76}
	_tmp78 = _tmp74 || _tmp77 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp74,_tmp77}
	IfZ _tmp78 Goto _L7 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp78}
	_tmp79 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72}
	PushParam _tmp79 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp79}
	LCall _PrintString ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72}
	PopParams 4 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72}
	LCall _Halt ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72}
_L7:
	_tmp80 = 4 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72}
	_tmp81 = _tmp80 * _tmp72 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp72,_tmp80}
	_tmp82 = _tmp71 + _tmp81 ;	# live variables = {this,gRnd,r,temp,_tmp71,_tmp81}
	_tmp83 = *(this + 8) ;	# live variables = {this,gRnd,r,temp,_tmp82}
	_tmp84 = 0 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83}
	_tmp85 = r < _tmp84 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp84}
	_tmp86 = *(_tmp83 + -4) ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp84,_tmp85}
	_tmp87 = r < _tmp86 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp84,_tmp85,_tmp86}
	_tmp88 = _tmp87 == _tmp84 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp84,_tmp85,_tmp87}
	_tmp89 = _tmp85 || _tmp88 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp85,_tmp88}
	IfZ _tmp89 Goto _L8 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp89}
	_tmp90 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83}
	PushParam _tmp90 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp90}
	LCall _PrintString ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83}
	PopParams 4 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83}
	LCall _Halt ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83}
_L8:
	_tmp91 = 4 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83}
	_tmp92 = _tmp91 * r ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp91}
	_tmp93 = _tmp83 + _tmp92 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp83,_tmp92}
	_tmp94 = *(_tmp93) ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp93}
	*(_tmp82) = _tmp94 ;	# live variables = {this,gRnd,r,temp,_tmp82,_tmp94}
	_tmp95 = *(this + 8) ;	# live variables = {this,gRnd,r,temp}
	_tmp96 = 0 ;	# live variables = {this,gRnd,r,temp,_tmp95}
	_tmp97 = r < _tmp96 ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp96}
	_tmp98 = *(_tmp95 + -4) ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp96,_tmp97}
	_tmp99 = r < _tmp98 ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp96,_tmp97,_tmp98}
	_tmp100 = _tmp99 == _tmp96 ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp96,_tmp97,_tmp99}
	_tmp101 = _tmp97 || _tmp100 ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp97,_tmp100}
	IfZ _tmp101 Goto _L9 ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp101}
	_tmp102 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,gRnd,r,temp,_tmp95}
	PushParam _tmp102 ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp102}
	LCall _PrintString ;	# live variables = {this,gRnd,r,temp,_tmp95}
	PopParams 4 ;	# live variables = {this,gRnd,r,temp,_tmp95}
	LCall _Halt ;	# live variables = {this,gRnd,r,temp,_tmp95}
_L9:
	_tmp103 = 4 ;	# live variables = {this,gRnd,r,temp,_tmp95}
	_tmp104 = _tmp103 * r ;	# live variables = {this,gRnd,r,temp,_tmp95,_tmp103}
	_tmp105 = _tmp95 + _tmp104 ;	# live variables = {this,gRnd,temp,_tmp95,_tmp104}
	*(_tmp105) = temp ;	# live variables = {this,gRnd,temp,_tmp105}
	Goto _L4 ;	# live variables = {this,gRnd}
_L5:
	EndFunc ;	# live variables = {}
_Deck.GetCard:
	BeginFunc 92 ;	# live variables = {this}
	_tmp106 = *(this + 4) ;	# live variables = {this}
	_tmp107 = 52 ;	# live variables = {this,_tmp106}
	_tmp108 = _tmp107 < _tmp106 ;	# live variables = {this,_tmp106,_tmp107}
	_tmp109 = _tmp107 == _tmp106 ;	# live variables = {this,_tmp106,_tmp107,_tmp108}
	_tmp110 = _tmp108 || _tmp109 ;	# live variables = {this,_tmp108,_tmp109}
	IfZ _tmp110 Goto _L10 ;	# live variables = {this,_tmp110}
	_tmp111 = 0 ;	# live variables = {}
	Return _tmp111 ;	# live variables = {_tmp111}
_L10:
	_tmp112 = *(this + 8) ;	# live variables = {this}
	_tmp113 = *(this + 4) ;	# live variables = {this,_tmp112}
	_tmp114 = 0 ;	# live variables = {this,_tmp112,_tmp113}
	_tmp115 = _tmp113 < _tmp114 ;	# live variables = {this,_tmp112,_tmp113,_tmp114}
	_tmp116 = *(_tmp112 + -4) ;	# live variables = {this,_tmp112,_tmp113,_tmp114,_tmp115}
	_tmp117 = _tmp113 < _tmp116 ;	# live variables = {this,_tmp112,_tmp113,_tmp114,_tmp115,_tmp116}
	_tmp118 = _tmp117 == _tmp114 ;	# live variables = {this,_tmp112,_tmp113,_tmp114,_tmp115,_tmp117}
	_tmp119 = _tmp115 || _tmp118 ;	# live variables = {this,_tmp112,_tmp113,_tmp115,_tmp118}
	IfZ _tmp119 Goto _L11 ;	# live variables = {this,_tmp112,_tmp113,_tmp119}
	_tmp120 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,_tmp112,_tmp113}
	PushParam _tmp120 ;	# live variables = {this,_tmp112,_tmp113,_tmp120}
	LCall _PrintString ;	# live variables = {this,_tmp112,_tmp113}
	PopParams 4 ;	# live variables = {this,_tmp112,_tmp113}
	LCall _Halt ;	# live variables = {this,_tmp112,_tmp113}
_L11:
	_tmp121 = 4 ;	# live variables = {this,_tmp112,_tmp113}
	_tmp122 = _tmp121 * _tmp113 ;	# live variables = {this,_tmp112,_tmp113,_tmp121}
	_tmp123 = _tmp112 + _tmp122 ;	# live variables = {this,_tmp112,_tmp122}
	_tmp124 = *(_tmp123) ;	# live variables = {_tmp123,this}
	result = _tmp124 ;	# live variables = {_tmp124,this}
	_tmp125 = *(this + 4) ;	# live variables = {this,result}
	_tmp126 = 1 ;	# live variables = {_tmp125,this,result}
	_tmp127 = _tmp125 + _tmp126 ;	# live variables = {_tmp125,_tmp126,this,result}
	*(this + 4) = _tmp127 ;	# live variables = {_tmp127,this,result}
	Return result ;	# live variables = {result}
	EndFunc ;	# live variables = {}
VTable Deck =
	_Deck.Init,
	_Deck.Shuffle,
	_Deck.GetCard,
; 
_BJDeck.Init:
	BeginFunc 176 ;	# live variables = {this}
	_tmp128 = 8 ;	# live variables = {this}
	_tmp129 = 1 ;	# live variables = {_tmp128,this}
	_tmp130 = _tmp128 < _tmp129 ;	# live variables = {_tmp128,_tmp129,this}
	IfZ _tmp130 Goto _L12 ;	# live variables = {_tmp128,_tmp130,this}
	_tmp131 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {_tmp128,this}
	PushParam _tmp131 ;	# live variables = {_tmp128,_tmp131,this}
	LCall _PrintString ;	# live variables = {_tmp128,this}
	PopParams 4 ;	# live variables = {_tmp128,this}
	LCall _Halt ;	# live variables = {_tmp128,this}
_L12:
	_tmp132 = 1 ;	# live variables = {_tmp128,this}
	_tmp133 = _tmp132 + _tmp128 ;	# live variables = {_tmp128,_tmp132,this}
	_tmp134 = 4 ;	# live variables = {_tmp128,_tmp133,this}
	_tmp135 = _tmp133 * _tmp134 ;	# live variables = {_tmp128,_tmp133,_tmp134,this}
	PushParam _tmp135 ;	# live variables = {_tmp128,_tmp134,_tmp135,this}
	_tmp136 = LCall _Alloc ;	# live variables = {_tmp128,_tmp134,this}
	PopParams 4 ;	# live variables = {_tmp128,_tmp134,_tmp136,this}
	*(_tmp136) = _tmp128 ;	# live variables = {_tmp128,_tmp134,_tmp136,this}
	_tmp137 = _tmp136 + _tmp134 ;	# live variables = {_tmp134,_tmp136,this}
	*(this + 4) = _tmp137 ;	# live variables = {_tmp137,this}
	_tmp138 = 0 ;	# live variables = {this}
	i = _tmp138 ;	# live variables = {_tmp138,this}
_L13:
	_tmp139 = 8 ;	# live variables = {i,this}
	_tmp140 = i < _tmp139 ;	# live variables = {i,_tmp139,this}
	IfZ _tmp140 Goto _L14 ;	# live variables = {i,_tmp140,this}
	_tmp141 = *(this + 4) ;	# live variables = {i,this}
	_tmp142 = 0 ;	# live variables = {i,_tmp141,this}
	_tmp143 = i < _tmp142 ;	# live variables = {i,_tmp141,_tmp142,this}
	_tmp144 = *(_tmp141 + -4) ;	# live variables = {i,_tmp141,_tmp142,_tmp143,this}
	_tmp145 = i < _tmp144 ;	# live variables = {i,_tmp141,_tmp142,_tmp143,_tmp144,this}
	_tmp146 = _tmp145 == _tmp142 ;	# live variables = {i,_tmp141,_tmp142,_tmp143,_tmp145,this}
	_tmp147 = _tmp143 || _tmp146 ;	# live variables = {i,_tmp141,_tmp143,_tmp146,this}
	IfZ _tmp147 Goto _L15 ;	# live variables = {i,_tmp141,_tmp147,this}
	_tmp148 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp141,this}
	PushParam _tmp148 ;	# live variables = {i,_tmp141,_tmp148,this}
	LCall _PrintString ;	# live variables = {i,_tmp141,this}
	PopParams 4 ;	# live variables = {i,_tmp141,this}
	LCall _Halt ;	# live variables = {i,_tmp141,this}
_L15:
	_tmp149 = 4 ;	# live variables = {i,_tmp141,this}
	_tmp150 = _tmp149 * i ;	# live variables = {i,_tmp141,_tmp149,this}
	_tmp151 = _tmp141 + _tmp150 ;	# live variables = {i,_tmp141,_tmp150,this}
	_tmp152 = 12 ;	# live variables = {i,_tmp151,this}
	PushParam _tmp152 ;	# live variables = {i,_tmp151,_tmp152,this}
	_tmp153 = LCall _Alloc ;	# live variables = {i,_tmp151,this}
	PopParams 4 ;	# live variables = {i,_tmp151,_tmp153,this}
	_tmp154 = Deck ;	# live variables = {i,_tmp151,_tmp153,this}
	*(_tmp153) = _tmp154 ;	# live variables = {i,_tmp151,_tmp153,_tmp154,this}
	*(_tmp151) = _tmp153 ;	# live variables = {i,_tmp151,_tmp153,this}
	_tmp155 = *(this + 4) ;	# live variables = {i,this}
	_tmp156 = 0 ;	# live variables = {i,_tmp155,this}
	_tmp157 = i < _tmp156 ;	# live variables = {i,_tmp155,_tmp156,this}
	_tmp158 = *(_tmp155 + -4) ;	# live variables = {i,_tmp155,_tmp156,_tmp157,this}
	_tmp159 = i < _tmp158 ;	# live variables = {i,_tmp155,_tmp156,_tmp157,_tmp158,this}
	_tmp160 = _tmp159 == _tmp156 ;	# live variables = {i,_tmp155,_tmp156,_tmp157,_tmp159,this}
	_tmp161 = _tmp157 || _tmp160 ;	# live variables = {i,_tmp155,_tmp157,_tmp160,this}
	IfZ _tmp161 Goto _L16 ;	# live variables = {i,_tmp155,_tmp161,this}
	_tmp162 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp155,this}
	PushParam _tmp162 ;	# live variables = {i,_tmp155,_tmp162,this}
	LCall _PrintString ;	# live variables = {i,_tmp155,this}
	PopParams 4 ;	# live variables = {i,_tmp155,this}
	LCall _Halt ;	# live variables = {i,_tmp155,this}
_L16:
	_tmp163 = 4 ;	# live variables = {i,_tmp155,this}
	_tmp164 = _tmp163 * i ;	# live variables = {i,_tmp155,_tmp163,this}
	_tmp165 = _tmp155 + _tmp164 ;	# live variables = {i,_tmp155,_tmp164,this}
	_tmp166 = *(_tmp165) ;	# live variables = {i,_tmp165,this}
	_tmp167 = *(_tmp166) ;	# live variables = {i,_tmp166,this}
	_tmp168 = *(_tmp167) ;	# live variables = {i,_tmp166,_tmp167,this}
	PushParam _tmp166 ;	# live variables = {i,_tmp166,_tmp168,this}
	ACall _tmp168 ;	# live variables = {i,_tmp168,this}
	PopParams 4 ;	# live variables = {i,this}
	_tmp169 = 1 ;	# live variables = {i,this}
	_tmp170 = i + _tmp169 ;	# live variables = {i,_tmp169,this}
	i = _tmp170 ;	# live variables = {_tmp170,this}
	Goto _L13 ;	# live variables = {i,this}
_L14:
	EndFunc ;	# live variables = {}
_BJDeck.DealCard:
	BeginFunc 164 ;	# live variables = {this,gRnd}
	_tmp171 = 0 ;	# live variables = {this,gRnd}
	c = _tmp171 ;	# live variables = {_tmp171,this,gRnd}
	_tmp172 = *(this + 8) ;	# live variables = {c,this,gRnd}
	_tmp173 = 8 ;	# live variables = {c,_tmp172,this,gRnd}
	_tmp174 = 52 ;	# live variables = {c,_tmp172,_tmp173,this,gRnd}
	_tmp175 = _tmp173 * _tmp174 ;	# live variables = {c,_tmp172,_tmp173,_tmp174,this,gRnd}
	_tmp176 = _tmp175 < _tmp172 ;	# live variables = {c,_tmp172,_tmp175,this,gRnd}
	_tmp177 = _tmp175 == _tmp172 ;	# live variables = {c,_tmp172,_tmp175,_tmp176,this,gRnd}
	_tmp178 = _tmp176 || _tmp177 ;	# live variables = {c,_tmp176,_tmp177,this,gRnd}
	IfZ _tmp178 Goto _L17 ;	# live variables = {c,_tmp178,this,gRnd}
	_tmp179 = 11 ;	# live variables = {}
	Return _tmp179 ;	# live variables = {_tmp179}
_L17:
_L18:
	_tmp180 = 0 ;	# live variables = {c,this,gRnd}
	_tmp181 = c == _tmp180 ;	# live variables = {c,_tmp180,this,gRnd}
	IfZ _tmp181 Goto _L19 ;	# live variables = {c,_tmp181,this,gRnd}
	_tmp182 = 8 ;	# live variables = {this,gRnd}
	_tmp183 = *(gRnd) ;	# live variables = {_tmp182,this,gRnd}
	_tmp184 = *(_tmp183 + 8) ;	# live variables = {_tmp182,_tmp183,this,gRnd}
	PushParam _tmp182 ;	# live variables = {_tmp182,_tmp184,this,gRnd}
	PushParam gRnd ;	# live variables = {_tmp184,this,gRnd}
	_tmp185 = ACall _tmp184 ;	# live variables = {_tmp184,this,gRnd}
	PopParams 8 ;	# live variables = {_tmp185,this,gRnd}
	d = _tmp185 ;	# live variables = {_tmp185,this,gRnd}
	_tmp186 = *(this + 4) ;	# live variables = {d,this,gRnd}
	_tmp187 = 0 ;	# live variables = {d,_tmp186,this,gRnd}
	_tmp188 = d < _tmp187 ;	# live variables = {d,_tmp186,_tmp187,this,gRnd}
	_tmp189 = *(_tmp186 + -4) ;	# live variables = {d,_tmp186,_tmp187,_tmp188,this,gRnd}
	_tmp190 = d < _tmp189 ;	# live variables = {d,_tmp186,_tmp187,_tmp188,_tmp189,this,gRnd}
	_tmp191 = _tmp190 == _tmp187 ;	# live variables = {d,_tmp186,_tmp187,_tmp188,_tmp190,this,gRnd}
	_tmp192 = _tmp188 || _tmp191 ;	# live variables = {d,_tmp186,_tmp188,_tmp191,this,gRnd}
	IfZ _tmp192 Goto _L20 ;	# live variables = {d,_tmp186,_tmp192,this,gRnd}
	_tmp193 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {d,_tmp186,this,gRnd}
	PushParam _tmp193 ;	# live variables = {d,_tmp186,_tmp193,this,gRnd}
	LCall _PrintString ;	# live variables = {d,_tmp186,this,gRnd}
	PopParams 4 ;	# live variables = {d,_tmp186,this,gRnd}
	LCall _Halt ;	# live variables = {d,_tmp186,this,gRnd}
_L20:
	_tmp194 = 4 ;	# live variables = {d,_tmp186,this,gRnd}
	_tmp195 = _tmp194 * d ;	# live variables = {d,_tmp186,_tmp194,this,gRnd}
	_tmp196 = _tmp186 + _tmp195 ;	# live variables = {_tmp186,_tmp195,this,gRnd}
	_tmp197 = *(_tmp196) ;	# live variables = {_tmp196,this,gRnd}
	_tmp198 = *(_tmp197) ;	# live variables = {_tmp197,this,gRnd}
	_tmp199 = *(_tmp198 + 8) ;	# live variables = {_tmp197,_tmp198,this,gRnd}
	PushParam _tmp197 ;	# live variables = {_tmp197,_tmp199,this,gRnd}
	_tmp200 = ACall _tmp199 ;	# live variables = {_tmp199,this,gRnd}
	PopParams 4 ;	# live variables = {_tmp200,this,gRnd}
	c = _tmp200 ;	# live variables = {_tmp200,this,gRnd}
	Goto _L18 ;	# live variables = {c,this,gRnd}
_L19:
	_tmp201 = 10 ;	# live variables = {c,this}
	_tmp202 = _tmp201 < c ;	# live variables = {c,_tmp201,this}
	IfZ _tmp202 Goto _L21 ;	# live variables = {c,_tmp202,this}
	_tmp203 = 10 ;	# live variables = {this}
	c = _tmp203 ;	# live variables = {_tmp203,this}
	Goto _L22 ;	# live variables = {c,this}
_L21:
	_tmp204 = 1 ;	# live variables = {c,this}
	_tmp205 = c == _tmp204 ;	# live variables = {c,_tmp204,this}
	IfZ _tmp205 Goto _L23 ;	# live variables = {c,_tmp205,this}
	_tmp206 = 11 ;	# live variables = {this}
	c = _tmp206 ;	# live variables = {_tmp206,this}
_L23:
_L22:
	_tmp207 = *(this + 8) ;	# live variables = {c,this}
	_tmp208 = 1 ;	# live variables = {c,_tmp207,this}
	_tmp209 = _tmp207 + _tmp208 ;	# live variables = {c,_tmp207,_tmp208,this}
	*(this + 8) = _tmp209 ;	# live variables = {c,_tmp209,this}
	Return c ;	# live variables = {c}
	EndFunc ;	# live variables = {}
_BJDeck.Shuffle:
	BeginFunc 92 ;	# live variables = {this}
	_tmp210 = "Shuffling..." ;	# live variables = {this}
	PushParam _tmp210 ;	# live variables = {_tmp210,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp211 = 0 ;	# live variables = {this}
	i = _tmp211 ;	# live variables = {_tmp211,this}
_L24:
	_tmp212 = 8 ;	# live variables = {i,this}
	_tmp213 = i < _tmp212 ;	# live variables = {i,_tmp212,this}
	IfZ _tmp213 Goto _L25 ;	# live variables = {i,_tmp213,this}
	_tmp214 = *(this + 4) ;	# live variables = {i,this}
	_tmp215 = 0 ;	# live variables = {i,_tmp214,this}
	_tmp216 = i < _tmp215 ;	# live variables = {i,_tmp214,_tmp215,this}
	_tmp217 = *(_tmp214 + -4) ;	# live variables = {i,_tmp214,_tmp215,_tmp216,this}
	_tmp218 = i < _tmp217 ;	# live variables = {i,_tmp214,_tmp215,_tmp216,_tmp217,this}
	_tmp219 = _tmp218 == _tmp215 ;	# live variables = {i,_tmp214,_tmp215,_tmp216,_tmp218,this}
	_tmp220 = _tmp216 || _tmp219 ;	# live variables = {i,_tmp214,_tmp216,_tmp219,this}
	IfZ _tmp220 Goto _L26 ;	# live variables = {i,_tmp214,_tmp220,this}
	_tmp221 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp214,this}
	PushParam _tmp221 ;	# live variables = {i,_tmp214,_tmp221,this}
	LCall _PrintString ;	# live variables = {i,_tmp214,this}
	PopParams 4 ;	# live variables = {i,_tmp214,this}
	LCall _Halt ;	# live variables = {i,_tmp214,this}
_L26:
	_tmp222 = 4 ;	# live variables = {i,_tmp214,this}
	_tmp223 = _tmp222 * i ;	# live variables = {i,_tmp214,_tmp222,this}
	_tmp224 = _tmp214 + _tmp223 ;	# live variables = {i,_tmp214,_tmp223,this}
	_tmp225 = *(_tmp224) ;	# live variables = {i,_tmp224,this}
	_tmp226 = *(_tmp225) ;	# live variables = {i,_tmp225,this}
	_tmp227 = *(_tmp226 + 4) ;	# live variables = {i,_tmp225,_tmp226,this}
	PushParam _tmp225 ;	# live variables = {i,_tmp225,_tmp227,this}
	ACall _tmp227 ;	# live variables = {i,_tmp227,this}
	PopParams 4 ;	# live variables = {i,this}
	_tmp228 = 1 ;	# live variables = {i,this}
	_tmp229 = i + _tmp228 ;	# live variables = {i,_tmp228,this}
	i = _tmp229 ;	# live variables = {_tmp229,this}
	Goto _L24 ;	# live variables = {i,this}
_L25:
	_tmp230 = 0 ;	# live variables = {this}
	*(this + 8) = _tmp230 ;	# live variables = {_tmp230,this}
	_tmp231 = "done.\n" ;	# live variables = {}
	PushParam _tmp231 ;	# live variables = {_tmp231}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_BJDeck.NumCardsRemaining:
	BeginFunc 20 ;	# live variables = {this}
	_tmp232 = 8 ;	# live variables = {this}
	_tmp233 = 52 ;	# live variables = {_tmp232,this}
	_tmp234 = _tmp232 * _tmp233 ;	# live variables = {_tmp232,_tmp233,this}
	_tmp235 = *(this + 8) ;	# live variables = {_tmp234,this}
	_tmp236 = _tmp234 - _tmp235 ;	# live variables = {_tmp234,_tmp235}
	Return _tmp236 ;	# live variables = {_tmp236}
	EndFunc ;	# live variables = {}
VTable BJDeck =
	_BJDeck.Init,
	_BJDeck.DealCard,
	_BJDeck.Shuffle,
	_BJDeck.NumCardsRemaining,
; 
_Player.Init:
	BeginFunc 16 ;	# live variables = {num,this}
	_tmp237 = 1000 ;	# live variables = {num,this}
	*(this + 12) = _tmp237 ;	# live variables = {num,_tmp237,this}
	_tmp238 = "What is the name of player #" ;	# live variables = {num,this}
	PushParam _tmp238 ;	# live variables = {num,_tmp238,this}
	LCall _PrintString ;	# live variables = {num,this}
	PopParams 4 ;	# live variables = {num,this}
	PushParam num ;	# live variables = {num,this}
	LCall _PrintInt ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp239 = "? " ;	# live variables = {this}
	PushParam _tmp239 ;	# live variables = {_tmp239,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp240 = LCall _ReadLine ;	# live variables = {this}
	*(this + 16) = _tmp240 ;	# live variables = {_tmp240,this}
	EndFunc ;	# live variables = {}
_Player.Hit:
	BeginFunc 120 ;	# live variables = {deck,this}
	_tmp241 = *(deck) ;	# live variables = {deck,this}
	_tmp242 = *(_tmp241 + 4) ;	# live variables = {deck,_tmp241,this}
	PushParam deck ;	# live variables = {deck,_tmp242,this}
	_tmp243 = ACall _tmp242 ;	# live variables = {_tmp242,this}
	PopParams 4 ;	# live variables = {_tmp243,this}
	card = _tmp243 ;	# live variables = {_tmp243,this}
	_tmp244 = *(this + 16) ;	# live variables = {card,this}
	PushParam _tmp244 ;	# live variables = {card,_tmp244,this}
	LCall _PrintString ;	# live variables = {card,this}
	PopParams 4 ;	# live variables = {card,this}
	_tmp245 = " was dealt a " ;	# live variables = {card,this}
	PushParam _tmp245 ;	# live variables = {card,_tmp245,this}
	LCall _PrintString ;	# live variables = {card,this}
	PopParams 4 ;	# live variables = {card,this}
	PushParam card ;	# live variables = {card,this}
	LCall _PrintInt ;	# live variables = {card,this}
	PopParams 4 ;	# live variables = {card,this}
	_tmp246 = ".\n" ;	# live variables = {card,this}
	PushParam _tmp246 ;	# live variables = {card,_tmp246,this}
	LCall _PrintString ;	# live variables = {card,this}
	PopParams 4 ;	# live variables = {card,this}
	_tmp247 = *(this + 24) ;	# live variables = {card,this}
	_tmp248 = _tmp247 + card ;	# live variables = {card,_tmp247,this}
	*(this + 24) = _tmp248 ;	# live variables = {card,_tmp248,this}
	_tmp249 = *(this + 20) ;	# live variables = {card,this}
	_tmp250 = 1 ;	# live variables = {card,_tmp249,this}
	_tmp251 = _tmp249 + _tmp250 ;	# live variables = {card,_tmp249,_tmp250,this}
	*(this + 20) = _tmp251 ;	# live variables = {card,_tmp251,this}
	_tmp252 = 11 ;	# live variables = {card,this}
	_tmp253 = card == _tmp252 ;	# live variables = {card,_tmp252,this}
	IfZ _tmp253 Goto _L27 ;	# live variables = {_tmp253,this}
	_tmp254 = *(this + 4) ;	# live variables = {this}
	_tmp255 = 1 ;	# live variables = {_tmp254,this}
	_tmp256 = _tmp254 + _tmp255 ;	# live variables = {_tmp254,_tmp255,this}
	*(this + 4) = _tmp256 ;	# live variables = {_tmp256,this}
_L27:
_L28:
	_tmp257 = *(this + 24) ;	# live variables = {this}
	_tmp258 = 21 ;	# live variables = {_tmp257,this}
	_tmp259 = _tmp258 < _tmp257 ;	# live variables = {_tmp257,_tmp258,this}
	_tmp260 = *(this + 4) ;	# live variables = {_tmp259,this}
	_tmp261 = 0 ;	# live variables = {_tmp259,_tmp260,this}
	_tmp262 = _tmp261 < _tmp260 ;	# live variables = {_tmp259,_tmp260,_tmp261,this}
	_tmp263 = _tmp259 && _tmp262 ;	# live variables = {_tmp259,_tmp262,this}
	IfZ _tmp263 Goto _L29 ;	# live variables = {_tmp263,this}
	_tmp264 = *(this + 24) ;	# live variables = {this}
	_tmp265 = 10 ;	# live variables = {_tmp264,this}
	_tmp266 = _tmp264 - _tmp265 ;	# live variables = {_tmp264,_tmp265,this}
	*(this + 24) = _tmp266 ;	# live variables = {_tmp266,this}
	_tmp267 = *(this + 4) ;	# live variables = {this}
	_tmp268 = 1 ;	# live variables = {_tmp267,this}
	_tmp269 = _tmp267 - _tmp268 ;	# live variables = {_tmp267,_tmp268,this}
	*(this + 4) = _tmp269 ;	# live variables = {_tmp269,this}
	Goto _L28 ;	# live variables = {this}
_L29:
	EndFunc ;	# live variables = {}
_Player.DoubleDown:
	BeginFunc 104 ;	# live variables = {deck,this}
	_tmp270 = *(this + 24) ;	# live variables = {deck,this}
	_tmp271 = 10 ;	# live variables = {deck,_tmp270,this}
	_tmp272 = _tmp270 == _tmp271 ;	# live variables = {deck,_tmp270,_tmp271,this}
	_tmp273 = 0 ;	# live variables = {deck,_tmp272,this}
	_tmp274 = _tmp272 == _tmp273 ;	# live variables = {deck,_tmp272,_tmp273,this}
	_tmp275 = *(this + 24) ;	# live variables = {deck,_tmp274,this}
	_tmp276 = 11 ;	# live variables = {deck,_tmp274,_tmp275,this}
	_tmp277 = _tmp275 == _tmp276 ;	# live variables = {deck,_tmp274,_tmp275,_tmp276,this}
	_tmp278 = 0 ;	# live variables = {deck,_tmp274,_tmp277,this}
	_tmp279 = _tmp277 == _tmp278 ;	# live variables = {deck,_tmp274,_tmp277,_tmp278,this}
	_tmp280 = _tmp274 && _tmp279 ;	# live variables = {deck,_tmp274,_tmp279,this}
	IfZ _tmp280 Goto _L30 ;	# live variables = {deck,_tmp280,this}
	_tmp281 = 0 ;	# live variables = {}
	Return _tmp281 ;	# live variables = {_tmp281}
_L30:
	_tmp282 = "Would you like to double down?" ;	# live variables = {deck,this}
	PushParam _tmp282 ;	# live variables = {deck,_tmp282,this}
	_tmp283 = LCall _GetYesOrNo ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,_tmp283,this}
	IfZ _tmp283 Goto _L31 ;	# live variables = {deck,_tmp283,this}
	_tmp284 = *(this + 8) ;	# live variables = {deck,this}
	_tmp285 = 2 ;	# live variables = {_tmp284,deck,this}
	_tmp286 = _tmp284 * _tmp285 ;	# live variables = {_tmp284,_tmp285,deck,this}
	*(this + 8) = _tmp286 ;	# live variables = {_tmp286,deck,this}
	_tmp287 = *(this) ;	# live variables = {deck,this}
	_tmp288 = *(_tmp287 + 4) ;	# live variables = {_tmp287,deck,this}
	PushParam deck ;	# live variables = {_tmp288,deck,this}
	PushParam this ;	# live variables = {_tmp288,this}
	ACall _tmp288 ;	# live variables = {_tmp288,this}
	PopParams 8 ;	# live variables = {this}
	_tmp289 = *(this + 16) ;	# live variables = {this}
	PushParam _tmp289 ;	# live variables = {_tmp289,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp290 = ", your total is " ;	# live variables = {this}
	PushParam _tmp290 ;	# live variables = {_tmp290,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp291 = *(this + 24) ;	# live variables = {this}
	PushParam _tmp291 ;	# live variables = {_tmp291}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp292 = ".\n" ;	# live variables = {}
	PushParam _tmp292 ;	# live variables = {_tmp292}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp293 = 1 ;	# live variables = {}
	Return _tmp293 ;	# live variables = {_tmp293}
_L31:
	_tmp294 = 0 ;	# live variables = {}
	Return _tmp294 ;	# live variables = {_tmp294}
	EndFunc ;	# live variables = {}
_Player.TakeTurn:
	BeginFunc 168 ;	# live variables = {deck,this}
	_tmp295 = "\n" ;	# live variables = {deck,this}
	PushParam _tmp295 ;	# live variables = {deck,_tmp295,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp296 = *(this + 16) ;	# live variables = {deck,this}
	PushParam _tmp296 ;	# live variables = {deck,_tmp296,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp297 = "'s turn.\n" ;	# live variables = {deck,this}
	PushParam _tmp297 ;	# live variables = {deck,_tmp297,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp298 = 0 ;	# live variables = {deck,this}
	*(this + 24) = _tmp298 ;	# live variables = {deck,_tmp298,this}
	_tmp299 = 0 ;	# live variables = {deck,this}
	*(this + 4) = _tmp299 ;	# live variables = {deck,_tmp299,this}
	_tmp300 = 0 ;	# live variables = {deck,this}
	*(this + 20) = _tmp300 ;	# live variables = {deck,_tmp300,this}
	_tmp301 = *(this) ;	# live variables = {deck,this}
	_tmp302 = *(_tmp301 + 4) ;	# live variables = {deck,_tmp301,this}
	PushParam deck ;	# live variables = {deck,_tmp302,this}
	PushParam this ;	# live variables = {deck,_tmp302,this}
	ACall _tmp302 ;	# live variables = {deck,_tmp302,this}
	PopParams 8 ;	# live variables = {deck,this}
	_tmp303 = *(this) ;	# live variables = {deck,this}
	_tmp304 = *(_tmp303 + 4) ;	# live variables = {deck,_tmp303,this}
	PushParam deck ;	# live variables = {deck,_tmp304,this}
	PushParam this ;	# live variables = {deck,_tmp304,this}
	ACall _tmp304 ;	# live variables = {deck,_tmp304,this}
	PopParams 8 ;	# live variables = {deck,this}
	_tmp305 = *(this) ;	# live variables = {deck,this}
	_tmp306 = *(_tmp305 + 8) ;	# live variables = {deck,_tmp305,this}
	PushParam deck ;	# live variables = {deck,_tmp306,this}
	PushParam this ;	# live variables = {deck,_tmp306,this}
	_tmp307 = ACall _tmp306 ;	# live variables = {deck,_tmp306,this}
	PopParams 8 ;	# live variables = {deck,_tmp307,this}
	_tmp308 = 0 ;	# live variables = {deck,_tmp307,this}
	_tmp309 = _tmp307 == _tmp308 ;	# live variables = {deck,_tmp307,_tmp308,this}
	IfZ _tmp309 Goto _L32 ;	# live variables = {deck,_tmp309,this}
	_tmp310 = 1 ;	# live variables = {deck,this}
	stillGoing = _tmp310 ;	# live variables = {deck,_tmp310,this}
_L33:
	_tmp311 = *(this + 24) ;	# live variables = {deck,stillGoing,this}
	_tmp312 = 21 ;	# live variables = {deck,stillGoing,_tmp311,this}
	_tmp313 = _tmp311 < _tmp312 ;	# live variables = {deck,stillGoing,_tmp311,_tmp312,this}
	_tmp314 = _tmp311 == _tmp312 ;	# live variables = {deck,stillGoing,_tmp311,_tmp312,_tmp313,this}
	_tmp315 = _tmp313 || _tmp314 ;	# live variables = {deck,stillGoing,_tmp313,_tmp314,this}
	_tmp316 = _tmp315 && stillGoing ;	# live variables = {deck,stillGoing,_tmp315,this}
	IfZ _tmp316 Goto _L34 ;	# live variables = {deck,_tmp316,this}
	_tmp317 = *(this + 16) ;	# live variables = {deck,this}
	PushParam _tmp317 ;	# live variables = {deck,_tmp317,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp318 = ", your total is " ;	# live variables = {deck,this}
	PushParam _tmp318 ;	# live variables = {deck,_tmp318,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp319 = *(this + 24) ;	# live variables = {deck,this}
	PushParam _tmp319 ;	# live variables = {deck,_tmp319,this}
	LCall _PrintInt ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp320 = ".\n" ;	# live variables = {deck,this}
	PushParam _tmp320 ;	# live variables = {deck,_tmp320,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp321 = "Would you like a hit?" ;	# live variables = {deck,this}
	PushParam _tmp321 ;	# live variables = {deck,_tmp321,this}
	_tmp322 = LCall _GetYesOrNo ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,_tmp322,this}
	stillGoing = _tmp322 ;	# live variables = {deck,_tmp322,this}
	IfZ stillGoing Goto _L35 ;	# live variables = {deck,stillGoing,this}
	_tmp323 = *(this) ;	# live variables = {deck,stillGoing,this}
	_tmp324 = *(_tmp323 + 4) ;	# live variables = {deck,stillGoing,_tmp323,this}
	PushParam deck ;	# live variables = {deck,stillGoing,_tmp324,this}
	PushParam this ;	# live variables = {deck,stillGoing,_tmp324,this}
	ACall _tmp324 ;	# live variables = {deck,stillGoing,_tmp324,this}
	PopParams 8 ;	# live variables = {deck,stillGoing,this}
_L35:
	Goto _L33 ;	# live variables = {deck,stillGoing,this}
_L34:
_L32:
	_tmp325 = *(this + 24) ;	# live variables = {this}
	_tmp326 = 21 ;	# live variables = {_tmp325,this}
	_tmp327 = _tmp326 < _tmp325 ;	# live variables = {_tmp325,_tmp326,this}
	IfZ _tmp327 Goto _L36 ;	# live variables = {_tmp327,this}
	_tmp328 = *(this + 16) ;	# live variables = {this}
	PushParam _tmp328 ;	# live variables = {_tmp328,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp329 = " busts with the big " ;	# live variables = {this}
	PushParam _tmp329 ;	# live variables = {_tmp329,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp330 = *(this + 24) ;	# live variables = {this}
	PushParam _tmp330 ;	# live variables = {_tmp330}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp331 = "!\n" ;	# live variables = {}
	PushParam _tmp331 ;	# live variables = {_tmp331}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	Goto _L37 ;	# live variables = {}
_L36:
	_tmp332 = *(this + 16) ;	# live variables = {this}
	PushParam _tmp332 ;	# live variables = {_tmp332,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp333 = " stays at " ;	# live variables = {this}
	PushParam _tmp333 ;	# live variables = {_tmp333,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp334 = *(this + 24) ;	# live variables = {this}
	PushParam _tmp334 ;	# live variables = {_tmp334}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp335 = ".\n" ;	# live variables = {}
	PushParam _tmp335 ;	# live variables = {_tmp335}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
_L37:
	EndFunc ;	# live variables = {}
_Player.HasMoney:
	BeginFunc 12 ;	# live variables = {this}
	_tmp336 = *(this + 12) ;	# live variables = {this}
	_tmp337 = 0 ;	# live variables = {_tmp336}
	_tmp338 = _tmp337 < _tmp336 ;	# live variables = {_tmp336,_tmp337}
	Return _tmp338 ;	# live variables = {_tmp338}
	EndFunc ;	# live variables = {}
_Player.PrintMoney:
	BeginFunc 16 ;	# live variables = {this}
	_tmp339 = *(this + 16) ;	# live variables = {this}
	PushParam _tmp339 ;	# live variables = {_tmp339,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp340 = ", you have $" ;	# live variables = {this}
	PushParam _tmp340 ;	# live variables = {_tmp340,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp341 = *(this + 12) ;	# live variables = {this}
	PushParam _tmp341 ;	# live variables = {_tmp341}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp342 = ".\n" ;	# live variables = {}
	PushParam _tmp342 ;	# live variables = {_tmp342}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Player.PlaceBet:
	BeginFunc 56 ;	# live variables = {this}
	_tmp343 = 0 ;	# live variables = {this}
	*(this + 8) = _tmp343 ;	# live variables = {_tmp343,this}
	_tmp344 = *(this) ;	# live variables = {this}
	_tmp345 = *(_tmp344 + 20) ;	# live variables = {_tmp344,this}
	PushParam this ;	# live variables = {_tmp345,this}
	ACall _tmp345 ;	# live variables = {_tmp345,this}
	PopParams 4 ;	# live variables = {this}
_L38:
	_tmp346 = *(this + 8) ;	# live variables = {this}
	_tmp347 = 0 ;	# live variables = {_tmp346,this}
	_tmp348 = _tmp346 < _tmp347 ;	# live variables = {_tmp346,_tmp347,this}
	_tmp349 = _tmp346 == _tmp347 ;	# live variables = {_tmp346,_tmp347,_tmp348,this}
	_tmp350 = _tmp348 || _tmp349 ;	# live variables = {_tmp348,_tmp349,this}
	_tmp351 = *(this + 8) ;	# live variables = {_tmp350,this}
	_tmp352 = *(this + 12) ;	# live variables = {_tmp350,_tmp351,this}
	_tmp353 = _tmp352 < _tmp351 ;	# live variables = {_tmp350,_tmp351,_tmp352,this}
	_tmp354 = _tmp350 || _tmp353 ;	# live variables = {_tmp350,_tmp353,this}
	IfZ _tmp354 Goto _L39 ;	# live variables = {_tmp354,this}
	_tmp355 = "How much would you like to bet? " ;	# live variables = {this}
	PushParam _tmp355 ;	# live variables = {_tmp355,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp356 = LCall _ReadInteger ;	# live variables = {this}
	*(this + 8) = _tmp356 ;	# live variables = {_tmp356,this}
	Goto _L38 ;	# live variables = {this}
_L39:
	EndFunc ;	# live variables = {}
_Player.GetTotal:
	BeginFunc 4 ;	# live variables = {this}
	_tmp357 = *(this + 24) ;	# live variables = {this}
	Return _tmp357 ;	# live variables = {_tmp357}
	EndFunc ;	# live variables = {}
_Player.Resolve:
	BeginFunc 200 ;	# live variables = {dealer,this}
	_tmp358 = 0 ;	# live variables = {dealer,this}
	win = _tmp358 ;	# live variables = {dealer,_tmp358,this}
	_tmp359 = 0 ;	# live variables = {dealer,win,this}
	lose = _tmp359 ;	# live variables = {dealer,win,_tmp359,this}
	_tmp360 = *(this + 24) ;	# live variables = {dealer,win,lose,this}
	_tmp361 = 21 ;	# live variables = {dealer,win,lose,_tmp360,this}
	_tmp362 = _tmp360 == _tmp361 ;	# live variables = {dealer,win,lose,_tmp360,_tmp361,this}
	_tmp363 = *(this + 20) ;	# live variables = {dealer,win,lose,_tmp362,this}
	_tmp364 = 2 ;	# live variables = {dealer,win,lose,_tmp362,_tmp363,this}
	_tmp365 = _tmp363 == _tmp364 ;	# live variables = {dealer,win,lose,_tmp362,_tmp363,_tmp364,this}
	_tmp366 = _tmp362 && _tmp365 ;	# live variables = {dealer,win,lose,_tmp362,_tmp365,this}
	IfZ _tmp366 Goto _L40 ;	# live variables = {dealer,win,lose,_tmp366,this}
	_tmp367 = 2 ;	# live variables = {lose,this}
	win = _tmp367 ;	# live variables = {lose,_tmp367,this}
	Goto _L41 ;	# live variables = {win,lose,this}
_L40:
	_tmp368 = *(this + 24) ;	# live variables = {dealer,win,lose,this}
	_tmp369 = 21 ;	# live variables = {dealer,win,lose,_tmp368,this}
	_tmp370 = _tmp369 < _tmp368 ;	# live variables = {dealer,win,lose,_tmp368,_tmp369,this}
	IfZ _tmp370 Goto _L42 ;	# live variables = {dealer,win,lose,_tmp370,this}
	_tmp371 = 1 ;	# live variables = {win,this}
	lose = _tmp371 ;	# live variables = {win,_tmp371,this}
	Goto _L43 ;	# live variables = {win,lose,this}
_L42:
	_tmp372 = 21 ;	# live variables = {dealer,win,lose,this}
	_tmp373 = _tmp372 < dealer ;	# live variables = {dealer,win,lose,_tmp372,this}
	IfZ _tmp373 Goto _L44 ;	# live variables = {dealer,win,lose,_tmp373,this}
	_tmp374 = 1 ;	# live variables = {lose,this}
	win = _tmp374 ;	# live variables = {lose,_tmp374,this}
	Goto _L45 ;	# live variables = {win,lose,this}
_L44:
	_tmp375 = *(this + 24) ;	# live variables = {dealer,win,lose,this}
	_tmp376 = dealer < _tmp375 ;	# live variables = {dealer,win,lose,_tmp375,this}
	IfZ _tmp376 Goto _L46 ;	# live variables = {dealer,win,lose,_tmp376,this}
	_tmp377 = 1 ;	# live variables = {lose,this}
	win = _tmp377 ;	# live variables = {lose,_tmp377,this}
	Goto _L47 ;	# live variables = {win,lose,this}
_L46:
	_tmp378 = *(this + 24) ;	# live variables = {dealer,win,lose,this}
	_tmp379 = _tmp378 < dealer ;	# live variables = {dealer,win,lose,_tmp378,this}
	IfZ _tmp379 Goto _L48 ;	# live variables = {win,lose,_tmp379,this}
	_tmp380 = 1 ;	# live variables = {win,this}
	lose = _tmp380 ;	# live variables = {win,_tmp380,this}
_L48:
_L47:
_L45:
_L43:
_L41:
	_tmp381 = 1 ;	# live variables = {win,lose,this}
	_tmp382 = _tmp381 < win ;	# live variables = {win,lose,_tmp381,this}
	_tmp383 = _tmp381 == win ;	# live variables = {win,lose,_tmp381,_tmp382,this}
	_tmp384 = _tmp382 || _tmp383 ;	# live variables = {win,lose,_tmp382,_tmp383,this}
	IfZ _tmp384 Goto _L49 ;	# live variables = {win,lose,_tmp384,this}
	_tmp385 = *(this + 16) ;	# live variables = {win,lose,this}
	PushParam _tmp385 ;	# live variables = {win,lose,_tmp385,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp386 = ", you won $" ;	# live variables = {win,lose,this}
	PushParam _tmp386 ;	# live variables = {win,lose,_tmp386,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp387 = *(this + 8) ;	# live variables = {win,lose,this}
	PushParam _tmp387 ;	# live variables = {win,lose,_tmp387,this}
	LCall _PrintInt ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp388 = ".\n" ;	# live variables = {win,lose,this}
	PushParam _tmp388 ;	# live variables = {win,lose,_tmp388,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	Goto _L50 ;	# live variables = {win,lose,this}
_L49:
	_tmp389 = 1 ;	# live variables = {win,lose,this}
	_tmp390 = _tmp389 < lose ;	# live variables = {win,lose,_tmp389,this}
	_tmp391 = _tmp389 == lose ;	# live variables = {win,lose,_tmp389,_tmp390,this}
	_tmp392 = _tmp390 || _tmp391 ;	# live variables = {win,lose,_tmp390,_tmp391,this}
	IfZ _tmp392 Goto _L51 ;	# live variables = {win,lose,_tmp392,this}
	_tmp393 = *(this + 16) ;	# live variables = {win,lose,this}
	PushParam _tmp393 ;	# live variables = {win,lose,_tmp393,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp394 = ", you lost $" ;	# live variables = {win,lose,this}
	PushParam _tmp394 ;	# live variables = {win,lose,_tmp394,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp395 = *(this + 8) ;	# live variables = {win,lose,this}
	PushParam _tmp395 ;	# live variables = {win,lose,_tmp395,this}
	LCall _PrintInt ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp396 = ".\n" ;	# live variables = {win,lose,this}
	PushParam _tmp396 ;	# live variables = {win,lose,_tmp396,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	Goto _L52 ;	# live variables = {win,lose,this}
_L51:
	_tmp397 = *(this + 16) ;	# live variables = {win,lose,this}
	PushParam _tmp397 ;	# live variables = {win,lose,_tmp397,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
	_tmp398 = ", you push!\n" ;	# live variables = {win,lose,this}
	PushParam _tmp398 ;	# live variables = {win,lose,_tmp398,this}
	LCall _PrintString ;	# live variables = {win,lose,this}
	PopParams 4 ;	# live variables = {win,lose,this}
_L52:
_L50:
	_tmp399 = *(this + 8) ;	# live variables = {win,lose,this}
	_tmp400 = win * _tmp399 ;	# live variables = {win,lose,_tmp399,this}
	win = _tmp400 ;	# live variables = {lose,_tmp400,this}
	_tmp401 = *(this + 8) ;	# live variables = {win,lose,this}
	_tmp402 = lose * _tmp401 ;	# live variables = {win,lose,_tmp401,this}
	lose = _tmp402 ;	# live variables = {win,_tmp402,this}
	_tmp403 = *(this + 12) ;	# live variables = {win,lose,this}
	_tmp404 = _tmp403 + win ;	# live variables = {win,lose,_tmp403,this}
	_tmp405 = _tmp404 - lose ;	# live variables = {lose,_tmp404,this}
	*(this + 12) = _tmp405 ;	# live variables = {_tmp405,this}
	EndFunc ;	# live variables = {}
VTable Player =
	_Player.Init,
	_Player.Hit,
	_Player.DoubleDown,
	_Player.TakeTurn,
	_Player.HasMoney,
	_Player.PrintMoney,
	_Player.PlaceBet,
	_Player.GetTotal,
	_Player.Resolve,
; 
_Dealer.Init:
	BeginFunc 16 ;	# live variables = {this}
	_tmp406 = 0 ;	# live variables = {this}
	*(this + 24) = _tmp406 ;	# live variables = {_tmp406,this}
	_tmp407 = 0 ;	# live variables = {this}
	*(this + 4) = _tmp407 ;	# live variables = {_tmp407,this}
	_tmp408 = 0 ;	# live variables = {this}
	*(this + 20) = _tmp408 ;	# live variables = {_tmp408,this}
	_tmp409 = "Dealer" ;	# live variables = {this}
	*(this + 16) = _tmp409 ;	# live variables = {_tmp409,this}
	EndFunc ;	# live variables = {}
_Dealer.TakeTurn:
	BeginFunc 84 ;	# live variables = {deck,this}
	_tmp410 = "\n" ;	# live variables = {deck,this}
	PushParam _tmp410 ;	# live variables = {deck,_tmp410,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp411 = *(this + 16) ;	# live variables = {deck,this}
	PushParam _tmp411 ;	# live variables = {deck,_tmp411,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
	_tmp412 = "'s turn.\n" ;	# live variables = {deck,this}
	PushParam _tmp412 ;	# live variables = {deck,_tmp412,this}
	LCall _PrintString ;	# live variables = {deck,this}
	PopParams 4 ;	# live variables = {deck,this}
_L53:
	_tmp413 = *(this + 24) ;	# live variables = {deck,this}
	_tmp414 = 16 ;	# live variables = {deck,_tmp413,this}
	_tmp415 = _tmp413 < _tmp414 ;	# live variables = {deck,_tmp413,_tmp414,this}
	_tmp416 = _tmp413 == _tmp414 ;	# live variables = {deck,_tmp413,_tmp414,_tmp415,this}
	_tmp417 = _tmp415 || _tmp416 ;	# live variables = {deck,_tmp415,_tmp416,this}
	IfZ _tmp417 Goto _L54 ;	# live variables = {deck,_tmp417,this}
	_tmp418 = *(this) ;	# live variables = {deck,this}
	_tmp419 = *(_tmp418 + 4) ;	# live variables = {deck,_tmp418,this}
	PushParam deck ;	# live variables = {deck,_tmp419,this}
	PushParam this ;	# live variables = {deck,_tmp419,this}
	ACall _tmp419 ;	# live variables = {deck,_tmp419,this}
	PopParams 8 ;	# live variables = {deck,this}
	Goto _L53 ;	# live variables = {deck,this}
_L54:
	_tmp420 = *(this + 24) ;	# live variables = {this}
	_tmp421 = 21 ;	# live variables = {_tmp420,this}
	_tmp422 = _tmp421 < _tmp420 ;	# live variables = {_tmp420,_tmp421,this}
	IfZ _tmp422 Goto _L55 ;	# live variables = {_tmp422,this}
	_tmp423 = *(this + 16) ;	# live variables = {this}
	PushParam _tmp423 ;	# live variables = {_tmp423,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp424 = " busts with the big " ;	# live variables = {this}
	PushParam _tmp424 ;	# live variables = {_tmp424,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp425 = *(this + 24) ;	# live variables = {this}
	PushParam _tmp425 ;	# live variables = {_tmp425}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp426 = "!\n" ;	# live variables = {}
	PushParam _tmp426 ;	# live variables = {_tmp426}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	Goto _L56 ;	# live variables = {}
_L55:
	_tmp427 = *(this + 16) ;	# live variables = {this}
	PushParam _tmp427 ;	# live variables = {_tmp427,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp428 = " stays at " ;	# live variables = {this}
	PushParam _tmp428 ;	# live variables = {_tmp428,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp429 = *(this + 24) ;	# live variables = {this}
	PushParam _tmp429 ;	# live variables = {_tmp429}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp430 = ".\n" ;	# live variables = {}
	PushParam _tmp430 ;	# live variables = {_tmp430}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
_L56:
	EndFunc ;	# live variables = {}
VTable Dealer =
	_Dealer.Init,
	_Player.Hit,
	_Player.DoubleDown,
	_Dealer.TakeTurn,
	_Player.HasMoney,
	_Player.PrintMoney,
	_Player.PlaceBet,
	_Player.GetTotal,
	_Player.Resolve,
; 
_House.SetupGame:
	BeginFunc 84 ;	# live variables = {this}
	_tmp431 = "\nWelcome to CS143 BlackJack!\n" ;	# live variables = {this}
	PushParam _tmp431 ;	# live variables = {_tmp431,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp432 = "---------------------------\n" ;	# live variables = {this}
	PushParam _tmp432 ;	# live variables = {_tmp432,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp433 = 8 ;	# live variables = {this}
	PushParam _tmp433 ;	# live variables = {_tmp433,this}
	_tmp434 = LCall _Alloc ;	# live variables = {this}
	PopParams 4 ;	# live variables = {_tmp434,this}
	_tmp435 = Random ;	# live variables = {_tmp434,this}
	*(_tmp434) = _tmp435 ;	# live variables = {_tmp434,_tmp435,this}
	gRnd = _tmp434 ;	# live variables = {_tmp434,this}
	_tmp436 = "Please enter a random number seed: " ;	# live variables = {this,gRnd}
	PushParam _tmp436 ;	# live variables = {_tmp436,this,gRnd}
	LCall _PrintString ;	# live variables = {this,gRnd}
	PopParams 4 ;	# live variables = {this,gRnd}
	_tmp437 = LCall _ReadInteger ;	# live variables = {this,gRnd}
	_tmp438 = *(gRnd) ;	# live variables = {_tmp437,this,gRnd}
	_tmp439 = *(_tmp438) ;	# live variables = {_tmp437,_tmp438,this,gRnd}
	PushParam _tmp437 ;	# live variables = {_tmp437,_tmp439,this,gRnd}
	PushParam gRnd ;	# live variables = {_tmp439,this,gRnd}
	ACall _tmp439 ;	# live variables = {_tmp439,this}
	PopParams 8 ;	# live variables = {this}
	_tmp440 = 12 ;	# live variables = {this}
	PushParam _tmp440 ;	# live variables = {_tmp440,this}
	_tmp441 = LCall _Alloc ;	# live variables = {this}
	PopParams 4 ;	# live variables = {_tmp441,this}
	_tmp442 = BJDeck ;	# live variables = {_tmp441,this}
	*(_tmp441) = _tmp442 ;	# live variables = {_tmp441,_tmp442,this}
	*(this + 12) = _tmp441 ;	# live variables = {_tmp441,this}
	_tmp443 = 28 ;	# live variables = {this}
	PushParam _tmp443 ;	# live variables = {_tmp443,this}
	_tmp444 = LCall _Alloc ;	# live variables = {this}
	PopParams 4 ;	# live variables = {_tmp444,this}
	_tmp445 = Dealer ;	# live variables = {_tmp444,this}
	*(_tmp444) = _tmp445 ;	# live variables = {_tmp444,_tmp445,this}
	*(this + 8) = _tmp444 ;	# live variables = {_tmp444,this}
	_tmp446 = *(this + 12) ;	# live variables = {this}
	_tmp447 = *(_tmp446) ;	# live variables = {_tmp446,this}
	_tmp448 = *(_tmp447) ;	# live variables = {_tmp446,_tmp447,this}
	PushParam _tmp446 ;	# live variables = {_tmp446,_tmp448,this}
	ACall _tmp448 ;	# live variables = {_tmp448,this}
	PopParams 4 ;	# live variables = {this}
	_tmp449 = *(this + 12) ;	# live variables = {this}
	_tmp450 = *(_tmp449) ;	# live variables = {_tmp449}
	_tmp451 = *(_tmp450 + 8) ;	# live variables = {_tmp449,_tmp450}
	PushParam _tmp449 ;	# live variables = {_tmp449,_tmp451}
	ACall _tmp451 ;	# live variables = {_tmp451}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_House.SetupPlayers:
	BeginFunc 196 ;	# live variables = {this}
	_tmp452 = "How many players do we have today? " ;	# live variables = {this}
	PushParam _tmp452 ;	# live variables = {_tmp452,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp453 = LCall _ReadInteger ;	# live variables = {this}
	numPlayers = _tmp453 ;	# live variables = {_tmp453,this}
	_tmp454 = 1 ;	# live variables = {numPlayers,this}
	_tmp455 = numPlayers < _tmp454 ;	# live variables = {numPlayers,_tmp454,this}
	IfZ _tmp455 Goto _L57 ;	# live variables = {numPlayers,_tmp455,this}
	_tmp456 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {numPlayers,this}
	PushParam _tmp456 ;	# live variables = {numPlayers,_tmp456,this}
	LCall _PrintString ;	# live variables = {numPlayers,this}
	PopParams 4 ;	# live variables = {numPlayers,this}
	LCall _Halt ;	# live variables = {numPlayers,this}
_L57:
	_tmp457 = 1 ;	# live variables = {numPlayers,this}
	_tmp458 = _tmp457 + numPlayers ;	# live variables = {numPlayers,_tmp457,this}
	_tmp459 = 4 ;	# live variables = {numPlayers,_tmp458,this}
	_tmp460 = _tmp458 * _tmp459 ;	# live variables = {numPlayers,_tmp458,_tmp459,this}
	PushParam _tmp460 ;	# live variables = {numPlayers,_tmp459,_tmp460,this}
	_tmp461 = LCall _Alloc ;	# live variables = {numPlayers,_tmp459,this}
	PopParams 4 ;	# live variables = {numPlayers,_tmp459,_tmp461,this}
	*(_tmp461) = numPlayers ;	# live variables = {numPlayers,_tmp459,_tmp461,this}
	_tmp462 = _tmp461 + _tmp459 ;	# live variables = {_tmp459,_tmp461,this}
	*(this + 4) = _tmp462 ;	# live variables = {_tmp462,this}
	_tmp463 = 0 ;	# live variables = {this}
	i = _tmp463 ;	# live variables = {_tmp463,this}
_L58:
	_tmp464 = *(this + 4) ;	# live variables = {i,this}
	_tmp465 = *(_tmp464 + -4) ;	# live variables = {i,_tmp464,this}
	_tmp466 = i < _tmp465 ;	# live variables = {i,_tmp465,this}
	IfZ _tmp466 Goto _L59 ;	# live variables = {i,_tmp466,this}
	_tmp467 = *(this + 4) ;	# live variables = {i,this}
	_tmp468 = 0 ;	# live variables = {i,_tmp467,this}
	_tmp469 = i < _tmp468 ;	# live variables = {i,_tmp467,_tmp468,this}
	_tmp470 = *(_tmp467 + -4) ;	# live variables = {i,_tmp467,_tmp468,_tmp469,this}
	_tmp471 = i < _tmp470 ;	# live variables = {i,_tmp467,_tmp468,_tmp469,_tmp470,this}
	_tmp472 = _tmp471 == _tmp468 ;	# live variables = {i,_tmp467,_tmp468,_tmp469,_tmp471,this}
	_tmp473 = _tmp469 || _tmp472 ;	# live variables = {i,_tmp467,_tmp469,_tmp472,this}
	IfZ _tmp473 Goto _L60 ;	# live variables = {i,_tmp467,_tmp473,this}
	_tmp474 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp467,this}
	PushParam _tmp474 ;	# live variables = {i,_tmp467,_tmp474,this}
	LCall _PrintString ;	# live variables = {i,_tmp467,this}
	PopParams 4 ;	# live variables = {i,_tmp467,this}
	LCall _Halt ;	# live variables = {i,_tmp467,this}
_L60:
	_tmp475 = 4 ;	# live variables = {i,_tmp467,this}
	_tmp476 = _tmp475 * i ;	# live variables = {i,_tmp467,_tmp475,this}
	_tmp477 = _tmp467 + _tmp476 ;	# live variables = {i,_tmp467,_tmp476,this}
	_tmp478 = 28 ;	# live variables = {i,_tmp477,this}
	PushParam _tmp478 ;	# live variables = {i,_tmp477,_tmp478,this}
	_tmp479 = LCall _Alloc ;	# live variables = {i,_tmp477,this}
	PopParams 4 ;	# live variables = {i,_tmp477,_tmp479,this}
	_tmp480 = Player ;	# live variables = {i,_tmp477,_tmp479,this}
	*(_tmp479) = _tmp480 ;	# live variables = {i,_tmp477,_tmp479,_tmp480,this}
	*(_tmp477) = _tmp479 ;	# live variables = {i,_tmp477,_tmp479,this}
	_tmp481 = 1 ;	# live variables = {i,this}
	_tmp482 = i + _tmp481 ;	# live variables = {i,_tmp481,this}
	_tmp483 = *(this + 4) ;	# live variables = {i,_tmp482,this}
	_tmp484 = 0 ;	# live variables = {i,_tmp482,_tmp483,this}
	_tmp485 = i < _tmp484 ;	# live variables = {i,_tmp482,_tmp483,_tmp484,this}
	_tmp486 = *(_tmp483 + -4) ;	# live variables = {i,_tmp482,_tmp483,_tmp484,_tmp485,this}
	_tmp487 = i < _tmp486 ;	# live variables = {i,_tmp482,_tmp483,_tmp484,_tmp485,_tmp486,this}
	_tmp488 = _tmp487 == _tmp484 ;	# live variables = {i,_tmp482,_tmp483,_tmp484,_tmp485,_tmp487,this}
	_tmp489 = _tmp485 || _tmp488 ;	# live variables = {i,_tmp482,_tmp483,_tmp485,_tmp488,this}
	IfZ _tmp489 Goto _L61 ;	# live variables = {i,_tmp482,_tmp483,_tmp489,this}
	_tmp490 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp482,_tmp483,this}
	PushParam _tmp490 ;	# live variables = {i,_tmp482,_tmp483,_tmp490,this}
	LCall _PrintString ;	# live variables = {i,_tmp482,_tmp483,this}
	PopParams 4 ;	# live variables = {i,_tmp482,_tmp483,this}
	LCall _Halt ;	# live variables = {i,_tmp482,_tmp483,this}
_L61:
	_tmp491 = 4 ;	# live variables = {i,_tmp482,_tmp483,this}
	_tmp492 = _tmp491 * i ;	# live variables = {i,_tmp482,_tmp483,_tmp491,this}
	_tmp493 = _tmp483 + _tmp492 ;	# live variables = {i,_tmp482,_tmp483,_tmp492,this}
	_tmp494 = *(_tmp493) ;	# live variables = {i,_tmp482,_tmp493,this}
	_tmp495 = *(_tmp494) ;	# live variables = {i,_tmp482,_tmp494,this}
	_tmp496 = *(_tmp495) ;	# live variables = {i,_tmp482,_tmp494,_tmp495,this}
	PushParam _tmp482 ;	# live variables = {i,_tmp482,_tmp494,_tmp496,this}
	PushParam _tmp494 ;	# live variables = {i,_tmp494,_tmp496,this}
	ACall _tmp496 ;	# live variables = {i,_tmp496,this}
	PopParams 8 ;	# live variables = {i,this}
	_tmp497 = 1 ;	# live variables = {i,this}
	_tmp498 = i + _tmp497 ;	# live variables = {i,_tmp497,this}
	i = _tmp498 ;	# live variables = {_tmp498,this}
	Goto _L58 ;	# live variables = {i,this}
_L59:
	EndFunc ;	# live variables = {}
_House.TakeAllBets:
	BeginFunc 148 ;	# live variables = {this}
	_tmp499 = "\nFirst, let's take bets.\n" ;	# live variables = {this}
	PushParam _tmp499 ;	# live variables = {_tmp499,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp500 = 0 ;	# live variables = {this}
	i = _tmp500 ;	# live variables = {_tmp500,this}
_L62:
	_tmp501 = *(this + 4) ;	# live variables = {i,this}
	_tmp502 = *(_tmp501 + -4) ;	# live variables = {i,_tmp501,this}
	_tmp503 = i < _tmp502 ;	# live variables = {i,_tmp502,this}
	IfZ _tmp503 Goto _L63 ;	# live variables = {i,_tmp503,this}
	_tmp504 = *(this + 4) ;	# live variables = {i,this}
	_tmp505 = 0 ;	# live variables = {i,_tmp504,this}
	_tmp506 = i < _tmp505 ;	# live variables = {i,_tmp504,_tmp505,this}
	_tmp507 = *(_tmp504 + -4) ;	# live variables = {i,_tmp504,_tmp505,_tmp506,this}
	_tmp508 = i < _tmp507 ;	# live variables = {i,_tmp504,_tmp505,_tmp506,_tmp507,this}
	_tmp509 = _tmp508 == _tmp505 ;	# live variables = {i,_tmp504,_tmp505,_tmp506,_tmp508,this}
	_tmp510 = _tmp506 || _tmp509 ;	# live variables = {i,_tmp504,_tmp506,_tmp509,this}
	IfZ _tmp510 Goto _L64 ;	# live variables = {i,_tmp504,_tmp510,this}
	_tmp511 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp504,this}
	PushParam _tmp511 ;	# live variables = {i,_tmp504,_tmp511,this}
	LCall _PrintString ;	# live variables = {i,_tmp504,this}
	PopParams 4 ;	# live variables = {i,_tmp504,this}
	LCall _Halt ;	# live variables = {i,_tmp504,this}
_L64:
	_tmp512 = 4 ;	# live variables = {i,_tmp504,this}
	_tmp513 = _tmp512 * i ;	# live variables = {i,_tmp504,_tmp512,this}
	_tmp514 = _tmp504 + _tmp513 ;	# live variables = {i,_tmp504,_tmp513,this}
	_tmp515 = *(_tmp514) ;	# live variables = {i,_tmp514,this}
	_tmp516 = *(_tmp515) ;	# live variables = {i,_tmp515,this}
	_tmp517 = *(_tmp516 + 16) ;	# live variables = {i,_tmp515,_tmp516,this}
	PushParam _tmp515 ;	# live variables = {i,_tmp515,_tmp517,this}
	_tmp518 = ACall _tmp517 ;	# live variables = {i,_tmp517,this}
	PopParams 4 ;	# live variables = {i,_tmp518,this}
	IfZ _tmp518 Goto _L65 ;	# live variables = {i,_tmp518,this}
	_tmp519 = *(this + 4) ;	# live variables = {i,this}
	_tmp520 = 0 ;	# live variables = {i,_tmp519,this}
	_tmp521 = i < _tmp520 ;	# live variables = {i,_tmp519,_tmp520,this}
	_tmp522 = *(_tmp519 + -4) ;	# live variables = {i,_tmp519,_tmp520,_tmp521,this}
	_tmp523 = i < _tmp522 ;	# live variables = {i,_tmp519,_tmp520,_tmp521,_tmp522,this}
	_tmp524 = _tmp523 == _tmp520 ;	# live variables = {i,_tmp519,_tmp520,_tmp521,_tmp523,this}
	_tmp525 = _tmp521 || _tmp524 ;	# live variables = {i,_tmp519,_tmp521,_tmp524,this}
	IfZ _tmp525 Goto _L66 ;	# live variables = {i,_tmp519,_tmp525,this}
	_tmp526 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp519,this}
	PushParam _tmp526 ;	# live variables = {i,_tmp519,_tmp526,this}
	LCall _PrintString ;	# live variables = {i,_tmp519,this}
	PopParams 4 ;	# live variables = {i,_tmp519,this}
	LCall _Halt ;	# live variables = {i,_tmp519,this}
_L66:
	_tmp527 = 4 ;	# live variables = {i,_tmp519,this}
	_tmp528 = _tmp527 * i ;	# live variables = {i,_tmp519,_tmp527,this}
	_tmp529 = _tmp519 + _tmp528 ;	# live variables = {i,_tmp519,_tmp528,this}
	_tmp530 = *(_tmp529) ;	# live variables = {i,_tmp529,this}
	_tmp531 = *(_tmp530) ;	# live variables = {i,_tmp530,this}
	_tmp532 = *(_tmp531 + 24) ;	# live variables = {i,_tmp530,_tmp531,this}
	PushParam _tmp530 ;	# live variables = {i,_tmp530,_tmp532,this}
	ACall _tmp532 ;	# live variables = {i,_tmp532,this}
	PopParams 4 ;	# live variables = {i,this}
_L65:
	_tmp533 = 1 ;	# live variables = {i,this}
	_tmp534 = i + _tmp533 ;	# live variables = {i,_tmp533,this}
	i = _tmp534 ;	# live variables = {_tmp534,this}
	Goto _L62 ;	# live variables = {i,this}
_L63:
	EndFunc ;	# live variables = {}
_House.TakeAllTurns:
	BeginFunc 148 ;	# live variables = {this}
	_tmp535 = 0 ;	# live variables = {this}
	i = _tmp535 ;	# live variables = {_tmp535,this}
_L67:
	_tmp536 = *(this + 4) ;	# live variables = {i,this}
	_tmp537 = *(_tmp536 + -4) ;	# live variables = {i,_tmp536,this}
	_tmp538 = i < _tmp537 ;	# live variables = {i,_tmp537,this}
	IfZ _tmp538 Goto _L68 ;	# live variables = {i,_tmp538,this}
	_tmp539 = *(this + 4) ;	# live variables = {i,this}
	_tmp540 = 0 ;	# live variables = {i,_tmp539,this}
	_tmp541 = i < _tmp540 ;	# live variables = {i,_tmp539,_tmp540,this}
	_tmp542 = *(_tmp539 + -4) ;	# live variables = {i,_tmp539,_tmp540,_tmp541,this}
	_tmp543 = i < _tmp542 ;	# live variables = {i,_tmp539,_tmp540,_tmp541,_tmp542,this}
	_tmp544 = _tmp543 == _tmp540 ;	# live variables = {i,_tmp539,_tmp540,_tmp541,_tmp543,this}
	_tmp545 = _tmp541 || _tmp544 ;	# live variables = {i,_tmp539,_tmp541,_tmp544,this}
	IfZ _tmp545 Goto _L69 ;	# live variables = {i,_tmp539,_tmp545,this}
	_tmp546 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp539,this}
	PushParam _tmp546 ;	# live variables = {i,_tmp539,_tmp546,this}
	LCall _PrintString ;	# live variables = {i,_tmp539,this}
	PopParams 4 ;	# live variables = {i,_tmp539,this}
	LCall _Halt ;	# live variables = {i,_tmp539,this}
_L69:
	_tmp547 = 4 ;	# live variables = {i,_tmp539,this}
	_tmp548 = _tmp547 * i ;	# live variables = {i,_tmp539,_tmp547,this}
	_tmp549 = _tmp539 + _tmp548 ;	# live variables = {i,_tmp539,_tmp548,this}
	_tmp550 = *(_tmp549) ;	# live variables = {i,_tmp549,this}
	_tmp551 = *(_tmp550) ;	# live variables = {i,_tmp550,this}
	_tmp552 = *(_tmp551 + 16) ;	# live variables = {i,_tmp550,_tmp551,this}
	PushParam _tmp550 ;	# live variables = {i,_tmp550,_tmp552,this}
	_tmp553 = ACall _tmp552 ;	# live variables = {i,_tmp552,this}
	PopParams 4 ;	# live variables = {i,_tmp553,this}
	IfZ _tmp553 Goto _L70 ;	# live variables = {i,_tmp553,this}
	_tmp554 = *(this + 12) ;	# live variables = {i,this}
	_tmp555 = *(this + 4) ;	# live variables = {i,_tmp554,this}
	_tmp556 = 0 ;	# live variables = {i,_tmp554,_tmp555,this}
	_tmp557 = i < _tmp556 ;	# live variables = {i,_tmp554,_tmp555,_tmp556,this}
	_tmp558 = *(_tmp555 + -4) ;	# live variables = {i,_tmp554,_tmp555,_tmp556,_tmp557,this}
	_tmp559 = i < _tmp558 ;	# live variables = {i,_tmp554,_tmp555,_tmp556,_tmp557,_tmp558,this}
	_tmp560 = _tmp559 == _tmp556 ;	# live variables = {i,_tmp554,_tmp555,_tmp556,_tmp557,_tmp559,this}
	_tmp561 = _tmp557 || _tmp560 ;	# live variables = {i,_tmp554,_tmp555,_tmp557,_tmp560,this}
	IfZ _tmp561 Goto _L71 ;	# live variables = {i,_tmp554,_tmp555,_tmp561,this}
	_tmp562 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp554,_tmp555,this}
	PushParam _tmp562 ;	# live variables = {i,_tmp554,_tmp555,_tmp562,this}
	LCall _PrintString ;	# live variables = {i,_tmp554,_tmp555,this}
	PopParams 4 ;	# live variables = {i,_tmp554,_tmp555,this}
	LCall _Halt ;	# live variables = {i,_tmp554,_tmp555,this}
_L71:
	_tmp563 = 4 ;	# live variables = {i,_tmp554,_tmp555,this}
	_tmp564 = _tmp563 * i ;	# live variables = {i,_tmp554,_tmp555,_tmp563,this}
	_tmp565 = _tmp555 + _tmp564 ;	# live variables = {i,_tmp554,_tmp555,_tmp564,this}
	_tmp566 = *(_tmp565) ;	# live variables = {i,_tmp554,_tmp565,this}
	_tmp567 = *(_tmp566) ;	# live variables = {i,_tmp554,_tmp566,this}
	_tmp568 = *(_tmp567 + 12) ;	# live variables = {i,_tmp554,_tmp566,_tmp567,this}
	PushParam _tmp554 ;	# live variables = {i,_tmp554,_tmp566,_tmp568,this}
	PushParam _tmp566 ;	# live variables = {i,_tmp566,_tmp568,this}
	ACall _tmp568 ;	# live variables = {i,_tmp568,this}
	PopParams 8 ;	# live variables = {i,this}
_L70:
	_tmp569 = 1 ;	# live variables = {i,this}
	_tmp570 = i + _tmp569 ;	# live variables = {i,_tmp569,this}
	i = _tmp570 ;	# live variables = {_tmp570,this}
	Goto _L67 ;	# live variables = {i,this}
_L68:
	EndFunc ;	# live variables = {}
_House.ResolveAllPlayers:
	BeginFunc 164 ;	# live variables = {this}
	_tmp571 = "\nTime to resolve bets.\n" ;	# live variables = {this}
	PushParam _tmp571 ;	# live variables = {_tmp571,this}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp572 = 0 ;	# live variables = {this}
	i = _tmp572 ;	# live variables = {_tmp572,this}
_L72:
	_tmp573 = *(this + 4) ;	# live variables = {i,this}
	_tmp574 = *(_tmp573 + -4) ;	# live variables = {i,_tmp573,this}
	_tmp575 = i < _tmp574 ;	# live variables = {i,_tmp574,this}
	IfZ _tmp575 Goto _L73 ;	# live variables = {i,_tmp575,this}
	_tmp576 = *(this + 4) ;	# live variables = {i,this}
	_tmp577 = 0 ;	# live variables = {i,_tmp576,this}
	_tmp578 = i < _tmp577 ;	# live variables = {i,_tmp576,_tmp577,this}
	_tmp579 = *(_tmp576 + -4) ;	# live variables = {i,_tmp576,_tmp577,_tmp578,this}
	_tmp580 = i < _tmp579 ;	# live variables = {i,_tmp576,_tmp577,_tmp578,_tmp579,this}
	_tmp581 = _tmp580 == _tmp577 ;	# live variables = {i,_tmp576,_tmp577,_tmp578,_tmp580,this}
	_tmp582 = _tmp578 || _tmp581 ;	# live variables = {i,_tmp576,_tmp578,_tmp581,this}
	IfZ _tmp582 Goto _L74 ;	# live variables = {i,_tmp576,_tmp582,this}
	_tmp583 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp576,this}
	PushParam _tmp583 ;	# live variables = {i,_tmp576,_tmp583,this}
	LCall _PrintString ;	# live variables = {i,_tmp576,this}
	PopParams 4 ;	# live variables = {i,_tmp576,this}
	LCall _Halt ;	# live variables = {i,_tmp576,this}
_L74:
	_tmp584 = 4 ;	# live variables = {i,_tmp576,this}
	_tmp585 = _tmp584 * i ;	# live variables = {i,_tmp576,_tmp584,this}
	_tmp586 = _tmp576 + _tmp585 ;	# live variables = {i,_tmp576,_tmp585,this}
	_tmp587 = *(_tmp586) ;	# live variables = {i,_tmp586,this}
	_tmp588 = *(_tmp587) ;	# live variables = {i,_tmp587,this}
	_tmp589 = *(_tmp588 + 16) ;	# live variables = {i,_tmp587,_tmp588,this}
	PushParam _tmp587 ;	# live variables = {i,_tmp587,_tmp589,this}
	_tmp590 = ACall _tmp589 ;	# live variables = {i,_tmp589,this}
	PopParams 4 ;	# live variables = {i,_tmp590,this}
	IfZ _tmp590 Goto _L75 ;	# live variables = {i,_tmp590,this}
	_tmp591 = *(this + 8) ;	# live variables = {i,this}
	_tmp592 = *(_tmp591) ;	# live variables = {i,_tmp591,this}
	_tmp593 = *(_tmp592 + 28) ;	# live variables = {i,_tmp591,_tmp592,this}
	PushParam _tmp591 ;	# live variables = {i,_tmp591,_tmp593,this}
	_tmp594 = ACall _tmp593 ;	# live variables = {i,_tmp593,this}
	PopParams 4 ;	# live variables = {i,_tmp594,this}
	_tmp595 = *(this + 4) ;	# live variables = {i,_tmp594,this}
	_tmp596 = 0 ;	# live variables = {i,_tmp594,_tmp595,this}
	_tmp597 = i < _tmp596 ;	# live variables = {i,_tmp594,_tmp595,_tmp596,this}
	_tmp598 = *(_tmp595 + -4) ;	# live variables = {i,_tmp594,_tmp595,_tmp596,_tmp597,this}
	_tmp599 = i < _tmp598 ;	# live variables = {i,_tmp594,_tmp595,_tmp596,_tmp597,_tmp598,this}
	_tmp600 = _tmp599 == _tmp596 ;	# live variables = {i,_tmp594,_tmp595,_tmp596,_tmp597,_tmp599,this}
	_tmp601 = _tmp597 || _tmp600 ;	# live variables = {i,_tmp594,_tmp595,_tmp597,_tmp600,this}
	IfZ _tmp601 Goto _L76 ;	# live variables = {i,_tmp594,_tmp595,_tmp601,this}
	_tmp602 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,_tmp594,_tmp595,this}
	PushParam _tmp602 ;	# live variables = {i,_tmp594,_tmp595,_tmp602,this}
	LCall _PrintString ;	# live variables = {i,_tmp594,_tmp595,this}
	PopParams 4 ;	# live variables = {i,_tmp594,_tmp595,this}
	LCall _Halt ;	# live variables = {i,_tmp594,_tmp595,this}
_L76:
	_tmp603 = 4 ;	# live variables = {i,_tmp594,_tmp595,this}
	_tmp604 = _tmp603 * i ;	# live variables = {i,_tmp594,_tmp595,_tmp603,this}
	_tmp605 = _tmp595 + _tmp604 ;	# live variables = {i,_tmp594,_tmp595,this,_tmp604}
	_tmp606 = *(_tmp605) ;	# live variables = {i,_tmp594,this,_tmp605}
	_tmp607 = *(_tmp606) ;	# live variables = {i,_tmp594,this,_tmp606}
	_tmp608 = *(_tmp607 + 32) ;	# live variables = {i,_tmp594,this,_tmp606,_tmp607}
	PushParam _tmp594 ;	# live variables = {i,_tmp594,this,_tmp606,_tmp608}
	PushParam _tmp606 ;	# live variables = {i,this,_tmp606,_tmp608}
	ACall _tmp608 ;	# live variables = {i,this,_tmp608}
	PopParams 8 ;	# live variables = {i,this}
_L75:
	_tmp609 = 1 ;	# live variables = {i,this}
	_tmp610 = i + _tmp609 ;	# live variables = {i,this,_tmp609}
	i = _tmp610 ;	# live variables = {this,_tmp610}
	Goto _L72 ;	# live variables = {i,this}
_L73:
	EndFunc ;	# live variables = {}
_House.PrintAllMoney:
	BeginFunc 84 ;	# live variables = {this}
	_tmp611 = 0 ;	# live variables = {this}
	i = _tmp611 ;	# live variables = {this,_tmp611}
_L77:
	_tmp612 = *(this + 4) ;	# live variables = {this,i}
	_tmp613 = *(_tmp612 + -4) ;	# live variables = {this,i,_tmp612}
	_tmp614 = i < _tmp613 ;	# live variables = {this,i,_tmp613}
	IfZ _tmp614 Goto _L78 ;	# live variables = {this,i,_tmp614}
	_tmp615 = *(this + 4) ;	# live variables = {this,i}
	_tmp616 = 0 ;	# live variables = {this,i,_tmp615}
	_tmp617 = i < _tmp616 ;	# live variables = {this,i,_tmp615,_tmp616}
	_tmp618 = *(_tmp615 + -4) ;	# live variables = {this,i,_tmp615,_tmp616,_tmp617}
	_tmp619 = i < _tmp618 ;	# live variables = {this,i,_tmp615,_tmp616,_tmp617,_tmp618}
	_tmp620 = _tmp619 == _tmp616 ;	# live variables = {this,i,_tmp615,_tmp616,_tmp617,_tmp619}
	_tmp621 = _tmp617 || _tmp620 ;	# live variables = {this,i,_tmp615,_tmp617,_tmp620}
	IfZ _tmp621 Goto _L79 ;	# live variables = {this,i,_tmp615,_tmp621}
	_tmp622 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,i,_tmp615}
	PushParam _tmp622 ;	# live variables = {this,i,_tmp615,_tmp622}
	LCall _PrintString ;	# live variables = {this,i,_tmp615}
	PopParams 4 ;	# live variables = {this,i,_tmp615}
	LCall _Halt ;	# live variables = {this,i,_tmp615}
_L79:
	_tmp623 = 4 ;	# live variables = {this,i,_tmp615}
	_tmp624 = _tmp623 * i ;	# live variables = {this,i,_tmp615,_tmp623}
	_tmp625 = _tmp615 + _tmp624 ;	# live variables = {this,i,_tmp615,_tmp624}
	_tmp626 = *(_tmp625) ;	# live variables = {this,i,_tmp625}
	_tmp627 = *(_tmp626) ;	# live variables = {this,i,_tmp626}
	_tmp628 = *(_tmp627 + 20) ;	# live variables = {this,i,_tmp626,_tmp627}
	PushParam _tmp626 ;	# live variables = {this,i,_tmp626,_tmp628}
	ACall _tmp628 ;	# live variables = {this,i,_tmp628}
	PopParams 4 ;	# live variables = {this,i}
	_tmp629 = 1 ;	# live variables = {this,i}
	_tmp630 = i + _tmp629 ;	# live variables = {this,i,_tmp629}
	i = _tmp630 ;	# live variables = {this,_tmp630}
	Goto _L77 ;	# live variables = {this,i}
_L78:
	EndFunc ;	# live variables = {}
_House.PlayOneGame:
	BeginFunc 112 ;	# live variables = {this}
	_tmp631 = *(this + 12) ;	# live variables = {this}
	_tmp632 = *(_tmp631) ;	# live variables = {this,_tmp631}
	_tmp633 = *(_tmp632 + 12) ;	# live variables = {this,_tmp631,_tmp632}
	PushParam _tmp631 ;	# live variables = {this,_tmp631,_tmp633}
	_tmp634 = ACall _tmp633 ;	# live variables = {this,_tmp633}
	PopParams 4 ;	# live variables = {this,_tmp634}
	_tmp635 = 26 ;	# live variables = {this,_tmp634}
	_tmp636 = _tmp634 < _tmp635 ;	# live variables = {this,_tmp634,_tmp635}
	IfZ _tmp636 Goto _L80 ;	# live variables = {this,_tmp636}
	_tmp637 = *(this + 12) ;	# live variables = {this}
	_tmp638 = *(_tmp637) ;	# live variables = {this,_tmp637}
	_tmp639 = *(_tmp638 + 8) ;	# live variables = {this,_tmp637,_tmp638}
	PushParam _tmp637 ;	# live variables = {this,_tmp637,_tmp639}
	ACall _tmp639 ;	# live variables = {this,_tmp639}
	PopParams 4 ;	# live variables = {this}
_L80:
	_tmp640 = *(this) ;	# live variables = {this}
	_tmp641 = *(_tmp640 + 8) ;	# live variables = {this,_tmp640}
	PushParam this ;	# live variables = {this,_tmp641}
	ACall _tmp641 ;	# live variables = {this,_tmp641}
	PopParams 4 ;	# live variables = {this}
	_tmp642 = "\nDealer starts. " ;	# live variables = {this}
	PushParam _tmp642 ;	# live variables = {this,_tmp642}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp643 = 0 ;	# live variables = {this}
	_tmp644 = *(this + 8) ;	# live variables = {this,_tmp643}
	_tmp645 = *(_tmp644) ;	# live variables = {this,_tmp643,_tmp644}
	_tmp646 = *(_tmp645) ;	# live variables = {this,_tmp643,_tmp644,_tmp645}
	PushParam _tmp643 ;	# live variables = {this,_tmp643,_tmp644,_tmp646}
	PushParam _tmp644 ;	# live variables = {this,_tmp644,_tmp646}
	ACall _tmp646 ;	# live variables = {this,_tmp646}
	PopParams 8 ;	# live variables = {this}
	_tmp647 = *(this + 12) ;	# live variables = {this}
	_tmp648 = *(this + 8) ;	# live variables = {this,_tmp647}
	_tmp649 = *(_tmp648) ;	# live variables = {this,_tmp647,_tmp648}
	_tmp650 = *(_tmp649 + 4) ;	# live variables = {this,_tmp647,_tmp648,_tmp649}
	PushParam _tmp647 ;	# live variables = {this,_tmp647,_tmp648,_tmp650}
	PushParam _tmp648 ;	# live variables = {this,_tmp648,_tmp650}
	ACall _tmp650 ;	# live variables = {this,_tmp650}
	PopParams 8 ;	# live variables = {this}
	_tmp651 = *(this) ;	# live variables = {this}
	_tmp652 = *(_tmp651 + 12) ;	# live variables = {this,_tmp651}
	PushParam this ;	# live variables = {this,_tmp652}
	ACall _tmp652 ;	# live variables = {this,_tmp652}
	PopParams 4 ;	# live variables = {this}
	_tmp653 = *(this + 12) ;	# live variables = {this}
	_tmp654 = *(this + 8) ;	# live variables = {this,_tmp653}
	_tmp655 = *(_tmp654) ;	# live variables = {this,_tmp653,_tmp654}
	_tmp656 = *(_tmp655 + 12) ;	# live variables = {this,_tmp653,_tmp654,_tmp655}
	PushParam _tmp653 ;	# live variables = {this,_tmp653,_tmp654,_tmp656}
	PushParam _tmp654 ;	# live variables = {this,_tmp654,_tmp656}
	ACall _tmp656 ;	# live variables = {this,_tmp656}
	PopParams 8 ;	# live variables = {this}
	_tmp657 = *(this) ;	# live variables = {this}
	_tmp658 = *(_tmp657 + 16) ;	# live variables = {this,_tmp657}
	PushParam this ;	# live variables = {this,_tmp658}
	ACall _tmp658 ;	# live variables = {_tmp658}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
VTable House =
	_House.SetupGame,
	_House.SetupPlayers,
	_House.TakeAllBets,
	_House.TakeAllTurns,
	_House.ResolveAllPlayers,
	_House.PrintAllMoney,
	_House.PlayOneGame,
; 
_GetYesOrNo:
	BeginFunc 32 ;	# live variables = {prompt}
	PushParam prompt ;	# live variables = {prompt}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp659 = " (y/n) " ;	# live variables = {}
	PushParam _tmp659 ;	# live variables = {_tmp659}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp660 = LCall _ReadLine ;	# live variables = {}
	answer = _tmp660 ;	# live variables = {_tmp660}
	_tmp661 = "y" ;	# live variables = {answer}
	PushParam _tmp661 ;	# live variables = {answer,_tmp661}
	PushParam answer ;	# live variables = {answer}
	_tmp662 = LCall _StringEqual ;	# live variables = {answer}
	PopParams 8 ;	# live variables = {answer,_tmp662}
	_tmp663 = "Y" ;	# live variables = {answer,_tmp662}
	PushParam _tmp663 ;	# live variables = {answer,_tmp662,_tmp663}
	PushParam answer ;	# live variables = {answer,_tmp662}
	_tmp664 = LCall _StringEqual ;	# live variables = {_tmp662}
	PopParams 8 ;	# live variables = {_tmp662,_tmp664}
	_tmp665 = _tmp662 || _tmp664 ;	# live variables = {_tmp662,_tmp664}
	Return _tmp665 ;	# live variables = {_tmp665}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 76 ;	# live variables = {}
	_tmp666 = 1 ;	# live variables = {}
	keepPlaying = _tmp666 ;	# live variables = {_tmp666}
	_tmp667 = 16 ;	# live variables = {keepPlaying}
	PushParam _tmp667 ;	# live variables = {keepPlaying,_tmp667}
	_tmp668 = LCall _Alloc ;	# live variables = {keepPlaying}
	PopParams 4 ;	# live variables = {keepPlaying,_tmp668}
	_tmp669 = House ;	# live variables = {keepPlaying,_tmp668}
	*(_tmp668) = _tmp669 ;	# live variables = {keepPlaying,_tmp668,_tmp669}
	house = _tmp668 ;	# live variables = {keepPlaying,_tmp668}
	_tmp670 = *(house) ;	# live variables = {keepPlaying,house}
	_tmp671 = *(_tmp670) ;	# live variables = {keepPlaying,house,_tmp670}
	PushParam house ;	# live variables = {keepPlaying,house,_tmp671}
	ACall _tmp671 ;	# live variables = {keepPlaying,house,_tmp671}
	PopParams 4 ;	# live variables = {keepPlaying,house}
	_tmp672 = *(house) ;	# live variables = {keepPlaying,house}
	_tmp673 = *(_tmp672 + 4) ;	# live variables = {keepPlaying,house,_tmp672}
	PushParam house ;	# live variables = {keepPlaying,house,_tmp673}
	ACall _tmp673 ;	# live variables = {keepPlaying,house,_tmp673}
	PopParams 4 ;	# live variables = {keepPlaying,house}
_L81:
	IfZ keepPlaying Goto _L82 ;	# live variables = {keepPlaying,house}
	_tmp674 = *(house) ;	# live variables = {house}
	_tmp675 = *(_tmp674 + 24) ;	# live variables = {house,_tmp674}
	PushParam house ;	# live variables = {house,_tmp675}
	ACall _tmp675 ;	# live variables = {house,_tmp675}
	PopParams 4 ;	# live variables = {house}
	_tmp676 = "\nDo you want to play another hand?" ;	# live variables = {house}
	PushParam _tmp676 ;	# live variables = {house,_tmp676}
	_tmp677 = LCall _GetYesOrNo ;	# live variables = {house}
	PopParams 4 ;	# live variables = {house,_tmp677}
	keepPlaying = _tmp677 ;	# live variables = {house,_tmp677}
	Goto _L81 ;	# live variables = {keepPlaying,house}
_L82:
	_tmp678 = *(house) ;	# live variables = {house}
	_tmp679 = *(_tmp678 + 20) ;	# live variables = {house,_tmp678}
	PushParam house ;	# live variables = {house,_tmp679}
	ACall _tmp679 ;	# live variables = {_tmp679}
	PopParams 4 ;	# live variables = {}
	_tmp680 = "Thank you for playing...come again soon.\n" ;	# live variables = {}
	PushParam _tmp680 ;	# live variables = {_tmp680}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp681 = "\nCS143 BlackJack Copyright (c) 1999 by Peter Mor..." ;	# live variables = {}
	PushParam _tmp681 ;	# live variables = {_tmp681}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp682 = "(2001 mods by jdz)\n" ;	# live variables = {}
	PushParam _tmp682 ;	# live variables = {_tmp682}
	LCall _PrintString ;	# live variables = {}
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
