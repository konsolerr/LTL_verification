grammar ltlGrammar;

BoolConst : 'TRUE' | 'FALSE' ;

fragment ValidNameSymbol : [a-z0-9_] ;
fragment Letter : [a-z] ;
ID : Letter ValidNameSymbol*;


formula : '(' formula ')' # Brackets
    | ID                  # Prop
    | BoolConst           # Bool
    | formula '&&' formula # And
    | formula '||' formula # Or
    | '!' formula         # Not
    | 'X' formula         # Next
    | 'F' formula         # Future
    | 'G' formula         # Global
    | formula 'U' formula # Until
    | formula 'R' formula # Release
    ;

WS : [ \t\u000C\r\n]+ -> skip ;