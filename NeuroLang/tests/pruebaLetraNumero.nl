channel C3 : eeg;
channel C4 : eeg;

threshold alto  : 0.80;
threshold medio : 0.60;
threshold bajo  : 0.40;

when signal(C3) > alto  { output("A"); }
when signal(C3) > medio { output("B"); }
when signal(C3) > bajo  { output("C"); }

when signal(C4) > alto  { output("1"); }
when signal(C4) > medio { output("2"); }
when signal(C4) > bajo  { output("3"); }
