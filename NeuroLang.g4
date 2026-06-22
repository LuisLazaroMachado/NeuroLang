grammar NeuroLang;

// ========== REGLAS DEL PARSER ==========

// ---------- PUNTO DE ENTRADA
program : statement* EOF ;

// ---------- SENTENCIAS
statement
    : channelDecl
    | thresholdDecl
    | whenStmt
    ;

// ---------- DECLARACIÓN DE CANAL
// Ejemplos válidos:
//   channel C3 : eeg;
//   channel C4 : emg;
channelDecl : CHANNEL ID COLON signalType SEMI ;

// ---------- DECLARACIÓN DE UMBRAL
// Ejemplos válidos:
//   threshold alto : 0.80;
//   threshold bajo : 0.40;
thresholdDecl : THRESHOLD ID COLON NUMBER SEMI ;

// ---------- SENTENCIA WHEN
// Ejemplo válido:
//   when signal(C3) > alto { output("A"); }
whenStmt : WHEN signal RELOP expression LBRACE outputStmt* RBRACE ;

// ---------- SALIDA
// Ejemplo válido:
//   output("A");
outputStmt : OUTPUT LPAREN STRING_LIT RPAREN SEMI ;

// ---------- SEÑAL
// Ejemplo válido:
//   signal(C3)
signal : SIGNAL LPAREN ID RPAREN ;

// ---------- EXPRESIÓN
expression : NUMBER | ID ;

// ---------- TIPOS DE SEÑAL
signalType : EEG | EMG | EOG ;

// ========== REGLAS DEL LEXER ==========

// ---------- PALABRAS CLAVE
CHANNEL   : 'channel'   ;
THRESHOLD : 'threshold' ;
WHEN      : 'when'      ;
OUTPUT    : 'output'    ;
SIGNAL    : 'signal'    ;

// ---------- TIPOS DE SEÑAL
EEG : 'eeg' ;
EMG : 'emg' ;
EOG : 'eog' ;

// ---------- OPERADORES
RELOP : '>' | '<' | '>=' | '<=' | '==' | '!=' ;

// ---------- DELIMITADORES
COLON  : ':' ;
SEMI   : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;

// ---------- LITERALES
NUMBER     : [0-9]+ ('.' [0-9]+)? ;
STRING_LIT : '"' ~["\r\n]* '"' ;
ID         : [a-zA-Z_][a-zA-Z_0-9]* ;

// ---------- ESPACIOS (ignorados)
WS : [ \t\r\n]+ -> skip ;
