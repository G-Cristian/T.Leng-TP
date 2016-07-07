from lexer_rules_v2 import tokens
from expressions_v2 import *
import pdb

variables = {
}

def getType(ex):
        if ex.type != 'VAR':
                return ex.type
        else:
                return variables.get(ex.value, 'undef')

class ParserException(Exception):
        def __init__(self, message, line):
                msg = message
                msg += "\nline: " + str(line)
                super(ParserException, self).__init__(msg)

#code & statements

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

        type1 = getType(ex1)
        type2 = getType(ex2)

        if isNumeric(type1) and isNumeric(type2):
                unifyNumeric(ex1, ex2)
                se[0] = BinaryOperationNode(ex1, ex2, op, type2, ex1.line)
        elif ex1.type == "str" and ex2.type == "str":
                if op != '+':
                        raise Exception("Operador invalido")
                se[0] = StrConcatNode(ex1, ex2, se[1].line)
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
                type1 = getType(ex1)
                if isNumeric(type1):
                        se[0] = UnaryOperationNode(ex1, op, type1, ex1.line, True)
                else:
                        raise ParserException("Error de tipos en operador aritmetico unario",ex1.line)

def p_unaryExp_double(se):
        'unaryExp : DOUBLE_AO unaryExp'
        op1 = se[1]
        ex1 = se[2]
        type1 = getType(ex1)
        if isNumeric(type1):
                se[0] = UnaryOperationNode(ex1, op1, type1, ex1.line, True)
        else:
                raise Exception("Error de tipos en operador aritmetico unario doble")

def p_unaryExp_double_unaryExp2(se):
        'unaryExp : unaryExp2'
        se[0] = se[1]

def p_unaryExp_double2(se):
        'unaryExp2 : unaryExp2 DOUBLE_AO'
        op1 = se[2]
        ex1 = se[1]
        type1 = getType(ex1)

        if isNumeric(type1):
                se[0] = UnaryOperationNode(ex1, op1, type1, ex1.line, False)
        else:
                raise ParserException("Error de tipos en operador aritmetico unario doble", ex1.line)

def p_unaryExp2_factor(se):
        'unaryExp2 : factorExp'
        se[0] = se[1]

def p_factorExp_Num(se):
        'factorExp : factorNumExp'
        se[0] = se[1]

def p_factorExp_Bool(se):
        'factorExp : bool_atom'
        se[0] = se[1]

def p_factorExp_VectorAt(se):
        'factorExp : expressionVectorAt'
        se[0] = se[1]

def p_factorExp_paren(se):
        'factorExp : LPAREN expression RPAREN'
        ex1 = se[2]
        type1 = getType(ex1)
        se[0] = ParenOperationNode(ex1, type1, ex1.line)

def p_factorExp_function(se):
        'factorExp : expressionFunction'
        se[0] = se[1]

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

def p_bool_comp(se):
        'expressionComp : expressionComp COMP aritExp'
        exp1 = se[1]
        comp = se[2]
        exp2 = se[3]
        type1 = getType(exp1)
        type2 = getType(exp2)
        if type1 != type2:
                raise ParserException("Tipos de operandos distintos en comparacion", exp1.line)
        else:
                se[0] = BooleanCompNode(exp1, comp, exp2, exp1.line)

def p_bool_comp_arit(se):
        'expressionComp : aritExp'
        se[0] = se[1]

# Cadenas
def p_string(se):
        'unaryExp : STRING'
        se[0] = StrNode(se[1]["value"], se[1]["line"])

# Vectores
def p_vector(se):
        'expressionVector : LBRACKET vector_items RBRACKET'
        items = se[2]
        se[0] = VectorNode(items, items.line, items.type)

def p_vector_items(se):
        'vector_items : expression COMMA vector_items'
        head = se[1]
        tail = se[3]
        unifyNumeric(head, tail)
        checkType(head, tail.type)
        type1 = getType(head)
        se[0] = VectorItemsNode(head, tail, head.line, type1)

def p_vector_single_item(se):
        'vector_items : expression'
        if se[1].type == 'VAR':
                raise ParserException("Variable no asignada", se[1].line)
        se[0] = se[1]

def p_vector_at(se):
        'expressionVectorAt : expressionVectorAt LBRACKET expression RBRACKET'
        vect = se[1]
        index = se[3]
        checkType(vect, "vector")
        checkType(index, "int")
        type1 = getType(vect)
        se[0] = VectorAtNode(vect, index, vect.line, type1)

def p_vector_at_vector(se):
        'expressionVectorAt : expressionVector'
        se[0] = se[1]

def p_vector_at_var(se):
        'expressionVectorAt : factorVar'
        se[0] = se[1]

#vectorAt que tiene por lo menos un par de brackets
def p_varVector_at(se):
        'expressionVectorVar : expressionVectorAt LBRACKET expression RBRACKET'
        vect = se[1]
        index = se[3]
        type1 = getType(vect)
        try:
                checkType(vect, "vector")
        except :
                if type1 != 'undef':
                        raise ParserException("La parte izquierda debe ser una variable sin definir o un vector.", vect.line)
        checkType(index, "int")
        se[0] = VectorAtNode(vect, index, vect.line, type1)

#asignaciones
def p_var_equals(se):
        'expressionAssign : factorVar EQUAL expressionAssign'
        ex1 = se[1]
        ex2 = se[3]
        op = se[2]

        type2 = getType(ex2)
        if type2 != 'undef':
                variables[ex1.value] = type2
                se[0] = AssignOperationNode(ex1, ex2, op, type2, ex1.line)
        else:
                raise ParserException("No se puede asignar una variable sin tipo",ex1.line)

def p_vector_equals(se):
        'expressionAssign :  expressionVectorVar EQUAL expressionAssign'

        ex1 = se[1]
        ex2 = se[3]
        op = se[2]

        type1 = getType(ex1)
        type2 = getType(ex2)
        #Lo de la derecha tiene que estar definido
        if type2 != 'undef':
                #El vector de expresionVectorAt tiene que ser una variable
                #Es decir es una variable de tipo vector de algun tipo
                if vectorIsVar(ex1.vect):
                        vect = getVector(ex1)
                        #si el tipo del vector todavia no se asigno lo va a asignar al tipo de la derecha.
                        #si es del mismo tipo hace lo mismo.
                        if type1 == 'undef' or type1 == type2:
                                newType = 'undef'
                                currentVectorLevel = 0
                                if isTuple(type2):
                                        newType = type2[0]
                                        currentVectorLevel = type2[1]
                                else:
                                        newType = type2

                                currentVectorLevel1 = 0
                                typeOfVector = getType(vect)
                                if typeOfVector != 'undef':
                                        currentVectorLevel = typeOfVector[1] - 1

                                variables[vect.value] = (newType,1+currentVectorLevel)


                                se[0] = AssignOperationNode(ex1, ex2, op, type2, ex1.line)
                        else:
                                #si es de otro tipo entonces no se puede hacer la asignacion
                                raise ParserException("No se puede asignar el tipo " + str(ex2.type) + " a vector de tipo " + str(ex1.type), ex1.line)
                else:
                        raise ParserException("El vector no es una variable.", ex1.line)
        else:
                raise ParserException("No se puede asignar una variable sin tipo",ex1.line)

def p_assign_TernaryCond(se):
        'expressionAssign : expressionTernaryCond'
        se[0] = se[1]

# Registros
def p_reg_assign(se):
        'expressionAssign : factorVar EQUAL LBRACE reg_items RBRACE'
        for f in se[4].fields():
                variables["%s.%s" % (se[1].value, f.key.value)] = f.value.type
        # se[0] = RegisterNode(se[4], se[1].line)
        se[0] = AssignOperationNode(se[1],  RegisterNode(se[4], se[1].line), se[2], 'reg', se[1].line)

def p_reg_items(se):
        'reg_items : reg_field COMMA reg_items'
        se[0] = RegisterItemsNode(se[1], se[3])

def p_reg_single_item(se):
        'reg_items : reg_field'
        se[0] = se[1]

def p_reg_field(se):
        'reg_field : factorVar COLON expression'
        key = se[1]
        exp = se[3]
        se[0] = RegFieldNode(key, exp)


def p_comments_empty(se):
        'comments : '
        se[0] = EmptyNode()

# Blocks
def p_block(se):
        'block : LBRACE code RBRACE'
        code = se[2]
        se[0] = BlockNode(code, code.line)


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

#ternary conditional
def p_ternaryConditiopnal(se):
        'expressionTernaryCond : expressionBoolOp QUESTION expression COLON expression'
        cond = se[1]
        caseTrue = se[3]
        caseFalse = se[5]
        checkType(cond, 'bool')
        checkType(caseTrue, caseFalse.type)
        se[0] = TernaryConditionalNode(cond, caseTrue, caseFalse, caseTrue.type, cond.line)

def p_ternaryConditiopnal_BoolOp(se):
        'expressionTernaryCond : expressionBoolOp'
        se[0] = se[1]

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


#funciones
def p_scalarMultiplication_1(se):
        'expressionFunction : MULTIPLICACIONESCALAR LPAREN expression COMMA expression RPAREN'
        function = se[1]
        ex1 = se[3]
        ex2 = se[5]
        checkType(ex1, "vector")
        if not isNumeric(getType(ex1)[0]) or getType(ex1)[1] != 1:
                raise ParserException("Se esperaba un vector numerico en el primer parametro de multiplicacionEscalar",ex1.line)
        if not isNumeric(getType(ex2)):
                raise ParserException("Se esperaba tipo numerico en el segundo parametro de multiplicacionEscalar",ex2.line)

        se[0] = ScalarMultiplicationNode(ex1, ex2, None, ex1.line)

def p_scalarMultiplication_2(se):
        'expressionFunction : MULTIPLICACIONESCALAR LPAREN expression COMMA expression COMMA expression RPAREN'
        function = se[1]
        ex1 = se[3]
        ex2 = se[5]
        ex3 = se[7]
        checkType(ex1, "vector")
        if not isNumeric(getType(ex1)[0]) or getType(ex1)[1] != 1:
                raise ParserException("Se esperaba un vector numerico en el primer parametro de multiplicacionEscalar",ex1.line)
        if not isNumeric(getType(ex2)):
                raise ParserException("Se esperaba tipo numerico en el segundo parametro de multiplicacionEscalar",ex2.line)

        checkType(ex3, "bool")
        se[0] = ScalarMultiplicationNode(ex1, ex2, ex3, ex1.line)

def p_capitalize(se):
        'expressionFunction : CAPITALIZAR LPAREN expression RPAREN'

        ex1 = se[3]
        checkType(ex1, 'str')

        se[0] = CapitalizeNode(ex1, ex1.line)

def p_collinear(se):
        'expressionFunction : COLINEALES LPAREN expression COMMA expression RPAREN'
        ex1 = se[3]
        ex2 = se[5]
        checkType(ex1, "vector")
        if not isNumeric(getType(ex1)[0]) or getType(ex1)[1] != 1:
                raise ParserException("Se esperaba un vector numerico en el primer parametro de colineales",ex1.line)

        checkType(ex2, "vector")
        if not isNumeric(getType(ex2)[0]) or getType(ex2)[1] != 1:
                raise ParserException("Se esperaba un vector numerico en el segundo parametro de colineales",ex2.line)

        se[0] = CollinearNode(ex1, ex2, ex1.line)

def p_print(se):
        'expressionFunction : PRINT LPAREN expression RPAREN'
        ex1 = se[3]
        se[0] = PrintNode(ex1, ex1.line)

def p_length(se):
        'expressionFunction : LENGTH LPAREN expression RPAREN'
        ex1 = se[3]
        type1 = getType(ex1)
        try:
                checkType(ex1, "vector")
        except :
                if type1 != 'str':
                        raise ParserException("length recibe un vector o una cadena.", ex1.line)

        se[0] = LengthNode(ex1, ex1.line)

#auxiliares
def isNumeric(nType):
        return nType == "float" or nType == "int"

def unifyNumeric(a, b):
        if isNumeric(a.type) and isNumeric(b.type) and a.type != b.type:
                a.type = b.type = "float"
        # caso vectores:
        if isTuple(a.type) and isTuple(b.type) and isNumeric(a.type[0]) and isNumeric(b.type[0]) and a.type[0] != b.type[0]:
                a.type[0] = b.type[0] = "float"


def checkType(elem, type):
        typeToCheck = elem.type
        if elem.type == 'VAR':
                typeToCheck = getType(elem)
        if (type != "vector" and typeToCheck != type) or (type == "vector" and not isTuple(typeToCheck)) :
                raise Exception("Error de tipos: se esperaba %s y se encontro %s" % (type, typeToCheck))

def getVector(vec):
        if vec.__class__.__name__ == 'VectorNode' or vec.__class__.__name__ == 'VarNode':
                return vec
        else:
                if vec.__class__.__name__ != 'VectorAtNode':
                        raise Exception("No se puede consegir un vector de algo que no es un 'VectorNode' ni un 'VarNode' ni un 'VectorAtNode'" + vec.__class__.__name__)
                else:
                        return getVector(vec.vect)

def vectorIsVar(vec):
        if vec.type == 'VAR':
                return True
        else:
                if vec.__class__.__name__ != 'VectorAtNode':
                        return False
                else:
                        return vectorIsVar(vec.vect)

def p_error(token):
        message = "[Syntax error]"
        if token is not None:
                message += "\ntype: " + token.type
                message += "\nvalue: " + str(token.value)
                message += "\nline: " + str(token.lineno)
                message += "\nposition: " + str(token.lexpos)
        raise Exception(message)
