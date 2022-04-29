_foo:
	BeginFunc 16 ;	# live variables = {a,c}
	IfZ c Goto _L0 ;	# live variables = {a,c}
	_tmp0 = 2 ;	# live variables = {a}
	_tmp1 = a + _tmp0 ;	# live variables = {a,_tmp0}
	Return _tmp1 ;	# live variables = {_tmp1}
	Goto _L1 ;	# live variables = {}
_L0:
	PushParam a ;	# live variables = {a}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp2 = " wacky.\n" ;	# live variables = {}
	PushParam _tmp2 ;	# live variables = {_tmp2}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
_L1:
	_tmp3 = 18 ;	# live variables = {}
	Return _tmp3 ;	# live variables = {_tmp3}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 84 ;	# live variables = {}
	_tmp4 = 10 ;	# live variables = {}
	a = _tmp4 ;	# live variables = {_tmp4}
	_tmp5 = 2 ;	# live variables = {a}
	_tmp6 = a / _tmp5 ;	# live variables = {a,_tmp5}
	b = _tmp6 ;	# live variables = {a,_tmp6}
	_tmp7 = 1 ;	# live variables = {a,b}
	PushParam _tmp7 ;	# live variables = {a,b,_tmp7}
	PushParam a ;	# live variables = {a,b}
	_tmp8 = LCall _foo ;	# live variables = {a,b}
	PopParams 8 ;	# live variables = {a,b}
	_tmp9 = 2 ;	# live variables = {a,b}
	_tmp10 = b + _tmp9 ;	# live variables = {a,b,_tmp9}
	_tmp11 = a < b ;	# live variables = {a,b,_tmp10}
	_tmp12 = a == b ;	# live variables = {a,b,_tmp10,_tmp11}
	_tmp13 = _tmp11 || _tmp12 ;	# live variables = {_tmp10,_tmp11,_tmp12}
	PushParam _tmp13 ;	# live variables = {_tmp10,_tmp13}
	PushParam _tmp10 ;	# live variables = {_tmp10}
	_tmp14 = LCall _foo ;	# live variables = {}
	PopParams 8 ;	# live variables = {}
	_tmp15 = 3 ;	# live variables = {}
	_tmp16 = 1 ;	# live variables = {_tmp15}
	_tmp17 = 0 ;	# live variables = {_tmp15,_tmp16}
	_tmp18 = _tmp16 && _tmp17 ;	# live variables = {_tmp15,_tmp16,_tmp17}
	PushParam _tmp18 ;	# live variables = {_tmp15,_tmp18}
	PushParam _tmp15 ;	# live variables = {_tmp15}
	_tmp19 = LCall _foo ;	# live variables = {}
	PopParams 8 ;	# live variables = {_tmp19}
	_tmp20 = 1 ;	# live variables = {_tmp19}
	_tmp21 = 0 ;	# live variables = {_tmp19,_tmp20}
	_tmp22 = _tmp20 == _tmp21 ;	# live variables = {_tmp19,_tmp20,_tmp21}
	PushParam _tmp22 ;	# live variables = {_tmp19,_tmp22}
	PushParam _tmp19 ;	# live variables = {_tmp19}
	_tmp23 = LCall _foo ;	# live variables = {}
	PopParams 8 ;	# live variables = {}
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
