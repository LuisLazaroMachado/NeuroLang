channel C3 : eeg;
channel C4 : emg;
channel F3 : eog;
channel F4 : eeg;

threshold altisimo : 0.90;
threshold alto     : 0.80;
threshold medio    : 0.60;
threshold bajo     : 0.40;

when signal(C3) > altisimo { output("A"); }
when signal(C3) > alto     { output("B"); }
when signal(C3) > medio    { output("C"); }
when signal(C3) > bajo     { output("D"); }

when signal(C4) > altisimo { output("E"); }
when signal(C4) > alto     { output("F"); }
when signal(C4) > medio    { output("G"); }
when signal(C4) > bajo     { output("H"); }

when signal(F3) > altisimo { output("1"); }
when signal(F3) > alto     { output("2"); }
when signal(F3) > medio    { output("3"); }
when signal(F3) > bajo     { output("4"); }

when signal(F4) > altisimo { output("5"); }
when signal(F4) > alto     { output("6"); }
when signal(F4) > medio    { output("7"); }
when signal(F4) > bajo     { output("8"); }
