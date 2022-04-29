_ReadArray:
	BeginFunc 128 ;	# live variables = {}
	_tmp0 = "How many scores? " ;	# live variables = {}
	PushParam _tmp0 ;	# live variables = {_tmp0}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp1 = LCall _ReadInteger ;	# live variables = {}
	numScores = _tmp1 ;	# live variables = {_tmp1}
	_tmp2 = 1 ;	# live variables = {numScores}
	_tmp3 = numScores < _tmp2 ;	# live variables = {numScores,_tmp2}
	IfZ _tmp3 Goto _L0 ;	# live variables = {numScores,_tmp3}
	_tmp4 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {numScores}
	PushParam _tmp4 ;	# live variables = {numScores,_tmp4}
	LCall _PrintString ;	# live variables = {numScores}
	PopParams 4 ;	# live variables = {numScores}
	LCall _Halt ;	# live variables = {numScores}
_L0:
	_tmp5 = 1 ;	# live variables = {numScores}
	_tmp6 = _tmp5 + numScores ;	# live variables = {numScores,_tmp5}
	_tmp7 = 4 ;	# live variables = {numScores,_tmp6}
	_tmp8 = _tmp6 * _tmp7 ;	# live variables = {numScores,_tmp6,_tmp7}
	PushParam _tmp8 ;	# live variables = {numScores,_tmp7,_tmp8}
	_tmp9 = LCall _Alloc ;	# live variables = {numScores,_tmp7}
	PopParams 4 ;	# live variables = {numScores,_tmp7,_tmp9}
	*(_tmp9) = numScores ;	# live variables = {numScores,_tmp7,_tmp9}
	_tmp10 = _tmp9 + _tmp7 ;	# live variables = {_tmp7,_tmp9}
	arr = _tmp10 ;	# live variables = {_tmp10}
	_tmp11 = 0 ;	# live variables = {arr}
	i = _tmp11 ;	# live variables = {arr,_tmp11}
_L1:
	_tmp12 = *(arr + -4) ;	# live variables = {i,arr}
	_tmp13 = i < _tmp12 ;	# live variables = {i,arr,_tmp12}
	IfZ _tmp13 Goto _L2 ;	# live variables = {i,arr,_tmp13}
	_tmp14 = "Enter next number: " ;	# live variables = {i,arr}
	PushParam _tmp14 ;	# live variables = {i,arr,_tmp14}
	LCall _PrintString ;	# live variables = {i,arr}
	PopParams 4 ;	# live variables = {i,arr}
	_tmp15 = LCall _ReadInteger ;	# live variables = {i,arr}
	num = _tmp15 ;	# live variables = {i,arr,_tmp15}
	_tmp16 = 0 ;	# live variables = {i,num,arr}
	_tmp17 = i < _tmp16 ;	# live variables = {i,num,arr,_tmp16}
	_tmp18 = *(arr + -4) ;	# live variables = {i,num,arr,_tmp16,_tmp17}
	_tmp19 = i < _tmp18 ;	# live variables = {i,num,arr,_tmp16,_tmp17,_tmp18}
	_tmp20 = _tmp19 == _tmp16 ;	# live variables = {i,num,arr,_tmp16,_tmp17,_tmp19}
	_tmp21 = _tmp17 || _tmp20 ;	# live variables = {i,num,arr,_tmp17,_tmp20}
	IfZ _tmp21 Goto _L3 ;	# live variables = {i,num,arr,_tmp21}
	_tmp22 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {i,num,arr}
	PushParam _tmp22 ;	# live variables = {i,num,arr,_tmp22}
	LCall _PrintString ;	# live variables = {i,num,arr}
	PopParams 4 ;	# live variables = {i,num,arr}
	LCall _Halt ;	# live variables = {i,num,arr}
_L3:
	_tmp23 = 4 ;	# live variables = {i,num,arr}
	_tmp24 = _tmp23 * i ;	# live variables = {i,num,arr,_tmp23}
	_tmp25 = arr + _tmp24 ;	# live variables = {i,num,arr,_tmp24}
	*(_tmp25) = num ;	# live variables = {i,num,arr,_tmp25}
	_tmp26 = 1 ;	# live variables = {i,arr}
	_tmp27 = i + _tmp26 ;	# live variables = {i,arr,_tmp26}
	i = _tmp27 ;	# live variables = {arr,_tmp27}
	Goto _L1 ;	# live variables = {i,arr}
_L2:
	Return arr ;	# live variables = {arr}
	EndFunc ;	# live variables = {}
_Sort:
	BeginFunc 304 ;	# live variables = {arr}
	_tmp28 = 1 ;	# live variables = {arr}
	i = _tmp28 ;	# live variables = {arr,_tmp28}
_L4:
	_tmp29 = *(arr + -4) ;	# live variables = {arr,i}
	_tmp30 = i < _tmp29 ;	# live variables = {arr,i,_tmp29}
	IfZ _tmp30 Goto _L5 ;	# live variables = {arr,i,_tmp30}
	_tmp31 = 1 ;	# live variables = {arr,i}
	_tmp32 = i - _tmp31 ;	# live variables = {arr,i,_tmp31}
	j = _tmp32 ;	# live variables = {arr,i,_tmp32}
	_tmp33 = 0 ;	# live variables = {arr,i,j}
	_tmp34 = i < _tmp33 ;	# live variables = {arr,i,j,_tmp33}
	_tmp35 = *(arr + -4) ;	# live variables = {arr,i,j,_tmp33,_tmp34}
	_tmp36 = i < _tmp35 ;	# live variables = {arr,i,j,_tmp33,_tmp34,_tmp35}
	_tmp37 = _tmp36 == _tmp33 ;	# live variables = {arr,i,j,_tmp33,_tmp34,_tmp36}
	_tmp38 = _tmp34 || _tmp37 ;	# live variables = {arr,i,j,_tmp34,_tmp37}
	IfZ _tmp38 Goto _L6 ;	# live variables = {arr,i,j,_tmp38}
	_tmp39 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i,j}
	PushParam _tmp39 ;	# live variables = {arr,i,j,_tmp39}
	LCall _PrintString ;	# live variables = {arr,i,j}
	PopParams 4 ;	# live variables = {arr,i,j}
	LCall _Halt ;	# live variables = {arr,i,j}
_L6:
	_tmp40 = 4 ;	# live variables = {arr,i,j}
	_tmp41 = _tmp40 * i ;	# live variables = {arr,i,j,_tmp40}
	_tmp42 = arr + _tmp41 ;	# live variables = {arr,i,j,_tmp41}
	_tmp43 = *(_tmp42) ;	# live variables = {arr,i,j,_tmp42}
	val = _tmp43 ;	# live variables = {arr,i,j,_tmp43}
_L7:
	_tmp44 = 0 ;	# live variables = {arr,i,j,val}
	_tmp45 = _tmp44 < j ;	# live variables = {arr,i,j,val,_tmp44}
	_tmp46 = _tmp44 == j ;	# live variables = {arr,i,j,val,_tmp44,_tmp45}
	_tmp47 = _tmp45 || _tmp46 ;	# live variables = {arr,i,j,val,_tmp45,_tmp46}
	IfZ _tmp47 Goto _L8 ;	# live variables = {arr,i,j,val,_tmp47}
	_tmp48 = 0 ;	# live variables = {arr,i,j,val}
	_tmp49 = j < _tmp48 ;	# live variables = {arr,i,j,val,_tmp48}
	_tmp50 = *(arr + -4) ;	# live variables = {arr,i,j,val,_tmp48,_tmp49}
	_tmp51 = j < _tmp50 ;	# live variables = {arr,i,j,val,_tmp48,_tmp49,_tmp50}
	_tmp52 = _tmp51 == _tmp48 ;	# live variables = {arr,i,j,val,_tmp48,_tmp49,_tmp51}
	_tmp53 = _tmp49 || _tmp52 ;	# live variables = {arr,i,j,val,_tmp49,_tmp52}
	IfZ _tmp53 Goto _L9 ;	# live variables = {arr,i,j,val,_tmp53}
	_tmp54 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i,j,val}
	PushParam _tmp54 ;	# live variables = {arr,i,j,val,_tmp54}
	LCall _PrintString ;	# live variables = {arr,i,j,val}
	PopParams 4 ;	# live variables = {arr,i,j,val}
	LCall _Halt ;	# live variables = {arr,i,j,val}
_L9:
	_tmp55 = 4 ;	# live variables = {arr,i,j,val}
	_tmp56 = _tmp55 * j ;	# live variables = {arr,i,j,val,_tmp55}
	_tmp57 = arr + _tmp56 ;	# live variables = {arr,i,j,val,_tmp56}
	_tmp58 = *(_tmp57) ;	# live variables = {arr,i,j,val,_tmp57}
	_tmp59 = _tmp58 < val ;	# live variables = {arr,i,j,val,_tmp58}
	_tmp60 = _tmp58 == val ;	# live variables = {arr,i,j,val,_tmp58,_tmp59}
	_tmp61 = _tmp59 || _tmp60 ;	# live variables = {arr,i,j,val,_tmp59,_tmp60}
	IfZ _tmp61 Goto _L10 ;	# live variables = {arr,i,j,val,_tmp61}
	Goto _L8 ;	# live variables = {arr,i,j,val}
_L10:
	_tmp62 = 1 ;	# live variables = {arr,i,j,val}
	_tmp63 = j + _tmp62 ;	# live variables = {arr,i,j,val,_tmp62}
	_tmp64 = 0 ;	# live variables = {arr,i,j,val,_tmp63}
	_tmp65 = _tmp63 < _tmp64 ;	# live variables = {arr,i,j,val,_tmp63,_tmp64}
	_tmp66 = *(arr + -4) ;	# live variables = {arr,i,j,val,_tmp63,_tmp64,_tmp65}
	_tmp67 = _tmp63 < _tmp66 ;	# live variables = {arr,i,j,val,_tmp63,_tmp64,_tmp65,_tmp66}
	_tmp68 = _tmp67 == _tmp64 ;	# live variables = {arr,i,j,val,_tmp63,_tmp64,_tmp65,_tmp67}
	_tmp69 = _tmp65 || _tmp68 ;	# live variables = {arr,i,j,val,_tmp63,_tmp65,_tmp68}
	IfZ _tmp69 Goto _L11 ;	# live variables = {arr,i,j,val,_tmp63,_tmp69}
	_tmp70 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i,j,val,_tmp63}
	PushParam _tmp70 ;	# live variables = {arr,i,j,val,_tmp63,_tmp70}
	LCall _PrintString ;	# live variables = {arr,i,j,val,_tmp63}
	PopParams 4 ;	# live variables = {arr,i,j,val,_tmp63}
	LCall _Halt ;	# live variables = {arr,i,j,val,_tmp63}
_L11:
	_tmp71 = 4 ;	# live variables = {arr,i,j,val,_tmp63}
	_tmp72 = _tmp71 * _tmp63 ;	# live variables = {arr,i,j,val,_tmp63,_tmp71}
	_tmp73 = arr + _tmp72 ;	# live variables = {arr,i,j,val,_tmp72}
	_tmp74 = 0 ;	# live variables = {arr,i,j,val,_tmp73}
	_tmp75 = j < _tmp74 ;	# live variables = {arr,i,j,val,_tmp73,_tmp74}
	_tmp76 = *(arr + -4) ;	# live variables = {arr,i,j,val,_tmp73,_tmp74,_tmp75}
	_tmp77 = j < _tmp76 ;	# live variables = {arr,i,j,val,_tmp73,_tmp74,_tmp75,_tmp76}
	_tmp78 = _tmp77 == _tmp74 ;	# live variables = {arr,i,j,val,_tmp73,_tmp74,_tmp75,_tmp77}
	_tmp79 = _tmp75 || _tmp78 ;	# live variables = {arr,i,j,val,_tmp73,_tmp75,_tmp78}
	IfZ _tmp79 Goto _L12 ;	# live variables = {arr,i,j,val,_tmp73,_tmp79}
	_tmp80 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i,j,val,_tmp73}
	PushParam _tmp80 ;	# live variables = {arr,i,j,val,_tmp73,_tmp80}
	LCall _PrintString ;	# live variables = {arr,i,j,val,_tmp73}
	PopParams 4 ;	# live variables = {arr,i,j,val,_tmp73}
	LCall _Halt ;	# live variables = {arr,i,j,val,_tmp73}
_L12:
	_tmp81 = 4 ;	# live variables = {arr,i,j,val,_tmp73}
	_tmp82 = _tmp81 * j ;	# live variables = {arr,i,j,val,_tmp73,_tmp81}
	_tmp83 = arr + _tmp82 ;	# live variables = {arr,i,j,val,_tmp73,_tmp82}
	_tmp84 = *(_tmp83) ;	# live variables = {arr,i,j,val,_tmp73,_tmp83}
	*(_tmp73) = _tmp84 ;	# live variables = {arr,i,j,val,_tmp73,_tmp84}
	_tmp85 = 1 ;	# live variables = {arr,i,j,val}
	_tmp86 = j - _tmp85 ;	# live variables = {arr,i,j,val,_tmp85}
	j = _tmp86 ;	# live variables = {arr,i,val,_tmp86}
	Goto _L7 ;	# live variables = {arr,i,j,val}
_L8:
	_tmp87 = 1 ;	# live variables = {arr,i,j,val}
	_tmp88 = j + _tmp87 ;	# live variables = {arr,i,j,val,_tmp87}
	_tmp89 = 0 ;	# live variables = {arr,i,val,_tmp88}
	_tmp90 = _tmp88 < _tmp89 ;	# live variables = {arr,i,val,_tmp88,_tmp89}
	_tmp91 = *(arr + -4) ;	# live variables = {arr,i,val,_tmp88,_tmp89,_tmp90}
	_tmp92 = _tmp88 < _tmp91 ;	# live variables = {arr,i,val,_tmp88,_tmp89,_tmp90,_tmp91}
	_tmp93 = _tmp92 == _tmp89 ;	# live variables = {arr,i,val,_tmp88,_tmp89,_tmp90,_tmp92}
	_tmp94 = _tmp90 || _tmp93 ;	# live variables = {arr,i,val,_tmp88,_tmp90,_tmp93}
	IfZ _tmp94 Goto _L13 ;	# live variables = {arr,i,val,_tmp88,_tmp94}
	_tmp95 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i,val,_tmp88}
	PushParam _tmp95 ;	# live variables = {arr,i,val,_tmp88,_tmp95}
	LCall _PrintString ;	# live variables = {arr,i,val,_tmp88}
	PopParams 4 ;	# live variables = {arr,i,val,_tmp88}
	LCall _Halt ;	# live variables = {arr,i,val,_tmp88}
_L13:
	_tmp96 = 4 ;	# live variables = {arr,i,val,_tmp88}
	_tmp97 = _tmp96 * _tmp88 ;	# live variables = {arr,i,val,_tmp88,_tmp96}
	_tmp98 = arr + _tmp97 ;	# live variables = {arr,i,val,_tmp97}
	*(_tmp98) = val ;	# live variables = {arr,i,val,_tmp98}
	_tmp99 = 1 ;	# live variables = {arr,i}
	_tmp100 = i + _tmp99 ;	# live variables = {arr,i,_tmp99}
	i = _tmp100 ;	# live variables = {arr,_tmp100}
	Goto _L4 ;	# live variables = {arr,i}
_L5:
	EndFunc ;	# live variables = {}
_PrintArray:
	BeginFunc 80 ;	# live variables = {arr}
	_tmp101 = 0 ;	# live variables = {arr}
	i = _tmp101 ;	# live variables = {arr,_tmp101}
	_tmp102 = "Sorted results: " ;	# live variables = {arr,i}
	PushParam _tmp102 ;	# live variables = {arr,i,_tmp102}
	LCall _PrintString ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
_L14:
	_tmp103 = *(arr + -4) ;	# live variables = {arr,i}
	_tmp104 = i < _tmp103 ;	# live variables = {arr,i,_tmp103}
	IfZ _tmp104 Goto _L15 ;	# live variables = {arr,i,_tmp104}
	_tmp105 = 0 ;	# live variables = {arr,i}
	_tmp106 = i < _tmp105 ;	# live variables = {arr,i,_tmp105}
	_tmp107 = *(arr + -4) ;	# live variables = {arr,i,_tmp105,_tmp106}
	_tmp108 = i < _tmp107 ;	# live variables = {arr,i,_tmp105,_tmp106,_tmp107}
	_tmp109 = _tmp108 == _tmp105 ;	# live variables = {arr,i,_tmp105,_tmp106,_tmp108}
	_tmp110 = _tmp106 || _tmp109 ;	# live variables = {arr,i,_tmp106,_tmp109}
	IfZ _tmp110 Goto _L16 ;	# live variables = {arr,i,_tmp110}
	_tmp111 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i}
	PushParam _tmp111 ;	# live variables = {arr,i,_tmp111}
	LCall _PrintString ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
	LCall _Halt ;	# live variables = {arr,i}
_L16:
	_tmp112 = 4 ;	# live variables = {arr,i}
	_tmp113 = _tmp112 * i ;	# live variables = {arr,i,_tmp112}
	_tmp114 = arr + _tmp113 ;	# live variables = {arr,i,_tmp113}
	_tmp115 = *(_tmp114) ;	# live variables = {arr,i,_tmp114}
	PushParam _tmp115 ;	# live variables = {arr,i,_tmp115}
	LCall _PrintInt ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
	_tmp116 = " " ;	# live variables = {arr,i}
	PushParam _tmp116 ;	# live variables = {arr,i,_tmp116}
	LCall _PrintString ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
	_tmp117 = 1 ;	# live variables = {arr,i}
	_tmp118 = i + _tmp117 ;	# live variables = {arr,i,_tmp117}
	i = _tmp118 ;	# live variables = {arr,_tmp118}
	Goto _L14 ;	# live variables = {arr,i}
_L15:
	_tmp119 = "\n" ;	# live variables = {}
	PushParam _tmp119 ;	# live variables = {_tmp119}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 16 ;	# live variables = {}
	_tmp120 = "\nThis program will read in a bunch of numbers an..." ;	# live variables = {}
	PushParam _tmp120 ;	# live variables = {_tmp120}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp121 = "back out in sorted order.\n\n" ;	# live variables = {}
	PushParam _tmp121 ;	# live variables = {_tmp121}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp122 = LCall _ReadArray ;	# live variables = {}
	arr = _tmp122 ;	# live variables = {_tmp122}
	PushParam arr ;	# live variables = {arr}
	LCall _Sort ;	# live variables = {arr}
	PopParams 4 ;	# live variables = {arr}
	PushParam arr ;	# live variables = {arr}
	LCall _PrintArray ;	# live variables = {}
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
