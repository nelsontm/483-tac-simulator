_fib:
	BeginFunc 68 ;	# live variables = {base,f2}
	_tmp0 = 1 ;	# live variables = {base,f2}
	_tmp1 = base < _tmp0 ;	# live variables = {base,_tmp0,f2}
	_tmp2 = base == _tmp0 ;	# live variables = {base,_tmp0,_tmp1,f2}
	_tmp3 = _tmp1 || _tmp2 ;	# live variables = {base,_tmp1,_tmp2,f2}
	IfZ _tmp3 Goto _L0 ;	# live variables = {base,_tmp3,f2}
	Return base ;	# live variables = {base}
	Goto _L1 ;	# live variables = {}
_L0:
	_tmp4 = 0 ;	# live variables = {base,f2}
	f0 = _tmp4 ;	# live variables = {base,f2,_tmp4}
	_tmp5 = 1 ;	# live variables = {base,f0,f2}
	f1 = _tmp5 ;	# live variables = {base,f0,f2,_tmp5}
	_tmp6 = 2 ;	# live variables = {base,f0,f1,f2}
	i = _tmp6 ;	# live variables = {base,f0,f1,f2,_tmp6}
_L2:
	_tmp7 = i < base ;	# live variables = {base,i,f0,f1,f2}
	_tmp8 = i == base ;	# live variables = {base,i,f0,f1,f2,_tmp7}
	_tmp9 = _tmp7 || _tmp8 ;	# live variables = {base,i,f0,f1,f2,_tmp7,_tmp8}
	IfZ _tmp9 Goto _L3 ;	# live variables = {base,i,f0,f1,f2,_tmp9}
	_tmp10 = f0 + f1 ;	# live variables = {base,i,f0,f1}
	f2 = _tmp10 ;	# live variables = {base,i,f1,_tmp10}
	f0 = f1 ;	# live variables = {base,i,f1,f2}
	f1 = f2 ;	# live variables = {base,i,f0,f2}
	_tmp11 = 1 ;	# live variables = {base,i,f0,f1,f2}
	_tmp12 = i + _tmp11 ;	# live variables = {base,i,f0,f1,f2,_tmp11}
	i = _tmp12 ;	# live variables = {base,f0,f1,f2,_tmp12}
	Goto _L2 ;	# live variables = {base,i,f0,f1,f2}
_L3:
	Return f2 ;	# live variables = {f2}
_L1:
	EndFunc ;	# live variables = {}
main:
	BeginFunc 56 ;	# live variables = {}
	_tmp13 = "\nThis program computes Fibonacci numbers (slowly..." ;	# live variables = {}
	PushParam _tmp13 ;	# live variables = {_tmp13}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
_L4:
	_tmp14 = 1 ;	# live variables = {}
	IfZ _tmp14 Goto _L5 ;	# live variables = {_tmp14}
	_tmp15 = "\nEnter the fibonacci number you want: (-1 to qui..." ;	# live variables = {}
	PushParam _tmp15 ;	# live variables = {_tmp15}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp16 = LCall _ReadInteger ;	# live variables = {}
	n = _tmp16 ;	# live variables = {_tmp16}
	_tmp17 = 1 ;	# live variables = {n}
	_tmp18 = 0 ;	# live variables = {n,_tmp17}
	_tmp19 = _tmp18 - _tmp17 ;	# live variables = {n,_tmp17,_tmp18}
	_tmp20 = n == _tmp19 ;	# live variables = {n,_tmp19}
	IfZ _tmp20 Goto _L6 ;	# live variables = {n,_tmp20}
	Goto _L5 ;	# live variables = {}
_L6:
	_tmp21 = "Fib(" ;	# live variables = {n}
	PushParam _tmp21 ;	# live variables = {n,_tmp21}
	LCall _PrintString ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	PushParam n ;	# live variables = {n}
	LCall _PrintInt ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	_tmp22 = ") = " ;	# live variables = {n}
	PushParam _tmp22 ;	# live variables = {n,_tmp22}
	LCall _PrintString ;	# live variables = {n}
	PopParams 4 ;	# live variables = {n}
	PushParam n ;	# live variables = {n}
	_tmp23 = LCall _fib ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp23}
	PushParam _tmp23 ;	# live variables = {_tmp23}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp24 = "\n" ;	# live variables = {}
	PushParam _tmp24 ;	# live variables = {_tmp24}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	Goto _L4 ;	# live variables = {}
_L5:
	_tmp25 = "Goodbye!\n" ;	# live variables = {}
	PushParam _tmp25 ;	# live variables = {_tmp25}
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
