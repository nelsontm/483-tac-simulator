/* File: codegen.cc
 * ----------------
 * Implementation for the CodeGenerator class. The methods don't do anything
 * too fancy, mostly just create objects of the various Tac instruction
 * classes and append them to the list.
 */

#include "codegen.h"
#include <string.h>
#include "tac.h"
#include "mips.h"
#include "ast_decl.h"
#include "errors.h"
  
CodeGenerator::CodeGenerator()
{
  code = new List<Instruction*>();
  curGlobalOffset = 0;
}

char *CodeGenerator::NewLabel()
{
  static int nextLabelNum = 0;
  char temp[10];
  sprintf(temp, "_L%d", nextLabelNum++);
  return strdup(temp);
}


Location *CodeGenerator::GenTempVar()
{
  static int nextTempNum;
  char temp[10];
  Location *result = NULL;
  sprintf(temp, "_tmp%d", nextTempNum++);
  return GenLocalVariable(temp);
}


Location *CodeGenerator::GenLocalVariable(const char *varName)
{            
    curStackOffset -= VarSize;
    return new Location(fpRelative, curStackOffset+4,  varName);
}

Location *CodeGenerator::GenGlobalVariable(const char *varName)
{
    curGlobalOffset += VarSize;
    return new Location(gpRelative, curGlobalOffset -4, varName);
}
 

Location *CodeGenerator::GenLoadConstant(int value)
{
  Location *result = GenTempVar();
  code->Append(new LoadConstant(result, value));
  return result;
}

Location *CodeGenerator::GenLoadConstant(const char *s)
{
  Location *result = GenTempVar();
  code->Append(new LoadStringConstant(result, s));
  return result;
} 

Location *CodeGenerator::GenLoadLabel(const char *label)
{
  Location *result = GenTempVar();
  code->Append(new LoadLabel(result, label));
  return result;
} 


void CodeGenerator::GenAssign(Location *dst, Location *src)
{
  code->Append(new Assign(dst, src));
}


Location *CodeGenerator::GenLoad(Location *ref, int offset)
{
  Location *result = GenTempVar();
  code->Append(new Load(result, ref, offset));
  return result;
}

void CodeGenerator::GenStore(Location *dst,Location *src, int offset)
{
  code->Append(new Store(dst, src, offset));
}


Location *CodeGenerator::GenBinaryOp(const char *opName, Location *op1,
						     Location *op2)
{
  Location *result = GenTempVar();
  code->Append(new BinaryOp(BinaryOp::OpCodeForName(opName), result, op1, op2));
  return result;
}


void CodeGenerator::GenLabel(const char *label)
{
  code->Append(new Label(label));
}

void CodeGenerator::GenIfZ(Location *test, const char *label)
{
  code->Append(new IfZ(test, label));
}

void CodeGenerator::GenGoto(const char *label)
{
  code->Append(new Goto(label));
}

void CodeGenerator::GenReturn(Location *val)
{
  code->Append(new Return(val));
}


BeginFunc *CodeGenerator::GenBeginFunc(FnDecl *fn)
{
  BeginFunc *result = new BeginFunc;
  code->Append(insideFn = result);
  List<VarDecl*> *formals = fn->GetFormals();
  if(fn->IsMethodDecl()){
    if(formals->NumElements() == 0) result->formList = "(this";
    else result->formList = "(this, ";
  }
  else result->formList = "(";
  int start = OffsetToFirstParam;
  if (fn->IsMethodDecl()) start += VarSize;
  for (int i = 0; i < formals->NumElements(); i++){
    formals->Nth(i)->rtLoc = new Location(fpRelative, i*VarSize + start, formals->Nth(i)->GetName());
    result->formList.append(formals->Nth(i)->GetName());
    if(i!=formals->NumElements()-1) result->formList.append(", ");
  }
  result->formList.append(")");
  curStackOffset = OffsetToFirstLocal;
  return result;
}

void CodeGenerator::GenEndFunc()
{
  code->Append(new EndFunc());
  insideFn->SetFrameSize(OffsetToFirstLocal-curStackOffset);
  insideFn = NULL;
}

void CodeGenerator::GenPushParam(Location *param)
{
  code->Append(new PushParam(param));
}

void CodeGenerator::GenPopParams(int numBytesOfParams)
{
  Assert(numBytesOfParams >= 0 && numBytesOfParams % VarSize == 0); // sanity check
  if (numBytesOfParams > 0)
    code->Append(new PopParams(numBytesOfParams));
}

Location *CodeGenerator::GenLCall(const char *label, bool fnHasReturnValue)
{
  Location *result = fnHasReturnValue ? GenTempVar() : NULL;
  code->Append(new LCall(label, result));
  return result;
}

Location *CodeGenerator::GenFunctionCall(const char *fnLabel, List<Location*> *args, bool hasReturnValue)
{
  for (int i = args->NumElements()-1; i >= 0; i--) // push params right to left
    GenPushParam(args->Nth(i));
  Location *result = GenLCall(fnLabel, hasReturnValue);
  GenPopParams(args->NumElements()*VarSize);
  return result;
}

Location *CodeGenerator::GenACall(Location *fnAddr, bool fnHasReturnValue)
{
  Location *result = fnHasReturnValue ? GenTempVar() : NULL;
  code->Append(new ACall(fnAddr, result));
  return result;
}
 
Location *CodeGenerator::GenMethodCall(Location *rcvr,
			     Location *meth, List<Location*> *args, bool fnHasReturnValue)
{
  for (int i = args->NumElements()-1; i >= 0; i--)
    GenPushParam(args->Nth(i));
  GenPushParam(rcvr);	// hidden "this" parameter
  Location *result= GenACall(meth, fnHasReturnValue);
  GenPopParams((args->NumElements()+1)*VarSize);
  return result;
}


static struct _builtin {
  const char *label;
  int numArgs;
  bool hasReturn;
} builtins[] =
 {{"_Alloc", 1, true},
  {"_ReadLine", 0, true},
  {"_ReadInteger", 0, true},
  {"_StringEqual", 2, true},
  {"_PrintInt", 1, false},
  {"_PrintString", 1, false},
  {"_PrintBool", 1, false},
  {"_Halt", 0, false}};

Location *CodeGenerator::GenBuiltInCall(BuiltIn bn,Location *arg1, Location *arg2)
{
  Assert(bn >= 0 && bn < NumBuiltIns);
  struct _builtin *b = &builtins[bn];
  Location *result = NULL;

  if (b->hasReturn) result = GenTempVar();
                // verify appropriate number of non-NULL arguments given
  Assert((b->numArgs == 0 && !arg1 && !arg2)
	|| (b->numArgs == 1 && arg1 && !arg2)
	|| (b->numArgs == 2 && arg1 && arg2));
  if (arg2) code->Append(new PushParam(arg2));
  if (arg1) code->Append(new PushParam(arg1));
  code->Append(new LCall(b->label, result));
  GenPopParams(VarSize*b->numArgs);
  return result;
}


void CodeGenerator::GenVTable(const char *className, List<const char *> *methodLabels)
{
  code->Append(new VTable(className, methodLabels));
}

void SysCallCodeGen();

void CodeGenerator::DoFinalCodeGen()
{
  LivenessAnalysis();
  if (IsDebugOn("tac")) { // if debug don't translate to mips, just print Tac
    for (int i = 0; i < code->NumElements(); i++)
	code->Nth(i)->Print();
   }  else {
     Mips mips;
     List<Location*> locations;
     for (int i = 0; i < code->NumElements(); ++i) {
         for (int j = 0; j < code->Nth(i)->GetLiveVariables()->NumElements(); ++j)
             locations.Append(code->Nth(i)->GetLiveVariables()->Nth(j));
     }
     locations.Unique();
     mips.AllocateRegisters(&locations);
     mips.EmitPreamble();
     for (int i = 0; i < code->NumElements(); i++)
	 code->Nth(i)->Emit(&mips);
   SysCallCodeGen();
  }
}



Location *CodeGenerator::GenArrayLen(Location *array)
{
  return GenLoad(array, -4);
}

Location *CodeGenerator::GenNew(const char *vTableLabel, int instanceSize)
{
  Location *size = GenLoadConstant(instanceSize);
  Location *result = GenBuiltInCall(Alloc, size);
  Location *vt = GenLoadLabel(vTableLabel);
  GenStore(result, vt);
  return result;
}


Location *CodeGenerator::GenDynamicDispatch(Location *rcvr, int vtableOffset, List<Location*> *args, bool hasReturnValue)
{
  Location *vptr = GenLoad(rcvr); // load vptr
  Assert(vtableOffset >= 0);
  Location *m = GenLoad(vptr, vtableOffset*4);
  return GenMethodCall(rcvr, m, args, hasReturnValue);
}

// all variables (ints, bools, ptrs, arrays) are 4 bytes in for code generation
// so this simplifies the math for offsets
Location *CodeGenerator::GenSubscript(Location *array, Location *index)
{
  Location *zero = GenLoadConstant(0);
  Location *isNegative = GenBinaryOp("<", index, zero);
  Location *count = GenLoad(array, -4);
  Location *isWithinRange = GenBinaryOp("<", index, count);
  Location *pastEnd = GenBinaryOp("==", isWithinRange, zero);
  Location *outOfRange = GenBinaryOp("||", isNegative, pastEnd);
  const char *pastError = NewLabel();
  GenIfZ(outOfRange, pastError);
  GenHaltWithMessage(err_arr_out_of_bounds);
  GenLabel(pastError);
  Location *four = GenLoadConstant(VarSize);
  Location *offset = GenBinaryOp("*", four, index);
  Location *elem = GenBinaryOp("+", array, offset);
  return new Location(elem, 0); 
}



Location *CodeGenerator::GenNewArray(Location *numElems)
{
  Location *one = GenLoadConstant(1);
  Location *isNonpositive = GenBinaryOp("<", numElems, one);
  const char *pastError = NewLabel();
  GenIfZ(isNonpositive, pastError);
  GenHaltWithMessage(err_arr_bad_size);
  GenLabel(pastError);

  // need (numElems+1)*VarSize total bytes (extra 1 is for length)
  Location *arraySize = GenLoadConstant(1);
  Location *num = GenBinaryOp("+", arraySize, numElems);
  Location *four = GenLoadConstant(VarSize);
  Location *bytes = GenBinaryOp("*", num, four);
  Location *result = GenBuiltInCall(Alloc, bytes);
  GenStore(result, numElems);
  return GenBinaryOp("+", result, four);
}

void CodeGenerator::GenHaltWithMessage(const char *message)
{
   Location *msg = GenLoadConstant(message);
   GenBuiltInCall(PrintString, msg);
   GenBuiltInCall(Halt, NULL);
}

void SysCallCodeGen()
{
    printf("  _PrintInt:\n");
    printf("	  subu $sp, $sp, 8	# decrement sp to make space to save ra,fp\n");
    printf("	  sw $fp, 8($sp)	# save fp\n");
    printf("	  sw $ra, 4($sp)	# save ra\n");
    printf("	  addiu $fp, $sp, 8	# set up new fp\n");
    printf("	  lw $a0, 4($fp)	# fill a from $fp+4\n");
    printf("	# LCall _PrintInt\n");
    printf("	  li $v0, 1\n");
    printf("	  syscall\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp		# pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)	# restore saved ra\n");
    printf("	  lw $fp, 0($fp)	# restore saved fp\n");
    printf("	  jr $ra		# return from function\n");
    printf("\n");
    printf("  _ReadInteger:\n");
    printf("	  subu $sp, $sp, 8	# decrement sp to make space to save ra,fp\n");
    printf("	  sw $fp, 8($sp)	# save fp\n");
    printf("	  sw $ra, 4($sp)	# save ra\n");
    printf("	  addiu $fp, $sp, 8	# set up new fp\n");
    printf("	  li $v0, 5\n");
    printf("	  syscall\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp		# pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)	# restore saved ra\n");
    printf("	  lw $fp, 0($fp)	# restore saved fp\n");
    printf("	  jr $ra		# return from function\n");
    printf("\n");
    printf("\n");
    printf("  _PrintBool:\n");
    printf("	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp\n");
    printf("	  sw $fp, 8($sp)        # save fp\n");
    printf("	  sw $ra, 4($sp)        # save ra\n");
    printf("	  addiu $fp, $sp, 8     # set up new fp\n");
    printf("	  lw $a0, 4($fp)        # fill a from $fp+4\n");
    printf("	  li $v0, 4\n");
    printf("	  beq $a0, $0, PrintBoolFalse\n");
    printf("	  la $a0, _PrintBoolTrueString\n");
    printf("	  j PrintBoolEnd\n");
    printf("  PrintBoolFalse:\n");
    printf(" 	  la $a0, _PrintBoolFalseString\n");
    printf("  PrintBoolEnd:\n");
    printf("	  syscall\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp         # pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)       # restore saved ra\n");
    printf("	  lw $fp, 0($fp)        # restore saved fp\n");
    printf("	  jr $ra                # return from function\n");
    printf("\n");
    printf("      .data			# create string constant marked with label\n");
    printf("      _PrintBoolTrueString: .asciiz \"true\"\n");
    printf("      .text\n");
    printf("\n");
    printf("      .data			# create string constant marked with label\n");
    printf("      _PrintBoolFalseString: .asciiz \"false\"\n");
    printf("      .text\n");
    printf("\n");
    printf("  _PrintString:\n");
    printf("	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp\n");
    printf("	  sw $fp, 8($sp)        # save fp\n");
    printf("	  sw $ra, 4($sp)        # save ra\n");
    printf("	  addiu $fp, $sp, 8     # set up new fp\n");
    printf("	  lw $a0, 4($fp)        # fill a from $fp+4\n");
    printf("	  li $v0, 4\n");
    printf("	  syscall\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp         # pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)       # restore saved ra\n");
    printf("	  lw $fp, 0($fp)        # restore saved fp\n");
    printf("	  jr $ra                # return from function\n");
    printf("\n");
    printf("  _Alloc:\n");
    printf("	  subu $sp, $sp, 8      # decrement sp to make space to save ra,fp\n");
    printf("	  sw $fp, 8($sp)        # save fp\n");
    printf("	  sw $ra, 4($sp)        # save ra\n");
    printf("	  addiu $fp, $sp, 8     # set up new fp\n");
    printf("	  lw $a0, 4($fp)        # fill a from $fp+4\n");
    printf("	  li $v0, 9\n");
    printf("	  syscall\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp         # pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)       # restore saved ra\n");
    printf("	  lw $fp, 0($fp)        # restore saved fp\n");
    printf("	  jr $ra                # return from function\n");
    printf("\n");
    printf("  _Halt:\n");
    printf("	  li $v0, 10\n");
    printf("	  syscall\n");
    printf("	# EndFunc\n");
    printf("\n");
    printf("\n");
    printf("  _StringEqual:\n");
    printf("	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp\n");
    printf("	  sw $fp, 8($sp)        # save fp\n");
    printf("	  sw $ra, 4($sp)        # save ra\n");
    printf("	  addiu $fp, $sp, 8     # set up new fp\n");
    printf("	  lw $a0, 4($fp)        # fill a from $fp+4\n");
    printf("	  lw $a1, 8($fp)        # fill a from $fp+8\n");
    printf("	  beq $a0,$a1,Lrunt10\n");
    printf("  Lrunt12:\n");
    printf("	  lbu  $v0,($a0)\n");
    printf("	  lbu  $a2,($a1)\n");
    printf("	  bne $v0,$a2,Lrunt11\n");
    printf("	  addiu $a0,$a0,1\n");
    printf("	  addiu $a1,$a1,1\n");
    printf("	  bne $v0,$0,Lrunt12\n");
    printf("      li  $v0,1\n");
    printf("      j Lrunt10\n");
    printf("  Lrunt11:\n");
    printf("	  li  $v0,0\n");
    printf("  Lrunt10:\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp         # pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)       # restore saved ra\n");
    printf("	  lw $fp, 0($fp)        # restore saved fp\n");
    printf("	  jr $ra                # return from function\n");
    printf("\n");
    printf("\n");
    printf("\n");
    printf("  _ReadLine:\n");
    printf("	  subu $sp, $sp, 8      # decrement sp to make space to save ra, fp\n");
    printf("	  sw $fp, 8($sp)        # save fp\n");
    printf("	  sw $ra, 4($sp)        # save ra\n");
    printf("	  addiu $fp, $sp, 8     # set up new fp\n");
    printf("	  li $a0, 101\n");
    printf("	  li $v0, 9\n");
    printf("	  syscall\n");
    printf("	  addi $a0, $v0, 0\n");
    printf("	  li $v0, 8\n");
    printf("	  li $a1,101 \n");
    printf("	  syscall\n");
    printf("	  addiu $v0,$a0,0       # pointer to begin of string\n");
    printf("  Lrunt21:\n");
    printf("	  lb $a1,($a0)          # load character at pointer\n");
    printf("	  addiu $a0,$a0,1       # forward pointer\n");
    printf("	  bnez $a1,Lrunt21      # loop until end of string is reached\n");
    printf("	  lb $a1,-2($a0)        # load character before end of string\n");
    printf("	  li $a2,10             # newline character");
    printf("	  bneq $a1,$a2,Lrunt20  # do not remove last character if not newline\n");
    printf("	  sb $0,-2($a0)         # Add the terminating character in its place\n");
    printf("  Lrunt20:\n");
    printf("	# EndFunc\n");
    printf("	# (below handles reaching end of fn body with no explicit return)\n");
    printf("	  move $sp, $fp         # pop callee frame off stack\n");
    printf("	  lw $ra, -4($fp)       # restore saved ra\n");
    printf("	  lw $fp, 0($fp)        # restore saved fp\n");
    printf("	  jr $ra                # return from function\n");
}


/*To be implemented.*/
void CodeGenerator::LivenessAnalysis() {

}