_Matrix.Init:
	BeginFunc 0 (this) ;
	EndFunc ;
_Matrix.Set:
	BeginFunc 0 (this, x, y, value) ;
	EndFunc ;
_Matrix.Get:
	BeginFunc 0 (this, x, y) ;
	EndFunc ;
_Matrix.PrintMatrix:
	BeginFunc 68 (this) ;
	_tmp0 = 0 ;
	i = _tmp0 ;
_L0:
	_tmp1 = 10 ;
	_tmp2 = i < _tmp1 ;
	IfZ _tmp2 Goto _L1 ;
	_tmp3 = 0 ;
	j = _tmp3 ;
_L2:
	_tmp4 = 10 ;
	_tmp5 = j < _tmp4 ;
	IfZ _tmp5 Goto _L3 ;
	_tmp6 = *(this) ;
	_tmp7 = *(_tmp6 + 8) ;
	PushParam j ;
	PushParam i ;
	PushParam this ;
	_tmp8 = ACall _tmp7 ;
	PopParams 12 ;
	PushParam _tmp8 ;
	LCall _PrintInt ;
	PopParams 4 ;
	_tmp9 = "\t" ;
	PushParam _tmp9 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp10 = 1 ;
	_tmp11 = j + _tmp10 ;
	j = _tmp11 ;
	Goto _L2 ;
_L3:
	_tmp12 = "\n" ;
	PushParam _tmp12 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp13 = 1 ;
	_tmp14 = i + _tmp13 ;
	i = _tmp14 ;
	Goto _L0 ;
_L1:
	EndFunc ;
_Matrix.SeedMatrix:
	BeginFunc 180 (this) ;
	_tmp15 = 0 ;
	i = _tmp15 ;
_L4:
	_tmp16 = 5 ;
	_tmp17 = i < _tmp16 ;
	IfZ _tmp17 Goto _L5 ;
	_tmp18 = 0 ;
	j = _tmp18 ;
_L6:
	_tmp19 = 5 ;
	_tmp20 = j < _tmp19 ;
	IfZ _tmp20 Goto _L7 ;
	_tmp21 = i + j ;
	_tmp22 = *(this) ;
	_tmp23 = *(_tmp22 + 4) ;
	PushParam _tmp21 ;
	PushParam j ;
	PushParam i ;
	PushParam this ;
	ACall _tmp23 ;
	PopParams 16 ;
	_tmp24 = 1 ;
	_tmp25 = j + _tmp24 ;
	j = _tmp25 ;
	Goto _L6 ;
_L7:
	_tmp26 = 1 ;
	_tmp27 = i + _tmp26 ;
	i = _tmp27 ;
	Goto _L4 ;
_L5:
	_tmp28 = 2 ;
	_tmp29 = 3 ;
	_tmp30 = 4 ;
	_tmp31 = *(this) ;
	_tmp32 = *(_tmp31 + 4) ;
	PushParam _tmp30 ;
	PushParam _tmp29 ;
	PushParam _tmp28 ;
	PushParam this ;
	ACall _tmp32 ;
	PopParams 16 ;
	_tmp33 = 4 ;
	_tmp34 = 6 ;
	_tmp35 = 2 ;
	_tmp36 = *(this) ;
	_tmp37 = *(_tmp36 + 4) ;
	PushParam _tmp35 ;
	PushParam _tmp34 ;
	PushParam _tmp33 ;
	PushParam this ;
	ACall _tmp37 ;
	PopParams 16 ;
	_tmp38 = 2 ;
	_tmp39 = 3 ;
	_tmp40 = 5 ;
	_tmp41 = *(this) ;
	_tmp42 = *(_tmp41 + 4) ;
	PushParam _tmp40 ;
	PushParam _tmp39 ;
	PushParam _tmp38 ;
	PushParam this ;
	ACall _tmp42 ;
	PopParams 16 ;
	_tmp43 = 0 ;
	_tmp44 = 0 ;
	_tmp45 = 1 ;
	_tmp46 = *(this) ;
	_tmp47 = *(_tmp46 + 4) ;
	PushParam _tmp45 ;
	PushParam _tmp44 ;
	PushParam _tmp43 ;
	PushParam this ;
	ACall _tmp47 ;
	PopParams 16 ;
	_tmp48 = 1 ;
	_tmp49 = 6 ;
	_tmp50 = 3 ;
	_tmp51 = *(this) ;
	_tmp52 = *(_tmp51 + 4) ;
	PushParam _tmp50 ;
	PushParam _tmp49 ;
	PushParam _tmp48 ;
	PushParam this ;
	ACall _tmp52 ;
	PopParams 16 ;
	_tmp53 = 7 ;
	_tmp54 = 7 ;
	_tmp55 = 7 ;
	_tmp56 = *(this) ;
	_tmp57 = *(_tmp56 + 4) ;
	PushParam _tmp55 ;
	PushParam _tmp54 ;
	PushParam _tmp53 ;
	PushParam this ;
	ACall _tmp57 ;
	PopParams 16 ;
	EndFunc ;
VTable Matrix =
	_Matrix.Init,
	_Matrix.Set,
	_Matrix.Get,
	_Matrix.PrintMatrix,
	_Matrix.SeedMatrix,
; 
_DenseMatrix.Init:
	BeginFunc 284 (this) ;
	_tmp58 = 10 ;
	_tmp59 = 1 ;
	_tmp60 = _tmp58 < _tmp59 ;
	IfZ _tmp60 Goto _L8 ;
	_tmp61 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp61 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L8:
	_tmp62 = 1 ;
	_tmp63 = _tmp62 + _tmp58 ;
	_tmp64 = 4 ;
	_tmp65 = _tmp63 * _tmp64 ;
	PushParam _tmp65 ;
	_tmp66 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp66) = _tmp58 ;
	_tmp67 = _tmp66 + _tmp64 ;
	*(this + 4) = _tmp67 ;
	_tmp68 = 0 ;
	i = _tmp68 ;
_L9:
	_tmp69 = 10 ;
	_tmp70 = i < _tmp69 ;
	IfZ _tmp70 Goto _L10 ;
	_tmp71 = *(this + 4) ;
	_tmp72 = 0 ;
	_tmp73 = i < _tmp72 ;
	_tmp74 = *(_tmp71 + -4) ;
	_tmp75 = i < _tmp74 ;
	_tmp76 = _tmp75 == _tmp72 ;
	_tmp77 = _tmp73 || _tmp76 ;
	IfZ _tmp77 Goto _L11 ;
	_tmp78 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp78 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L11:
	_tmp79 = 4 ;
	_tmp80 = _tmp79 * i ;
	_tmp81 = _tmp71 + _tmp80 ;
	_tmp82 = 10 ;
	_tmp83 = 1 ;
	_tmp84 = _tmp82 < _tmp83 ;
	IfZ _tmp84 Goto _L12 ;
	_tmp85 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp85 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L12:
	_tmp86 = 1 ;
	_tmp87 = _tmp86 + _tmp82 ;
	_tmp88 = 4 ;
	_tmp89 = _tmp87 * _tmp88 ;
	PushParam _tmp89 ;
	_tmp90 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp90) = _tmp82 ;
	_tmp91 = _tmp90 + _tmp88 ;
	*(_tmp81) = _tmp91 ;
	_tmp92 = 1 ;
	_tmp93 = i + _tmp92 ;
	i = _tmp93 ;
	Goto _L9 ;
_L10:
	_tmp94 = 0 ;
	i = _tmp94 ;
_L13:
	_tmp95 = 10 ;
	_tmp96 = i < _tmp95 ;
	IfZ _tmp96 Goto _L14 ;
	_tmp97 = 0 ;
	j = _tmp97 ;
_L15:
	_tmp98 = 10 ;
	_tmp99 = j < _tmp98 ;
	IfZ _tmp99 Goto _L16 ;
	_tmp100 = *(this + 4) ;
	_tmp101 = 0 ;
	_tmp102 = i < _tmp101 ;
	_tmp103 = *(_tmp100 + -4) ;
	_tmp104 = i < _tmp103 ;
	_tmp105 = _tmp104 == _tmp101 ;
	_tmp106 = _tmp102 || _tmp105 ;
	IfZ _tmp106 Goto _L17 ;
	_tmp107 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp107 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L17:
	_tmp108 = 4 ;
	_tmp109 = _tmp108 * i ;
	_tmp110 = _tmp100 + _tmp109 ;
	_tmp111 = *(_tmp110) ;
	_tmp112 = 0 ;
	_tmp113 = j < _tmp112 ;
	_tmp114 = *(_tmp111 + -4) ;
	_tmp115 = j < _tmp114 ;
	_tmp116 = _tmp115 == _tmp112 ;
	_tmp117 = _tmp113 || _tmp116 ;
	IfZ _tmp117 Goto _L18 ;
	_tmp118 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp118 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L18:
	_tmp119 = 4 ;
	_tmp120 = _tmp119 * j ;
	_tmp121 = _tmp111 + _tmp120 ;
	_tmp122 = 0 ;
	*(_tmp121) = _tmp122 ;
	_tmp123 = 1 ;
	_tmp124 = j + _tmp123 ;
	j = _tmp124 ;
	Goto _L15 ;
_L16:
	_tmp125 = 1 ;
	_tmp126 = i + _tmp125 ;
	i = _tmp126 ;
	Goto _L13 ;
_L14:
	EndFunc ;
_DenseMatrix.Set:
	BeginFunc 88 (this, x, y, value) ;
	_tmp127 = *(this + 4) ;
	_tmp128 = 0 ;
	_tmp129 = x < _tmp128 ;
	_tmp130 = *(_tmp127 + -4) ;
	_tmp131 = x < _tmp130 ;
	_tmp132 = _tmp131 == _tmp128 ;
	_tmp133 = _tmp129 || _tmp132 ;
	IfZ _tmp133 Goto _L19 ;
	_tmp134 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp134 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L19:
	_tmp135 = 4 ;
	_tmp136 = _tmp135 * x ;
	_tmp137 = _tmp127 + _tmp136 ;
	_tmp138 = *(_tmp137) ;
	_tmp139 = 0 ;
	_tmp140 = y < _tmp139 ;
	_tmp141 = *(_tmp138 + -4) ;
	_tmp142 = y < _tmp141 ;
	_tmp143 = _tmp142 == _tmp139 ;
	_tmp144 = _tmp140 || _tmp143 ;
	IfZ _tmp144 Goto _L20 ;
	_tmp145 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp145 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L20:
	_tmp146 = 4 ;
	_tmp147 = _tmp146 * y ;
	_tmp148 = _tmp138 + _tmp147 ;
	*(_tmp148) = value ;
	EndFunc ;
_DenseMatrix.Get:
	BeginFunc 92 (this, x, y) ;
	_tmp149 = *(this + 4) ;
	_tmp150 = 0 ;
	_tmp151 = x < _tmp150 ;
	_tmp152 = *(_tmp149 + -4) ;
	_tmp153 = x < _tmp152 ;
	_tmp154 = _tmp153 == _tmp150 ;
	_tmp155 = _tmp151 || _tmp154 ;
	IfZ _tmp155 Goto _L21 ;
	_tmp156 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp156 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L21:
	_tmp157 = 4 ;
	_tmp158 = _tmp157 * x ;
	_tmp159 = _tmp149 + _tmp158 ;
	_tmp160 = *(_tmp159) ;
	_tmp161 = 0 ;
	_tmp162 = y < _tmp161 ;
	_tmp163 = *(_tmp160 + -4) ;
	_tmp164 = y < _tmp163 ;
	_tmp165 = _tmp164 == _tmp161 ;
	_tmp166 = _tmp162 || _tmp165 ;
	IfZ _tmp166 Goto _L22 ;
	_tmp167 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp167 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L22:
	_tmp168 = 4 ;
	_tmp169 = _tmp168 * y ;
	_tmp170 = _tmp160 + _tmp169 ;
	_tmp171 = *(_tmp170) ;
	Return _tmp171 ;
	EndFunc ;
VTable DenseMatrix =
	_DenseMatrix.Init,
	_DenseMatrix.Set,
	_DenseMatrix.Get,
	_Matrix.PrintMatrix,
	_Matrix.SeedMatrix,
; 
_SparseItem.Init:
	BeginFunc 0 (this, d, y, next) ;
	*(this + 4) = d ;
	*(this + 8) = y ;
	*(this + 12) = next ;
	EndFunc ;
_SparseItem.GetNext:
	BeginFunc 4 (this) ;
	_tmp172 = *(this + 12) ;
	Return _tmp172 ;
	EndFunc ;
_SparseItem.GetY:
	BeginFunc 4 (this) ;
	_tmp173 = *(this + 8) ;
	Return _tmp173 ;
	EndFunc ;
_SparseItem.GetData:
	BeginFunc 4 (this) ;
	_tmp174 = *(this + 4) ;
	Return _tmp174 ;
	EndFunc ;
_SparseItem.SetData:
	BeginFunc 0 (this, val) ;
	*(this + 4) = val ;
	EndFunc ;
VTable SparseItem =
	_SparseItem.Init,
	_SparseItem.GetNext,
	_SparseItem.GetY,
	_SparseItem.GetData,
	_SparseItem.SetData,
; 
_SparseMatrix.Init:
	BeginFunc 112 (this) ;
	_tmp175 = 10 ;
	_tmp176 = 1 ;
	_tmp177 = _tmp175 < _tmp176 ;
	IfZ _tmp177 Goto _L23 ;
	_tmp178 = "Decaf runtime error: Array size is <= 0\n" ;
	PushParam _tmp178 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L23:
	_tmp179 = 1 ;
	_tmp180 = _tmp179 + _tmp175 ;
	_tmp181 = 4 ;
	_tmp182 = _tmp180 * _tmp181 ;
	PushParam _tmp182 ;
	_tmp183 = LCall _Alloc ;
	PopParams 4 ;
	*(_tmp183) = _tmp175 ;
	_tmp184 = _tmp183 + _tmp181 ;
	*(this + 4) = _tmp184 ;
	_tmp185 = 0 ;
	i = _tmp185 ;
_L24:
	_tmp186 = 10 ;
	_tmp187 = i < _tmp186 ;
	IfZ _tmp187 Goto _L25 ;
	_tmp188 = *(this + 4) ;
	_tmp189 = 0 ;
	_tmp190 = i < _tmp189 ;
	_tmp191 = *(_tmp188 + -4) ;
	_tmp192 = i < _tmp191 ;
	_tmp193 = _tmp192 == _tmp189 ;
	_tmp194 = _tmp190 || _tmp193 ;
	IfZ _tmp194 Goto _L26 ;
	_tmp195 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp195 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L26:
	_tmp196 = 4 ;
	_tmp197 = _tmp196 * i ;
	_tmp198 = _tmp188 + _tmp197 ;
	_tmp199 = 0 ;
	*(_tmp198) = _tmp199 ;
	_tmp200 = 1 ;
	_tmp201 = i + _tmp200 ;
	i = _tmp201 ;
	Goto _L24 ;
_L25:
	EndFunc ;
_SparseMatrix.Find:
	BeginFunc 100 (this, x, y) ;
	_tmp202 = *(this + 4) ;
	_tmp203 = 0 ;
	_tmp204 = x < _tmp203 ;
	_tmp205 = *(_tmp202 + -4) ;
	_tmp206 = x < _tmp205 ;
	_tmp207 = _tmp206 == _tmp203 ;
	_tmp208 = _tmp204 || _tmp207 ;
	IfZ _tmp208 Goto _L27 ;
	_tmp209 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp209 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L27:
	_tmp210 = 4 ;
	_tmp211 = _tmp210 * x ;
	_tmp212 = _tmp202 + _tmp211 ;
	_tmp213 = *(_tmp212) ;
	elem = _tmp213 ;
_L28:
	_tmp214 = 0 ;
	_tmp215 = elem == _tmp214 ;
	_tmp216 = 0 ;
	_tmp217 = _tmp215 == _tmp216 ;
	IfZ _tmp217 Goto _L29 ;
	_tmp218 = *(elem) ;
	_tmp219 = *(_tmp218 + 8) ;
	PushParam elem ;
	_tmp220 = ACall _tmp219 ;
	PopParams 4 ;
	_tmp221 = _tmp220 == y ;
	IfZ _tmp221 Goto _L30 ;
	Return elem ;
_L30:
	_tmp222 = *(elem) ;
	_tmp223 = *(_tmp222 + 4) ;
	PushParam elem ;
	_tmp224 = ACall _tmp223 ;
	PopParams 4 ;
	elem = _tmp224 ;
	Goto _L28 ;
_L29:
	_tmp225 = 0 ;
	Return _tmp225 ;
	EndFunc ;
_SparseMatrix.Set:
	BeginFunc 152 (this, x, y, value) ;
	_tmp226 = *(this) ;
	_tmp227 = *(_tmp226 + 20) ;
	PushParam y ;
	PushParam x ;
	PushParam this ;
	_tmp228 = ACall _tmp227 ;
	PopParams 12 ;
	elem = _tmp228 ;
	_tmp229 = 0 ;
	_tmp230 = elem == _tmp229 ;
	_tmp231 = 0 ;
	_tmp232 = _tmp230 == _tmp231 ;
	IfZ _tmp232 Goto _L31 ;
	_tmp233 = *(elem) ;
	_tmp234 = *(_tmp233 + 16) ;
	PushParam value ;
	PushParam elem ;
	ACall _tmp234 ;
	PopParams 8 ;
	Goto _L32 ;
_L31:
	_tmp235 = 16 ;
	PushParam _tmp235 ;
	_tmp236 = LCall _Alloc ;
	PopParams 4 ;
	_tmp237 = SparseItem ;
	*(_tmp236) = _tmp237 ;
	elem = _tmp236 ;
	_tmp238 = *(this + 4) ;
	_tmp239 = 0 ;
	_tmp240 = x < _tmp239 ;
	_tmp241 = *(_tmp238 + -4) ;
	_tmp242 = x < _tmp241 ;
	_tmp243 = _tmp242 == _tmp239 ;
	_tmp244 = _tmp240 || _tmp243 ;
	IfZ _tmp244 Goto _L33 ;
	_tmp245 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp245 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L33:
	_tmp246 = 4 ;
	_tmp247 = _tmp246 * x ;
	_tmp248 = _tmp238 + _tmp247 ;
	_tmp249 = *(_tmp248) ;
	_tmp250 = *(elem) ;
	_tmp251 = *(_tmp250) ;
	PushParam _tmp249 ;
	PushParam y ;
	PushParam value ;
	PushParam elem ;
	ACall _tmp251 ;
	PopParams 16 ;
	_tmp252 = *(this + 4) ;
	_tmp253 = 0 ;
	_tmp254 = x < _tmp253 ;
	_tmp255 = *(_tmp252 + -4) ;
	_tmp256 = x < _tmp255 ;
	_tmp257 = _tmp256 == _tmp253 ;
	_tmp258 = _tmp254 || _tmp257 ;
	IfZ _tmp258 Goto _L34 ;
	_tmp259 = "Decaf runtime error: Array subscript out of bounds\n" ;
	PushParam _tmp259 ;
	LCall _PrintString ;
	PopParams 4 ;
	LCall _Halt ;
_L34:
	_tmp260 = 4 ;
	_tmp261 = _tmp260 * x ;
	_tmp262 = _tmp252 + _tmp261 ;
	*(_tmp262) = elem ;
_L32:
	EndFunc ;
_SparseMatrix.Get:
	BeginFunc 48 (this, x, y) ;
	_tmp263 = *(this) ;
	_tmp264 = *(_tmp263 + 20) ;
	PushParam y ;
	PushParam x ;
	PushParam this ;
	_tmp265 = ACall _tmp264 ;
	PopParams 12 ;
	elem = _tmp265 ;
	_tmp266 = 0 ;
	_tmp267 = elem == _tmp266 ;
	_tmp268 = 0 ;
	_tmp269 = _tmp267 == _tmp268 ;
	IfZ _tmp269 Goto _L35 ;
	_tmp270 = *(elem) ;
	_tmp271 = *(_tmp270 + 12) ;
	PushParam elem ;
	_tmp272 = ACall _tmp271 ;
	PopParams 4 ;
	Return _tmp272 ;
	Goto _L36 ;
_L35:
	_tmp273 = 0 ;
	Return _tmp273 ;
_L36:
	EndFunc ;
VTable SparseMatrix =
	_SparseMatrix.Init,
	_SparseMatrix.Set,
	_SparseMatrix.Get,
	_Matrix.PrintMatrix,
	_Matrix.SeedMatrix,
	_SparseMatrix.Find,
; 
main:
	BeginFunc 84 () ;
	_tmp274 = "Dense Rep \n" ;
	PushParam _tmp274 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp275 = 8 ;
	PushParam _tmp275 ;
	_tmp276 = LCall _Alloc ;
	PopParams 4 ;
	_tmp277 = DenseMatrix ;
	*(_tmp276) = _tmp277 ;
	m = _tmp276 ;
	_tmp278 = *(m) ;
	_tmp279 = *(_tmp278) ;
	PushParam m ;
	ACall _tmp279 ;
	PopParams 4 ;
	_tmp280 = *(m) ;
	_tmp281 = *(_tmp280 + 16) ;
	PushParam m ;
	ACall _tmp281 ;
	PopParams 4 ;
	_tmp282 = *(m) ;
	_tmp283 = *(_tmp282 + 12) ;
	PushParam m ;
	ACall _tmp283 ;
	PopParams 4 ;
	_tmp284 = "Sparse Rep \n" ;
	PushParam _tmp284 ;
	LCall _PrintString ;
	PopParams 4 ;
	_tmp285 = 8 ;
	PushParam _tmp285 ;
	_tmp286 = LCall _Alloc ;
	PopParams 4 ;
	_tmp287 = SparseMatrix ;
	*(_tmp286) = _tmp287 ;
	m = _tmp286 ;
	_tmp288 = *(m) ;
	_tmp289 = *(_tmp288) ;
	PushParam m ;
	ACall _tmp289 ;
	PopParams 4 ;
	_tmp290 = *(m) ;
	_tmp291 = *(_tmp290 + 16) ;
	PushParam m ;
	ACall _tmp291 ;
	PopParams 4 ;
	_tmp292 = *(m) ;
	_tmp293 = *(_tmp292 + 12) ;
	PushParam m ;
	ACall _tmp293 ;
	PopParams 4 ;
	EndFunc ;
