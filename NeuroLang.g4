grammar NeuroLang;

program : statement* EOF ;

statement
    : channelDecl
    | thresholdDecl
    | whenStmt
    ;

channelDecl : CHANNEL ID COLON signalType SEMI ;
thresholdDecl : THRESHOLD ID COLON NUMBER SEMI ;
whenStmt : WHEN signal RELOP expression LBRACE outputStmt* RBRACE ;
outputStmt : OUTPUT LPAREN STRING_LIT RPAREN SEMI ;
signal : SIGNAL LPAREN ID RPAREN ;
expression : NUMBER | ID ;
signalType : EEG | EMG | EOG ;

CHANNEL   : 'channel'   ;
THRESHOLD : 'threshold' ;
WHEN      : 'when'      ;
OUTPUT    : 'output'    ;
SIGNAL    : 'signal'    ;
EEG : 'eeg' ;
EMG : 'emg' ;
EOG : 'eog' ;

RELOP      : '>' | '<' | '>=' | '<=' | '==' | '!=' ;
COLON      : ':' ;
SEMI       : ';' ;
LPAREN     : '(' ;
RPAREN     : ')' ;
LBRACE     : '{' ;
RBRACE     : '}' ;
NUMBER     : [0-9]+ ('.' [0-9]+)? ;
STRING_LIT : '"' ~["\r\n]* '"' ;
ID         : [a-zA-Z_][a-zA-Z_0-9]* ;
WS         : [ \t\r\n]+ -> skip ;
