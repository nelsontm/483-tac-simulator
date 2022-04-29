_Animal.InitAnimal:
	BeginFunc 0 ;	# live variables = {this,h,mom}
	*(this + 4) = h ;	# live variables = {this,h,mom}
	*(this + 8) = mom ;	# live variables = {this,mom}
	EndFunc ;	# live variables = {}
_Animal.GetHeight:
	BeginFunc 4 ;	# live variables = {this}
	_tmp0 = *(this + 4) ;	# live variables = {this}
	Return _tmp0 ;	# live variables = {_tmp0}
	EndFunc ;	# live variables = {}
_Animal.GetMom:
	BeginFunc 4 ;	# live variables = {this}
	_tmp1 = *(this + 8) ;	# live variables = {this}
	Return _tmp1 ;	# live variables = {_tmp1}
	EndFunc ;	# live variables = {}
VTable Animal =
	_Animal.InitAnimal,
	_Animal.GetHeight,
	_Animal.GetMom,
; 
_Cow.InitCow:
	BeginFunc 8 ;	# live variables = {this,h,m,spot}
	*(this + 12) = spot ;	# live variables = {this,h,m,spot}
	_tmp2 = *(this) ;	# live variables = {this,h,m}
	_tmp3 = *(_tmp2) ;	# live variables = {this,h,m,_tmp2}
	PushParam m ;	# live variables = {this,h,m,_tmp3}
	PushParam h ;	# live variables = {this,h,_tmp3}
	PushParam this ;	# live variables = {this,_tmp3}
	ACall _tmp3 ;	# live variables = {_tmp3}
	PopParams 12 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Cow.IsSpottedCow:
	BeginFunc 4 ;	# live variables = {this}
	_tmp4 = *(this + 12) ;	# live variables = {this}
	Return _tmp4 ;	# live variables = {_tmp4}
	EndFunc ;	# live variables = {}
VTable Cow =
	_Animal.InitAnimal,
	_Animal.GetHeight,
	_Animal.GetMom,
	_Cow.InitCow,
	_Cow.IsSpottedCow,
; 
main:
	BeginFunc 84 ;	# live variables = {}
	_tmp5 = 16 ;	# live variables = {}
	PushParam _tmp5 ;	# live variables = {_tmp5}
	_tmp6 = LCall _Alloc ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp6}
	_tmp7 = Cow ;	# live variables = {_tmp6}
	*(_tmp6) = _tmp7 ;	# live variables = {_tmp6,_tmp7}
	betsy = _tmp6 ;	# live variables = {_tmp6}
	_tmp8 = 5 ;	# live variables = {betsy}
	_tmp9 = 0 ;	# live variables = {betsy,_tmp8}
	_tmp10 = 1 ;	# live variables = {betsy,_tmp8,_tmp9}
	_tmp11 = *(betsy) ;	# live variables = {betsy,_tmp8,_tmp9,_tmp10}
	_tmp12 = *(_tmp11 + 12) ;	# live variables = {betsy,_tmp8,_tmp9,_tmp10,_tmp11}
	PushParam _tmp10 ;	# live variables = {betsy,_tmp8,_tmp9,_tmp10,_tmp12}
	PushParam _tmp9 ;	# live variables = {betsy,_tmp8,_tmp9,_tmp12}
	PushParam _tmp8 ;	# live variables = {betsy,_tmp8,_tmp12}
	PushParam betsy ;	# live variables = {betsy,_tmp12}
	ACall _tmp12 ;	# live variables = {betsy,_tmp12}
	PopParams 16 ;	# live variables = {betsy}
	b = betsy ;	# live variables = {betsy}
	_tmp13 = *(b) ;	# live variables = {betsy,b}
	_tmp14 = *(_tmp13 + 8) ;	# live variables = {betsy,b,_tmp13}
	PushParam b ;	# live variables = {betsy,b,_tmp14}
	_tmp15 = ACall _tmp14 ;	# live variables = {betsy,b,_tmp14}
	PopParams 4 ;	# live variables = {betsy,b}
	_tmp16 = "spots: " ;	# live variables = {betsy,b}
	PushParam _tmp16 ;	# live variables = {betsy,b,_tmp16}
	LCall _PrintString ;	# live variables = {betsy,b}
	PopParams 4 ;	# live variables = {betsy,b}
	_tmp17 = *(betsy) ;	# live variables = {betsy,b}
	_tmp18 = *(_tmp17 + 16) ;	# live variables = {betsy,b,_tmp17}
	PushParam betsy ;	# live variables = {betsy,b,_tmp18}
	_tmp19 = ACall _tmp18 ;	# live variables = {b,_tmp18}
	PopParams 4 ;	# live variables = {b,_tmp19}
	PushParam _tmp19 ;	# live variables = {b,_tmp19}
	LCall _PrintBool ;	# live variables = {b}
	PopParams 4 ;	# live variables = {b}
	_tmp20 = "    height: " ;	# live variables = {b}
	PushParam _tmp20 ;	# live variables = {b,_tmp20}
	LCall _PrintString ;	# live variables = {b}
	PopParams 4 ;	# live variables = {b}
	_tmp21 = *(b) ;	# live variables = {b}
	_tmp22 = *(_tmp21 + 4) ;	# live variables = {b,_tmp21}
	PushParam b ;	# live variables = {b,_tmp22}
	_tmp23 = ACall _tmp22 ;	# live variables = {_tmp22}
	PopParams 4 ;	# live variables = {_tmp23}
	PushParam _tmp23 ;	# live variables = {_tmp23}
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
