channel C3 : eeg;

threshold alto  : 0.80;
threshold medio : 0.60;
threshold bajo  : 0.40;

when signal(C3) > alto  { output("A"); }
when signal(C3) > medio { output("B"); }
when signal(C3) > bajo  { output("C"); }
