from lexer_rules_v2 import tokens
from expressions_v2 import *
import pdb

class ParserException(Exception):
        def __init__(self, message, line):
                msg = message
                msg += "\nline: " + str(line)
                super(ParserException, self).__init__(msg)

#codeIni va aca arriba para que sea el primero de la produccion

#code & statements

#En este se llama a un statement y luego mas codigo
#Notar el statement permite poner comentarios al finalizar el statement
def p_code_statement(se):
        'code : statement code'
        ex1 = se[1]
        ex2 = se[2]
        se[0] = CodeNode(ex1, ex2, ex1.line)

def p_code_comment(se):
        'code : COMMENT code'
        ex1 = se[1]
        ex2 = se[2]
        se[0] = CommentNode(ex1["value"], ex2, ex1["line"])

def p_code_empty(se):
        'code : '
        se[0] = EmptyNode()
#statements
def p_statement_1(se):
        'statement : expression SEMICOLON'
        exp = se[1]
        se[0] = StatementNode(exp, exp.line)

def p_statement_block(se):
        'statement : block'
        se[0] = se[1]
        # se[0] = ExpressionStatementNode(block, comment, block.line)

def p_statement_if(se):
        'statement : if '
        se[0] = se[1]

def p_statement_while(se):
        'statement : while'
        se[0] = se[1]

def p_statement_for(se):
        'statement : for'
        se[0] = se[1]

def p_statement_do_while(se):
        'statement : do_while'
        se[0] = se[1]

#Expresiones
def p_expression_aritmethic(se):
        'expression : expressionAssign'
        se[0] = se[1]

# def p_expression_boolean(se):
#         'expression : bool'
#         se[0] = se[1]

# def p_expression_string(se):
#         'expression : string'
#         se[0] = se[1]

# def p_expression_vector(se):
#         'expression : vector'
#         se[0] = se[1]

def p_optional_expr(se):
        'optional_expr : expression'
        se[0] = se[1]

def p_optional_expr_empty(se):
        'optional_expr : '
        se[0] = EmptyNode()

#aritmeticas
def p_aritExp(se):
        'aritExp : aritExp AO unaryExp'
        ex1 = se[1]
        ex2 = se[3]
        op = se[2]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                unifyNumeric(ex1, ex2)
                se[0] = BinaryOperationNode(ex1, ex2, op, ex1.type, ex1.line)
        else:
                raise ParserException("Error de tipos en operador aritmetico binario", ex1.line)

def p_aritExp_unary(se):
        'aritExp : unaryExp'
        se[0] = se[1]

def p_unaryExp(se):
        'unaryExp : AO unaryExp'
        op = se[1]
        ex1 = se[2]
        if op != "+" and op != "-":
                raise Exception("Error en operador unario")
        else:
                if isNumeric(ex1.type):
                        ntype = ex1.type
                        se[0] = UnaryOperationNode(ex1, op, ntype, ex1.line, True)
                else:
                        raise ParserException("Error de tipos en operador aritmetico unario",ex1.line)

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
                raise ParserException("Error de tipos en operador aritmetico unario doble", ex1.line)

def p_unaryExp2_factor(se):
        'unaryExp2 : factorExp'
        se[0] = se[1]

def p_factorExp_Var(se):
        'factorExp : factorVar'
        se[0] = se[1]

def p_factorExp_Num(se):
        'factorExp : factorNumExp'
        se[0] = se[1]

def p_factorExp_Bool(se):
        'factorExp : bool_atom'
        se[0] = se[1]

def p_factorExp_Vector(se):
        'factorExp : expressionVector'
        se[0] = se[1]

def p_factorExp_VectorAt(se):
        'factorExp : expressionVectorAt'
        se[0] = se[1]

def p_factorExp_paren(se):
        'factorExp : LPAREN expression RPAREN'
        ex1 = se[2]
        se[0] = ParenOperationNode(ex1, ex1.type, ex1.line)

def p_factorVarExp(se):
        'factorVar : VAR'
        se[0] = VarNode(se[1]["value"],se[1]["line"])

def p_factorNumExp(se):
        'factorNumExp : NUMBER'
        se[0] = NumberNode(se[1]["value"], se[1]["type"], se[1]["line"])

# Boolean

def p_bool_true(se):
        'bool_atom : TRUE'
        se[0] = BooleanNode(se[1]["value"], se[1]["line"])

def p_bool_false(se):
        'bool_atom : FALSE'
        se[0] = BooleanNode(se[1]["value"], se[1]["line"])

#def p_bool_atom(se):
#        'expression : bool_atom'
#        se[0] = se[1]

def p_bool_op(se):
        'expressionBoolOp : expressionBoolOp BOOL_OP expressionComp'
        bool1 = se[1]
        bool2 = se[3]
        checkType(bool1, 'bool')
        checkType(bool2, 'bool')
        op = se[2]
        se[0] = BooleanOperationNode(bool1, bool2, op, bool1.line)

def p_bool_op_comp(se):
        'expressionBoolOp : expressionComp'
        se[0] = se[1]

def p_bool_neg(se):
        'unaryExp : NOT unaryExp'
        bool1 = se[2]
        checkType(bool1, 'bool')
        se[0] = BooleanNegationNode(bool1, bool1.line)

#def p_bool_paren(se):
#        'bool_atom : LPAREN expression RPAREN'
#        expr = se[2]
#        checkType(expr, 'bool')
#        se[0] = BooleanParenExpression(expr, expr.line)

def p_bool_comp(se):
        'expressionComp : expressionComp COMP aritExp'
        exp1 = se[1]
        comp = se[2]
        exp2 = se[3]
        if exp1.type != exp2.type:
                raise ParserException("Tipos de operandos distintos en comparacion", exp1.line)
        else:
                se[0] = BooleanCompNode(exp1, comp, exp2, exp1.line)

def p_bool_comp_arit(se):
        'expressionComp : aritExp'
        se[0] = se[1]

# Cadenas
def p_string(se):
        'expression : STRING'
        se[0] = StrNode(se[1]["value"], se[1]["line"])

def p_string_concat(se):
        'expression : expression AO STRING'
        op = se[2]
        if op != '+':
                raise Exception("Operador invalido")
        string = se[1]
        checkType(string, 'str')
        se[0] = StrConcatNode(string, se[3], se[1].line)


# Vectores
def p_vector(se):
        'expressionVector : LBRACKET vector_items RBRACKET'
        items = se[2]
        se[0] = VectorNode(items, items.line, items.type)

def p_vector_items(se):
        'vector_items : expression COMMA vector_items'
        head = se[1]
        tail = se[3]
        # pdb.set_trace()
        unifyNumeric(head, tail)
        checkType(head, tail.type)
        se[0] = VectorItemsNode(head, tail, head.line, head.type)

def p_vector_single_item(se):
        'vector_items : expression'
        se[0] = se[1]

def p_vector_at(se):
        'expressionVectorAt : expressionVectorAt LBRACKET expression RBRACKET'
        vect = se[1]
        index = se[3]
        checkType(vect, "vector")
        checkType(index, "int")
        se[0] = VectorAtNode(vect, index, vect.line, vect.type)

def p_vector_at_vector(se):
        'expressionVectorAt : expressionVector'
        se[0] = se[1]

def p_vector_at_var(se):
        'expressionVectorAt : factorVar'
        se[0] = se[1]

#asignaciones
def p_var_equals(se):
        'expressionAssign : factorVar EQUAL expressionAssign'
        ex1 = se[1]
        ex2 = se[3]
        op = se[2]

        ex1.type = ex2.type
        se[0] = AssignOperationNode(ex1, ex2, op, ex1.line)

def p_vector_equals(se):
        'expressionAssign :  expressionVectorAt EQUAL expressionAssign'

        ex1 = se[1]
        ex2 = se[3]
        op = se[2]

        #El vector de expresionVectorAt tiene que ser una variable
        #Es decir es una variable de tipo vector de algun tipo
        if isVar(ex1.vect):
                #si el tipo del vector todavia no se asigno lo va a asignar al tipo de la derecha.
                #si es del mismo tipo hace lo mismo.
                if checkType(ex1, 'VAR') or checkType(ex1, ex2.type):
                        ex1.type[0] = ex2.type
                        se[0] = AssignOperationNode(ex1, ex2, op, line)
                else:
                        #si es de otro tipo entonces no se puede hacer la asignacion
                        ParserException("No se puede asignar el tipo " + str(exp2.type) + " a vector de tipo " + str(exp1.type), exp1.line)
        else:
                ParserException("El vector no es una variable.", exp1.line)

def p_assign_BoolOp(se):
        'expressionAssign : expressionBoolOp'
        se[0] = se[1]

# Registros
# def p_reg(se):
#         'expression : LBRACE reg_items RBRACE'
#         se[0] = RegisterNode(se[2])

# def p_reg_items(se):
#         'reg_items : reg_field COMMA reg_items'
#         se[0] = RegisterItemsNode(se[1], se[3])

# def p_reg_single_item(se):
#         'reg_items : reg_field'
#         se[0] = se[1]

# def p_reg_field(se):
#         'reg_field : ........ COLON expression'
#         key = se[1]
#         checkType(key......)

#comments
# def p_comments(se):
#         'comments : COMMENT comments'
#         se[0] = CommentNode(se[1]["value"], se[2] ,se[1]["line"])

def p_comments_empty(se):
        'comments : '
        se[0] = EmptyNode()

# Blocks
def p_block(se):
        'block : LBRACE code RBRACE'
        code = se[2]
        se[0] = BlockNode(code, code.line)

# Single Statements
def p_single_statement_block(se):
        'singleStatement : block'
        se[0] = se[1]

def p_single_statement_comment(se):
        'singleStatement : COMMENT singleStatement'
        comm = se[1]
        se[0] = CommentNode(comm["value"], se[2], comm["line"])

def p_single_statement(se):
        'singleStatement : statement'
        se[0] = se[1]

# Conditional

def p_if(se):
        'if : IF LPAREN expression RPAREN singleStatement else'
        cond = se[3]
        checkType(cond, 'bool')
        caseTrue = se[5]
        caseFalse = se[6]
        se[0] = IfNode(cond, caseTrue, caseFalse, cond.line)

def p_else(se):
        'else : ELSE singleStatement'
        se[0] = ElseNode(se[2], se[2].line)

def p_else_empty(se):
        'else : '
        se[0] = EmptyNode()

# Loops
def p_while(se):
        'while : WHILE LPAREN expression RPAREN singleStatement'
        cond = se[3]
        checkType(cond, 'bool')
        statement = se[5]
        se[0] = WhileNode(cond, statement, cond.line)

def p_for(se):
        'for : FOR LPAREN optional_expr SEMICOLON expression SEMICOLON optional_expr RPAREN singleStatement'
        init = se[3]
        cond = se[5]
        checkType(cond, 'bool')
        post = se[7]
        content = se[9]
        se[0] = ForNode(init, cond, post, content)

def p_do_while(se):
        'do_while : DO singleStatement WHILE LPAREN expression RPAREN SEMICOLON'
        statement = se[2]
        cond = se[5]
        checkType(cond, 'bool')
        se[0] = DoWhileNode(statement, cond, statement.line)

def isNumeric(nType):
        return nType == "float" or nType == "int"

def unifyNumeric(a, b):
        if isNumeric(a.type) and isNumeric(b.type) and a.type != b.type:
                a.type = b.type = "float"
        # caso vectores:
        if isTuple(a.type) and isTuple(b.type) and isNumeric(a.type[0]) and isNumeric(b.type[0]) and a.type[0] != b.type[0]:
                a.type[0] = b.type[0] = "float"


def checkType(elem, type):
        # pdb.set_trace()
        if (type != "vector" and elem.type != type) or (type == "vector" and not isTuple(elem.type)) :
                raise Exception("Error de tipos: se esperaba %s y se encontro %s" % (type, elem.type))

def p_error(token):
        message = "[Syntax error]"
        if token is not None:
                message += "\ntype: " + token.type
                message += "\nvalue: " + str(token.value)
                message += "\nline: " + str(token.lineno)
                message += "\nposition: " + str(token.lexpos)
        raise Exception(message)
