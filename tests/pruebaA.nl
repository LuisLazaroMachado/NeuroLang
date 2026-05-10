channel C3 : eeg;
threshold alto : 0.80;
when signal(C3) > alto { output("A"); }
