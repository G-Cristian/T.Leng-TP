import lexer_rules_v2
import parser_rules_v2
from ply.lex import lex
from ply.yacc import yacc

lexer = lex(module=lexer_rules_v2)
parser = yacc(module=parser_rules_v2)
text = """1++

"""
ast = parser.parse(text, lexer)
print (ast.evaluate(0,0))
