C3 = 0.0
C4 = 0.0
F3 = 0.0
F4 = 0.0
altisimo = 0.90
alto = 0.80
medio = 0.60
bajo = 0.40
t1 = C3 > altisimo
if t1 goto L0_si else goto L0_fin
L0_si:
  output("A")
  goto L0_fin
L0_fin:
t2 = C3 > alto
if t2 goto L1_si else goto L1_fin
L1_si:
  output("B")
  goto L1_fin
L1_fin:
t3 = C3 > medio
if t3 goto L2_si else goto L2_fin
L2_si:
  output("C")
  goto L2_fin
L2_fin:
t4 = C3 > bajo
if t4 goto L3_si else goto L3_fin
L3_si:
  output("D")
  goto L3_fin
L3_fin:
t5 = C4 > altisimo
if t5 goto L4_si else goto L4_fin
L4_si:
  output("E")
  goto L4_fin
L4_fin:
t6 = C4 > alto
if t6 goto L5_si else goto L5_fin
L5_si:
  output("F")
  goto L5_fin
L5_fin:
t7 = C4 > medio
if t7 goto L6_si else goto L6_fin
L6_si:
  output("G")
  goto L6_fin
L6_fin:
t8 = C4 > bajo
if t8 goto L7_si else goto L7_fin
L7_si:
  output("H")
  goto L7_fin
L7_fin:
t9 = F3 > altisimo
if t9 goto L8_si else goto L8_fin
L8_si:
  output("1")
  goto L8_fin
L8_fin:
t10 = F3 > alto
if t10 goto L9_si else goto L9_fin
L9_si:
  output("2")
  goto L9_fin
L9_fin:
t11 = F3 > medio
if t11 goto L10_si else goto L10_fin
L10_si:
  output("3")
  goto L10_fin
L10_fin:
t12 = F3 > bajo
if t12 goto L11_si else goto L11_fin
L11_si:
  output("4")
  goto L11_fin
L11_fin:
t13 = F4 > altisimo
if t13 goto L12_si else goto L12_fin
L12_si:
  output("5")
  goto L12_fin
L12_fin:
t14 = F4 > alto
if t14 goto L13_si else goto L13_fin
L13_si:
  output("6")
  goto L13_fin
L13_fin:
t15 = F4 > medio
if t15 goto L14_si else goto L14_fin
L14_si:
  output("7")
  goto L14_fin
L14_fin:
t16 = F4 > bajo
if t16 goto L15_si else goto L15_fin
L15_si:
  output("8")
  goto L15_fin
L15_fin: