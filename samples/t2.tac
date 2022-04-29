_tester:
	BeginFunc 188 ;	# live variables = {sz}
	_tmp0 = 1 ;	# live variables = {sz}
	_tmp1 = 1 ;	# live variables = {sz,_tmp0}
	_tmp2 = _tmp0 < _tmp1 ;	# live variables = {sz,_tmp0,_tmp1}
	IfZ _tmp2 Goto _L0 ;	# live variables = {sz,_tmp0,_tmp2}
	_tmp3 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {sz,_tmp0}
	PushParam _tmp3 ;	# live variables = {sz,_tmp0,_tmp3}
	LCall _PrintString ;	# live variables = {sz,_tmp0}
	PopParams 4 ;	# live variables = {sz,_tmp0}
	LCall _Halt ;	# live variables = {sz,_tmp0}
_L0:
	_tmp4 = 1 ;	# live variables = {sz,_tmp0}
	_tmp5 = _tmp4 + _tmp0 ;	# live variables = {sz,_tmp0,_tmp4}
	_tmp6 = 4 ;	# live variables = {sz,_tmp0,_tmp5}
	_tmp7 = _tmp5 * _tmp6 ;	# live variables = {sz,_tmp0,_tmp5,_tmp6}
	PushParam _tmp7 ;	# live variables = {sz,_tmp0,_tmp6,_tmp7}
	_tmp8 = LCall _Alloc ;	# live variables = {sz,_tmp0,_tmp6}
	PopParams 4 ;	# live variables = {sz,_tmp0,_tmp6,_tmp8}
	*(_tmp8) = _tmp0 ;	# live variables = {sz,_tmp0,_tmp6,_tmp8}
	_tmp9 = _tmp8 + _tmp6 ;	# live variables = {sz,_tmp6,_tmp8}
	b = _tmp9 ;	# live variables = {sz,_tmp9}
	_tmp10 = 1 ;	# live variables = {b,sz}
	_tmp11 = sz < _tmp10 ;	# live variables = {b,sz,_tmp10}
	IfZ _tmp11 Goto _L1 ;	# live variables = {b,sz,_tmp11}
	_tmp12 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {b,sz}
	PushParam _tmp12 ;	# live variables = {b,sz,_tmp12}
	LCall _PrintString ;	# live variables = {b,sz}
	PopParams 4 ;	# live variables = {b,sz}
	LCall _Halt ;	# live variables = {b,sz}
_L1:
	_tmp13 = 1 ;	# live variables = {b,sz}
	_tmp14 = _tmp13 + sz ;	# live variables = {b,sz,_tmp13}
	_tmp15 = 4 ;	# live variables = {b,sz,_tmp14}
	_tmp16 = _tmp14 * _tmp15 ;	# live variables = {b,sz,_tmp14,_tmp15}
	PushParam _tmp16 ;	# live variables = {b,sz,_tmp15,_tmp16}
	_tmp17 = LCall _Alloc ;	# live variables = {b,sz,_tmp15}
	PopParams 4 ;	# live variables = {b,sz,_tmp15,_tmp17}
	*(_tmp17) = sz ;	# live variables = {b,sz,_tmp15,_tmp17}
	_tmp18 = _tmp17 + _tmp15 ;	# live variables = {b,sz,_tmp15,_tmp17}
	result = _tmp18 ;	# live variables = {b,sz,_tmp18}
	_tmp19 = 0 ;	# live variables = {b,sz,result}
	i = _tmp19 ;	# live variables = {b,sz,result,_tmp19}
_L2:
	_tmp20 = i < sz ;	# live variables = {b,sz,i,result}
	IfZ _tmp20 Goto _L3 ;	# live variables = {b,sz,i,result,_tmp20}
	_tmp21 = 0 ;	# live variables = {b,sz,i,result}
	_tmp22 = i < _tmp21 ;	# live variables = {b,sz,i,result,_tmp21}
	_tmp23 = *(result + -4) ;	# live variables = {b,sz,i,result,_tmp21,_tmp22}
	_tmp24 = i < _tmp23 ;	# live variables = {b,sz,i,result,_tmp21,_tmp22,_tmp23}
	_tmp25 = _tmp24 == _tmp21 ;	# live variables = {b,sz,i,result,_tmp21,_tmp22,_tmp24}
	_tmp26 = _tmp22 || _tmp25 ;	# live variables = {b,sz,i,result,_tmp22,_tmp25}
	IfZ _tmp26 Goto _L4 ;	# live variables = {b,sz,i,result,_tmp26}
	_tmp27 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,sz,i,result}
	PushParam _tmp27 ;	# live variables = {b,sz,i,result,_tmp27}
	LCall _PrintString ;	# live variables = {b,sz,i,result}
	PopParams 4 ;	# live variables = {b,sz,i,result}
	LCall _Halt ;	# live variables = {b,sz,i,result}
_L4:
	_tmp28 = 4 ;	# live variables = {b,sz,i,result}
	_tmp29 = _tmp28 * i ;	# live variables = {b,sz,i,result,_tmp28}
	_tmp30 = result + _tmp29 ;	# live variables = {b,sz,i,result,_tmp29}
	*(_tmp30) = i ;	# live variables = {b,sz,i,result,_tmp30}
	_tmp31 = 1 ;	# live variables = {b,sz,i,result}
	_tmp32 = i + _tmp31 ;	# live variables = {b,sz,i,result,_tmp31}
	i = _tmp32 ;	# live variables = {b,sz,result,_tmp32}
	Goto _L2 ;	# live variables = {b,sz,i,result}
_L3:
	_tmp33 = 0 ;	# live variables = {b,result}
	_tmp34 = 0 ;	# live variables = {b,result,_tmp33}
	_tmp35 = _tmp33 < _tmp34 ;	# live variables = {b,result,_tmp33,_tmp34}
	_tmp36 = *(b + -4) ;	# live variables = {b,result,_tmp33,_tmp34,_tmp35}
	_tmp37 = _tmp33 < _tmp36 ;	# live variables = {b,result,_tmp33,_tmp34,_tmp35,_tmp36}
	_tmp38 = _tmp37 == _tmp34 ;	# live variables = {b,result,_tmp33,_tmp34,_tmp35,_tmp37}
	_tmp39 = _tmp35 || _tmp38 ;	# live variables = {b,result,_tmp33,_tmp35,_tmp38}
	IfZ _tmp39 Goto _L5 ;	# live variables = {b,result,_tmp33,_tmp39}
	_tmp40 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,result,_tmp33}
	PushParam _tmp40 ;	# live variables = {b,result,_tmp33,_tmp40}
	LCall _PrintString ;	# live variables = {b,result,_tmp33}
	PopParams 4 ;	# live variables = {b,result,_tmp33}
	LCall _Halt ;	# live variables = {b,result,_tmp33}
_L5:
	_tmp41 = 4 ;	# live variables = {b,result,_tmp33}
	_tmp42 = _tmp41 * _tmp33 ;	# live variables = {b,result,_tmp33,_tmp41}
	_tmp43 = b + _tmp42 ;	# live variables = {b,result,_tmp42}
	_tmp44 = "Done" ;	# live variables = {result,_tmp43}
	*(_tmp43) = _tmp44 ;	# live variables = {result,_tmp43,_tmp44}
	Return result ;	# live variables = {result}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 168 ;	# live variables = {b}
	_tmp45 = 8 ;	# live variables = {b}
	PushParam _tmp45 ;	# live variables = {b,_tmp45}
	_tmp46 = LCall _tester ;	# live variables = {b}
	PopParams 4 ;	# live variables = {b,_tmp46}
	d = _tmp46 ;	# live variables = {b,_tmp46}
	_tmp47 = 1 ;	# live variables = {b,d}
	_tmp48 = 0 ;	# live variables = {b,d,_tmp47}
	_tmp49 = _tmp47 < _tmp48 ;	# live variables = {b,d,_tmp47,_tmp48}
	_tmp50 = *(d + -4) ;	# live variables = {b,d,_tmp47,_tmp48,_tmp49}
	_tmp51 = _tmp47 < _tmp50 ;	# live variables = {b,d,_tmp47,_tmp48,_tmp49,_tmp50}
	_tmp52 = _tmp51 == _tmp48 ;	# live variables = {b,d,_tmp47,_tmp48,_tmp49,_tmp51}
	_tmp53 = _tmp49 || _tmp52 ;	# live variables = {b,d,_tmp47,_tmp49,_tmp52}
	IfZ _tmp53 Goto _L6 ;	# live variables = {b,d,_tmp47,_tmp53}
	_tmp54 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,d,_tmp47}
	PushParam _tmp54 ;	# live variables = {b,d,_tmp47,_tmp54}
	LCall _PrintString ;	# live variables = {b,d,_tmp47}
	PopParams 4 ;	# live variables = {b,d,_tmp47}
	LCall _Halt ;	# live variables = {b,d,_tmp47}
_L6:
	_tmp55 = 4 ;	# live variables = {b,d,_tmp47}
	_tmp56 = _tmp55 * _tmp47 ;	# live variables = {b,d,_tmp47,_tmp55}
	_tmp57 = d + _tmp56 ;	# live variables = {b,d,_tmp56}
	_tmp58 = *(_tmp57) ;	# live variables = {b,d,_tmp57}
	_tmp59 = 0 ;	# live variables = {b,d,_tmp58}
	_tmp60 = _tmp58 < _tmp59 ;	# live variables = {b,d,_tmp58,_tmp59}
	_tmp61 = *(d + -4) ;	# live variables = {b,d,_tmp58,_tmp59,_tmp60}
	_tmp62 = _tmp58 < _tmp61 ;	# live variables = {b,d,_tmp58,_tmp59,_tmp60,_tmp61}
	_tmp63 = _tmp62 == _tmp59 ;	# live variables = {b,d,_tmp58,_tmp59,_tmp60,_tmp62}
	_tmp64 = _tmp60 || _tmp63 ;	# live variables = {b,d,_tmp58,_tmp60,_tmp63}
	IfZ _tmp64 Goto _L7 ;	# live variables = {b,d,_tmp58,_tmp64}
	_tmp65 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,d,_tmp58}
	PushParam _tmp65 ;	# live variables = {b,d,_tmp58,_tmp65}
	LCall _PrintString ;	# live variables = {b,d,_tmp58}
	PopParams 4 ;	# live variables = {b,d,_tmp58}
	LCall _Halt ;	# live variables = {b,d,_tmp58}
_L7:
	_tmp66 = 4 ;	# live variables = {b,d,_tmp58}
	_tmp67 = _tmp66 * _tmp58 ;	# live variables = {b,d,_tmp58,_tmp66}
	_tmp68 = d + _tmp67 ;	# live variables = {b,d,_tmp67}
	_tmp69 = *(_tmp68) ;	# live variables = {b,d,_tmp68}
	PushParam _tmp69 ;	# live variables = {b,d,_tmp69}
	LCall _PrintInt ;	# live variables = {b,d}
	PopParams 4 ;	# live variables = {b,d}
	_tmp70 = "\n" ;	# live variables = {b,d}
	PushParam _tmp70 ;	# live variables = {b,d,_tmp70}
	LCall _PrintString ;	# live variables = {b,d}
	PopParams 4 ;	# live variables = {b,d}
	_tmp71 = *(d + -4) ;	# live variables = {b,d}
	PushParam _tmp71 ;	# live variables = {b,_tmp71}
	LCall _PrintInt ;	# live variables = {b}
	PopParams 4 ;	# live variables = {b}
	_tmp72 = "\n" ;	# live variables = {b}
	PushParam _tmp72 ;	# live variables = {b,_tmp72}
	LCall _PrintString ;	# live variables = {b}
	PopParams 4 ;	# live variables = {b}
	_tmp73 = 0 ;	# live variables = {b}
	_tmp74 = 0 ;	# live variables = {b,_tmp73}
	_tmp75 = _tmp73 < _tmp74 ;	# live variables = {b,_tmp73,_tmp74}
	_tmp76 = *(b + -4) ;	# live variables = {b,_tmp73,_tmp74,_tmp75}
	_tmp77 = _tmp73 < _tmp76 ;	# live variables = {b,_tmp73,_tmp74,_tmp75,_tmp76}
	_tmp78 = _tmp77 == _tmp74 ;	# live variables = {b,_tmp73,_tmp74,_tmp75,_tmp77}
	_tmp79 = _tmp75 || _tmp78 ;	# live variables = {b,_tmp73,_tmp75,_tmp78}
	IfZ _tmp79 Goto _L8 ;	# live variables = {b,_tmp73,_tmp79}
	_tmp80 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {b,_tmp73}
	PushParam _tmp80 ;	# live variables = {b,_tmp73,_tmp80}
	LCall _PrintString ;	# live variables = {b,_tmp73}
	PopParams 4 ;	# live variables = {b,_tmp73}
	LCall _Halt ;	# live variables = {b,_tmp73}
_L8:
	_tmp81 = 4 ;	# live variables = {b,_tmp73}
	_tmp82 = _tmp81 * _tmp73 ;	# live variables = {b,_tmp73,_tmp81}
	_tmp83 = b + _tmp82 ;	# live variables = {b,_tmp82}
	_tmp84 = *(_tmp83) ;	# live variables = {_tmp83}
	PushParam _tmp84 ;	# live variables = {_tmp84}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp85 = "\n" ;	# live variables = {}
	PushParam _tmp85 ;	# live variables = {_tmp85}
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
