main:
	BeginFunc 40 ;	# live variables = {}
	_tmp0 = 12 ;	# live variables = {}
	PushParam _tmp0 ;	# live variables = {_tmp0}
	_tmp1 = LCall _Alloc ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp1}
	_tmp2 = Cow ;	# live variables = {_tmp1}
	*(_tmp1) = _tmp2 ;	# live variables = {_tmp1,_tmp2}
	betsy = _tmp1 ;	# live variables = {_tmp1}
	_tmp3 = 100 ;	# live variables = {betsy}
	_tmp4 = 122 ;	# live variables = {betsy,_tmp3}
	_tmp5 = *(betsy) ;	# live variables = {betsy,_tmp3,_tmp4}
	_tmp6 = *(_tmp5) ;	# live variables = {betsy,_tmp3,_tmp4,_tmp5}
	PushParam _tmp4 ;	# live variables = {betsy,_tmp3,_tmp4,_tmp6}
	PushParam _tmp3 ;	# live variables = {betsy,_tmp3,_tmp6}
	PushParam betsy ;	# live variables = {betsy,_tmp6}
	ACall _tmp6 ;	# live variables = {betsy,_tmp6}
	PopParams 12 ;	# live variables = {betsy}
	_tmp7 = *(betsy) ;	# live variables = {betsy}
	_tmp8 = *(_tmp7 + 4) ;	# live variables = {betsy,_tmp7}
	PushParam betsy ;	# live variables = {betsy,_tmp8}
	ACall _tmp8 ;	# live variables = {_tmp8}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Cow.Init:
	BeginFunc 0 ;	# live variables = {this,w,h}
	*(this + 8) = w ;	# live variables = {this,w,h}
	*(this + 4) = h ;	# live variables = {this,h}
	EndFunc ;	# live variables = {}
_Cow.Moo:
	BeginFunc 16 ;	# live variables = {this}
	_tmp9 = *(this + 4) ;	# live variables = {this}
	PushParam _tmp9 ;	# live variables = {this,_tmp9}
	LCall _PrintInt ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp10 = " " ;	# live variables = {this}
	PushParam _tmp10 ;	# live variables = {this,_tmp10}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp11 = *(this + 8) ;	# live variables = {this}
	PushParam _tmp11 ;	# live variables = {_tmp11}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp12 = "\n" ;	# live variables = {}
	PushParam _tmp12 ;	# live variables = {_tmp12}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
VTable Cow =
	_Cow.Init,
	_Cow.Moo,
; 
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