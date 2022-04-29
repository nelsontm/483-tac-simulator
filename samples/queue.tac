_QueueItem.Init:
	BeginFunc 0 ;	# live variables = {this,data,next,prev}
	*(this + 4) = data ;	# live variables = {this,data,next,prev}
	*(this + 8) = next ;	# live variables = {this,next,prev}
	*(next + 12) = this ;	# live variables = {this,next,prev}
	*(this + 12) = prev ;	# live variables = {this,prev}
	*(prev + 8) = this ;	# live variables = {this,prev}
	EndFunc ;	# live variables = {}
_QueueItem.GetData:
	BeginFunc 4 ;	# live variables = {this}
	_tmp0 = *(this + 4) ;	# live variables = {this}
	Return _tmp0 ;	# live variables = {_tmp0}
	EndFunc ;	# live variables = {}
_QueueItem.GetNext:
	BeginFunc 4 ;	# live variables = {this}
	_tmp1 = *(this + 8) ;	# live variables = {this}
	Return _tmp1 ;	# live variables = {_tmp1}
	EndFunc ;	# live variables = {}
_QueueItem.GetPrev:
	BeginFunc 4 ;	# live variables = {this}
	_tmp2 = *(this + 12) ;	# live variables = {this}
	Return _tmp2 ;	# live variables = {_tmp2}
	EndFunc ;	# live variables = {}
_QueueItem.SetNext:
	BeginFunc 0 ;	# live variables = {this,n}
	*(this + 8) = n ;	# live variables = {this,n}
	EndFunc ;	# live variables = {}
_QueueItem.SetPrev:
	BeginFunc 0 ;	# live variables = {this,p}
	*(this + 12) = p ;	# live variables = {this,p}
	EndFunc ;	# live variables = {}
VTable QueueItem =
	_QueueItem.Init,
	_QueueItem.GetData,
	_QueueItem.GetNext,
	_QueueItem.GetPrev,
	_QueueItem.SetNext,
	_QueueItem.SetPrev,
; 
_Queue.Init:
	BeginFunc 36 ;	# live variables = {this}
	_tmp3 = 16 ;	# live variables = {this}
	PushParam _tmp3 ;	# live variables = {this,_tmp3}
	_tmp4 = LCall _Alloc ;	# live variables = {this}
	PopParams 4 ;	# live variables = {this,_tmp4}
	_tmp5 = QueueItem ;	# live variables = {this,_tmp4}
	*(_tmp4) = _tmp5 ;	# live variables = {this,_tmp4,_tmp5}
	*(this + 4) = _tmp4 ;	# live variables = {this,_tmp4}
	_tmp6 = 0 ;	# live variables = {this}
	_tmp7 = *(this + 4) ;	# live variables = {this,_tmp6}
	_tmp8 = *(this + 4) ;	# live variables = {this,_tmp6,_tmp7}
	_tmp9 = *(this + 4) ;	# live variables = {this,_tmp6,_tmp7,_tmp8}
	_tmp10 = *(_tmp9) ;	# live variables = {_tmp6,_tmp7,_tmp8,_tmp9}
	_tmp11 = *(_tmp10) ;	# live variables = {_tmp6,_tmp7,_tmp8,_tmp9,_tmp10}
	PushParam _tmp8 ;	# live variables = {_tmp6,_tmp7,_tmp8,_tmp9,_tmp11}
	PushParam _tmp7 ;	# live variables = {_tmp6,_tmp7,_tmp9,_tmp11}
	PushParam _tmp6 ;	# live variables = {_tmp6,_tmp9,_tmp11}
	PushParam _tmp9 ;	# live variables = {_tmp9,_tmp11}
	ACall _tmp11 ;	# live variables = {_tmp11}
	PopParams 16 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Queue.EnQueue:
	BeginFunc 44 ;	# live variables = {this,i}
	_tmp12 = 16 ;	# live variables = {this,i}
	PushParam _tmp12 ;	# live variables = {this,i,_tmp12}
	_tmp13 = LCall _Alloc ;	# live variables = {this,i}
	PopParams 4 ;	# live variables = {this,i,_tmp13}
	_tmp14 = QueueItem ;	# live variables = {this,i,_tmp13}
	*(_tmp13) = _tmp14 ;	# live variables = {this,i,_tmp13,_tmp14}
	temp = _tmp13 ;	# live variables = {this,i,_tmp13}
	_tmp15 = *(this + 4) ;	# live variables = {this,i,temp}
	_tmp16 = *(_tmp15) ;	# live variables = {this,i,temp,_tmp15}
	_tmp17 = *(_tmp16 + 8) ;	# live variables = {this,i,temp,_tmp15,_tmp16}
	PushParam _tmp15 ;	# live variables = {this,i,temp,_tmp15,_tmp17}
	_tmp18 = ACall _tmp17 ;	# live variables = {this,i,temp,_tmp17}
	PopParams 4 ;	# live variables = {this,i,temp,_tmp18}
	_tmp19 = *(this + 4) ;	# live variables = {this,i,temp,_tmp18}
	_tmp20 = *(temp) ;	# live variables = {i,temp,_tmp18,_tmp19}
	_tmp21 = *(_tmp20) ;	# live variables = {i,temp,_tmp18,_tmp19,_tmp20}
	PushParam _tmp19 ;	# live variables = {i,temp,_tmp18,_tmp19,_tmp21}
	PushParam _tmp18 ;	# live variables = {i,temp,_tmp18,_tmp21}
	PushParam i ;	# live variables = {i,temp,_tmp21}
	PushParam temp ;	# live variables = {temp,_tmp21}
	ACall _tmp21 ;	# live variables = {_tmp21}
	PopParams 16 ;	# live variables = {}
	EndFunc ;	# live variables = {}
_Queue.DeQueue:
	BeginFunc 132 ;	# live variables = {this}
	_tmp22 = *(this + 4) ;	# live variables = {this}
	_tmp23 = *(_tmp22) ;	# live variables = {this,_tmp22}
	_tmp24 = *(_tmp23 + 12) ;	# live variables = {this,_tmp22,_tmp23}
	PushParam _tmp22 ;	# live variables = {this,_tmp22,_tmp24}
	_tmp25 = ACall _tmp24 ;	# live variables = {this,_tmp24}
	PopParams 4 ;	# live variables = {this,_tmp25}
	_tmp26 = *(this + 4) ;	# live variables = {this,_tmp25}
	_tmp27 = _tmp25 == _tmp26 ;	# live variables = {this,_tmp25,_tmp26}
	IfZ _tmp27 Goto _L0 ;	# live variables = {this,_tmp27}
	_tmp28 = "Queue Is Empty" ;	# live variables = {}
	PushParam _tmp28 ;	# live variables = {_tmp28}
	LCall _PrintString ;	# live variables = {}
	PopParams 4 ;	# live variables = {}
	_tmp29 = 0 ;	# live variables = {}
	Return _tmp29 ;	# live variables = {_tmp29}
	Goto _L1 ;	# live variables = {val}
_L0:
	_tmp30 = *(this + 4) ;	# live variables = {this}
	_tmp31 = *(_tmp30) ;	# live variables = {_tmp30}
	_tmp32 = *(_tmp31 + 12) ;	# live variables = {_tmp30,_tmp31}
	PushParam _tmp30 ;	# live variables = {_tmp30,_tmp32}
	_tmp33 = ACall _tmp32 ;	# live variables = {_tmp32}
	PopParams 4 ;	# live variables = {_tmp33}
	temp = _tmp33 ;	# live variables = {_tmp33}
	_tmp34 = *(temp) ;	# live variables = {temp}
	_tmp35 = *(_tmp34 + 4) ;	# live variables = {temp,_tmp34}
	PushParam temp ;	# live variables = {temp,_tmp35}
	_tmp36 = ACall _tmp35 ;	# live variables = {temp,_tmp35}
	PopParams 4 ;	# live variables = {temp,_tmp36}
	val = _tmp36 ;	# live variables = {temp,_tmp36}
	_tmp37 = *(temp) ;	# live variables = {val,temp}
	_tmp38 = *(_tmp37 + 8) ;	# live variables = {val,temp,_tmp37}
	PushParam temp ;	# live variables = {val,temp,_tmp38}
	_tmp39 = ACall _tmp38 ;	# live variables = {val,temp,_tmp38}
	PopParams 4 ;	# live variables = {val,temp,_tmp39}
	_tmp40 = *(temp) ;	# live variables = {val,temp,_tmp39}
	_tmp41 = *(_tmp40 + 12) ;	# live variables = {val,temp,_tmp39,_tmp40}
	PushParam temp ;	# live variables = {val,temp,_tmp39,_tmp41}
	_tmp42 = ACall _tmp41 ;	# live variables = {val,temp,_tmp39,_tmp41}
	PopParams 4 ;	# live variables = {val,temp,_tmp39,_tmp42}
	_tmp43 = *(_tmp42) ;	# live variables = {val,temp,_tmp39,_tmp42}
	_tmp44 = *(_tmp43 + 16) ;	# live variables = {val,temp,_tmp39,_tmp42,_tmp43}
	PushParam _tmp39 ;	# live variables = {val,temp,_tmp39,_tmp42,_tmp44}
	PushParam _tmp42 ;	# live variables = {val,temp,_tmp42,_tmp44}
	ACall _tmp44 ;	# live variables = {val,temp,_tmp44}
	PopParams 8 ;	# live variables = {val,temp}
	_tmp45 = *(temp) ;	# live variables = {val,temp}
	_tmp46 = *(_tmp45 + 12) ;	# live variables = {val,temp,_tmp45}
	PushParam temp ;	# live variables = {val,temp,_tmp46}
	_tmp47 = ACall _tmp46 ;	# live variables = {val,temp,_tmp46}
	PopParams 4 ;	# live variables = {val,temp,_tmp47}
	_tmp48 = *(temp) ;	# live variables = {val,temp,_tmp47}
	_tmp49 = *(_tmp48 + 8) ;	# live variables = {val,temp,_tmp47,_tmp48}
	PushParam temp ;	# live variables = {val,temp,_tmp47,_tmp49}
	_tmp50 = ACall _tmp49 ;	# live variables = {val,_tmp47,_tmp49}
	PopParams 4 ;	# live variables = {val,_tmp47,_tmp50}
	_tmp51 = *(_tmp50) ;	# live variables = {val,_tmp47,_tmp50}
	_tmp52 = *(_tmp51 + 20) ;	# live variables = {val,_tmp47,_tmp50,_tmp51}
	PushParam _tmp47 ;	# live variables = {val,_tmp47,_tmp50,_tmp52}
	PushParam _tmp50 ;	# live variables = {val,_tmp50,_tmp52}
	ACall _tmp52 ;	# live variables = {val,_tmp52}
	PopParams 8 ;	# live variables = {val}
_L1:
	Return val ;	# live variables = {val}
	EndFunc ;	# live variables = {}
VTable Queue =
	_Queue.Init,
	_Queue.EnQueue,
	_Queue.DeQueue,
; 
main:
	BeginFunc 196 ;	# live variables = {}
	_tmp53 = 8 ;	# live variables = {}
	PushParam _tmp53 ;	# live variables = {_tmp53}
	_tmp54 = LCall _Alloc ;	# live variables = {}
	PopParams 4 ;	# live variables = {_tmp54}
	_tmp55 = Queue ;	# live variables = {_tmp54}
	*(_tmp54) = _tmp55 ;	# live variables = {_tmp54,_tmp55}
	q = _tmp54 ;	# live variables = {_tmp54}
	_tmp56 = *(q) ;	# live variables = {q}
	_tmp57 = *(_tmp56) ;	# live variables = {q,_tmp56}
	PushParam q ;	# live variables = {q,_tmp57}
	ACall _tmp57 ;	# live variables = {q,_tmp57}
	PopParams 4 ;	# live variables = {q}
	_tmp58 = 0 ;	# live variables = {q}
	i = _tmp58 ;	# live variables = {q,_tmp58}
_L2:
	_tmp59 = 10 ;	# live variables = {q,i}
	_tmp60 = i == _tmp59 ;	# live variables = {q,i,_tmp59}
	_tmp61 = 0 ;	# live variables = {q,i,_tmp60}
	_tmp62 = _tmp60 == _tmp61 ;	# live variables = {q,i,_tmp60,_tmp61}
	IfZ _tmp62 Goto _L3 ;	# live variables = {q,i,_tmp62}
	_tmp63 = *(q) ;	# live variables = {q,i}
	_tmp64 = *(_tmp63 + 4) ;	# live variables = {q,i,_tmp63}
	PushParam i ;	# live variables = {q,i,_tmp64}
	PushParam q ;	# live variables = {q,i,_tmp64}
	ACall _tmp64 ;	# live variables = {q,i,_tmp64}
	PopParams 8 ;	# live variables = {q,i}
	_tmp65 = 1 ;	# live variables = {q,i}
	_tmp66 = i + _tmp65 ;	# live variables = {q,i,_tmp65}
	i = _tmp66 ;	# live variables = {q,_tmp66}
	Goto _L2 ;	# live variables = {q,i}
_L3:
	_tmp67 = 0 ;	# live variables = {q}
	i = _tmp67 ;	# live variables = {q,_tmp67}
_L4:
	_tmp68 = 4 ;	# live variables = {q,i}
	_tmp69 = i == _tmp68 ;	# live variables = {q,i,_tmp68}
	_tmp70 = 0 ;	# live variables = {q,i,_tmp69}
	_tmp71 = _tmp69 == _tmp70 ;	# live variables = {q,i,_tmp69,_tmp70}
	IfZ _tmp71 Goto _L5 ;	# live variables = {q,i,_tmp71}
	_tmp72 = *(q) ;	# live variables = {q,i}
	_tmp73 = *(_tmp72 + 8) ;	# live variables = {q,i,_tmp72}
	PushParam q ;	# live variables = {q,i,_tmp73}
	_tmp74 = ACall _tmp73 ;	# live variables = {q,i,_tmp73}
	PopParams 4 ;	# live variables = {q,i,_tmp74}
	PushParam _tmp74 ;	# live variables = {q,i,_tmp74}
	LCall _PrintInt ;	# live variables = {q,i}
	PopParams 4 ;	# live variables = {q,i}
	_tmp75 = " " ;	# live variables = {q,i}
	PushParam _tmp75 ;	# live variables = {q,i,_tmp75}
	LCall _PrintString ;	# live variables = {q,i}
	PopParams 4 ;	# live variables = {q,i}
	_tmp76 = 1 ;	# live variables = {q,i}
	_tmp77 = i + _tmp76 ;	# live variables = {q,i,_tmp76}
	i = _tmp77 ;	# live variables = {q,_tmp77}
	Goto _L4 ;	# live variables = {q,i}
_L5:
	_tmp78 = "\n" ;	# live variables = {q}
	PushParam _tmp78 ;	# live variables = {q,_tmp78}
	LCall _PrintString ;	# live variables = {q}
	PopParams 4 ;	# live variables = {q}
	_tmp79 = 0 ;	# live variables = {q}
	i = _tmp79 ;	# live variables = {q,_tmp79}
_L6:
	_tmp80 = 10 ;	# live variables = {q,i}
	_tmp81 = i == _tmp80 ;	# live variables = {q,i,_tmp80}
	_tmp82 = 0 ;	# live variables = {q,i,_tmp81}
	_tmp83 = _tmp81 == _tmp82 ;	# live variables = {q,i,_tmp81,_tmp82}
	IfZ _tmp83 Goto _L7 ;	# live variables = {q,i,_tmp83}
	_tmp84 = *(q) ;	# live variables = {q,i}
	_tmp85 = *(_tmp84 + 4) ;	# live variables = {q,i,_tmp84}
	PushParam i ;	# live variables = {q,i,_tmp85}
	PushParam q ;	# live variables = {q,i,_tmp85}
	ACall _tmp85 ;	# live variables = {q,i,_tmp85}
	PopParams 8 ;	# live variables = {q,i}
	_tmp86 = 1 ;	# live variables = {q,i}
	_tmp87 = i + _tmp86 ;	# live variables = {q,i,_tmp86}
	i = _tmp87 ;	# live variables = {q,_tmp87}
	Goto _L6 ;	# live variables = {q,i}
_L7:
	_tmp88 = 0 ;	# live variables = {q}
	i = _tmp88 ;	# live variables = {q,_tmp88}
_L8:
	_tmp89 = 17 ;	# live variables = {q,i}
	_tmp90 = i == _tmp89 ;	# live variables = {q,i,_tmp89}
	_tmp91 = 0 ;	# live variables = {q,i,_tmp90}
	_tmp92 = _tmp90 == _tmp91 ;	# live variables = {q,i,_tmp90,_tmp91}
	IfZ _tmp92 Goto _L9 ;	# live variables = {q,i,_tmp92}
	_tmp93 = *(q) ;	# live variables = {q,i}
	_tmp94 = *(_tmp93 + 8) ;	# live variables = {q,i,_tmp93}
	PushParam q ;	# live variables = {q,i,_tmp94}
	_tmp95 = ACall _tmp94 ;	# live variables = {q,i,_tmp94}
	PopParams 4 ;	# live variables = {q,i,_tmp95}
	PushParam _tmp95 ;	# live variables = {q,i,_tmp95}
	LCall _PrintInt ;	# live variables = {q,i}
	PopParams 4 ;	# live variables = {q,i}
	_tmp96 = " " ;	# live variables = {q,i}
	PushParam _tmp96 ;	# live variables = {q,i,_tmp96}
	LCall _PrintString ;	# live variables = {q,i}
	PopParams 4 ;	# live variables = {q,i}
	_tmp97 = 1 ;	# live variables = {q,i}
	_tmp98 = i + _tmp97 ;	# live variables = {q,i,_tmp97}
	i = _tmp98 ;	# live variables = {q,_tmp98}
	Goto _L8 ;	# live variables = {q,i}
_L9:
	_tmp99 = "\n" ;	# live variables = {}
	PushParam _tmp99 ;	# live variables = {_tmp99}
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
