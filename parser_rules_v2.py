from lexer_rules_v2 import tokens
from expressions_v2 import *
import pdb

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
        'statement : expression SEMICOLON comments'
        ex1 = se[1]
        ex2 = se[3]
        se[0] = ExpressionStatementNode(ex1, ex2, ex1.line)

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
        'expression : aritExp'
        se[0] = se[1]

def p_expression_boolean(se):
        'expression : bool'
        se[0] = se[1]

def p_expression_string(se):
        'expression : string'
        se[0] = se[1]

def p_expression_vector(se):
        'expression : vector'
        se[0] = se[1]

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

# Boolean

def p_bool_true(se):
        'bool_atom : TRUE'
        se[0] = BooleanNode(se[1]["value"], se[1]["line"])

def p_bool_false(se):
        'bool_atom : FALSE'
        se[0] = BooleanNode(se[1]["value"], se[1]["line"])

def p_bool_atom(se):
        'bool : bool_atom'
        se[0] = se[1]

def p_bool_op(se):
        'bool : bool BOOL_OP bool_atom'
        bool1 = se[1]
        bool2 = se[3]
        op = se[2]
        se[0] = BooleanOperationNode(bool1, bool2, op, bool1.line)

def p_bool_neg(se):
        'bool : NOT bool'
        bool1 = se[2]
        se[0] = BooleanNegationNode(bool1, bool1.line)

def p_bool_paren(se):
        'bool_atom : LPAREN bool RPAREN'
        expr = se[2]
        se[0] = BooleanParenExpression(expr, expr.line)

def p_bool_comp(se):
        'bool : aritExp COMP aritExp'
        exp1 = se[1]
        comp = se[2]
        exp2 = se[3]
        se[0] = BooleanCompNode(exp1, comp, exp2, exp1.line)

# Cadenas
def p_string(se):
        'string : STRING'
        se[0] = StrNode(se[1]["value"], se[1]["line"])

def p_string_concat(se):
        'string : string AO STRING'
        op = se[2]
        if op != '+':
                raise Exception("Operador invalido")
        se[0] = StrConcatNode(se[1], se[3], se[1].line)


# Vectores
def p_vector(se):
        'vector : LBRACKET vector_items RBRACKET'
        items = se[2]
        se[0] = VectorNode(items, items.line, items.type)

def p_vector_items(se):
        'vector_items : expression COMMA vector_items'
        head = se[1]
        tail = se[3]
        # pdb.set_trace()
        unifyNumeric(head, tail)
        if head.type != tail.type:
                raise Exception("Error de tipos en vector")
        se[0] = VectorItemsNode(head, tail, head.line, head.type)

def p_vector_single_item(se):
        'vector_items : expression'
        se[0] = se[1]

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

# Conditional

def p_if(se):
        'if : IF LPAREN bool RPAREN statement else'
        cond = se[3]
        caseTrue = se[5]
        caseFalse = se[6]
        se[0] = IfNode(cond, caseTrue, caseFalse, cond.line)

def p_else(se):
        'else : ELSE statement'
        se[0] = ElseNode(se[2], se[2].line)

def p_else_empty(se):
        'else : '
        se[0] = EmptyNode()

# Loops
def p_while(se):
        'while : WHILE LPAREN bool RPAREN statement'
        cond = se[3]
        statement = se[5]
        se[0] = WhileNode(cond, statement, cond.line)

def p_for(se):
        'for : FOR LPAREN optional_expr SEMICOLON bool SEMICOLON optional_expr RPAREN statement '
        init = se[3]
        cond = se[5]
        post = se[7]
        content = se[9]
        se[0] = ForNode(init, cond, post, content)

def p_do_while(se):
        'do_while : DO statement WHILE LPAREN bool RPAREN SEMICOLON'
        statement = se[2]
        cond = se[5]
        se[0] = DoWhileNode(statement, cond, statement.line)

def isNumeric(nType):
        return nType == "float" or nType == "int"

def unifyNumeric(a, b):
        if isNumeric(a.type) and isNumeric(b.type) and a.type != b.type:
                a.type = b.type = "float"

def p_error(token):
        message = "[Syntax error]"
        if token is not None:
                message += "\ntype: " + token.type
                message += "\nvalue: " + str(token.value)
                message += "\nline: " + str(token.lineno)
                message += "\nposition: " + str(token.lexpos)
        raise Exception(message)
