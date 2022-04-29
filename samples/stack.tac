_Stack.Init:
	BeginFunc 56 ;	# live variables = {this}
	_tmp0 = 100 ;	# live variables = {this}
	_tmp1 = 1 ;	# live variables = {this,_tmp0}
	_tmp2 = _tmp0 < _tmp1 ;	# live variables = {this,_tmp0,_tmp1}
	IfZ _tmp2 Goto _L0 ;	# live variables = {this,_tmp0,_tmp2}
	_tmp3 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {this,_tmp0}
	PushParam _tmp3 ;	# live variables = {this,_tmp0,_tmp3}
	LCall _PrintString ;	# live variables = {this,_tmp0}
	PopParams 4 ;	# live variables = {this,_tmp0}
	LCall _Halt ;	# live variables = {this,_tmp0}
_L0:
	_tmp4 = 1 ;	# live variables = {this,_tmp0}
	_tmp5 = _tmp4 + _tmp0 ;	# live variables = {this,_tmp0,_tmp4}
	_tmp6 = 4 ;	# live variables = {this,_tmp0,_tmp5}
	_tmp7 = _tmp5 * _tmp6 ;	# live variables = {this,_tmp0,_tmp5,_tmp6}
	PushParam _tmp7 ;	# live variables = {this,_tmp0,_tmp6,_tmp7}
	_tmp8 = LCall _Alloc ;	# live variables = {this,_tmp0,_tmp6}
	PopParams 4 ;	# live variables = {this,_tmp0,_tmp6,_tmp8}
	*(_tmp8) = _tmp0 ;	# live variables = {this,_tmp0,_tmp6,_tmp8}
	_tmp9 = _tmp8 + _tmp6 ;	# live variables = {this,_tmp6,_tmp8}
	*(this + 8) = _tmp9 ;	# live variables = {this,_tmp9}
	_tmp10 = 0 ;	# live variables = {this}
	*(this + 4) = _tmp10 ;	# live variables = {this,_tmp10}
	_tmp11 = 3 ;	# live variables = {this}
	_tmp12 = *(this) ;	# live variables = {this,_tmp11}
	_tmp13 = *(_tmp12 + 4) ;	# live variables = {this,_tmp11,_tmp12}
	PushParam _tmp11 ;	# live variables = {this,_tmp11,_tmp13}
	PushParam this ;	# live variables = {this,_tmp13}
	ACall _tmp13 ;	# live variables = {_tmp13}
	PopParams 8 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Stack.Push:
	BeginFunc 60 ;	# live variables = {this,i}
	_tmp14 = *(this + 8) ;	# live variables = {this,i}
	_tmp15 = *(this + 4) ;	# live variables = {this,i,_tmp14}
	_tmp16 = 0 ;	# live variables = {this,i,_tmp14,_tmp15}
	_tmp17 = _tmp15 < _tmp16 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp16}
	_tmp18 = *(_tmp14 + -4) ;	# live variables = {this,i,_tmp14,_tmp15,_tmp16,_tmp17}
	_tmp19 = _tmp15 < _tmp18 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp16,_tmp17,_tmp18}
	_tmp20 = _tmp19 == _tmp16 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp16,_tmp17,_tmp19}
	_tmp21 = _tmp17 || _tmp20 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp17,_tmp20}
	IfZ _tmp21 Goto _L1 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp21}
	_tmp22 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,i,_tmp14,_tmp15}
	PushParam _tmp22 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp22}
	LCall _PrintString ;	# live variables = {this,i,_tmp14,_tmp15}
	PopParams 4 ;	# live variables = {this,i,_tmp14,_tmp15}
	LCall _Halt ;	# live variables = {this,i,_tmp14,_tmp15}
_L1:
	_tmp23 = 4 ;	# live variables = {this,i,_tmp14,_tmp15}
	_tmp24 = _tmp23 * _tmp15 ;	# live variables = {this,i,_tmp14,_tmp15,_tmp23}
	_tmp25 = _tmp14 + _tmp24 ;	# live variables = {this,i,_tmp14,_tmp24}
	*(_tmp25) = i ;	# live variables = {this,i,_tmp25}
	_tmp26 = *(this + 4) ;	# live variables = {this}
	_tmp27 = 1 ;	# live variables = {this,_tmp26}
	_tmp28 = _tmp26 + _tmp27 ;	# live variables = {this,_tmp26,_tmp27}
	*(this + 4) = _tmp28 ;	# live variables = {this,_tmp28}
	EndFunc ;	# live variables = {}
_Stack.Pop:
	BeginFunc 76 ;	# live variables = {this}
	_tmp29 = *(this + 8) ;	# live variables = {this}
	_tmp30 = *(this + 4) ;	# live variables = {this,_tmp29}
	_tmp31 = 1 ;	# live variables = {this,_tmp29,_tmp30}
	_tmp32 = _tmp30 - _tmp31 ;	# live variables = {this,_tmp29,_tmp30,_tmp31}
	_tmp33 = 0 ;	# live variables = {this,_tmp29,_tmp32}
	_tmp34 = _tmp32 < _tmp33 ;	# live variables = {this,_tmp29,_tmp32,_tmp33}
	_tmp35 = *(_tmp29 + -4) ;	# live variables = {this,_tmp29,_tmp32,_tmp33,_tmp34}
	_tmp36 = _tmp32 < _tmp35 ;	# live variables = {this,_tmp29,_tmp32,_tmp33,_tmp34,_tmp35}
	_tmp37 = _tmp36 == _tmp33 ;	# live variables = {this,_tmp29,_tmp32,_tmp33,_tmp34,_tmp36}
	_tmp38 = _tmp34 || _tmp37 ;	# live variables = {this,_tmp29,_tmp32,_tmp34,_tmp37}
	IfZ _tmp38 Goto _L2 ;	# live variables = {this,_tmp29,_tmp32,_tmp38}
	_tmp39 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {this,_tmp29,_tmp32}
	PushParam _tmp39 ;	# live variables = {this,_tmp29,_tmp32,_tmp39}
	LCall _PrintString ;	# live variables = {this,_tmp29,_tmp32}
	PopParams 4 ;	# live variables = {this,_tmp29,_tmp32}
	LCall _Halt ;	# live variables = {this,_tmp29,_tmp32}
_L2:
	_tmp40 = 4 ;	# live variables = {this,_tmp29,_tmp32}
	_tmp41 = _tmp40 * _tmp32 ;	# live variables = {this,_tmp29,_tmp32,_tmp40}
	_tmp42 = _tmp29 + _tmp41 ;	# live variables = {this,_tmp29,_tmp41}
	_tmp43 = *(_tmp42) ;	# live variables = {this,_tmp42}
	val = _tmp43 ;	# live variables = {this,_tmp43}
	_tmp44 = *(this + 4) ;	# live variables = {this,val}
	_tmp45 = 1 ;	# live variables = {this,val,_tmp44}
	_tmp46 = _tmp44 - _tmp45 ;	# live variables = {this,val,_tmp44,_tmp45}
	*(this + 4) = _tmp46 ;	# live variables = {this,val,_tmp46}
	Return val ;	# live variables = {val}
	EndFunc ;	# live variables = {}
_Stack.NumElems:
	BeginFunc 4 ;	# live variables = {this}
	_tmp47 = *(this + 4) ;	# live variables = {this}
	Return _tmp47 ;	# live variables = {_tmp47}
	EndFunc ;	# live variables = {}
VTable Stack =
	_Stack.Init,
	_Stack.Push,
	_Stack.Pop,
	_Stack.NumElems,
; 
main:
	BeginFunc 136 ;	# live variables = {}
	_tmp48 = 12 ;	# live variables = {}
	PushParam _tmp48 ;	# live variables = {_tmp48}
	_tmp49 = LCall _Alloc ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp49}
	_tmp50 = Stack ;	# live variables = {_tmp49}
	*(_tmp49) = _tmp50 ;	# live variables = {_tmp49,_tmp50}
	s = _tmp49 ;	# live variables = {_tmp49}
	_tmp51 = *(s) ;	# live variables = {s}
	_tmp52 = *(_tmp51) ;	# live variables = {s,_tmp51}
	PushParam s ;	# live variables = {s,_tmp52}
	ACall _tmp52 ;	# live variables = {s,_tmp52}
	PopParams 4 ;	# live variables = {s}
	_tmp53 = 3 ;	# live variables = {s}
	_tmp54 = *(s) ;	# live variables = {s,_tmp53}
	_tmp55 = *(_tmp54 + 4) ;	# live variables = {s,_tmp53,_tmp54}
	PushParam _tmp53 ;	# live variables = {s,_tmp53,_tmp55}
	PushParam s ;	# live variables = {s,_tmp55}
	ACall _tmp55 ;	# live variables = {s,_tmp55}
	PopParams 8 ;	# live variables = {s}
	_tmp56 = 7 ;	# live variables = {s}
	_tmp57 = *(s) ;	# live variables = {s,_tmp56}
	_tmp58 = *(_tmp57 + 4) ;	# live variables = {s,_tmp56,_tmp57}
	PushParam _tmp56 ;	# live variables = {s,_tmp56,_tmp58}
	PushParam s ;	# live variables = {s,_tmp58}
	ACall _tmp58 ;	# live variables = {s,_tmp58}
	PopParams 8 ;	# live variables = {s}
	_tmp59 = 4 ;	# live variables = {s}
	_tmp60 = *(s) ;	# live variables = {s,_tmp59}
	_tmp61 = *(_tmp60 + 4) ;	# live variables = {s,_tmp59,_tmp60}
	PushParam _tmp59 ;	# live variables = {s,_tmp59,_tmp61}
	PushParam s ;	# live variables = {s,_tmp61}
	ACall _tmp61 ;	# live variables = {s,_tmp61}
	PopParams 8 ;	# live variables = {s}
	_tmp62 = *(s) ;	# live variables = {s}
	_tmp63 = *(_tmp62 + 12) ;	# live variables = {s,_tmp62}
	PushParam s ;	# live variables = {s,_tmp63}
	_tmp64 = ACall _tmp63 ;	# live variables = {s,_tmp63}
	PopParams 4 ;	# live variables = {s,_tmp64}
	PushParam _tmp64 ;	# live variables = {s,_tmp64}
	LCall _PrintInt ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp65 = " " ;	# live variables = {s}
	PushParam _tmp65 ;	# live variables = {s,_tmp65}
	LCall _PrintString ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp66 = *(s) ;	# live variables = {s}
	_tmp67 = *(_tmp66 + 8) ;	# live variables = {s,_tmp66}
	PushParam s ;	# live variables = {s,_tmp67}
	_tmp68 = ACall _tmp67 ;	# live variables = {s,_tmp67}
	PopParams 4 ;	# live variables = {s,_tmp68}
	PushParam _tmp68 ;	# live variables = {s,_tmp68}
	LCall _PrintInt ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp69 = " " ;	# live variables = {s}
	PushParam _tmp69 ;	# live variables = {s,_tmp69}
	LCall _PrintString ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp70 = *(s) ;	# live variables = {s}
	_tmp71 = *(_tmp70 + 8) ;	# live variables = {s,_tmp70}
	PushParam s ;	# live variables = {s,_tmp71}
	_tmp72 = ACall _tmp71 ;	# live variables = {s,_tmp71}
	PopParams 4 ;	# live variables = {s,_tmp72}
	PushParam _tmp72 ;	# live variables = {s,_tmp72}
	LCall _PrintInt ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp73 = " " ;	# live variables = {s}
	PushParam _tmp73 ;	# live variables = {s,_tmp73}
	LCall _PrintString ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp74 = *(s) ;	# live variables = {s}
	_tmp75 = *(_tmp74 + 8) ;	# live variables = {s,_tmp74}
	PushParam s ;	# live variables = {s,_tmp75}
	_tmp76 = ACall _tmp75 ;	# live variables = {s,_tmp75}
	PopParams 4 ;	# live variables = {s,_tmp76}
	PushParam _tmp76 ;	# live variables = {s,_tmp76}
	LCall _PrintInt ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp77 = " " ;	# live variables = {s}
	PushParam _tmp77 ;	# live variables = {s,_tmp77}
	LCall _PrintString ;	# live variables = {s}
	PopParams 4 ;	# live variables = {s}
	_tmp78 = *(s) ;	# live variables = {s}
	_tmp79 = *(_tmp78 + 12) ;	# live variables = {s,_tmp78}
	PushParam s ;	# live variables = {s,_tmp79}
	_tmp80 = ACall _tmp79 ;	# live variables = {_tmp79}
	PopParams 4 ;	# live variables = {_tmp80}
	PushParam _tmp80 ;	# live variables = {_tmp80}
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
