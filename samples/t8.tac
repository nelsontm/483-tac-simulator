_Squash.Grow:
	BeginFunc 16 ;	# live variables = {}
	_tmp0 = "But I don't like squash\n" ;	# live variables = {}
	PushParam _tmp0 ;	# live variables = {_tmp0}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp1 = 10 ;	# live variables = {}
	_tmp2 = 5 ;	# live variables = {_tmp1}
	_tmp3 = _tmp1 * _tmp2 ;	# live variables = {_tmp1,_tmp2}
	PushParam _tmp3 ;	# live variables = {_tmp3}
	LCall _PrintInt ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
VTable Squash =
	_Vegetable.Eat,
	_Squash.Grow,
; 
_Vegetable.Eat:
	BeginFunc 40 ;	# live variables = {this,veg,s,w}
	_tmp4 = 5 ;	# live variables = {this,veg,s,w}
	_tmp5 = 2 ;	# live variables = {this,veg,s,w,_tmp4}
	_tmp6 = _tmp4 % _tmp5 ;	# live variables = {this,veg,s,w,_tmp4,_tmp5}
	*(this + 4) = _tmp6 ;	# live variables = {this,veg,s,w,_tmp6}
	_tmp7 = "Yum! " ;	# live variables = {this,veg,s,w}
	PushParam _tmp7 ;	# live variables = {this,veg,s,w,_tmp7}
	LCall _PrintString ;	# live variables = {this,veg,s,w}
	PopParams 4 ;	# live variables = {this,veg,s,w}
	_tmp8 = *(this + 4) ;	# live variables = {this,veg,s,w}
	PushParam _tmp8 ;	# live variables = {veg,s,w,_tmp8}
	LCall _PrintInt ;	# live variables = {veg,s,w}
	PopParams 4 ;	# live variables = {veg,s,w}
	_tmp9 = "\n" ;	# live variables = {veg,s,w}
	PushParam _tmp9 ;	# live variables = {veg,s,w,_tmp9}
	LCall _PrintString ;	# live variables = {veg,s,w}
	PopParams 4 ;	# live variables = {veg,s,w}
	_tmp10 = *(veg) ;	# live variables = {veg,s,w}
	_tmp11 = *(_tmp10 + 4) ;	# live variables = {veg,s,w,_tmp10}
	PushParam w ;	# live variables = {veg,s,w,_tmp11}
	PushParam s ;	# live variables = {veg,s,_tmp11}
	PushParam veg ;	# live variables = {veg,_tmp11}
	ACall _tmp11 ;	# live variables = {_tmp11}
	PopParams 12 ;	# live variables = {}
	Return  ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Vegetable.Grow:
	BeginFunc 12 ;	# live variables = {this}
	_tmp12 = "Grow, little vegetables, grow!\n" ;	# live variables = {this}
	PushParam _tmp12 ;	# live variables = {this,_tmp12}
	LCall _PrintString ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this}
	_tmp13 = *(this) ;	# live variables = {this}
	_tmp14 = *(_tmp13) ;	# live variables = {this,_tmp13}
	PushParam this ;	# live variables = {this,_tmp14}
	PushParam this ;	# live variables = {this,_tmp14}
	ACall _tmp14 ;	# live variables = {_tmp14}
	PopParams 8 ;	# live variables = {}
	EndFunc ;	# live variables = {}
VTable Vegetable =
	_Vegetable.Eat,
	_Vegetable.Grow,
; 
_Grow:
	BeginFunc 4 ;	# live variables = {}
	_tmp15 = "mmm... veggies!\n" ;	# live variables = {}
	PushParam _tmp15 ;	# live variables = {_tmp15}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	EndFunc ;	# live variables = {}
VTable Seeds =
; 
main:
	BeginFunc 264 ;	# live variables = {}
	_tmp16 = 2 ;	# live variables = {}
	_tmp17 = 1 ;	# live variables = {_tmp16}
	_tmp18 = _tmp16 < _tmp17 ;	# live variables = {_tmp16,_tmp17}
	IfZ _tmp18 Goto _L0 ;	# live variables = {_tmp16,_tmp18}
	_tmp19 = "Decaf runtime error: Array size is <= 0\n" ;	# live variables = {_tmp16}
	PushParam _tmp19 ;	# live variables = {_tmp16,_tmp19}
	LCall _PrintString ;	# live variables = {_tmp16}
	PopParams 4 ;	# live variables = {_tmp16}
	LCall _Halt ;	# live variables = {_tmp16}
_L0:
	_tmp20 = 1 ;	# live variables = {_tmp16}
	_tmp21 = _tmp20 + _tmp16 ;	# live variables = {_tmp16,_tmp20}
	_tmp22 = 4 ;	# live variables = {_tmp16,_tmp21}
	_tmp23 = _tmp21 * _tmp22 ;	# live variables = {_tmp16,_tmp21,_tmp22}
	PushParam _tmp23 ;	# live variables = {_tmp16,_tmp22,_tmp23}
	_tmp24 = LCall _Alloc ;	# live variables = {_tmp16,_tmp22}
	PopParams 4 ;	# live variables = {_tmp16,_tmp22,_tmp24}
	*(_tmp24) = _tmp16 ;	# live variables = {_tmp16,_tmp22,_tmp24}
	_tmp25 = _tmp24 + _tmp22 ;	# live variables = {_tmp22,_tmp24}
	veggies = _tmp25 ;	# live variables = {_tmp25}
	_tmp26 = 0 ;	# live variables = {veggies}
	_tmp27 = 0 ;	# live variables = {veggies,_tmp26}
	_tmp28 = _tmp26 < _tmp27 ;	# live variables = {veggies,_tmp26,_tmp27}
	_tmp29 = *(veggies + -4) ;	# live variables = {veggies,_tmp26,_tmp27,_tmp28}
	_tmp30 = _tmp26 < _tmp29 ;	# live variables = {veggies,_tmp26,_tmp27,_tmp28,_tmp29}
	_tmp31 = _tmp30 == _tmp27 ;	# live variables = {veggies,_tmp26,_tmp27,_tmp28,_tmp30}
	_tmp32 = _tmp28 || _tmp31 ;	# live variables = {veggies,_tmp26,_tmp28,_tmp31}
	IfZ _tmp32 Goto _L1 ;	# live variables = {veggies,_tmp26,_tmp32}
	_tmp33 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {veggies,_tmp26}
	PushParam _tmp33 ;	# live variables = {veggies,_tmp26,_tmp33}
	LCall _PrintString ;	# live variables = {veggies,_tmp26}
	PopParams 4 ;	# live variables = {veggies,_tmp26}
	LCall _Halt ;	# live variables = {veggies,_tmp26}
_L1:
	_tmp34 = 4 ;	# live variables = {veggies,_tmp26}
	_tmp35 = _tmp34 * _tmp26 ;	# live variables = {veggies,_tmp26,_tmp34}
	_tmp36 = veggies + _tmp35 ;	# live variables = {veggies,_tmp35}
	_tmp37 = 12 ;	# live variables = {veggies,_tmp36}
	PushParam _tmp37 ;	# live variables = {veggies,_tmp36,_tmp37}
	_tmp38 = LCall _Alloc ;	# live variables = {veggies,_tmp36}
	PopParams 4 ;	# live variables = {veggies,_tmp36,_tmp38}
	_tmp39 = Squash ;	# live variables = {veggies,_tmp36,_tmp38}
	*(_tmp38) = _tmp39 ;	# live variables = {veggies,_tmp36,_tmp38,_tmp39}
	*(_tmp36) = _tmp38 ;	# live variables = {veggies,_tmp36,_tmp38}
	_tmp40 = 1 ;	# live variables = {veggies}
	_tmp41 = 0 ;	# live variables = {veggies,_tmp40}
	_tmp42 = _tmp40 < _tmp41 ;	# live variables = {veggies,_tmp40,_tmp41}
	_tmp43 = *(veggies + -4) ;	# live variables = {veggies,_tmp40,_tmp41,_tmp42}
	_tmp44 = _tmp40 < _tmp43 ;	# live variables = {veggies,_tmp40,_tmp41,_tmp42,_tmp43}
	_tmp45 = _tmp44 == _tmp41 ;	# live variables = {veggies,_tmp40,_tmp41,_tmp42,_tmp44}
	_tmp46 = _tmp42 || _tmp45 ;	# live variables = {veggies,_tmp40,_tmp42,_tmp45}
	IfZ _tmp46 Goto _L2 ;	# live variables = {veggies,_tmp40,_tmp46}
	_tmp47 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {veggies,_tmp40}
	PushParam _tmp47 ;	# live variables = {veggies,_tmp40,_tmp47}
	LCall _PrintString ;	# live variables = {veggies,_tmp40}
	PopParams 4 ;	# live variables = {veggies,_tmp40}
	LCall _Halt ;	# live variables = {veggies,_tmp40}
_L2:
	_tmp48 = 4 ;	# live variables = {veggies,_tmp40}
	_tmp49 = _tmp48 * _tmp40 ;	# live variables = {veggies,_tmp40,_tmp48}
	_tmp50 = veggies + _tmp49 ;	# live variables = {veggies,_tmp49}
	_tmp51 = 12 ;	# live variables = {veggies,_tmp50}
	PushParam _tmp51 ;	# live variables = {veggies,_tmp50,_tmp51}
	_tmp52 = LCall _Alloc ;	# live variables = {veggies,_tmp50}
	PopParams 4 ;	# live variables = {veggies,_tmp50,_tmp52}
	_tmp53 = Vegetable ;	# live variables = {veggies,_tmp50,_tmp52}
	*(_tmp52) = _tmp53 ;	# live variables = {veggies,_tmp50,_tmp52,_tmp53}
	*(_tmp50) = _tmp52 ;	# live variables = {veggies,_tmp50,_tmp52}
	_tmp54 = 10 ;	# live variables = {veggies}
	PushParam _tmp54 ;	# live variables = {veggies,_tmp54}
	LCall _Grow ;	# live variables = {veggies}
	PopParams 4 ;	# live variables = {veggies}
	_tmp55 = 0 ;	# live variables = {veggies}
	_tmp56 = 0 ;	# live variables = {veggies,_tmp55}
	_tmp57 = _tmp55 < _tmp56 ;	# live variables = {veggies,_tmp55,_tmp56}
	_tmp58 = *(veggies + -4) ;	# live variables = {veggies,_tmp55,_tmp56,_tmp57}
	_tmp59 = _tmp55 < _tmp58 ;	# live variables = {veggies,_tmp55,_tmp56,_tmp57,_tmp58}
	_tmp60 = _tmp59 == _tmp56 ;	# live variables = {veggies,_tmp55,_tmp56,_tmp57,_tmp59}
	_tmp61 = _tmp57 || _tmp60 ;	# live variables = {veggies,_tmp55,_tmp57,_tmp60}
	IfZ _tmp61 Goto _L3 ;	# live variables = {veggies,_tmp55,_tmp61}
	_tmp62 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {veggies,_tmp55}
	PushParam _tmp62 ;	# live variables = {veggies,_tmp55,_tmp62}
	LCall _PrintString ;	# live variables = {veggies,_tmp55}
	PopParams 4 ;	# live variables = {veggies,_tmp55}
	LCall _Halt ;	# live variables = {veggies,_tmp55}
_L3:
	_tmp63 = 4 ;	# live variables = {veggies,_tmp55}
	_tmp64 = _tmp63 * _tmp55 ;	# live variables = {veggies,_tmp55,_tmp63}
	_tmp65 = veggies + _tmp64 ;	# live variables = {veggies,_tmp64}
	_tmp66 = *(_tmp65) ;	# live variables = {veggies,_tmp65}
	_tmp67 = 1 ;	# live variables = {veggies,_tmp66}
	_tmp68 = 0 ;	# live variables = {veggies,_tmp66,_tmp67}
	_tmp69 = _tmp67 < _tmp68 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp68}
	_tmp70 = *(veggies + -4) ;	# live variables = {veggies,_tmp66,_tmp67,_tmp68,_tmp69}
	_tmp71 = _tmp67 < _tmp70 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp68,_tmp69,_tmp70}
	_tmp72 = _tmp71 == _tmp68 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp68,_tmp69,_tmp71}
	_tmp73 = _tmp69 || _tmp72 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp69,_tmp72}
	IfZ _tmp73 Goto _L4 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp73}
	_tmp74 = "Decaf runtime error: Array subscript out of bound..." ;	# live variables = {veggies,_tmp66,_tmp67}
	PushParam _tmp74 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp74}
	LCall _PrintString ;	# live variables = {veggies,_tmp66,_tmp67}
	PopParams 4 ;	# live variables = {veggies,_tmp66,_tmp67}
	LCall _Halt ;	# live variables = {veggies,_tmp66,_tmp67}
_L4:
	_tmp75 = 4 ;	# live variables = {veggies,_tmp66,_tmp67}
	_tmp76 = _tmp75 * _tmp67 ;	# live variables = {veggies,_tmp66,_tmp67,_tmp75}
	_tmp77 = veggies + _tmp76 ;	# live variables = {veggies,_tmp66,_tmp76}
	_tmp78 = *(_tmp77) ;	# live variables = {_tmp66,_tmp77}
	_tmp79 = *(_tmp78) ;	# live variables = {_tmp66,_tmp78}
	_tmp80 = *(_tmp79) ;	# live variables = {_tmp66,_tmp78,_tmp79}
	PushParam _tmp66 ;	# live variables = {_tmp66,_tmp78,_tmp80}
	PushParam _tmp78 ;	# live variables = {_tmp78,_tmp80}
	ACall _tmp80 ;	# live variables = {_tmp80}
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
