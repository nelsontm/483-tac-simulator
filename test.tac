
BeginFunc 16 (this, seeds, water)
_tmp0 = "But I don't like squash\n"
PushParam _tmp0
LCall _PrintString
PopParams 4
_tmp1 = 10
_tmp2 = 5
_tmp3 = _tmp1 * _tmp2
PushParam _tmp3
LCall _PrintInt
PopParams 4
EndFunc





BeginFunc 40 (this, veg)
_tmp4 = 5
_tmp5 = 2
_tmp6 = _tmp4 % _tmp5
*(this + 4) = _tmp6
_tmp7 = "Yum! "
PushParam _tmp7
LCall _PrintString
PopParams 4
_tmp8 = *(this + 4)
PushParam _tmp8
LCall _PrintInt
PopParams 4
_tmp9 = "\n"
PushParam _tmp9
LCall _PrintString
PopParams 4
_tmp10 = *(veg)
_tmp11 = *(_tmp10 + 4)
PushParam w
PushParam s
PushParam veg
ACall _tmp11
PopParams 12
Return
EndFunc

BeginFunc 12 (this, seeds, water)
_tmp12 = "Grow, little vegetables, grow!\n"
PushParam _tmp12
LCall _PrintString
PopParams 4
_tmp13 = *(this)
_tmp14 = *(_tmp13)
PushParam this
PushParam this
ACall _tmp14
PopParams 8
EndFunc





BeginFunc 4 (a)
_tmp15 = "mmm... veggies!\n"
PushParam _tmp15
LCall _PrintString
PopParams 4
EndFunc



BeginFunc 264 ()
_tmp16 = 2
_tmp17 = 1
_tmp18 = _tmp16 < _tmp17
IfZ _tmp18 Goto _L0
_tmp19 = "Decaf runtime error: Array size is <= 0\n"
PushParam _tmp19
LCall _PrintString
PopParams 4
LCall _Halt

_tmp20 = 1
_tmp21 = _tmp20 + _tmp16
_tmp22 = 4
_tmp23 = _tmp21 * _tmp22
PushParam _tmp23
_tmp24 = LCall _Alloc
PopParams 4
*(_tmp24) = _tmp16
_tmp25 = _tmp24 + _tmp22
veggies = _tmp25
_tmp26 = 0
_tmp27 = 0
_tmp28 = _tmp26 < _tmp27
_tmp29 = *(veggies + -4)
_tmp30 = _tmp26 < _tmp29
_tmp31 = _tmp30 == _tmp27
_tmp32 = _tmp28 || _tmp31
IfZ _tmp32 Goto _L1
_tmp33 = "Decaf runtime error: Array subscript out of bound..."
PushParam _tmp33
LCall _PrintString
PopParams 4
LCall _Halt

_tmp34 = 4
_tmp35 = _tmp34 * _tmp26
_tmp36 = veggies + _tmp35
_tmp37 = 12
PushParam _tmp37
_tmp38 = LCall _Alloc
PopParams 4
_tmp39 = Squash
*(_tmp38) = _tmp39
*(_tmp36) = _tmp38
_tmp40 = 1
_tmp41 = 0
_tmp42 = _tmp40 < _tmp41
_tmp43 = *(veggies + -4)
_tmp44 = _tmp40 < _tmp43
_tmp45 = _tmp44 == _tmp41
_tmp46 = _tmp42 || _tmp45
IfZ _tmp46 Goto _L2
_tmp47 = "Decaf runtime error: Array subscript out of bound..."
PushParam _tmp47
LCall _PrintString
PopParams 4
LCall _Halt

_tmp48 = 4
_tmp49 = _tmp48 * _tmp40
_tmp50 = veggies + _tmp49
_tmp51 = 12
PushParam _tmp51
_tmp52 = LCall _Alloc
PopParams 4
_tmp53 = Vegetable
*(_tmp52) = _tmp53
*(_tmp50) = _tmp52
_tmp54 = 10
PushParam _tmp54
LCall _Grow
PopParams 4
_tmp55 = 0
_tmp56 = 0
_tmp57 = _tmp55 < _tmp56
_tmp58 = *(veggies + -4)
_tmp59 = _tmp55 < _tmp58
_tmp60 = _tmp59 == _tmp56
_tmp61 = _tmp57 || _tmp60
IfZ _tmp61 Goto _L3
_tmp62 = "Decaf runtime error: Array subscript out of bound..."
PushParam _tmp62
LCall _PrintString
PopParams 4
LCall _Halt

_tmp63 = 4
_tmp64 = _tmp63 * _tmp55
_tmp65 = veggies + _tmp64
_tmp66 = *(_tmp65)
_tmp67 = 1
_tmp68 = 0
_tmp69 = _tmp67 < _tmp68
_tmp70 = *(veggies + -4)
_tmp71 = _tmp67 < _tmp70
_tmp72 = _tmp71 == _tmp68
_tmp73 = _tmp69 || _tmp72
IfZ _tmp73 Goto _L4
_tmp74 = "Decaf runtime error: Array subscript out of bound..."
PushParam _tmp74
LCall _PrintString
PopParams 4
LCall _Halt

_tmp75 = 4
_tmp76 = _tmp75 * _tmp67
_tmp77 = veggies + _tmp76
_tmp78 = *(_tmp77)
_tmp79 = *(_tmp78)
_tmp80 = *(_tmp79)
PushParam _tmp66
PushParam _tmp78
ACall _tmp80
PopParams 8
EndFunc
