import lexer_rules_v2
import parser_rules_v2
from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules_v2)
parser = yacc(module=parser_rules_v2)
text = """
{
# un comentario
if (  (NOT true) OR false ){
1+2; 3    *4; #holaaa
  {
  111;}
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

{
# digo 3
3;
}
for (; true; 5           ) {6        ;}

do { 1+2+2; } while (NOT true);
}
#un vector
[true, false, true   ][0] OR true;
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
