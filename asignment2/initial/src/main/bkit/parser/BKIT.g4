grammar BKIT;
// 1720031
@lexer::header {
1720031
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : glovardeclprt? funcdeclprt EOF ;

glovardeclprt : vardecl+ ;

vardecl : VAR COLON varlist SEMI ;

varlist : vari (COMMA vari)* ;

vari : vari_array|vari_scalar ;

vari_array : ID indexop+ (ASSIGN lit)? ;

vari_scalar : ID (ASSIGN lit)? ;

indexop : LS INTLIT RS ;

lit : INTLIT|FLOATLIT|BOOLLIT ;

funcdeclprt : funcdecl* ;

funcdecl : FUNCTION COLON ID (parafun)? bodyfun ;

parafun : PARA COLON paralist ;

paralist : para (COMMA para)* ;

para : vari ;

//localvar : ID | ID LS INTLIT RS (LS INTLIT RS)? ; //30052020 remove line due to parameter is same as variable decl

bodyfun : BODY COLON nulstmtlst ENDBODY DOT ;

stmttype : asstmt|ifstmt|forstmt|whilestmt|dowhistmt|breakstmt|contstmt|callstmt|returnstmt ;

nulstmtlst : varstmt* stmttype*   ;

varstmt : vardecl ;

asstmt : value ASSIGN exp SEMI ;

value : ID (LS exp RS)* ; //mang hoac id, mang index = bieu thuc 30.05.2020

//ifstmt : IF exp THEN stmtlst (ELSEIF exp THEN stmtlst)* (ELSE stmtlst)? ENDIF DOT ;

ifthenStmt: IF exp THEN stmtlst (ELSEIF exp THEN stmtlst)* ;

elseStmt: (ELSE stmtlst)? ENDIF DOT ;

ifstmt: ifthenStmt elseStmt ;

stmtlst : varstmt* stmttype+ |  varstmt+ stmttype* ;

forstmt : FOR LB scava ASSIGN inex COMMA conExp COMMA scava ASSIGN upex RB DO stmtlst ENDFOR DOT ;

scava : ID ;

inex : exp ;

//number :  ([1-9][0-9]*) | '0' ;

//conExp : ID (LESS|GREAT|LEEQ|GREQ) number ;

//conExp : ID (LESS|GREAT|LEEQ|GREQ) INTLIT ;   //30.05.2020 revise number to INLIT

conExp: exp ;  //30.05.2020

upex : exp ;

whilestmt : WHILE exp DO stmtlst ENDWHILE DOT ;

dowhistmt : DO stmtlst WHILE exp SEMI ;

breakstmt : BREAK SEMI ;

contstmt : CONTINUE SEMI ;

callstmt : ID LB bet? RB SEMI ; //call stmt

bet : exp (COMMA exp)* ;

returnstmt : RETURN exp? SEMI ;

CMT: '**' .*? '**' -> skip ;

ID: [a-z][a-zA-Z_0-9]* ;

COMMA: ',' ;

SEMI: ';' ;

COLON: ':' ;

DOT: '.' ;

ASSIGN : '=' ;

VAR: 'Var' ;

FUNCTION : 'Function' ;

PARA : 'Parameter' ;

BODY : 'Body' ;

ENDBODY : 'EndBody' ;

BREAK : 'Break' ;

CONTINUE : 'Continue' ;

DO: 'Do' ;

ELSE: 'Else' ;

ELSEIF : 'ElseIf' ;

ENDIF : 'EndIf' ;

ENDFOR : 'EndFor' ;

ENDWHILE : 'EndWhile' ;

FOR : 'For' ;

IF: 'If' ;

RETURN : 'Return' ;

THEN : 'Then' ;

WHILE: 'While' ;

//TRUE : 'True' ; //remove this line 30.05.2020 b/c BOOLLIT already defined

//FALSE : 'False' ; //remove this line 30.05.2020 b/c BOOLLIT already defined

IADD : '+' ;

FADD : '+.' ;

ISUB: '-';

FSUB : '-.' ;

IMUL: '*';

FMUL : '*.' ;

IDIV : '\\' ;

FDIV: '/';

IREM : '%' ;

NEG : '!' ;

CONJ : '&&' ;

DISJ : '||' ;

EQ : '==' ;

NOEQ : '!=' ;

LESS : '<' ;

GREAT : '>' ;

LEEQ : '<=' ;

GREQ : '>=' ;

NOEQF: '=/=' ;

LEF : '<.' ;

GRF : '>.' ;

LEQF : '<=.' ;

GEQF : '>=.' ;

LS: '[';

RS: ']';

LB: '(' ;

RB: ')' ;

fragment Dec: '0' |[1-9]+[0-9]* ;
fragment Hex: '0' ('x'|'X') [0-9A-F]+ ;
fragment Oct: '0' ('o'|'O') [0-7]+ ;
INTLIT : (Dec|Hex|Oct)+ ;


fragment Intprt : [0-9]+ ;
fragment Deciprt : '.' [0-9]* ;
fragment Exprt : [Ee] [+-]? [0-9]+ ;
FLOATLIT: Intprt Deciprt? Exprt | Intprt Deciprt Exprt? ; //add

BOOLLIT: 'True'|'False';

fragment StringCharacter: ~["\\\r\n] | EscapeSequence;
fragment StringCharacters: StringCharacter+;
fragment EscapeSequence: '\\' [btnfr"'\\];
STRINGLIT: '"' StringCharacters? '"';

//index : LS exp RS | LS exp RS index ;

exp : exp (EQ|NOEQ|LESS|GREAT|LEEQ|GREQ|NOEQF|LEF|GRF|LEQF|GEQF) exp1 | exp1 ;
exp1 : exp1 (CONJ|DISJ) exp2|exp2 ;
exp2 : exp2 (IADD|FADD|ISUB|FSUB) exp3|exp3 ;
exp3 : exp3 (IMUL|FMUL|IDIV|FDIV|IREM) exp4|exp4 ;
exp4 : NEG exp5 | exp5 ;
exp5 : (ISUB|FSUB) exp6 | exp6 ;
exp6 : value | LB exp RB| funccall | INTLIT|FLOATLIT| STRINGLIT | BOOLLIT ; //30.05.2020 - add variable array and fix ( exp )

funccall : ID LB explist? RB ; //callexpr
explist : exp COMMA explist | exp ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

INTTYPE: 'int' ;

BOOLEANTYPE: 'boolean';

STRINGTYPE: 'string';

ARRAYTYPE: 'array';


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
