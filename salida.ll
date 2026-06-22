; ModuleID = "neurolang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = constant [4 x i8] c"%s\0a\00"
define i32 @"main"()
{
entry:
  %"C3" = alloca double
  store double              0x0, double* %"C3"
  %"C4" = alloca double
  store double              0x0, double* %"C4"
  %"F3" = alloca double
  store double              0x0, double* %"F3"
  %"F4" = alloca double
  store double              0x0, double* %"F4"
  %"C3_val" = load double, double* %"C3"
  %"cond" = fcmp ogt double %"C3_val", 0x3feccccccccccccd
  br i1 %"cond", label %"cuando_si", label %"cuando_fin"
cuando_si:
  %"sptr" = getelementptr [2 x i8], [2 x i8]* @"str_0", i32 0, i32 0
  %"fptr" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"fptr", i8* %"sptr")
  br label %"cuando_fin"
cuando_fin:
  %"C3_val.1" = load double, double* %"C3"
  %"cond.1" = fcmp ogt double %"C3_val.1", 0x3fe999999999999a
  br i1 %"cond.1", label %"cuando_si.1", label %"cuando_fin.1"
cuando_si.1:
  %"sptr.1" = getelementptr [2 x i8], [2 x i8]* @"str_1", i32 0, i32 0
  %"fptr.1" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %"fptr.1", i8* %"sptr.1")
  br label %"cuando_fin.1"
cuando_fin.1:
  %"C3_val.2" = load double, double* %"C3"
  %"cond.2" = fcmp ogt double %"C3_val.2", 0x3fe3333333333333
  br i1 %"cond.2", label %"cuando_si.2", label %"cuando_fin.2"
cuando_si.2:
  %"sptr.2" = getelementptr [2 x i8], [2 x i8]* @"str_2", i32 0, i32 0
  %"fptr.2" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %"fptr.2", i8* %"sptr.2")
  br label %"cuando_fin.2"
cuando_fin.2:
  %"C3_val.3" = load double, double* %"C3"
  %"cond.3" = fcmp ogt double %"C3_val.3", 0x3fd999999999999a
  br i1 %"cond.3", label %"cuando_si.3", label %"cuando_fin.3"
cuando_si.3:
  %"sptr.3" = getelementptr [2 x i8], [2 x i8]* @"str_3", i32 0, i32 0
  %"fptr.3" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".16" = call i32 (i8*, ...) @"printf"(i8* %"fptr.3", i8* %"sptr.3")
  br label %"cuando_fin.3"
cuando_fin.3:
  %"C4_val" = load double, double* %"C4"
  %"cond.4" = fcmp ogt double %"C4_val", 0x3feccccccccccccd
  br i1 %"cond.4", label %"cuando_si.4", label %"cuando_fin.4"
cuando_si.4:
  %"sptr.4" = getelementptr [2 x i8], [2 x i8]* @"str_4", i32 0, i32 0
  %"fptr.4" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %"fptr.4", i8* %"sptr.4")
  br label %"cuando_fin.4"
cuando_fin.4:
  %"C4_val.1" = load double, double* %"C4"
  %"cond.5" = fcmp ogt double %"C4_val.1", 0x3fe999999999999a
  br i1 %"cond.5", label %"cuando_si.5", label %"cuando_fin.5"
cuando_si.5:
  %"sptr.5" = getelementptr [2 x i8], [2 x i8]* @"str_5", i32 0, i32 0
  %"fptr.5" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".22" = call i32 (i8*, ...) @"printf"(i8* %"fptr.5", i8* %"sptr.5")
  br label %"cuando_fin.5"
cuando_fin.5:
  %"C4_val.2" = load double, double* %"C4"
  %"cond.6" = fcmp ogt double %"C4_val.2", 0x3fe3333333333333
  br i1 %"cond.6", label %"cuando_si.6", label %"cuando_fin.6"
cuando_si.6:
  %"sptr.6" = getelementptr [2 x i8], [2 x i8]* @"str_6", i32 0, i32 0
  %"fptr.6" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".25" = call i32 (i8*, ...) @"printf"(i8* %"fptr.6", i8* %"sptr.6")
  br label %"cuando_fin.6"
cuando_fin.6:
  %"C4_val.3" = load double, double* %"C4"
  %"cond.7" = fcmp ogt double %"C4_val.3", 0x3fd999999999999a
  br i1 %"cond.7", label %"cuando_si.7", label %"cuando_fin.7"
cuando_si.7:
  %"sptr.7" = getelementptr [2 x i8], [2 x i8]* @"str_7", i32 0, i32 0
  %"fptr.7" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".28" = call i32 (i8*, ...) @"printf"(i8* %"fptr.7", i8* %"sptr.7")
  br label %"cuando_fin.7"
cuando_fin.7:
  %"F3_val" = load double, double* %"F3"
  %"cond.8" = fcmp ogt double %"F3_val", 0x3feccccccccccccd
  br i1 %"cond.8", label %"cuando_si.8", label %"cuando_fin.8"
cuando_si.8:
  %"sptr.8" = getelementptr [2 x i8], [2 x i8]* @"str_8", i32 0, i32 0
  %"fptr.8" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".31" = call i32 (i8*, ...) @"printf"(i8* %"fptr.8", i8* %"sptr.8")
  br label %"cuando_fin.8"
cuando_fin.8:
  %"F3_val.1" = load double, double* %"F3"
  %"cond.9" = fcmp ogt double %"F3_val.1", 0x3fe999999999999a
  br i1 %"cond.9", label %"cuando_si.9", label %"cuando_fin.9"
cuando_si.9:
  %"sptr.9" = getelementptr [2 x i8], [2 x i8]* @"str_9", i32 0, i32 0
  %"fptr.9" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".34" = call i32 (i8*, ...) @"printf"(i8* %"fptr.9", i8* %"sptr.9")
  br label %"cuando_fin.9"
cuando_fin.9:
  %"F3_val.2" = load double, double* %"F3"
  %"cond.10" = fcmp ogt double %"F3_val.2", 0x3fe3333333333333
  br i1 %"cond.10", label %"cuando_si.10", label %"cuando_fin.10"
cuando_si.10:
  %"sptr.10" = getelementptr [2 x i8], [2 x i8]* @"str_10", i32 0, i32 0
  %"fptr.10" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".37" = call i32 (i8*, ...) @"printf"(i8* %"fptr.10", i8* %"sptr.10")
  br label %"cuando_fin.10"
cuando_fin.10:
  %"F3_val.3" = load double, double* %"F3"
  %"cond.11" = fcmp ogt double %"F3_val.3", 0x3fd999999999999a
  br i1 %"cond.11", label %"cuando_si.11", label %"cuando_fin.11"
cuando_si.11:
  %"sptr.11" = getelementptr [2 x i8], [2 x i8]* @"str_11", i32 0, i32 0
  %"fptr.11" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".40" = call i32 (i8*, ...) @"printf"(i8* %"fptr.11", i8* %"sptr.11")
  br label %"cuando_fin.11"
cuando_fin.11:
  %"F4_val" = load double, double* %"F4"
  %"cond.12" = fcmp ogt double %"F4_val", 0x3feccccccccccccd
  br i1 %"cond.12", label %"cuando_si.12", label %"cuando_fin.12"
cuando_si.12:
  %"sptr.12" = getelementptr [2 x i8], [2 x i8]* @"str_12", i32 0, i32 0
  %"fptr.12" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".43" = call i32 (i8*, ...) @"printf"(i8* %"fptr.12", i8* %"sptr.12")
  br label %"cuando_fin.12"
cuando_fin.12:
  %"F4_val.1" = load double, double* %"F4"
  %"cond.13" = fcmp ogt double %"F4_val.1", 0x3fe999999999999a
  br i1 %"cond.13", label %"cuando_si.13", label %"cuando_fin.13"
cuando_si.13:
  %"sptr.13" = getelementptr [2 x i8], [2 x i8]* @"str_13", i32 0, i32 0
  %"fptr.13" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".46" = call i32 (i8*, ...) @"printf"(i8* %"fptr.13", i8* %"sptr.13")
  br label %"cuando_fin.13"
cuando_fin.13:
  %"F4_val.2" = load double, double* %"F4"
  %"cond.14" = fcmp ogt double %"F4_val.2", 0x3fe3333333333333
  br i1 %"cond.14", label %"cuando_si.14", label %"cuando_fin.14"
cuando_si.14:
  %"sptr.14" = getelementptr [2 x i8], [2 x i8]* @"str_14", i32 0, i32 0
  %"fptr.14" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".49" = call i32 (i8*, ...) @"printf"(i8* %"fptr.14", i8* %"sptr.14")
  br label %"cuando_fin.14"
cuando_fin.14:
  %"F4_val.3" = load double, double* %"F4"
  %"cond.15" = fcmp ogt double %"F4_val.3", 0x3fd999999999999a
  br i1 %"cond.15", label %"cuando_si.15", label %"cuando_fin.15"
cuando_si.15:
  %"sptr.15" = getelementptr [2 x i8], [2 x i8]* @"str_15", i32 0, i32 0
  %"fptr.15" = getelementptr [4 x i8], [4 x i8]* @"fmt", i32 0, i32 0
  %".52" = call i32 (i8*, ...) @"printf"(i8* %"fptr.15", i8* %"sptr.15")
  br label %"cuando_fin.15"
cuando_fin.15:
  ret i32 0
}

@"str_0" = constant [2 x i8] c"A\00"
@"str_1" = constant [2 x i8] c"B\00"
@"str_2" = constant [2 x i8] c"C\00"
@"str_3" = constant [2 x i8] c"D\00"
@"str_4" = constant [2 x i8] c"E\00"
@"str_5" = constant [2 x i8] c"F\00"
@"str_6" = constant [2 x i8] c"G\00"
@"str_7" = constant [2 x i8] c"H\00"
@"str_8" = constant [2 x i8] c"1\00"
@"str_9" = constant [2 x i8] c"2\00"
@"str_10" = constant [2 x i8] c"3\00"
@"str_11" = constant [2 x i8] c"4\00"
@"str_12" = constant [2 x i8] c"5\00"
@"str_13" = constant [2 x i8] c"6\00"
@"str_14" = constant [2 x i8] c"7\00"
@"str_15" = constant [2 x i8] c"8\00"