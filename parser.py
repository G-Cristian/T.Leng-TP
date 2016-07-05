import lexer_rules_v2
import parser_rules_v2
from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules_v2)
parser = yacc(module=parser_rules_v2)
text = """
#comment inicial
if (1<2) {
# un comentario
if (  (NOT true) OR false ){
1+2; 3    *4; #holaaa
}
else
{ 0; }
if ( true )
              1;
              "hola" + " mundo";


1;
true AND (  false OR     true);
#otro comentario

while ( 1 < (2 + 3)   )

#comentario dentro del while
3;
# digo 3
while ( 5 == 2   ) {
3; "un string";
}
for (; true; 5           ) {6        ;}
for (; true; 5           ) 6 ;
do { 1+2+2; } while (NOT true);
do 1; while(true);
}1;
#un vector
[true, false, true   ][0] OR true;

#un vector de vectores
[[true,false], [false], [true,false]   ][2][1] OR true;

#esto tiene que funcionar (primero hace las sumas, despues las comparaciones y despues el or)
if(2+3<4 OR 3>5+4)
2+3;

#pero esto no tiene que funcionar
#if(2+(3<4) OR 3>5+4)
#2+3;

#y esto tampoco tiene que funcionar
#if(2+3<4 OR (3>5)+4)
#2+3;

2+[[1,2],[[2][0]*1]][6/[6][0]][0]*3;

++3;

++[3][0];

[3][0]++;

a=3;
#b=a+3;

"""

"""#comentarios iniciales #probando comentario dentro de comentario

#otra linea de comentario inicial
1++;
#Nueva lines #mas comentario en misma linea
2+3;     #comentario misma linea
3+4; #comentario mimsa linea


#comentario otra linea

4+2;
#comentario otra linea

"""
ast = parser.parse(text, lexer)
print (ast.evaluate(0,0))
