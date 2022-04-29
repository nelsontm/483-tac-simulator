_Random.Init:
	BeginFunc 0 (this, seedVal) ;
	*(this + 4) = seedVal ;
	EndFunc ;
_Random.GenRandom:
	BeginFunc 40 (this) ;
	_tmp0 = 15625 ;
	_tmp1 = *(this + 4) ;
	_tmp2 = 10000 ;
	_tmp3 = _tmp1 % _tmp2 ;
	_tmp4 = _tmp0 * _tmp3 ;
	_tmp5 = 22221 ;
	_tmp6 = _tmp4 + _tmp5 ;
	_tmp7 = 65536 ;
	_tmp8 = _tmp6 % _tmp7 ;
	*(this + 4) = _tmp8 ;
	_tmp9 = *(this + 4) ;
	Return _tmp9 ;
	EndFunc ;
_Random.RndInt:
	BeginFunc 16 (this, max) ;
	_tmp10 = *(this) ;
	_tmp11 = *(_tmp10 + 4) ;
	PushParam this ;
	_tmp12 = ACall _tmp11 ;
	PopParams 4 ;
	_tmp13 = _tmp12 % max ;
	Return _tmp13 ;
	EndFunc ;
VTable Random =
	_Random.Init,
	_Random.GenRandom,
	_Random.RndInt,
; 
_Deck.Init:
	BeginFunc 40 (this) ;
	_tmp14 = 52 ;
	_tmp15 = 1 ;
	_tmp16 = _tmp14 < _tmp15 ;
	IfZ _tmp16 Goto _L0 ;
	_tmp17 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp17 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L0:
	_tmp18 = 1 ;
	_tmp19 = _tmp18 + _tmp14 ;
	_tmp20 = 4 ;
	_tmp21 = _tmp19 * _tmp20 ;
	PushParam _tmp21 ;
	_tmp22 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp22) = _tmp14 ;
	_tmp23 = _tmp22 + _tmp20 ;
	*(this + 8) = _tmp23 ;
	EndFunc ;
_Deck.Shuffle:
	BeginFunc 336 (this) ;
	_tmp24 = 0 ;
	*(this + 4) = _tmp24 ;
_L1:
	_tmp25 = *(this + 4) ;
	_tmp26 = 52 ;
	_tmp27 = _tmp25 < _tmp26 ;
	IfZ _tmp27 Goto _L2 ;
	_tmp28 = *(this + 8) ;
	_tmp29 = *(this + 4) ;
	_tmp30 = 0 ;
	_tmp31 = _tmp29 < _tmp30 ;
	_tmp32 = *(_tmp28 + -4) ;
	_tmp33 = _tmp29 < _tmp32 ;
	_tmp34 = _tmp33 == _tmp30 ;
	_tmp35 = _tmp31 || _tmp34 ;
	IfZ _tmp35 Goto _L3 ;
	_tmp36 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp36 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L3:
	_tmp37 = 4 ;
	_tmp38 = _tmp37 * _tmp29 ;
	_tmp39 = _tmp28 + _tmp38 ;
	_tmp40 = *(this + 4) ;
	_tmp41 = 1 ;
	_tmp42 = _tmp40 + _tmp41 ;
	_tmp43 = 13 ;
	_tmp44 = _tmp42 % _tmp43 ;
	*(_tmp39) = _tmp44 ;
	_tmp45 = *(this + 4) ;
	_tmp46 = 1 ;
	_tmp47 = _tmp45 + _tmp46 ;
	*(this + 4) = _tmp47 ;
	Goto _L1 ;
_L2:
_L4:
	_tmp48 = *(this + 4) ;
	_tmp49 = 0 ;
	_tmp50 = _tmp49 < _tmp48 ;
	IfZ _tmp50 Goto _L5 ;
	_tmp51 = *(this + 4) ;
	_tmp52 = *(gRnd) ;
	_tmp53 = *(_tmp52 + 8) ;
	PushParam _tmp51 ;
	PushParam gRnd ;
	_tmp54 = ACall _tmp53 ;
	PopParams 8 ;
	r = _tmp54 ;
	_tmp55 = *(this + 4) ;
	_tmp56 = 1 ;
	_tmp57 = _tmp55 - _tmp56 ;
	*(this + 4) = _tmp57 ;
	_tmp58 = *(this + 8) ;
	_tmp59 = *(this + 4) ;
	_tmp60 = 0 ;
	_tmp61 = _tmp59 < _tmp60 ;
	_tmp62 = *(_tmp58 + -4) ;
	_tmp63 = _tmp59 < _tmp62 ;
	_tmp64 = _tmp63 == _tmp60 ;
	_tmp65 = _tmp61 || _tmp64 ;
	IfZ _tmp65 Goto _L6 ;
	_tmp66 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp66 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L6:
	_tmp67 = 4 ;
	_tmp68 = _tmp67 * _tmp59 ;
	_tmp69 = _tmp58 + _tmp68 ;
	_tmp70 = *(_tmp69) ;
	temp = _tmp70 ;
	_tmp71 = *(this + 8) ;
	_tmp72 = *(this + 4) ;
	_tmp73 = 0 ;
	_tmp74 = _tmp72 < _tmp73 ;
	_tmp75 = *(_tmp71 + -4) ;
	_tmp76 = _tmp72 < _tmp75 ;
	_tmp77 = _tmp76 == _tmp73 ;
	_tmp78 = _tmp74 || _tmp77 ;
	IfZ _tmp78 Goto _L7 ;
	_tmp79 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp79 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L7:
	_tmp80 = 4 ;
	_tmp81 = _tmp80 * _tmp72 ;
	_tmp82 = _tmp71 + _tmp81 ;
	_tmp83 = *(this + 8) ;
	_tmp84 = 0 ;
	_tmp85 = r < _tmp84 ;
	_tmp86 = *(_tmp83 + -4) ;
	_tmp87 = r < _tmp86 ;
	_tmp88 = _tmp87 == _tmp84 ;
	_tmp89 = _tmp85 || _tmp88 ;
	IfZ _tmp89 Goto _L8 ;
	_tmp90 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp90 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L8:
	_tmp91 = 4 ;
	_tmp92 = _tmp91 * r ;
	_tmp93 = _tmp83 + _tmp92 ;
	_tmp94 = *(_tmp93) ;
	*(_tmp82) = _tmp94 ;
	_tmp95 = *(this + 8) ;
	_tmp96 = 0 ;
	_tmp97 = r < _tmp96 ;
	_tmp98 = *(_tmp95 + -4) ;
	_tmp99 = r < _tmp98 ;
	_tmp100 = _tmp99 == _tmp96 ;
	_tmp101 = _tmp97 || _tmp100 ;
	IfZ _tmp101 Goto _L9 ;
	_tmp102 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp102 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L9:
	_tmp103 = 4 ;
	_tmp104 = _tmp103 * r ;
	_tmp105 = _tmp95 + _tmp104 ;
	*(_tmp105) = temp ;
	Goto _L4 ;
_L5:
	EndFunc ;
_Deck.GetCard:
	BeginFunc 92 (this) ;
	_tmp106 = *(this + 4) ;
	_tmp107 = 52 ;
	_tmp108 = _tmp107 < _tmp106 ;
	_tmp109 = _tmp107 == _tmp106 ;
	_tmp110 = _tmp108 || _tmp109 ;
	IfZ _tmp110 Goto _L10 ;
	_tmp111 = 0 ;
	Return _tmp111 ;
_L10:
	_tmp112 = *(this + 8) ;
	_tmp113 = *(this + 4) ;
	_tmp114 = 0 ;
	_tmp115 = _tmp113 < _tmp114 ;
	_tmp116 = *(_tmp112 + -4) ;
	_tmp117 = _tmp113 < _tmp116 ;
	_tmp118 = _tmp117 == _tmp114 ;
	_tmp119 = _tmp115 || _tmp118 ;
	IfZ _tmp119 Goto _L11 ;
	_tmp120 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp120 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L11:
	_tmp121 = 4 ;
	_tmp122 = _tmp121 * _tmp113 ;
	_tmp123 = _tmp112 + _tmp122 ;
	_tmp124 = *(_tmp123) ;
	result = _tmp124 ;
	_tmp125 = *(this + 4) ;
	_tmp126 = 1 ;
	_tmp127 = _tmp125 + _tmp126 ;
	*(this + 4) = _tmp127 ;
	Return result ;
	EndFunc ;
VTable Deck =
	_Deck.Init,
	_Deck.Shuffle,
	_Deck.GetCard,
; 
_BJDeck.Init:
	BeginFunc 176 (this) ;
	_tmp128 = 8 ;
	_tmp129 = 1 ;
	_tmp130 = _tmp128 < _tmp129 ;
	IfZ _tmp130 Goto _L12 ;
	_tmp131 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp131 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L12:
	_tmp132 = 1 ;
	_tmp133 = _tmp132 + _tmp128 ;
	_tmp134 = 4 ;
	_tmp135 = _tmp133 * _tmp134 ;
	PushParam _tmp135 ;
	_tmp136 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp136) = _tmp128 ;
	_tmp137 = _tmp136 + _tmp134 ;
	*(this + 4) = _tmp137 ;
	_tmp138 = 0 ;
	i = _tmp138 ;
_L13:
	_tmp139 = 8 ;
	_tmp140 = i < _tmp139 ;
	IfZ _tmp140 Goto _L14 ;
	_tmp141 = *(this + 4) ;
	_tmp142 = 0 ;
	_tmp143 = i < _tmp142 ;
	_tmp144 = *(_tmp141 + -4) ;
	_tmp145 = i < _tmp144 ;
	_tmp146 = _tmp145 == _tmp142 ;
	_tmp147 = _tmp143 || _tmp146 ;
	IfZ _tmp147 Goto _L15 ;
	_tmp148 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp148 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L15:
	_tmp149 = 4 ;
	_tmp150 = _tmp149 * i ;
	_tmp151 = _tmp141 + _tmp150 ;
	_tmp152 = 12 ;
	PushParam _tmp152 ;
	_tmp153 = LCall _Alloc ;
	PopParams 4 ;
	_tmp154 = Deck ;
	*(_tmp153) = _tmp154 ;
	*(_tmp151) = _tmp153 ;
	_tmp155 = *(this + 4) ;
	_tmp156 = 0 ;
	_tmp157 = i < _tmp156 ;
	_tmp158 = *(_tmp155 + -4) ;
	_tmp159 = i < _tmp158 ;
	_tmp160 = _tmp159 == _tmp156 ;
	_tmp161 = _tmp157 || _tmp160 ;
	IfZ _tmp161 Goto _L16 ;
	_tmp162 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp162 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L16:
	_tmp163 = 4 ;
	_tmp164 = _tmp163 * i ;
	_tmp165 = _tmp155 + _tmp164 ;
	_tmp166 = *(_tmp165) ;
	_tmp167 = *(_tmp166) ;
	_tmp168 = *(_tmp167) ;
	PushParam _tmp166 ;
	ACall _tmp168 ;
	PopParams 4 ;
	_tmp169 = 1 ;
	_tmp170 = i + _tmp169 ;
	i = _tmp170 ;
	Goto _L13 ;
_L14:
	EndFunc ;
_BJDeck.DealCard:
	BeginFunc 164 (this) ;
	_tmp171 = 0 ;
	c = _tmp171 ;
	_tmp172 = *(this + 8) ;
	_tmp173 = 8 ;
	_tmp174 = 52 ;
	_tmp175 = _tmp173 * _tmp174 ;
	_tmp176 = _tmp175 < _tmp172 ;
	_tmp177 = _tmp175 == _tmp172 ;
	_tmp178 = _tmp176 || _tmp177 ;
	IfZ _tmp178 Goto _L17 ;
	_tmp179 = 11 ;
	Return _tmp179 ;
_L17:
_L18:
	_tmp180 = 0 ;
	_tmp181 = c == _tmp180 ;
	IfZ _tmp181 Goto _L19 ;
	_tmp182 = 8 ;
	_tmp183 = *(gRnd) ;
	_tmp184 = *(_tmp183 + 8) ;
	PushParam _tmp182 ;
	PushParam gRnd ;
	_tmp185 = ACall _tmp184 ;
	PopParams 8 ;
	d = _tmp185 ;
	_tmp186 = *(this + 4) ;
	_tmp187 = 0 ;
	_tmp188 = d < _tmp187 ;
	_tmp189 = *(_tmp186 + -4) ;
	_tmp190 = d < _tmp189 ;
	_tmp191 = _tmp190 == _tmp187 ;
	_tmp192 = _tmp188 || _tmp191 ;
	IfZ _tmp192 Goto _L20 ;
	_tmp193 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp193 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L20:
	_tmp194 = 4 ;
	_tmp195 = _tmp194 * d ;
	_tmp196 = _tmp186 + _tmp195 ;
	_tmp197 = *(_tmp196) ;
	_tmp198 = *(_tmp197) ;
	_tmp199 = *(_tmp198 + 8) ;
	PushParam _tmp197 ;
	_tmp200 = ACall _tmp199 ;
	PopParams 4 ;
	c = _tmp200 ;
	Goto _L18 ;
_L19:
	_tmp201 = 10 ;
	_tmp202 = _tmp201 < c ;
	IfZ _tmp202 Goto _L21 ;
	_tmp203 = 10 ;
	c = _tmp203 ;
	Goto _L22 ;
_L21:
	_tmp204 = 1 ;
	_tmp205 = c == _tmp204 ;
	IfZ _tmp205 Goto _L23 ;
	_tmp206 = 11 ;
	c = _tmp206 ;
_L23:
_L22:
	_tmp207 = *(this + 8) ;
	_tmp208 = 1 ;
	_tmp209 = _tmp207 + _tmp208 ;
	*(this + 8) = _tmp209 ;
	Return c ;
	EndFunc ;
_BJDeck.Shuffle:
	BeginFunc 92 (this) ;
	_tmp210 = "Shuffling..." ;
	PushParam _tmp210 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp211 = 0 ;
	i = _tmp211 ;
_L24:
	_tmp212 = 8 ;
	_tmp213 = i < _tmp212 ;
	IfZ _tmp213 Goto _L25 ;
	_tmp214 = *(this + 4) ;
	_tmp215 = 0 ;
	_tmp216 = i < _tmp215 ;
	_tmp217 = *(_tmp214 + -4) ;
	_tmp218 = i < _tmp217 ;
	_tmp219 = _tmp218 == _tmp215 ;
	_tmp220 = _tmp216 || _tmp219 ;
	IfZ _tmp220 Goto _L26 ;
	_tmp221 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp221 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L26:
	_tmp222 = 4 ;
	_tmp223 = _tmp222 * i ;
	_tmp224 = _tmp214 + _tmp223 ;
	_tmp225 = *(_tmp224) ;
	_tmp226 = *(_tmp225) ;
	_tmp227 = *(_tmp226 + 4) ;
	PushParam _tmp225 ;
	ACall _tmp227 ;
	PopParams 4 ;
	_tmp228 = 1 ;
	_tmp229 = i + _tmp228 ;
	i = _tmp229 ;
	Goto _L24 ;
_L25:
	_tmp230 = 0 ;
	*(this + 8) = _tmp230 ;
	_tmp231 = "done.\n" ;
	PushParam _tmp231 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
_BJDeck.NumCardsRemaining:
	BeginFunc 20 (this) ;
	_tmp232 = 8 ;
	_tmp233 = 52 ;
	_tmp234 = _tmp232 * _tmp233 ;
	_tmp235 = *(this + 8) ;
	_tmp236 = _tmp234 - _tmp235 ;
	Return _tmp236 ;
	EndFunc ;
VTable BJDeck =
	_BJDeck.Init,
	_BJDeck.DealCard,
	_BJDeck.Shuffle,
	_BJDeck.NumCardsRemaining,
; 
_Player.Init:
	BeginFunc 16 (this, num) ;
	_tmp237 = 1000 ;
	*(this + 12) = _tmp237 ;
	_tmp238 = "What is the name of player #" ;
	PushParam _tmp238 ;
	LCall _PrintString ;
	PopParams 4 ;
	PushParam num ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp239 = "? " ;
	PushParam _tmp239 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp240 = LCall _ReadLine ;
	*(this + 16) = _tmp240 ;
	EndFunc ;
_Player.Hit:
	BeginFunc 120 (this, deck) ;
	_tmp241 = *(deck) ;
	_tmp242 = *(_tmp241 + 4) ;
	PushParam deck ;
	_tmp243 = ACall _tmp242 ;
	PopParams 4 ;
	card = _tmp243 ;
	_tmp244 = *(this + 16) ;
	PushParam _tmp244 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp245 = " was dealt a " ;
	PushParam _tmp245 ;
	LCall _PrintString ;
	PopParams 4 ;
	PushParam card ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp246 = ".\n" ;
	PushParam _tmp246 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp247 = *(this + 24) ;
	_tmp248 = _tmp247 + card ;
	*(this + 24) = _tmp248 ;
	_tmp249 = *(this + 20) ;
	_tmp250 = 1 ;
	_tmp251 = _tmp249 + _tmp250 ;
	*(this + 20) = _tmp251 ;
	_tmp252 = 11 ;
	_tmp253 = card == _tmp252 ;
	IfZ _tmp253 Goto _L27 ;
	_tmp254 = *(this + 4) ;
	_tmp255 = 1 ;
	_tmp256 = _tmp254 + _tmp255 ;
	*(this + 4) = _tmp256 ;
_L27:
_L28:
	_tmp257 = *(this + 24) ;
	_tmp258 = 21 ;
	_tmp259 = _tmp258 < _tmp257 ;
	_tmp260 = *(this + 4) ;
	_tmp261 = 0 ;
	_tmp262 = _tmp261 < _tmp260 ;
	_tmp263 = _tmp259 && _tmp262 ;
	IfZ _tmp263 Goto _L29 ;
	_tmp264 = *(this + 24) ;
	_tmp265 = 10 ;
	_tmp266 = _tmp264 - _tmp265 ;
	*(this + 24) = _tmp266 ;
	_tmp267 = *(this + 4) ;
	_tmp268 = 1 ;
	_tmp269 = _tmp267 - _tmp268 ;
	*(this + 4) = _tmp269 ;
	Goto _L28 ;
_L29:
	EndFunc ;
_Player.DoubleDown:
	BeginFunc 104 (this, deck) ;
	_tmp270 = *(this + 24) ;
	_tmp271 = 10 ;
	_tmp272 = _tmp270 == _tmp271 ;
	_tmp273 = 0 ;
	_tmp274 = _tmp272 == _tmp273 ;
	_tmp275 = *(this + 24) ;
	_tmp276 = 11 ;
	_tmp277 = _tmp275 == _tmp276 ;
	_tmp278 = 0 ;
	_tmp279 = _tmp277 == _tmp278 ;
	_tmp280 = _tmp274 && _tmp279 ;
	IfZ _tmp280 Goto _L30 ;
	_tmp281 = 0 ;
	Return _tmp281 ;
_L30:
	_tmp282 = "Would you like to double down?" ;
	PushParam _tmp282 ;
	_tmp283 = LCall _GetYesOrNo ;
	PopParams 4 ;
	IfZ _tmp283 Goto _L31 ;
	_tmp284 = *(this + 8) ;
	_tmp285 = 2 ;
	_tmp286 = _tmp284 * _tmp285 ;
	*(this + 8) = _tmp286 ;
	_tmp287 = *(this) ;
	_tmp288 = *(_tmp287 + 4) ;
	PushParam deck ;
	PushParam this ;
	ACall _tmp288 ;
	PopParams 8 ;
	_tmp289 = *(this + 16) ;
	PushParam _tmp289 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp290 = ", your total is " ;
	PushParam _tmp290 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp291 = *(this + 24) ;
	PushParam _tmp291 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp292 = ".\n" ;
	PushParam _tmp292 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp293 = 1 ;
	Return _tmp293 ;
_L31:
	_tmp294 = 0 ;
	Return _tmp294 ;
	EndFunc ;
_Player.TakeTurn:
	BeginFunc 168 (this, deck) ;
	_tmp295 = "\n" ;
	PushParam _tmp295 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp296 = *(this + 16) ;
	PushParam _tmp296 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp297 = "'s turn.\n" ;
	PushParam _tmp297 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp298 = 0 ;
	*(this + 24) = _tmp298 ;
	_tmp299 = 0 ;
	*(this + 4) = _tmp299 ;
	_tmp300 = 0 ;
	*(this + 20) = _tmp300 ;
	_tmp301 = *(this) ;
	_tmp302 = *(_tmp301 + 4) ;
	PushParam deck ;
	PushParam this ;
	ACall _tmp302 ;
	PopParams 8 ;
	_tmp303 = *(this) ;
	_tmp304 = *(_tmp303 + 4) ;
	PushParam deck ;
	PushParam this ;
	ACall _tmp304 ;
	PopParams 8 ;
	_tmp305 = *(this) ;
	_tmp306 = *(_tmp305 + 8) ;
	PushParam deck ;
	PushParam this ;
	_tmp307 = ACall _tmp306 ;
	PopParams 8 ;
	_tmp308 = 0 ;
	_tmp309 = _tmp307 == _tmp308 ;
	IfZ _tmp309 Goto _L32 ;
	_tmp310 = 1 ;
	stillGoing = _tmp310 ;
_L33:
	_tmp311 = *(this + 24) ;
	_tmp312 = 21 ;
	_tmp313 = _tmp311 < _tmp312 ;
	_tmp314 = _tmp311 == _tmp312 ;
	_tmp315 = _tmp313 || _tmp314 ;
	_tmp316 = _tmp315 && stillGoing ;
	IfZ _tmp316 Goto _L34 ;
	_tmp317 = *(this + 16) ;
	PushParam _tmp317 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp318 = ", your total is " ;
	PushParam _tmp318 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp319 = *(this + 24) ;
	PushParam _tmp319 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp320 = ".\n" ;
	PushParam _tmp320 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp321 = "Would you like a hit?" ;
	PushParam _tmp321 ;
	_tmp322 = LCall _GetYesOrNo ;
	PopParams 4 ;
	stillGoing = _tmp322 ;
	IfZ stillGoing Goto _L35 ;
	_tmp323 = *(this) ;
	_tmp324 = *(_tmp323 + 4) ;
	PushParam deck ;
	PushParam this ;
	ACall _tmp324 ;
	PopParams 8 ;
_L35:
	Goto _L33 ;
_L34:
_L32:
	_tmp325 = *(this + 24) ;
	_tmp326 = 21 ;
	_tmp327 = _tmp326 < _tmp325 ;
	IfZ _tmp327 Goto _L36 ;
	_tmp328 = *(this + 16) ;
	PushParam _tmp328 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp329 = " busts with the big " ;
	PushParam _tmp329 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp330 = *(this + 24) ;
	PushParam _tmp330 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp331 = "!\n" ;
	PushParam _tmp331 ;
	LCall _PrintString ;
	PopParams 4 ;
	Goto _L37 ;
_L36:
	_tmp332 = *(this + 16) ;
	PushParam _tmp332 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp333 = " stays at " ;
	PushParam _tmp333 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp334 = *(this + 24) ;
	PushParam _tmp334 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp335 = ".\n" ;
	PushParam _tmp335 ;
	LCall _PrintString ;
	PopParams 4 ;
_L37:
	EndFunc ;
_Player.HasMoney:
	BeginFunc 12 (this) ;
	_tmp336 = *(this + 12) ;
	_tmp337 = 0 ;
	_tmp338 = _tmp337 < _tmp336 ;
	Return _tmp338 ;
	EndFunc ;
_Player.PrintMoney:
	BeginFunc 16 (this) ;
	_tmp339 = *(this + 16) ;
	PushParam _tmp339 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp340 = ", you have $" ;
	PushParam _tmp340 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp341 = *(this + 12) ;
	PushParam _tmp341 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp342 = ".\n" ;
	PushParam _tmp342 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
_Player.PlaceBet:
	BeginFunc 56 (this) ;
	_tmp343 = 0 ;
	*(this + 8) = _tmp343 ;
	_tmp344 = *(this) ;
	_tmp345 = *(_tmp344 + 20) ;
	PushParam this ;
	ACall _tmp345 ;
	PopParams 4 ;
_L38:
	_tmp346 = *(this + 8) ;
	_tmp347 = 0 ;
	_tmp348 = _tmp346 < _tmp347 ;
	_tmp349 = _tmp346 == _tmp347 ;
	_tmp350 = _tmp348 || _tmp349 ;
	_tmp351 = *(this + 8) ;
	_tmp352 = *(this + 12) ;
	_tmp353 = _tmp352 < _tmp351 ;
	_tmp354 = _tmp350 || _tmp353 ;
	IfZ _tmp354 Goto _L39 ;
	_tmp355 = "How much would you like to bet? " ;
	PushParam _tmp355 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp356 = LCall _ReadInteger ;
	*(this + 8) = _tmp356 ;
	Goto _L38 ;
_L39:
	EndFunc ;
_Player.GetTotal:
	BeginFunc 4 (this) ;
	_tmp357 = *(this + 24) ;
	Return _tmp357 ;
	EndFunc ;
_Player.Resolve:
	BeginFunc 200 (this, dealer) ;
	_tmp358 = 0 ;
	win = _tmp358 ;
	_tmp359 = 0 ;
	lose = _tmp359 ;
	_tmp360 = *(this + 24) ;
	_tmp361 = 21 ;
	_tmp362 = _tmp360 == _tmp361 ;
	_tmp363 = *(this + 20) ;
	_tmp364 = 2 ;
	_tmp365 = _tmp363 == _tmp364 ;
	_tmp366 = _tmp362 && _tmp365 ;
	IfZ _tmp366 Goto _L40 ;
	_tmp367 = 2 ;
	win = _tmp367 ;
	Goto _L41 ;
_L40:
	_tmp368 = *(this + 24) ;
	_tmp369 = 21 ;
	_tmp370 = _tmp369 < _tmp368 ;
	IfZ _tmp370 Goto _L42 ;
	_tmp371 = 1 ;
	lose = _tmp371 ;
	Goto _L43 ;
_L42:
	_tmp372 = 21 ;
	_tmp373 = _tmp372 < dealer ;
	IfZ _tmp373 Goto _L44 ;
	_tmp374 = 1 ;
	win = _tmp374 ;
	Goto _L45 ;
_L44:
	_tmp375 = *(this + 24) ;
	_tmp376 = dealer < _tmp375 ;
	IfZ _tmp376 Goto _L46 ;
	_tmp377 = 1 ;
	win = _tmp377 ;
	Goto _L47 ;
_L46:
	_tmp378 = *(this + 24) ;
	_tmp379 = _tmp378 < dealer ;
	IfZ _tmp379 Goto _L48 ;
	_tmp380 = 1 ;
	lose = _tmp380 ;
_L48:
_L47:
_L45:
_L43:
_L41:
	_tmp381 = 1 ;
	_tmp382 = _tmp381 < win ;
	_tmp383 = _tmp381 == win ;
	_tmp384 = _tmp382 || _tmp383 ;
	IfZ _tmp384 Goto _L49 ;
	_tmp385 = *(this + 16) ;
	PushParam _tmp385 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp386 = ", you won $" ;
	PushParam _tmp386 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp387 = *(this + 8) ;
	PushParam _tmp387 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp388 = ".\n" ;
	PushParam _tmp388 ;
	LCall _PrintString ;
	PopParams 4 ;
	Goto _L50 ;
_L49:
	_tmp389 = 1 ;
	_tmp390 = _tmp389 < lose ;
	_tmp391 = _tmp389 == lose ;
	_tmp392 = _tmp390 || _tmp391 ;
	IfZ _tmp392 Goto _L51 ;
	_tmp393 = *(this + 16) ;
	PushParam _tmp393 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp394 = ", you lost $" ;
	PushParam _tmp394 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp395 = *(this + 8) ;
	PushParam _tmp395 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp396 = ".\n" ;
	PushParam _tmp396 ;
	LCall _PrintString ;
	PopParams 4 ;
	Goto _L52 ;
_L51:
	_tmp397 = *(this + 16) ;
	PushParam _tmp397 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp398 = ", you push!\n" ;
	PushParam _tmp398 ;
	LCall _PrintString ;
	PopParams 4 ;
_L52:
_L50:
	_tmp399 = *(this + 8) ;
	_tmp400 = win * _tmp399 ;
	win = _tmp400 ;
	_tmp401 = *(this + 8) ;
	_tmp402 = lose * _tmp401 ;
	lose = _tmp402 ;
	_tmp403 = *(this + 12) ;
	_tmp404 = _tmp403 + win ;
	_tmp405 = _tmp404 - lose ;
	*(this + 12) = _tmp405 ;
	EndFunc ;
VTable Player =
	_Player.Init,
	_Player.Hit,
	_Player.DoubleDown,
	_Player.TakeTurn,
	_Player.HasMoney,
	_Player.PrintMoney,
	_Player.PlaceBet,
	_Player.GetTotal,
	_Player.Resolve,
; 
_Dealer.Init:
	BeginFunc 16 (this, id) ;
	_tmp406 = 0 ;
	*(this + 24) = _tmp406 ;
	_tmp407 = 0 ;
	*(this + 4) = _tmp407 ;
	_tmp408 = 0 ;
	*(this + 20) = _tmp408 ;
	_tmp409 = "Dealer" ;
	*(this + 16) = _tmp409 ;
	EndFunc ;
_Dealer.TakeTurn:
	BeginFunc 84 (this, deck) ;
	_tmp410 = "\n" ;
	PushParam _tmp410 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp411 = *(this + 16) ;
	PushParam _tmp411 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp412 = "'s turn.\n" ;
	PushParam _tmp412 ;
	LCall _PrintString ;
	PopParams 4 ;
_L53:
	_tmp413 = *(this + 24) ;
	_tmp414 = 16 ;
	_tmp415 = _tmp413 < _tmp414 ;
	_tmp416 = _tmp413 == _tmp414 ;
	_tmp417 = _tmp415 || _tmp416 ;
	IfZ _tmp417 Goto _L54 ;
	_tmp418 = *(this) ;
	_tmp419 = *(_tmp418 + 4) ;
	PushParam deck ;
	PushParam this ;
	ACall _tmp419 ;
	PopParams 8 ;
	Goto _L53 ;
_L54:
	_tmp420 = *(this + 24) ;
	_tmp421 = 21 ;
	_tmp422 = _tmp421 < _tmp420 ;
	IfZ _tmp422 Goto _L55 ;
	_tmp423 = *(this + 16) ;
	PushParam _tmp423 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp424 = " busts with the big " ;
	PushParam _tmp424 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp425 = *(this + 24) ;
	PushParam _tmp425 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp426 = "!\n" ;
	PushParam _tmp426 ;
	LCall _PrintString ;
	PopParams 4 ;
	Goto _L56 ;
_L55:
	_tmp427 = *(this + 16) ;
	PushParam _tmp427 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp428 = " stays at " ;
	PushParam _tmp428 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp429 = *(this + 24) ;
	PushParam _tmp429 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp430 = ".\n" ;
	PushParam _tmp430 ;
	LCall _PrintString ;
	PopParams 4 ;
_L56:
	EndFunc ;
VTable Dealer =
	_Dealer.Init,
	_Player.Hit,
	_Player.DoubleDown,
	_Dealer.TakeTurn,
	_Player.HasMoney,
	_Player.PrintMoney,
	_Player.PlaceBet,
	_Player.GetTotal,
	_Player.Resolve,
; 
_House.SetupGame:
	BeginFunc 84 (this) ;
	_tmp431 = "\nWelcome to CS143 BlackJack!\n" ;
	PushParam _tmp431 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp432 = "---------------------------\n" ;
	PushParam _tmp432 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp433 = 8 ;
	PushParam _tmp433 ;
	_tmp434 = LCall _Alloc ;
	PopParams 4 ;
	_tmp435 = Random ;
	*(_tmp434) = _tmp435 ;
	gRnd = _tmp434 ;
	_tmp436 = "Please enter a random number seed: " ;
	PushParam _tmp436 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp437 = LCall _ReadInteger ;
	_tmp438 = *(gRnd) ;
	_tmp439 = *(_tmp438) ;
	PushParam _tmp437 ;
	PushParam gRnd ;
	ACall _tmp439 ;
	PopParams 8 ;
	_tmp440 = 12 ;
	PushParam _tmp440 ;
	_tmp441 = LCall _Alloc ;
	PopParams 4 ;
	_tmp442 = BJDeck ;
	*(_tmp441) = _tmp442 ;
	*(this + 12) = _tmp441 ;
	_tmp443 = 28 ;
	PushParam _tmp443 ;
	_tmp444 = LCall _Alloc ;
	PopParams 4 ;
	_tmp445 = Dealer ;
	*(_tmp444) = _tmp445 ;
	*(this + 8) = _tmp444 ;
	_tmp446 = *(this + 12) ;
	_tmp447 = *(_tmp446) ;
	_tmp448 = *(_tmp447) ;
	PushParam _tmp446 ;
	ACall _tmp448 ;
	PopParams 4 ;
	_tmp449 = *(this + 12) ;
	_tmp450 = *(_tmp449) ;
	_tmp451 = *(_tmp450 + 8) ;
	PushParam _tmp449 ;
	ACall _tmp451 ;
	PopParams 4 ;
	EndFunc ;
_House.SetupPlayers:
	BeginFunc 196 (this) ;
	_tmp452 = "How many players do we have today? " ;
	PushParam _tmp452 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp453 = LCall _ReadInteger ;
	numPlayers = _tmp453 ;
	_tmp454 = 1 ;
	_tmp455 = numPlayers < _tmp454 ;
	IfZ _tmp455 Goto _L57 ;
	_tmp456 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp456 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L57:
	_tmp457 = 1 ;
	_tmp458 = _tmp457 + numPlayers ;
	_tmp459 = 4 ;
	_tmp460 = _tmp458 * _tmp459 ;
	PushParam _tmp460 ;
	_tmp461 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp461) = numPlayers ;
	_tmp462 = _tmp461 + _tmp459 ;
	*(this + 4) = _tmp462 ;
	_tmp463 = 0 ;
	i = _tmp463 ;
_L58:
	_tmp464 = *(this + 4) ;
	_tmp465 = *(_tmp464 + -4) ;
	_tmp466 = i < _tmp465 ;
	IfZ _tmp466 Goto _L59 ;
	_tmp467 = *(this + 4) ;
	_tmp468 = 0 ;
	_tmp469 = i < _tmp468 ;
	_tmp470 = *(_tmp467 + -4) ;
	_tmp471 = i < _tmp470 ;
	_tmp472 = _tmp471 == _tmp468 ;
	_tmp473 = _tmp469 || _tmp472 ;
	IfZ _tmp473 Goto _L60 ;
	_tmp474 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp474 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L60:
	_tmp475 = 4 ;
	_tmp476 = _tmp475 * i ;
	_tmp477 = _tmp467 + _tmp476 ;
	_tmp478 = 28 ;
	PushParam _tmp478 ;
	_tmp479 = LCall _Alloc ;
	PopParams 4 ;
	_tmp480 = Player ;
	*(_tmp479) = _tmp480 ;
	*(_tmp477) = _tmp479 ;
	_tmp481 = 1 ;
	_tmp482 = i + _tmp481 ;
	_tmp483 = *(this + 4) ;
	_tmp484 = 0 ;
	_tmp485 = i < _tmp484 ;
	_tmp486 = *(_tmp483 + -4) ;
	_tmp487 = i < _tmp486 ;
	_tmp488 = _tmp487 == _tmp484 ;
	_tmp489 = _tmp485 || _tmp488 ;
	IfZ _tmp489 Goto _L61 ;
	_tmp490 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp490 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L61:
	_tmp491 = 4 ;
	_tmp492 = _tmp491 * i ;
	_tmp493 = _tmp483 + _tmp492 ;
	_tmp494 = *(_tmp493) ;
	_tmp495 = *(_tmp494) ;
	_tmp496 = *(_tmp495) ;
	PushParam _tmp482 ;
	PushParam _tmp494 ;
	ACall _tmp496 ;
	PopParams 8 ;
	_tmp497 = 1 ;
	_tmp498 = i + _tmp497 ;
	i = _tmp498 ;
	Goto _L58 ;
_L59:
	EndFunc ;
_House.TakeAllBets:
	BeginFunc 148 (this) ;
	_tmp499 = "\nFirst, let's take bets.\n" ;
	PushParam _tmp499 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp500 = 0 ;
	i = _tmp500 ;
_L62:
	_tmp501 = *(this + 4) ;
	_tmp502 = *(_tmp501 + -4) ;
	_tmp503 = i < _tmp502 ;
	IfZ _tmp503 Goto _L63 ;
	_tmp504 = *(this + 4) ;
	_tmp505 = 0 ;
	_tmp506 = i < _tmp505 ;
	_tmp507 = *(_tmp504 + -4) ;
	_tmp508 = i < _tmp507 ;
	_tmp509 = _tmp508 == _tmp505 ;
	_tmp510 = _tmp506 || _tmp509 ;
	IfZ _tmp510 Goto _L64 ;
	_tmp511 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp511 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L64:
	_tmp512 = 4 ;
	_tmp513 = _tmp512 * i ;
	_tmp514 = _tmp504 + _tmp513 ;
	_tmp515 = *(_tmp514) ;
	_tmp516 = *(_tmp515) ;
	_tmp517 = *(_tmp516 + 16) ;
	PushParam _tmp515 ;
	_tmp518 = ACall _tmp517 ;
	PopParams 4 ;
	IfZ _tmp518 Goto _L65 ;
	_tmp519 = *(this + 4) ;
	_tmp520 = 0 ;
	_tmp521 = i < _tmp520 ;
	_tmp522 = *(_tmp519 + -4) ;
	_tmp523 = i < _tmp522 ;
	_tmp524 = _tmp523 == _tmp520 ;
	_tmp525 = _tmp521 || _tmp524 ;
	IfZ _tmp525 Goto _L66 ;
	_tmp526 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp526 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L66:
	_tmp527 = 4 ;
	_tmp528 = _tmp527 * i ;
	_tmp529 = _tmp519 + _tmp528 ;
	_tmp530 = *(_tmp529) ;
	_tmp531 = *(_tmp530) ;
	_tmp532 = *(_tmp531 + 24) ;
	PushParam _tmp530 ;
	ACall _tmp532 ;
	PopParams 4 ;
_L65:
	_tmp533 = 1 ;
	_tmp534 = i + _tmp533 ;
	i = _tmp534 ;
	Goto _L62 ;
_L63:
	EndFunc ;
_House.TakeAllTurns:
	BeginFunc 148 (this) ;
	_tmp535 = 0 ;
	i = _tmp535 ;
_L67:
	_tmp536 = *(this + 4) ;
	_tmp537 = *(_tmp536 + -4) ;
	_tmp538 = i < _tmp537 ;
	IfZ _tmp538 Goto _L68 ;
	_tmp539 = *(this + 4) ;
	_tmp540 = 0 ;
	_tmp541 = i < _tmp540 ;
	_tmp542 = *(_tmp539 + -4) ;
	_tmp543 = i < _tmp542 ;
	_tmp544 = _tmp543 == _tmp540 ;
	_tmp545 = _tmp541 || _tmp544 ;
	IfZ _tmp545 Goto _L69 ;
	_tmp546 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp546 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L69:
	_tmp547 = 4 ;
	_tmp548 = _tmp547 * i ;
	_tmp549 = _tmp539 + _tmp548 ;
	_tmp550 = *(_tmp549) ;
	_tmp551 = *(_tmp550) ;
	_tmp552 = *(_tmp551 + 16) ;
	PushParam _tmp550 ;
	_tmp553 = ACall _tmp552 ;
	PopParams 4 ;
	IfZ _tmp553 Goto _L70 ;
	_tmp554 = *(this + 12) ;
	_tmp555 = *(this + 4) ;
	_tmp556 = 0 ;
	_tmp557 = i < _tmp556 ;
	_tmp558 = *(_tmp555 + -4) ;
	_tmp559 = i < _tmp558 ;
	_tmp560 = _tmp559 == _tmp556 ;
	_tmp561 = _tmp557 || _tmp560 ;
	IfZ _tmp561 Goto _L71 ;
	_tmp562 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp562 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L71:
	_tmp563 = 4 ;
	_tmp564 = _tmp563 * i ;
	_tmp565 = _tmp555 + _tmp564 ;
	_tmp566 = *(_tmp565) ;
	_tmp567 = *(_tmp566) ;
	_tmp568 = *(_tmp567 + 12) ;
	PushParam _tmp554 ;
	PushParam _tmp566 ;
	ACall _tmp568 ;
	PopParams 8 ;
_L70:
	_tmp569 = 1 ;
	_tmp570 = i + _tmp569 ;
	i = _tmp570 ;
	Goto _L67 ;
_L68:
	EndFunc ;
_House.ResolveAllPlayers:
	BeginFunc 164 (this) ;
	_tmp571 = "\nTime to resolve bets.\n" ;
	PushParam _tmp571 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp572 = 0 ;
	i = _tmp572 ;
_L72:
	_tmp573 = *(this + 4) ;
	_tmp574 = *(_tmp573 + -4) ;
	_tmp575 = i < _tmp574 ;
	IfZ _tmp575 Goto _L73 ;
	_tmp576 = *(this + 4) ;
	_tmp577 = 0 ;
	_tmp578 = i < _tmp577 ;
	_tmp579 = *(_tmp576 + -4) ;
	_tmp580 = i < _tmp579 ;
	_tmp581 = _tmp580 == _tmp577 ;
	_tmp582 = _tmp578 || _tmp581 ;
	IfZ _tmp582 Goto _L74 ;
	_tmp583 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp583 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L74:
	_tmp584 = 4 ;
	_tmp585 = _tmp584 * i ;
	_tmp586 = _tmp576 + _tmp585 ;
	_tmp587 = *(_tmp586) ;
	_tmp588 = *(_tmp587) ;
	_tmp589 = *(_tmp588 + 16) ;
	PushParam _tmp587 ;
	_tmp590 = ACall _tmp589 ;
	PopParams 4 ;
	IfZ _tmp590 Goto _L75 ;
	_tmp591 = *(this + 8) ;
	_tmp592 = *(_tmp591) ;
	_tmp593 = *(_tmp592 + 28) ;
	PushParam _tmp591 ;
	_tmp594 = ACall _tmp593 ;
	PopParams 4 ;
	_tmp595 = *(this + 4) ;
	_tmp596 = 0 ;
	_tmp597 = i < _tmp596 ;
	_tmp598 = *(_tmp595 + -4) ;
	_tmp599 = i < _tmp598 ;
	_tmp600 = _tmp599 == _tmp596 ;
	_tmp601 = _tmp597 || _tmp600 ;
	IfZ _tmp601 Goto _L76 ;
	_tmp602 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp602 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L76:
	_tmp603 = 4 ;
	_tmp604 = _tmp603 * i ;
	_tmp605 = _tmp595 + _tmp604 ;
	_tmp606 = *(_tmp605) ;
	_tmp607 = *(_tmp606) ;
	_tmp608 = *(_tmp607 + 32) ;
	PushParam _tmp594 ;
	PushParam _tmp606 ;
	ACall _tmp608 ;
	PopParams 8 ;
_L75:
	_tmp609 = 1 ;
	_tmp610 = i + _tmp609 ;
	i = _tmp610 ;
	Goto _L72 ;
_L73:
	EndFunc ;
_House.PrintAllMoney:
	BeginFunc 84 (this) ;
	_tmp611 = 0 ;
	i = _tmp611 ;
_L77:
	_tmp612 = *(this + 4) ;
	_tmp613 = *(_tmp612 + -4) ;
	_tmp614 = i < _tmp613 ;
	IfZ _tmp614 Goto _L78 ;
	_tmp615 = *(this + 4) ;
	_tmp616 = 0 ;
	_tmp617 = i < _tmp616 ;
	_tmp618 = *(_tmp615 + -4) ;
	_tmp619 = i < _tmp618 ;
	_tmp620 = _tmp619 == _tmp616 ;
	_tmp621 = _tmp617 || _tmp620 ;
	IfZ _tmp621 Goto _L79 ;
	_tmp622 = "Decaf runtime error: Array subscript out of bound..." ;
	PushParam _tmp622 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L79:
	_tmp623 = 4 ;
	_tmp624 = _tmp623 * i ;
	_tmp625 = _tmp615 + _tmp624 ;
	_tmp626 = *(_tmp625) ;
	_tmp627 = *(_tmp626) ;
	_tmp628 = *(_tmp627 + 20) ;
	PushParam _tmp626 ;
	ACall _tmp628 ;
	PopParams 4 ;
	_tmp629 = 1 ;
	_tmp630 = i + _tmp629 ;
	i = _tmp630 ;
	Goto _L77 ;
_L78:
	EndFunc ;
_House.PlayOneGame:
	BeginFunc 112 (this) ;
	_tmp631 = *(this + 12) ;
	_tmp632 = *(_tmp631) ;
	_tmp633 = *(_tmp632 + 12) ;
	PushParam _tmp631 ;
	_tmp634 = ACall _tmp633 ;
	PopParams 4 ;
	_tmp635 = 26 ;
	_tmp636 = _tmp634 < _tmp635 ;
	IfZ _tmp636 Goto _L80 ;
	_tmp637 = *(this + 12) ;
	_tmp638 = *(_tmp637) ;
	_tmp639 = *(_tmp638 + 8) ;
	PushParam _tmp637 ;
	ACall _tmp639 ;
	PopParams 4 ;
_L80:
	_tmp640 = *(this) ;
	_tmp641 = *(_tmp640 + 8) ;
	PushParam this ;
	ACall _tmp641 ;
	PopParams 4 ;
	_tmp642 = "\nDealer starts. " ;
	PushParam _tmp642 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp643 = 0 ;
	_tmp644 = *(this + 8) ;
	_tmp645 = *(_tmp644) ;
	_tmp646 = *(_tmp645) ;
	PushParam _tmp643 ;
	PushParam _tmp644 ;
	ACall _tmp646 ;
	PopParams 8 ;
	_tmp647 = *(this + 12) ;
	_tmp648 = *(this + 8) ;
	_tmp649 = *(_tmp648) ;
	_tmp650 = *(_tmp649 + 4) ;
	PushParam _tmp647 ;
	PushParam _tmp648 ;
	ACall _tmp650 ;
	PopParams 8 ;
	_tmp651 = *(this) ;
	_tmp652 = *(_tmp651 + 12) ;
	PushParam this ;
	ACall _tmp652 ;
	PopParams 4 ;
	_tmp653 = *(this + 12) ;
	_tmp654 = *(this + 8) ;
	_tmp655 = *(_tmp654) ;
	_tmp656 = *(_tmp655 + 12) ;
	PushParam _tmp653 ;
	PushParam _tmp654 ;
	ACall _tmp656 ;
	PopParams 8 ;
	_tmp657 = *(this) ;
	_tmp658 = *(_tmp657 + 16) ;
	PushParam this ;
	ACall _tmp658 ;
	PopParams 4 ;
	EndFunc ;
VTable House =
	_House.SetupGame,
	_House.SetupPlayers,
	_House.TakeAllBets,
	_House.TakeAllTurns,
	_House.ResolveAllPlayers,
	_House.PrintAllMoney,
	_House.PlayOneGame,
; 
_GetYesOrNo:
	BeginFunc 32 (prompt) ;
	PushParam prompt ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp659 = " (y/n) " ;
	PushParam _tmp659 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp660 = LCall _ReadLine ;
	answer = _tmp660 ;
	_tmp661 = "y" ;
	PushParam _tmp661 ;
	PushParam answer ;
	_tmp662 = LCall _StringEqual ;
	PopParams 8 ;
	_tmp663 = "Y" ;
	PushParam _tmp663 ;
	PushParam answer ;
	_tmp664 = LCall _StringEqual ;
	PopParams 8 ;
	_tmp665 = _tmp662 || _tmp664 ;
	Return _tmp665 ;
	EndFunc ;
main:
	BeginFunc 76 () ;
	_tmp666 = 1 ;
	keepPlaying = _tmp666 ;
	_tmp667 = 16 ;
	PushParam _tmp667 ;
	_tmp668 = LCall _Alloc ;
	PopParams 4 ;
	_tmp669 = House ;
	*(_tmp668) = _tmp669 ;
	house = _tmp668 ;
	_tmp670 = *(house) ;
	_tmp671 = *(_tmp670) ;
	PushParam house ;
	ACall _tmp671 ;
	PopParams 4 ;
	_tmp672 = *(house) ;
	_tmp673 = *(_tmp672 + 4) ;
	PushParam house ;
	ACall _tmp673 ;
	PopParams 4 ;
_L81:
	IfZ keepPlaying Goto _L82 ;
	_tmp674 = *(house) ;
	_tmp675 = *(_tmp674 + 24) ;
	PushParam house ;
	ACall _tmp675 ;
	PopParams 4 ;
	_tmp676 = "\nDo you want to play another hand?" ;
	PushParam _tmp676 ;
	_tmp677 = LCall _GetYesOrNo ;
	PopParams 4 ;
	keepPlaying = _tmp677 ;
	Goto _L81 ;
_L82:
	_tmp678 = *(house) ;
	_tmp679 = *(_tmp678 + 20) ;
	PushParam house ;
	ACall _tmp679 ;
	PopParams 4 ;
	_tmp680 = "Thank you for playing...come again soon.\n" ;
	PushParam _tmp680 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp681 = "\nCS143 BlackJack Copyright (c) 1999 by Peter Mor..." ;
	PushParam _tmp681 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp682 = "(2001 mods by jdz)\n" ;
	PushParam _tmp682 ;
	LCall _PrintString ;
	PopParams 4 ;
	EndFunc ;
