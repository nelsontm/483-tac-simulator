_factorial:
	BeginFunc 36 ;	# live variables = {n}
	_tmp0 = 1 ;	# live variables = {n}
	_tmp1 = n < _tmp0 ;	# live variables = {n,_tmp0}
	_tmp2 = n == _tmp0 ;	# live variables = {n,_tmp0,_tmp1}
	_tmp3 = _tmp1 || _tmp2 ;	# live variables = {n,_tmp1,_tmp2}
	IfZ _tmp3 Goto _L0 ;	# live variables = {n,_tmp3}
	_tmp4 = 1 ;	# live variables = {}
	Return _tmp4 ;	# live variables = {_tmp4}
_L0:
	_tmp5 = 1 ;	# live variables = {n}
	_tmp6 = n - _tmp5 ;	# live variables = {n,_tmp5}
	PushParam _tmp6 ;	# live variables = {n,_tmp6}
	_tmp7 = LCall _factorial ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n,_tmp7}
	_tmp8 = n * _tmp7 ;	# live variables = {n,_tmp7}
	Return _tmp8 ;	# live variables = {_tmp8}
	EndFunc ;	# live variables = {}
main:
	BeginFunc 48 ;	# live variables = {}
	_tmp9 = 1 ;	# live variables = {}
	n = _tmp9 ;	# live variables = {_tmp9}
_L1:
	_tmp10 = 15 ;	# live variables = {n}
	_tmp11 = n < _tmp10 ;	# live variables = {n,_tmp10}
	_tmp12 = n == _tmp10 ;	# live variables = {n,_tmp10,_tmp11}
	_tmp13 = _tmp11 || _tmp12 ;	# live variables = {n,_tmp11,_tmp12}
	IfZ _tmp13 Goto _L2 ;	# live variables = {n,_tmp13}
	_tmp14 = "Factorial(" ;	# live variables = {n}
	PushParam _tmp14 ;	# live variables = {n,_tmp14}
	LCall _PrintString ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	PushParam n ;	# live variables = {n}
	LCall _PrintInt ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	_tmp15 = ") = " ;	# live variables = {n}
	PushParam _tmp15 ;	# live variables = {n,_tmp15}
	LCall _PrintString ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	PushParam n ;	# live variables = {n}
	_tmp16 = LCall _factorial ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n,_tmp16}
	PushParam _tmp16 ;	# live variables = {n,_tmp16}
	LCall _PrintInt ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	_tmp17 = "\n" ;	# live variables = {n}
	PushParam _tmp17 ;	# live variables = {n,_tmp17}
	LCall _PrintString ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	_tmp18 = 1 ;	# live variables = {n}
	_tmp19 = n + _tmp18 ;	# live variables = {n,_tmp18}
	n = _tmp19 ;	# live variables = {_tmp19}
	Goto _L1 ;	# live variables = {n}
_L2:
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
