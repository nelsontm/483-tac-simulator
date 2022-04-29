main:
	BeginFunc 124 ;	# live variables = {}
	_tmp0 = 10 ;	# live variables = {}
	_tmp1 = 1 ;	# live variables = {_tmp0}
	_tmp2 = _tmp0 < _tmp1 ;	# live variables = {_tmp0,_tmp1}
	IfZ _tmp2 Goto _L0 ;	# live variables = {_tmp0,_tmp2}
	_tmp3 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {_tmp0}
	PushParam _tmp3 ;	# live variables = {_tmp0,_tmp3}
	LCall _PrintString ;	# live variables = {_tmp0}
	PopParams 4 ;	# live variables = {_tmp0}
	LCall _Halt ;	# live variables = {_tmp0}
_L0:
	_tmp4 = 1 ;	# live variables = {_tmp0}
	_tmp5 = _tmp4 + _tmp0 ;	# live variables = {_tmp0,_tmp4}
	_tmp6 = 4 ;	# live variables = {_tmp0,_tmp5}
	_tmp7 = _tmp5 * _tmp6 ;	# live variables = {_tmp0,_tmp5,_tmp6}
	PushParam _tmp7 ;	# live variables = {_tmp0,_tmp6,_tmp7}
	_tmp8 = LCall _Alloc ;	# live variables = {_tmp0,_tmp6}
	PopParams 4 ;	# live variables = {_tmp0,_tmp6,_tmp8}
	*(_tmp8) = _tmp0 ;	# live variables = {_tmp0,_tmp6,_tmp8}
	_tmp9 = _tmp8 + _tmp6 ;	# live variables = {_tmp6,_tmp8}
	arr = _tmp9 ;	# live variables = {_tmp9}
	_tmp10 = 0 ;	# live variables = {arr}
	i = _tmp10 ;	# live variables = {arr,_tmp10}
_L1:
	_tmp11 = 10 ;	# live variables = {arr,i}
	_tmp12 = i < _tmp11 ;	# live variables = {arr,i,_tmp11}
	_tmp13 = i == _tmp11 ;	# live variables = {arr,i,_tmp11,_tmp12}
	_tmp14 = _tmp12 || _tmp13 ;	# live variables = {arr,i,_tmp12,_tmp13}
	IfZ _tmp14 Goto _L2 ;	# live variables = {arr,i,_tmp14}
	_tmp15 = 0 ;	# live variables = {arr,i}
	_tmp16 = i < _tmp15 ;	# live variables = {arr,i,_tmp15}
	_tmp17 = *(arr + -4) ;	# live variables = {arr,i,_tmp15,_tmp16}
	_tmp18 = i < _tmp17 ;	# live variables = {arr,i,_tmp15,_tmp16,_tmp17}
	_tmp19 = _tmp18 == _tmp15 ;	# live variables = {arr,i,_tmp15,_tmp16,_tmp18}
	_tmp20 = _tmp16 || _tmp19 ;	# live variables = {arr,i,_tmp16,_tmp19}
	IfZ _tmp20 Goto _L3 ;	# live variables = {arr,i,_tmp20}
	_tmp21 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {arr,i}
	PushParam _tmp21 ;	# live variables = {arr,i,_tmp21}
	LCall _PrintString ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
	LCall _Halt ;	# live variables = {arr,i}
_L3:
	_tmp22 = 4 ;	# live variables = {arr,i}
	_tmp23 = _tmp22 * i ;	# live variables = {arr,i,_tmp22}
	_tmp24 = arr + _tmp23 ;	# live variables = {arr,i,_tmp23}
	*(_tmp24) = i ;	# live variables = {arr,i,_tmp24}
	PushParam i ;	# live variables = {arr,i}
	LCall _PrintInt ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
	_tmp25 = "\n" ;	# live variables = {arr,i}
	PushParam _tmp25 ;	# live variables = {arr,i,_tmp25}
	LCall _PrintString ;	# live variables = {arr,i}
	PopParams 4 ;	# live variables = {arr,i}
	_tmp26 = 1 ;	# live variables = {arr,i}
	_tmp27 = i + _tmp26 ;	# live variables = {arr,i,_tmp26}
	i = _tmp27 ;	# live variables = {arr,_tmp27}
	Goto _L1 ;	# live variables = {arr,i}
_L2:
	_tmp28 = "Done\n" ;	# live variables = {}
	PushParam _tmp28 ;	# live variables = {_tmp28}
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
