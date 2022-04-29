_Wild:
	BeginFunc 80 ;	# live variables = {names,answer}
	_tmp0 = 0 ;	# live variables = {names,answer}
	i = _tmp0 ;	# live variables = {names,answer,_tmp0}
_L0:
	_tmp1 = *(names + -4) ;	# live variables = {names,answer,i}
	_tmp2 = i < _tmp1 ;	# live variables = {names,answer,i,_tmp1}
	IfZ _tmp2 Goto _L1 ;	# live variables = {names,answer,i,_tmp2}
	_tmp3 = 0 ;	# live variables = {names,answer,i}
	_tmp4 = i < _tmp3 ;	# live variables = {names,answer,i,_tmp3}
	_tmp5 = *(names + -4) ;	# live variables = {names,answer,i,_tmp3,_tmp4}
	_tmp6 = i < _tmp5 ;	# live variables = {names,answer,i,_tmp3,_tmp4,_tmp5}
	_tmp7 = _tmp6 == _tmp3 ;	# live variables = {names,answer,i,_tmp3,_tmp4,_tmp6}
	_tmp8 = _tmp4 || _tmp7 ;	# live variables = {names,answer,i,_tmp4,_tmp7}
	IfZ _tmp8 Goto _L2 ;	# live variables = {names,answer,i,_tmp8}
	_tmp9 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {names,answer,i}
	PushParam _tmp9 ;	# live variables = {names,answer,i,_tmp9}
	LCall _PrintString ;	# live variables = {names,answer,i}
	PopParams 4 ;	# live variables = {names,answer,i}
	LCall _Halt ;	# live variables = {names,answer,i}
_L2:
	_tmp10 = 4 ;	# live variables = {names,answer,i}
	_tmp11 = _tmp10 * i ;	# live variables = {names,answer,i,_tmp10}
	_tmp12 = names + _tmp11 ;	# live variables = {names,answer,i,_tmp11}
	_tmp13 = *(_tmp12) ;	# live variables = {names,answer,i,_tmp12}
	PushParam answer ;	# live variables = {names,answer,i,_tmp13}
	PushParam _tmp13 ;	# live variables = {names,answer,i,_tmp13}
	_tmp14 = LCall _StringEqual ;	# live variables = {names,answer,i}
	PopParams 8 ;	# live variables = {names,answer,i,_tmp14}
	IfZ _tmp14 Goto _L3 ;	# live variables = {names,answer,i,_tmp14}
	_tmp15 = 1 ;	# live variables = {}
	Return _tmp15 ;	# live variables = {_tmp15}
_L3:
	_tmp16 = 1 ;	# live variables = {names,answer,i}
	_tmp17 = i + _tmp16 ;	# live variables = {names,answer,i,_tmp16}
	i = _tmp17 ;	# live variables = {names,answer,_tmp17}
	Goto _L0 ;	# live variables = {names,answer,i}
_L1:
	_tmp18 = 0 ;	# live variables = {}
	Return _tmp18 ;	# live variables = {_tmp18}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 212 ;	# live variables = {}
	_tmp19 = 3 ;	# live variables = {}
	_tmp20 = 1 ;	# live variables = {_tmp19}
	_tmp21 = _tmp19 < _tmp20 ;	# live variables = {_tmp19,_tmp20}
	IfZ _tmp21 Goto _L4 ;	# live variables = {_tmp19,_tmp21}
	_tmp22 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {_tmp19}
	PushParam _tmp22 ;	# live variables = {_tmp19,_tmp22}
	LCall _PrintString ;	# live variables = {_tmp19}
	PopParams 4 ;	# live variables = {_tmp19}
	LCall _Halt ;	# live variables = {_tmp19}
_L4:
	_tmp23 = 1 ;	# live variables = {_tmp19}
	_tmp24 = _tmp23 + _tmp19 ;	# live variables = {_tmp19,_tmp23}
	_tmp25 = 4 ;	# live variables = {_tmp19,_tmp24}
	_tmp26 = _tmp24 * _tmp25 ;	# live variables = {_tmp19,_tmp24,_tmp25}
	PushParam _tmp26 ;	# live variables = {_tmp19,_tmp25,_tmp26}
	_tmp27 = LCall _Alloc ;	# live variables = {_tmp19,_tmp25}
	PopParams 4 ;	# live variables = {_tmp19,_tmp25,_tmp27}
	*(_tmp27) = _tmp19 ;	# live variables = {_tmp19,_tmp25,_tmp27}
	_tmp28 = _tmp27 + _tmp25 ;	# live variables = {_tmp25,_tmp27}
	names = _tmp28 ;	# live variables = {_tmp28}
	_tmp29 = 0 ;	# live variables = {names}
	_tmp30 = 0 ;	# live variables = {names,_tmp29}
	_tmp31 = _tmp29 < _tmp30 ;	# live variables = {names,_tmp29,_tmp30}
	_tmp32 = *(names + -4) ;	# live variables = {names,_tmp29,_tmp30,_tmp31}
	_tmp33 = _tmp29 < _tmp32 ;	# live variables = {names,_tmp29,_tmp30,_tmp31,_tmp32}
	_tmp34 = _tmp33 == _tmp30 ;	# live variables = {names,_tmp29,_tmp30,_tmp31,_tmp33}
	_tmp35 = _tmp31 || _tmp34 ;	# live variables = {names,_tmp29,_tmp31,_tmp34}
	IfZ _tmp35 Goto _L5 ;	# live variables = {names,_tmp29,_tmp35}
	_tmp36 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {names,_tmp29}
	PushParam _tmp36 ;	# live variables = {names,_tmp29,_tmp36}
	LCall _PrintString ;	# live variables = {names,_tmp29}
	PopParams 4 ;	# live variables = {names,_tmp29}
	LCall _Halt ;	# live variables = {names,_tmp29}
_L5:
	_tmp37 = 4 ;	# live variables = {names,_tmp29}
	_tmp38 = _tmp37 * _tmp29 ;	# live variables = {names,_tmp29,_tmp37}
	_tmp39 = names + _tmp38 ;	# live variables = {names,_tmp38}
	_tmp40 = "Satish" ;	# live variables = {names,_tmp39}
	*(_tmp39) = _tmp40 ;	# live variables = {names,_tmp39,_tmp40}
	_tmp41 = 1 ;	# live variables = {names}
	_tmp42 = 0 ;	# live variables = {names,_tmp41}
	_tmp43 = _tmp41 < _tmp42 ;	# live variables = {names,_tmp41,_tmp42}
	_tmp44 = *(names + -4) ;	# live variables = {names,_tmp41,_tmp42,_tmp43}
	_tmp45 = _tmp41 < _tmp44 ;	# live variables = {names,_tmp41,_tmp42,_tmp43,_tmp44}
	_tmp46 = _tmp45 == _tmp42 ;	# live variables = {names,_tmp41,_tmp42,_tmp43,_tmp45}
	_tmp47 = _tmp43 || _tmp46 ;	# live variables = {names,_tmp41,_tmp43,_tmp46}
	IfZ _tmp47 Goto _L6 ;	# live variables = {names,_tmp41,_tmp47}
	_tmp48 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {names,_tmp41}
	PushParam _tmp48 ;	# live variables = {names,_tmp41,_tmp48}
	LCall _PrintString ;	# live variables = {names,_tmp41}
	PopParams 4 ;	# live variables = {names,_tmp41}
	LCall _Halt ;	# live variables = {names,_tmp41}
_L6:
	_tmp49 = 4 ;	# live variables = {names,_tmp41}
	_tmp50 = _tmp49 * _tmp41 ;	# live variables = {names,_tmp41,_tmp49}
	_tmp51 = names + _tmp50 ;	# live variables = {names,_tmp50}
	_tmp52 = "Chun" ;	# live variables = {names,_tmp51}
	*(_tmp51) = _tmp52 ;	# live variables = {names,_tmp51,_tmp52}
	_tmp53 = 2 ;	# live variables = {names}
	_tmp54 = 0 ;	# live variables = {names,_tmp53}
	_tmp55 = _tmp53 < _tmp54 ;	# live variables = {names,_tmp53,_tmp54}
	_tmp56 = *(names + -4) ;	# live variables = {names,_tmp53,_tmp54,_tmp55}
	_tmp57 = _tmp53 < _tmp56 ;	# live variables = {names,_tmp53,_tmp54,_tmp55,_tmp56}
	_tmp58 = _tmp57 == _tmp54 ;	# live variables = {names,_tmp53,_tmp54,_tmp55,_tmp57}
	_tmp59 = _tmp55 || _tmp58 ;	# live variables = {names,_tmp53,_tmp55,_tmp58}
	IfZ _tmp59 Goto _L7 ;	# live variables = {names,_tmp53,_tmp59}
	_tmp60 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {names,_tmp53}
	PushParam _tmp60 ;	# live variables = {names,_tmp53,_tmp60}
	LCall _PrintString ;	# live variables = {names,_tmp53}
	PopParams 4 ;	# live variables = {names,_tmp53}
	LCall _Halt ;	# live variables = {names,_tmp53}
_L7:
	_tmp61 = 4 ;	# live variables = {names,_tmp53}
	_tmp62 = _tmp61 * _tmp53 ;	# live variables = {names,_tmp53,_tmp61}
	_tmp63 = names + _tmp62 ;	# live variables = {names,_tmp62}
	_tmp64 = "Supriya" ;	# live variables = {names,_tmp63}
	*(_tmp63) = _tmp64 ;	# live variables = {names,_tmp63,_tmp64}
_L8:
	_tmp65 = 1 ;	# live variables = {names}
	IfZ _tmp65 Goto _L9 ;	# live variables = {names,_tmp65}
	_tmp66 = "\nWho is your favorite EECS483 staff member? " ;	# live variables = {names}
	PushParam _tmp66 ;	# live variables = {names,_tmp66}
	LCall _PrintString ;	# live variables = {names}
	PopParams 4 ;	# live variables = {names}
	_tmp67 = LCall _ReadLine ;	# live variables = {names}
	PushParam _tmp67 ;	# live variables = {names,_tmp67}
	PushParam names ;	# live variables = {names}
	_tmp68 = LCall _Wild ;	# live variables = {names}
	PopParams 8 ;	# live variables = {names,_tmp68}
	IfZ _tmp68 Goto _L10 ;	# live variables = {names,_tmp68}
	_tmp69 = "You just earned 1000 bonus points!\n" ;	# live variables = {}
	PushParam _tmp69 ;	# live variables = {_tmp69}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	Goto _L9 ;	# live variables = {}
_L10:
	_tmp70 = "That's not a good way to make points. Try again!\..." ;	# live variables = {names}
	PushParam _tmp70 ;	# live variables = {names,_tmp70}
	LCall _PrintString ;	# live variables = {names}
	PopParams 4 ;	# live variables = {names}
	Goto _L8 ;	# live variables = {names}
_L9:
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
