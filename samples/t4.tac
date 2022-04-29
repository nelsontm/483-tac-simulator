_Binky:
	BeginFunc 92 ;	# live variables = {b,c}
	_tmp0 = 0 ;	# live variables = {b,c}
	_tmp1 = 0 ;	# live variables = {b,c,_tmp0}
	_tmp2 = _tmp0 < _tmp1 ;	# live variables = {b,c,_tmp0,_tmp1}
	_tmp3 = *(c + -4) ;	# live variables = {b,c,_tmp0,_tmp1,_tmp2}
	_tmp4 = _tmp0 < _tmp3 ;	# live variables = {b,c,_tmp0,_tmp1,_tmp2,_tmp3}
	_tmp5 = _tmp4 == _tmp1 ;	# live variables = {b,c,_tmp0,_tmp1,_tmp2,_tmp4}
	_tmp6 = _tmp2 || _tmp5 ;	# live variables = {b,c,_tmp0,_tmp2,_tmp5}
	IfZ _tmp6 Goto _L0 ;	# live variables = {b,c,_tmp0,_tmp6}
	_tmp7 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,c,_tmp0}
	PushParam _tmp7 ;	# live variables = {b,c,_tmp0,_tmp7}
	LCall _PrintString ;	# live variables = {b,c,_tmp0}
	PopParams 4 ;	# live variables = {b,c,_tmp0}
	LCall _Halt ;	# live variables = {b,c,_tmp0}
_L0:
	_tmp8 = 4 ;	# live variables = {b,c,_tmp0}
	_tmp9 = _tmp8 * _tmp0 ;	# live variables = {b,c,_tmp0,_tmp8}
	_tmp10 = c + _tmp9 ;	# live variables = {b,c,_tmp9}
	_tmp11 = *(_tmp10) ;	# live variables = {b,_tmp10}
	_tmp12 = 0 ;	# live variables = {b,_tmp11}
	_tmp13 = _tmp11 < _tmp12 ;	# live variables = {b,_tmp11,_tmp12}
	_tmp14 = *(b + -4) ;	# live variables = {b,_tmp11,_tmp12,_tmp13}
	_tmp15 = _tmp11 < _tmp14 ;	# live variables = {b,_tmp11,_tmp12,_tmp13,_tmp14}
	_tmp16 = _tmp15 == _tmp12 ;	# live variables = {b,_tmp11,_tmp12,_tmp13,_tmp15}
	_tmp17 = _tmp13 || _tmp16 ;	# live variables = {b,_tmp11,_tmp13,_tmp16}
	IfZ _tmp17 Goto _L1 ;	# live variables = {b,_tmp11,_tmp17}
	_tmp18 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,_tmp11}
	PushParam _tmp18 ;	# live variables = {b,_tmp11,_tmp18}
	LCall _PrintString ;	# live variables = {b,_tmp11}
	PopParams 4 ;	# live variables = {b,_tmp11}
	LCall _Halt ;	# live variables = {b,_tmp11}
_L1:
	_tmp19 = 4 ;	# live variables = {b,_tmp11}
	_tmp20 = _tmp19 * _tmp11 ;	# live variables = {b,_tmp11,_tmp19}
	_tmp21 = b + _tmp20 ;	# live variables = {b,_tmp20}
	_tmp22 = *(_tmp21) ;	# live variables = {_tmp21}
	Return _tmp22 ;	# live variables = {_tmp22}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 508 ;	# live variables = {}
	_tmp23 = 5 ;	# live variables = {}
	_tmp24 = 1 ;	# live variables = {_tmp23}
	_tmp25 = _tmp23 < _tmp24 ;	# live variables = {_tmp23,_tmp24}
	IfZ _tmp25 Goto _L2 ;	# live variables = {_tmp23,_tmp25}
	_tmp26 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {_tmp23}
	PushParam _tmp26 ;	# live variables = {_tmp23,_tmp26}
	LCall _PrintString ;	# live variables = {_tmp23}
	PopParams 4 ;	# live variables = {_tmp23}
	LCall _Halt ;	# live variables = {_tmp23}
_L2:
	_tmp27 = 1 ;	# live variables = {_tmp23}
	_tmp28 = _tmp27 + _tmp23 ;	# live variables = {_tmp23,_tmp27}
	_tmp29 = 4 ;	# live variables = {_tmp23,_tmp28}
	_tmp30 = _tmp28 * _tmp29 ;	# live variables = {_tmp23,_tmp28,_tmp29}
	PushParam _tmp30 ;	# live variables = {_tmp23,_tmp29,_tmp30}
	_tmp31 = LCall _Alloc ;	# live variables = {_tmp23,_tmp29}
	PopParams 4 ;	# live variables = {_tmp23,_tmp29,_tmp31}
	*(_tmp31) = _tmp23 ;	# live variables = {_tmp23,_tmp29,_tmp31}
	_tmp32 = _tmp31 + _tmp29 ;	# live variables = {_tmp29,_tmp31}
	d = _tmp32 ;	# live variables = {_tmp32}
	_tmp33 = 0 ;	# live variables = {d}
	_tmp34 = 0 ;	# live variables = {d,_tmp33}
	_tmp35 = _tmp33 < _tmp34 ;	# live variables = {d,_tmp33,_tmp34}
	_tmp36 = *(d + -4) ;	# live variables = {d,_tmp33,_tmp34,_tmp35}
	_tmp37 = _tmp33 < _tmp36 ;	# live variables = {d,_tmp33,_tmp34,_tmp35,_tmp36}
	_tmp38 = _tmp37 == _tmp34 ;	# live variables = {d,_tmp33,_tmp34,_tmp35,_tmp37}
	_tmp39 = _tmp35 || _tmp38 ;	# live variables = {d,_tmp33,_tmp35,_tmp38}
	IfZ _tmp39 Goto _L3 ;	# live variables = {d,_tmp33,_tmp39}
	_tmp40 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {d,_tmp33}
	PushParam _tmp40 ;	# live variables = {d,_tmp33,_tmp40}
	LCall _PrintString ;	# live variables = {d,_tmp33}
	PopParams 4 ;	# live variables = {d,_tmp33}
	LCall _Halt ;	# live variables = {d,_tmp33}
_L3:
	_tmp41 = 4 ;	# live variables = {d,_tmp33}
	_tmp42 = _tmp41 * _tmp33 ;	# live variables = {d,_tmp33,_tmp41}
	_tmp43 = d + _tmp42 ;	# live variables = {d,_tmp42}
	_tmp44 = 12 ;	# live variables = {d,_tmp43}
	_tmp45 = 1 ;	# live variables = {d,_tmp43,_tmp44}
	_tmp46 = _tmp44 < _tmp45 ;	# live variables = {d,_tmp43,_tmp44,_tmp45}
	IfZ _tmp46 Goto _L4 ;	# live variables = {d,_tmp43,_tmp44,_tmp46}
	_tmp47 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {d,_tmp43,_tmp44}
	PushParam _tmp47 ;	# live variables = {d,_tmp43,_tmp44,_tmp47}
	LCall _PrintString ;	# live variables = {d,_tmp43,_tmp44}
	PopParams 4 ;	# live variables = {d,_tmp43,_tmp44}
	LCall _Halt ;	# live variables = {d,_tmp43,_tmp44}
_L4:
	_tmp48 = 1 ;	# live variables = {d,_tmp43,_tmp44}
	_tmp49 = _tmp48 + _tmp44 ;	# live variables = {d,_tmp43,_tmp44,_tmp48}
	_tmp50 = 4 ;	# live variables = {d,_tmp43,_tmp44,_tmp49}
	_tmp51 = _tmp49 * _tmp50 ;	# live variables = {d,_tmp43,_tmp44,_tmp49,_tmp50}
	PushParam _tmp51 ;	# live variables = {d,_tmp43,_tmp44,_tmp50,_tmp51}
	_tmp52 = LCall _Alloc ;	# live variables = {d,_tmp43,_tmp44,_tmp50}
	PopParams 4 ;	# live variables = {d,_tmp43,_tmp44,_tmp50,_tmp52}
	*(_tmp52) = _tmp44 ;	# live variables = {d,_tmp43,_tmp44,_tmp50,_tmp52}
	_tmp53 = _tmp52 + _tmp50 ;	# live variables = {d,_tmp43,_tmp50,_tmp52}
	*(_tmp43) = _tmp53 ;	# live variables = {d,_tmp43,_tmp53}
	_tmp54 = 10 ;	# live variables = {d}
	_tmp55 = 1 ;	# live variables = {d,_tmp54}
	_tmp56 = _tmp54 < _tmp55 ;	# live variables = {d,_tmp54,_tmp55}
	IfZ _tmp56 Goto _L5 ;	# live variables = {d,_tmp54,_tmp56}
	_tmp57 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {d,_tmp54}
	PushParam _tmp57 ;	# live variables = {d,_tmp54,_tmp57}
	LCall _PrintString ;	# live variables = {d,_tmp54}
	PopParams 4 ;	# live variables = {d,_tmp54}
	LCall _Halt ;	# live variables = {d,_tmp54}
_L5:
	_tmp58 = 1 ;	# live variables = {d,_tmp54}
	_tmp59 = _tmp58 + _tmp54 ;	# live variables = {d,_tmp54,_tmp58}
	_tmp60 = 4 ;	# live variables = {d,_tmp54,_tmp59}
	_tmp61 = _tmp59 * _tmp60 ;	# live variables = {d,_tmp54,_tmp59,_tmp60}
	PushParam _tmp61 ;	# live variables = {d,_tmp54,_tmp60,_tmp61}
	_tmp62 = LCall _Alloc ;	# live variables = {d,_tmp54,_tmp60}
	PopParams 4 ;	# live variables = {d,_tmp54,_tmp60,_tmp62}
	*(_tmp62) = _tmp54 ;	# live variables = {d,_tmp54,_tmp60,_tmp62}
	_tmp63 = _tmp62 + _tmp60 ;	# live variables = {d,_tmp60,_tmp62}
	c = _tmp63 ;	# live variables = {d,_tmp63}
	_tmp64 = 0 ;	# live variables = {c,d}
	_tmp65 = 0 ;	# live variables = {c,d,_tmp64}
	_tmp66 = _tmp64 < _tmp65 ;	# live variables = {c,d,_tmp64,_tmp65}
	_tmp67 = *(c + -4) ;	# live variables = {c,d,_tmp64,_tmp65,_tmp66}
	_tmp68 = _tmp64 < _tmp67 ;	# live variables = {c,d,_tmp64,_tmp65,_tmp66,_tmp67}
	_tmp69 = _tmp68 == _tmp65 ;	# live variables = {c,d,_tmp64,_tmp65,_tmp66,_tmp68}
	_tmp70 = _tmp66 || _tmp69 ;	# live variables = {c,d,_tmp64,_tmp66,_tmp69}
	IfZ _tmp70 Goto _L6 ;	# live variables = {c,d,_tmp64,_tmp70}
	_tmp71 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {c,d,_tmp64}
	PushParam _tmp71 ;	# live variables = {c,d,_tmp64,_tmp71}
	LCall _PrintString ;	# live variables = {c,d,_tmp64}
	PopParams 4 ;	# live variables = {c,d,_tmp64}
	LCall _Halt ;	# live variables = {c,d,_tmp64}
_L6:
	_tmp72 = 4 ;	# live variables = {c,d,_tmp64}
	_tmp73 = _tmp72 * _tmp64 ;	# live variables = {c,d,_tmp64,_tmp72}
	_tmp74 = c + _tmp73 ;	# live variables = {c,d,_tmp73}
	_tmp75 = 4 ;	# live variables = {c,d,_tmp74}
	_tmp76 = 5 ;	# live variables = {c,d,_tmp74,_tmp75}
	_tmp77 = 3 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp76}
	_tmp78 = _tmp76 * _tmp77 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp76,_tmp77}
	_tmp79 = 4 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp78}
	_tmp80 = _tmp78 / _tmp79 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp78,_tmp79}
	_tmp81 = 2 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp80}
	_tmp82 = _tmp80 % _tmp81 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp80,_tmp81}
	_tmp83 = _tmp75 + _tmp82 ;	# live variables = {c,d,_tmp74,_tmp75,_tmp82}
	*(_tmp74) = _tmp83 ;	# live variables = {c,d,_tmp74,_tmp83}
	_tmp84 = 0 ;	# live variables = {c,d}
	_tmp85 = 0 ;	# live variables = {c,d,_tmp84}
	_tmp86 = _tmp84 < _tmp85 ;	# live variables = {c,d,_tmp84,_tmp85}
	_tmp87 = *(d + -4) ;	# live variables = {c,d,_tmp84,_tmp85,_tmp86}
	_tmp88 = _tmp84 < _tmp87 ;	# live variables = {c,d,_tmp84,_tmp85,_tmp86,_tmp87}
	_tmp89 = _tmp88 == _tmp85 ;	# live variables = {c,d,_tmp84,_tmp85,_tmp86,_tmp88}
	_tmp90 = _tmp86 || _tmp89 ;	# live variables = {c,d,_tmp84,_tmp86,_tmp89}
	IfZ _tmp90 Goto _L7 ;	# live variables = {c,d,_tmp84,_tmp90}
	_tmp91 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {c,d,_tmp84}
	PushParam _tmp91 ;	# live variables = {c,d,_tmp84,_tmp91}
	LCall _PrintString ;	# live variables = {c,d,_tmp84}
	PopParams 4 ;	# live variables = {c,d,_tmp84}
	LCall _Halt ;	# live variables = {c,d,_tmp84}
_L7:
	_tmp92 = 4 ;	# live variables = {c,d,_tmp84}
	_tmp93 = _tmp92 * _tmp84 ;	# live variables = {c,d,_tmp84,_tmp92}
	_tmp94 = d + _tmp93 ;	# live variables = {c,d,_tmp93}
	_tmp95 = *(_tmp94) ;	# live variables = {c,d,_tmp94}
	_tmp96 = 0 ;	# live variables = {c,d,_tmp95}
	_tmp97 = 0 ;	# live variables = {c,d,_tmp95,_tmp96}
	_tmp98 = _tmp96 < _tmp97 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp97}
	_tmp99 = *(c + -4) ;	# live variables = {c,d,_tmp95,_tmp96,_tmp97,_tmp98}
	_tmp100 = _tmp96 < _tmp99 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp97,_tmp98,_tmp99}
	_tmp101 = _tmp100 == _tmp97 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp97,_tmp98,_tmp100}
	_tmp102 = _tmp98 || _tmp101 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp98,_tmp101}
	IfZ _tmp102 Goto _L8 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp102}
	_tmp103 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {c,d,_tmp95,_tmp96}
	PushParam _tmp103 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp103}
	LCall _PrintString ;	# live variables = {c,d,_tmp95,_tmp96}
	PopParams 4 ;	# live variables = {c,d,_tmp95,_tmp96}
	LCall _Halt ;	# live variables = {c,d,_tmp95,_tmp96}
_L8:
	_tmp104 = 4 ;	# live variables = {c,d,_tmp95,_tmp96}
	_tmp105 = _tmp104 * _tmp96 ;	# live variables = {c,d,_tmp95,_tmp96,_tmp104}
	_tmp106 = c + _tmp105 ;	# live variables = {c,d,_tmp95,_tmp105}
	_tmp107 = *(_tmp106) ;	# live variables = {c,d,_tmp95,_tmp106}
	_tmp108 = 0 ;	# live variables = {c,d,_tmp95,_tmp107}
	_tmp109 = _tmp107 < _tmp108 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp108}
	_tmp110 = *(_tmp95 + -4) ;	# live variables = {c,d,_tmp95,_tmp107,_tmp108,_tmp109}
	_tmp111 = _tmp107 < _tmp110 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp108,_tmp109,_tmp110}
	_tmp112 = _tmp111 == _tmp108 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp108,_tmp109,_tmp111}
	_tmp113 = _tmp109 || _tmp112 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp109,_tmp112}
	IfZ _tmp113 Goto _L9 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp113}
	_tmp114 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {c,d,_tmp95,_tmp107}
	PushParam _tmp114 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp114}
	LCall _PrintString ;	# live variables = {c,d,_tmp95,_tmp107}
	PopParams 4 ;	# live variables = {c,d,_tmp95,_tmp107}
	LCall _Halt ;	# live variables = {c,d,_tmp95,_tmp107}
_L9:
	_tmp115 = 4 ;	# live variables = {c,d,_tmp95,_tmp107}
	_tmp116 = _tmp115 * _tmp107 ;	# live variables = {c,d,_tmp95,_tmp107,_tmp115}
	_tmp117 = _tmp95 + _tmp116 ;	# live variables = {c,d,_tmp95,_tmp116}
	_tmp118 = 55 ;	# live variables = {c,d,_tmp117}
	*(_tmp117) = _tmp118 ;	# live variables = {c,d,_tmp117,_tmp118}
	_tmp119 = 0 ;	# live variables = {c,d}
	_tmp120 = 0 ;	# live variables = {c,d,_tmp119}
	_tmp121 = _tmp119 < _tmp120 ;	# live variables = {c,d,_tmp119,_tmp120}
	_tmp122 = *(c + -4) ;	# live variables = {c,d,_tmp119,_tmp120,_tmp121}
	_tmp123 = _tmp119 < _tmp122 ;	# live variables = {c,d,_tmp119,_tmp120,_tmp121,_tmp122}
	_tmp124 = _tmp123 == _tmp120 ;	# live variables = {c,d,_tmp119,_tmp120,_tmp121,_tmp123}
	_tmp125 = _tmp121 || _tmp124 ;	# live variables = {c,d,_tmp119,_tmp121,_tmp124}
	IfZ _tmp125 Goto _L10 ;	# live variables = {c,d,_tmp119,_tmp125}
	_tmp126 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {c,d,_tmp119}
	PushParam _tmp126 ;	# live variables = {c,d,_tmp119,_tmp126}
	LCall _PrintString ;	# live variables = {c,d,_tmp119}
	PopParams 4 ;	# live variables = {c,d,_tmp119}
	LCall _Halt ;	# live variables = {c,d,_tmp119}
_L10:
	_tmp127 = 4 ;	# live variables = {c,d,_tmp119}
	_tmp128 = _tmp127 * _tmp119 ;	# live variables = {c,d,_tmp119,_tmp127}
	_tmp129 = c + _tmp128 ;	# live variables = {c,d,_tmp128}
	_tmp130 = *(_tmp129) ;	# live variables = {c,d,_tmp129}
	PushParam _tmp130 ;	# live variables = {c,d,_tmp130}
	LCall _PrintInt ;	# live variables = {c,d}
	PopParams 4 ;	# live variables = {c,d}
	_tmp131 = " " ;	# live variables = {c,d}
	PushParam _tmp131 ;	# live variables = {c,d,_tmp131}
	LCall _PrintString ;	# live variables = {c,d}
	PopParams 4 ;	# live variables = {c,d}
	_tmp132 = 2 ;	# live variables = {c,d}
	_tmp133 = 100 ;	# live variables = {c,d,_tmp132}
	_tmp134 = 0 ;	# live variables = {c,d,_tmp132,_tmp133}
	_tmp135 = 0 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134}
	_tmp136 = _tmp134 < _tmp135 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp135}
	_tmp137 = *(d + -4) ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp135,_tmp136}
	_tmp138 = _tmp134 < _tmp137 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp135,_tmp136,_tmp137}
	_tmp139 = _tmp138 == _tmp135 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp135,_tmp136,_tmp138}
	_tmp140 = _tmp136 || _tmp139 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp136,_tmp139}
	IfZ _tmp140 Goto _L11 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp140}
	_tmp141 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134}
	PushParam _tmp141 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp141}
	LCall _PrintString ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134}
	PopParams 4 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134}
	LCall _Halt ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134}
_L11:
	_tmp142 = 4 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134}
	_tmp143 = _tmp142 * _tmp134 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp134,_tmp142}
	_tmp144 = d + _tmp143 ;	# live variables = {c,d,_tmp132,_tmp133,_tmp143}
	_tmp145 = *(_tmp144) ;	# live variables = {c,_tmp132,_tmp133,_tmp144}
	PushParam c ;	# live variables = {c,_tmp132,_tmp133,_tmp145}
	PushParam _tmp145 ;	# live variables = {_tmp132,_tmp133,_tmp145}
	PushParam _tmp133 ;	# live variables = {_tmp132,_tmp133}
	_tmp146 = LCall _Binky ;	# live variables = {_tmp132}
	PopParams 12 ;	# live variables = {_tmp132,_tmp146}
	_tmp147 = _tmp132 * _tmp146 ;	# live variables = {_tmp132,_tmp146}
	PushParam _tmp147 ;	# live variables = {_tmp147}
	LCall _PrintInt ;	# live variables = {}
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
