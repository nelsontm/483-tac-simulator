_QueueItem.Init:
	BeginFunc 0 (this, data, next, prev) ;
	*(this + 4) = data ;
	*(this + 8) = next ;
	*(next + 12) = this ;
	*(this + 12) = prev ;
	*(prev + 8) = this ;
	EndFunc ;
_QueueItem.GetData:
	BeginFunc 4 (this) ;
	_tmp0 = *(this + 4) ;
	Return _tmp0 ;
	EndFunc ;
_QueueItem.GetNext:
	BeginFunc 4 (this) ;
	_tmp1 = *(this + 8) ;
	Return _tmp1 ;
	EndFunc ;
_QueueItem.GetPrev:
	BeginFunc 4 (this) ;
	_tmp2 = *(this + 12) ;
	Return _tmp2 ;
	EndFunc ;
_QueueItem.SetNext:
	BeginFunc 0 (this, n) ;
	*(this + 8) = n ;
	EndFunc ;
_QueueItem.SetPrev:
	BeginFunc 0 (this, p) ;
	*(this + 12) = p ;
	EndFunc ;
VTable QueueItem =
	_QueueItem.Init,
	_QueueItem.GetData,
	_QueueItem.GetNext,
	_QueueItem.GetPrev,
	_QueueItem.SetNext,
	_QueueItem.SetPrev,
; 
_Queue.Init:
	BeginFunc 36 (this) ;
	_tmp3 = 16 ;
	PushParam _tmp3 ;
	_tmp4 = LCall _Alloc ;
	PopParams 4 ;
	_tmp5 = QueueItem ;
	*(_tmp4) = _tmp5 ;
	*(this + 4) = _tmp4 ;
	_tmp6 = 0 ;
	_tmp7 = *(this + 4) ;
	_tmp8 = *(this + 4) ;
	_tmp9 = *(this + 4) ;
	_tmp10 = *(_tmp9) ;
	_tmp11 = *(_tmp10) ;
	PushParam _tmp8 ;
	PushParam _tmp7 ;
	PushParam _tmp6 ;
	PushParam _tmp9 ;
	ACall _tmp11 ;
	PopParams 16 ;
	EndFunc ;
_Queue.EnQueue:
	BeginFunc 44 (this, i) ;
	_tmp12 = 16 ;
	PushParam _tmp12 ;
	_tmp13 = LCall _Alloc ;
	PopParams 4 ;
	_tmp14 = QueueItem ;
	*(_tmp13) = _tmp14 ;
	temp = _tmp13 ;
	_tmp15 = *(this + 4) ;
	_tmp16 = *(_tmp15) ;
	_tmp17 = *(_tmp16 + 8) ;
	PushParam _tmp15 ;
	_tmp18 = ACall _tmp17 ;
	PopParams 4 ;
	_tmp19 = *(this + 4) ;
	_tmp20 = *(temp) ;
	_tmp21 = *(_tmp20) ;
	PushParam _tmp19 ;
	PushParam _tmp18 ;
	PushParam i ;
	PushParam temp ;
	ACall _tmp21 ;
	PopParams 16 ;
	EndFunc ;
_Queue.DeQueue:
	BeginFunc 132 (this) ;
	_tmp22 = *(this + 4) ;
	_tmp23 = *(_tmp22) ;
	_tmp24 = *(_tmp23 + 12) ;
	PushParam _tmp22 ;
	_tmp25 = ACall _tmp24 ;
	PopParams 4 ;
	_tmp26 = *(this + 4) ;
	_tmp27 = _tmp25 == _tmp26 ;
	IfZ _tmp27 Goto _L0 ;
	_tmp28 = "Queue Is Empty" ;
	PushParam _tmp28 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp29 = 0 ;
	Return _tmp29 ;
	Goto _L1 ;
_L0:
	_tmp30 = *(this + 4) ;
	_tmp31 = *(_tmp30) ;
	_tmp32 = *(_tmp31 + 12) ;
	PushParam _tmp30 ;
	_tmp33 = ACall _tmp32 ;
	PopParams 4 ;
	temp = _tmp33 ;
	_tmp34 = *(temp) ;
	_tmp35 = *(_tmp34 + 4) ;
	PushParam temp ;
	_tmp36 = ACall _tmp35 ;
	PopParams 4 ;
	val = _tmp36 ;
	_tmp37 = *(temp) ;
	_tmp38 = *(_tmp37 + 8) ;
	PushParam temp ;
	_tmp39 = ACall _tmp38 ;
	PopParams 4 ;
	_tmp40 = *(temp) ;
	_tmp41 = *(_tmp40 + 12) ;
	PushParam temp ;
	_tmp42 = ACall _tmp41 ;
	PopParams 4 ;
	_tmp43 = *(_tmp42) ;
	_tmp44 = *(_tmp43 + 16) ;
	PushParam _tmp39 ;
	PushParam _tmp42 ;
	ACall _tmp44 ;
	PopParams 8 ;
	_tmp45 = *(temp) ;
	_tmp46 = *(_tmp45 + 12) ;
	PushParam temp ;
	_tmp47 = ACall _tmp46 ;
	PopParams 4 ;
	_tmp48 = *(temp) ;
	_tmp49 = *(_tmp48 + 8) ;
	PushParam temp ;
	_tmp50 = ACall _tmp49 ;
	PopParams 4 ;
	_tmp51 = *(_tmp50) ;
	_tmp52 = *(_tmp51 + 20) ;
	PushParam _tmp47 ;
	PushParam _tmp50 ;
	ACall _tmp52 ;
	PopParams 8 ;
_L1:
	Return val ;
	EndFunc ;
VTable Queue =
	_Queue.Init,
	_Queue.EnQueue,
	_Queue.DeQueue,
; 
main:
	BeginFunc 196 () ;
	_tmp53 = 8 ;
	PushParam _tmp53 ;
	_tmp54 = LCall _Alloc ;
	PopParams 4 ;
	_tmp55 = Queue ;
	*(_tmp54) = _tmp55 ;
	q = _tmp54 ;
	_tmp56 = *(q) ;
	_tmp57 = *(_tmp56) ;
	PushParam q ;
	ACall _tmp57 ;
	PopParams 4 ;
	_tmp58 = 0 ;
	i = _tmp58 ;
_L2:
	_tmp59 = 10 ;
	_tmp60 = i == _tmp59 ;
	_tmp61 = 0 ;
	_tmp62 = _tmp60 == _tmp61 ;
	IfZ _tmp62 Goto _L3 ;
	_tmp63 = *(q) ;
	_tmp64 = *(_tmp63 + 4) ;
	PushParam i ;
	PushParam q ;
	ACall _tmp64 ;
	PopParams 8 ;
	_tmp65 = 1 ;
	_tmp66 = i + _tmp65 ;
	i = _tmp66 ;
	Goto _L2 ;
_L3:
	_tmp67 = 0 ;
	i = _tmp67 ;
_L4:
	_tmp68 = 4 ;
	_tmp69 = i == _tmp68 ;
	_tmp70 = 0 ;
	_tmp71 = _tmp69 == _tmp70 ;
	IfZ _tmp71 Goto _L5 ;
	_tmp72 = *(q) ;
	_tmp73 = *(_tmp72 + 8) ;
	PushParam q ;
	_tmp74 = ACall _tmp73 ;
	PopParams 4 ;
	PushParam _tmp74 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp75 = " " ;
	PushParam _tmp75 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp76 = 1 ;
	_tmp77 = i + _tmp76 ;
	i = _tmp77 ;
	Goto _L4 ;
_L5:
	_tmp78 = "\n" ;
	PushParam _tmp78 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp79 = 0 ;
	i = _tmp79 ;
_L6:
	_tmp80 = 10 ;
	_tmp81 = i == _tmp80 ;
	_tmp82 = 0 ;
	_tmp83 = _tmp81 == _tmp82 ;
	IfZ _tmp83 Goto _L7 ;
	_tmp84 = *(q) ;
	_tmp85 = *(_tmp84 + 4) ;
	PushParam i ;
	PushParam q ;
	ACall _tmp85 ;
	PopParams 8 ;
	_tmp86 = 1 ;
	_tmp87 = i + _tmp86 ;
	i = _tmp87 ;
	Goto _L6 ;
_L7:
	_tmp88 = 0 ;
	i = _tmp88 ;
_L8:
	_tmp89 = 17 ;
	_tmp90 = i == _tmp89 ;
	_tmp91 = 0 ;
	_tmp92 = _tmp90 == _tmp91 ;
	IfZ _tmp92 Goto _L9 ;
	_tmp93 = *(q) ;
	_tmp94 = *(_tmp93 + 8) ;
	PushParam q ;
	_tmp95 = ACall _tmp94 ;
	PopParams 4 ;
	PushParam _tmp95 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp96 = " " ;
	PushParam _tmp96 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp97 = 1 ;
	_tmp98 = i + _tmp97 ;
	i = _tmp98 ;
	Goto _L8 ;
_L9:
	_tmp99 = "\n" ;
	PushParam _tmp99 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
