import lexer_rules_v2
import parser_rules_v2

from sys import argv, exit

from ply.lex import lex
from ply.yacc import yacc

if __name__ == "__main__":
    if len(argv) != 3:
        print ("Parametros invalidos.")
        print ("Uso:")
        print ("  parser.py archivo_entrada archivo_salida")
        exit(1)

    input_file = open(argv[1], "r")
    text = input_file.read()
    input_file.close()

    lexer = lex(module=lexer_rules_v2)
    parser = yacc(module=parser_rules_v2)

    try:
        ast = parser.parse(text, lexer)
    except Exception as e:
        print (str(e))
        exit(1)
        

    output_file = open(argv[2], "w")
    output_file.write(ast.evaluate(0,0))
    output_file.close()

    exit(0)
