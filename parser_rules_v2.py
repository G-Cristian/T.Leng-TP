from lexer_rules_v2 import tokens
from expressions_v2 import *

#Expresiones
def p_expression(se):
        'expression : aritExp'
        se[0] = se[1]

#aritmeticas
def p_aritExp(se):
        'aritExp : aritExp AO unaryExp'
        ex1 = se[1]
        ex2 = se[3]
        op = se[2]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                ntype = ex1.type
                if ex2.type == "float":
                        ntype = "float"
                se[0] = BinaryOperationNode(ex1, ex2, op, ntype, ex1.line)
        else:
                raise Exception("Error de tipos en operador aritmetico binario")

def p_aritExp_unary(se):
        'aritExp : unaryExp'
        se[0] = se[1]

def p_unaryExp(se):
        'unaryExp : AO unaryExp'
        op = se[1]
        ex1 = se[2]
        if op.value != "+" and op.value != "-":
                raise Exception("Error en operador unario")
        else:
                if isNumeric(ex1.type):
                        ntype = ex1.type
                        se[0] = UnaryOperationNode(ex1, op, ntype, ex1.line, True)
                else:
                        raise Exception("Error de tipos en operador aritmetico unario")
                        

def p_unaryExp_double(se):
        'unaryExp : DOUBLE_AO unaryExp'
        op1 = se[1]
        ex1 = se[2]
        if isNumeric(ex1.type):
                ntype = ex1.type
                se[0] = UnaryOperationNode(ex1, op1, ntype, ex1.line, True)
        else:
                raise Exception("Error de tipos en operador aritmetico unario doble")

def p_unaryExp_double_unaryExp2(se):
        'unaryExp : unaryExp2'
        se[0] = se[1]

def p_unaryExp_double2(se):
        'unaryExp2 : unaryExp2 DOUBLE_AO'
        op1 = se[2]
        ex1 = se[1]
        if isNumeric(ex1.type):
                ntype = ex1.type
                se[0] = UnaryOperationNode(ex1, op1, ntype, ex1.line, False)
        else:
                raise Exception("Error de tipos en operador aritmetico unario doble")

def p_unaryExp2_factor(se):
        'unaryExp2 : factorExp'
        se[0] = se[1]

def p_factorExp(se):
        'factorExp : NUMBER'
        se[0] = NumberNode(se[1]["value"], se[1]["type"], se[1]["line"])

def p_factorExp_paren(se):
        'factorExp : LPAREN expression RPAREN'
        ex1 = se[2]
        se[0] = ParenOperationNode(ex1, ex1.type, ex1.line)

def isNumeric(nType):
        return nType == "float" or nType == "int"

def p_error(token):
        message = "[Syntax error]"
        if token is not None:
                message += "\ntype:" + token.type
                message += "\nvalue:" + str(token.value)
                message += "\nline:" + str(token.lineno)
                message += "\nposition:" + str(token.lexpos)
        raise Exception(message)
