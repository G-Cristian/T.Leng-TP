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
b=a+3;

1+ (a=3);

#esto en c++ anda
c = 1+2< 5 ? b=2 : b = 4;
#mas tests con ?:
if(3 < 2)
{
c = 1+2< 5 ?
b=2 :
             b = 4;
 if(3 < 2)

  {
 c = (1+2< 5 ? true : false) ? 2<3 ?
               b =3 :
               5+4 : 2>3 ? 3 : b =2;
 #En cambio lo siguiente no funciona por la forma en que asocia.
 #c = 1+2< 5 ? true : false ? 2<3 ?
 #              b =3 :
 #              5+4 : 2>3 ? 3 : b =2;
 #Notar que en c++ anda pero porque devuelve true y lo transforma en int.
 #En nuestro caso no funciona porque pedi que los tipos devueltos sean del mismo tipo.
 #Esto lo hice asi porque de otra forma no se que tipo tiene que tener la expresion.

a = 3+c+a+2;

}
}
vec0 = [1,2];

vec1 = [[2],[3]];
#esto no tiene que andar
#a = 2+vec1[1];
vec1 = [1,2];
vec1[0] = 2;
a = 2+vec1[1];
vec2 = [[[1]],[[2,3]]];
vec2[2] = [[2]];
vec3 = vec2;
#no tiene que andar porque el vector es de tipo vector de vector y no de tipo numerico
#vec3[0] = [1];
vec3[0] = [[1]];
vec4[5] = [[2]];
#esto no tiene que andar
#vec4[0] = 1;
vec4[0] = [[1]];
#esto no tiene que andar porque vec5 no esta definido
#entonces no puede obtener la posicion 1 del algo no definido
#vec5[0][1] = 1;
vec5 = [[2]];
vec5[0][0] = 1;
vec5[0] = [1];

vec6 = [[[3]]];
vec6[0][0]=[1];
vec2=1;
#No tiene que andarr ya que vec2 ahora es de tipo numerico
#vec2[0] = 2;

#los siguientes tres no deben andar
#vec7 = [h, 1];
#vec7 = [1,h];
#vec7 = [h];

#sin tercer parametro
multiplicacionEscalar([2], 3);
multiplicacionEscalar([2], 3, false);#con tercer parametro

#no tiene que andar
#multiplicacionEscalar([[2]], 3);

#no tiene que andar
#multiplicacionEscalar(vec6, 3);

#si tiene que andar
multiplicacionEscalar(vec6[0][0], 3);

print(3+length(multiplicacionEscalar(multiplicacionEscalar(vec5[0], 2),3,true))*8);
if (colineales([2,3], multiplicacionEscalar([2],3)))
#son colinealeas
print("colinneales");
else
#no son colineales
#asi que imprimo false
print(false);

if(true) a=3;
else if (a==3) b=4;
else c=5;

if(a=true) while(2<3) print("hola");
else while(3<2) print ("chau");
if(a=true) colineales([2],[3]); 
else do
{colineales([3],[3]);
print (a);
}while(true);

a=2;
a-=3;

a=true;
b=false;
2<3? a : a ;
vector[0] = 3;
a = 3 + (vectorLibre[0]=3);
a = a-a;
a += 3;
#esto no
#3+=3;
#esto tampoco
#vectorNuevo[0] += 2;
vec8[2] = [1];
vec8[2][2] += 2;

a="hola";
b = "b";
a+=b;
a+="c";

#tiene que fallar
#a-="a";

a = 4;
a-=a;
a+=a;

a = {
hola : 5, chau:6};
a.hola + 3;
b = a;
b.hola = "hola";

#no tiene que andar
#a.hola + 3;

#pero esto si tiene que andar
a.hola += "3";

z = "z";
z = z + "z";
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
