from lexer_rules import tokens
from expressions import *

#statements
"""
def p_statement_compound(subExpr):
        'statement : compoundStatement'
        subExpr[0] = subExpr[1]

def p_statement_comment(subExpr):
        'statement : COMMENT'
        subExpr[0] = CommentaryOperation(subExpr[1], "Comment", subExpr[1].lineno)


def p_statement_if(subExpr):
        'statement : ifStatement'
        subExpr[0] = subExpr[1]

def p_statement_return(subExpr):
        'statement : returnStatement'
        subExpr[0] = subExpr[1]
"""
def p_statement_expression(subExpr):
        'statement : expressionStatement'
        subExpr[0] = StatementOperation(subExpr[1], subExpr[1].type, subExpr[1].line)
"""
def p_compoundStatement(subExpr):
        'compoundStatement : LBRACE statements RBRACE'
        statement = subExpr[2]
        subExpr[0] = BlockOperation(statement, statement.type, subExpr[1].lineno)
"""
def p_expressionStatement(subExpr):
        'expressionStatement : expression SEMICOLON'
        subExpr[0] = StatementsOperation(subExpr[1],subExpr[2],subExpr[1].type, subExpr[1].line)

def p_statements(subExpr):
        'statements : statement statements'
        subExpr[0] = StatementsOperation(subExpr[1],subExpr[2],subExpr[1].type, subExpr[1].line)

def p_statements_empty(subExpr):
        'statements : '
        subExpr[0] = StatementsOperation(None,None,"None", 0)

#expressions
def p_expression(subExpr):
        'expression : orExpression'
        subExpr[0] = subExpr[1]

def p_orExpression(subExpr):
        'orExpression : orExpression OR andExpression'
        orEx = subExpr[1]
        andEx = subExpr[3]
        if orEx.type == "bool" and andEx.type == "bool":
                subExpr[0] = BinaryOperation(orEx, andEx,"OR","bool", orEx.line)
        else:
                otherError("Tipos incompatibles",orEx.line)

def p_orExpression_and(subExpr):
        'orExpression : andExpression'
        subExpr[0] = subExpr[1]
       
def p_andExpression(subExpr):
        'andExpression : andExpression AND eqeqExpression'
        andEx = subExpr[1]
        eqeqEx = subExpr[3]
        if andEx.type == "bool" and eqeqEx.type == "bool":
                subExpr[0] = BinaryOperation(andEx, eqeqEx,"AND","bool", andEx.line)
        else:
                otherError("Tipos incompatibles",andEx.line)

def p_andExpression_eqeq(subExpr):
        'andExpression : eqeqExpression'
        subExpr[0] = subExpr[1]

def p_eqeqExpression(subExpr):
        'eqeqExpression : eqeqExpression EQUALS EQUALS noteqExpression'
        eqeqEx = subExpr[1]
        noteqEx = subExpr[4]
        if eqeqEx.type == "bool" and noteqEx.type == "bool":
                subExpr[0] = BinaryOperation(eqeqEx, noteqEx,"==","bool", eqeqEx.line)
        else:
                otherError("Tipos incompatibles",eqeqEx.line)

def p_eqeqExpression_not(subExpr):
        'eqeqExpression : noteqExpression'
        subExpr[0] = subExpr[1]


def p_noteqExpression(subExpr):
        'noteqExpression : noteqExpression NOTEQUALS lessExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if ex1.type == "bool" and ex2.type == "bool":
                subExpr[0] = BinaryOperation(ex1, ex2,"!=","bool", ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_noteqExpression_less(subExpr):
        'noteqExpression : lessExpression'
        subExpr[0] = subExpr[1]

def p_lessExpression(subExpr):
        'lessExpression : lessExpression LESS greaterExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                subExpr[0] = BinaryOperation(ex1, ex2,"<","bool", ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_lessExpression_greater(subExpr):
        'lessExpression : greaterExpression'
        subExpr[0] = subExpr[1]

def p_greaterExpression(subExpr):
        'greaterExpression : greaterExpression GREATER plusExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                subExpr[0] = BinaryOperation(ex1, ex2,">","bool", ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_greaterExpression_plus(subExpr):
        'greaterExpression : plusExpression'
        subExpr[0] = subExpr[1]

def p_plusExpression(subExpr):
        'plusExpression : plusExpression PLUS minusExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                nType = ex1.type
                if ex2.type == "float":
                        nType = "float"
                subExpr[0] = BinaryOperation(ex1, ex2,"+",nType, ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_plusExpression_minus(subExpr):
        'plusExpression : minusExpression'
        subExpr[0] = subExpr[1]

def p_minusExpression(subExpr):
        'minusExpression : minusExpression MINUS timesExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                nType = ex1.type
                if ex2.type == "float":
                        nType = "float"
                subExpr[0] = BinaryOperation(ex1, ex2,"-",nType, ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_minusExpression_times(subExpr):
        'minusExpression : timesExpression'
        subExpr[0] = subExpr[1]

def p_timesExpression(subExpr):
        'timesExpression : timesExpression TIMES divExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                nType = ex1.type
                if ex2.type == "float":
                        nType = "float"
                subExpr[0] = BinaryOperation(ex1, ex2,"*",nType, ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_timesExpression_div(subExpr):
        'timesExpression : divExpression'
        subExpr[0] = subExpr[1]

def p_divExpression(subExpr):
        'divExpression : divExpression DIV unaryMinusExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[3]
        if isNumeric(ex1.type) and isNumeric(ex2.type):
                nType = ex1.type
                if ex2.type == "float":
                        nType = "float"
                subExpr[0] = BinaryOperation(ex1, ex2,"/",nType, ex1.line)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_divExpression_unaryMinus(subExpr):
        'divExpression : '
        subExpr[0] = subExpr[1]

def p_unaryMinusExpression(subExpr):
        'unaryMinusExpression : MINUS factorExpression'
        ex1 = subExpr[1]
        ex2 = subExpr[2]
        if isNumeric(ex2.type):
                nType = ex2.type
                subExpr[0] = UnaryOperation(ex2,"-",nType, ex1.lineno)
        else:
                otherError("Tipos incompatibles",ex1.line)

def p_unaryMinusExpression_factor(subExpr):
        'unaryMinusExpression : factorExpression'
        subExpr[0] = subExpr[1]
        
def p_factorExpression_paren(subExpr):
        'factorExpression : LPAREN expression RPAREN'
        ex1 = subExpr[1]
        ex2 = subExpr[2]
        subExpr[0] = ParenOperation(ex2,ex2.type, ex1.lineno)

def p_factorExpression(subExpr):
        'factorExpression : NUMBER'
        subExpr[0] = Number(subExpr[1].value,subExpr[1].type, subExpr[1].lineno)


"""
def p_if(subExpr):
	'if : IF LPAREN bool RPAREN block else'
	subExpr[0] = "if(" + subExpr[3] + ")\n"+ subExpr[5] + subExpr[6]

def p_else(subExpr):
	'else : ELSE block'
	subExpr[0] = "else \n" + subExpr[1]

#def p_else_empty(subExpr):
#	'else : empty'

def p_bool(subExpr):
	'bool : expr rel expr otherBool'
	subExpr[0] = subExpr[1]["value"] + subExpr[2] + subExpr[3]["value"] + subExpr[4]

def p_rel_lEquals(subExpr):
	'rel : LEQUALS'
	subExpr[0] = "<="

def p_otherBool(subExpr):
	'otherBool : logico expr'
	subExpr[0] = subExpr[1] + subExpr[2]["value"]

def p_logico_AND(subExpr):
	'logico : AND'
	subExpr[0] = "AND"

#def p_otherBool_empty(subExpr):
#	'otherBool : empty'


def checkType(expr1, expr2):
	type1 = expr1["type"]
	type2 = expr2["type"]
	if type1 == 'float':
		if type2 != 'float' and type2 != 'int':
			raise Exception("Error de tipos")
		else:
			return 'float'
	else:
		if type2 == 'float':
			if type1 != 'float' and type1 != 'int':
				raise Exception("Error de tipos")
			else:
				return 'float'
		else:
			return 'int'
	return ''

def p_expression_plus(subexpressions):
	'expression : expression PLUS term'
	exprType = checkType(subexpressions[1],subexpressions[3])
	subexpressions[0] =  {"value": subexpressions[1]["value"] + "-" + subexpressions[3]["value"], "type":exprType}

def p_expression_minus(subexpressions):
	'expression : expression MINUS term'
	exprType = checkType(subexpressions[1],subexpressions[3])
	subexpressions[0] =  {"value": subexpressions[1]["value"] + "-" + subexpressions[3]["value"], "type":exprType}


def p_expression_term(subexpressions):
	'expression : term'
	subexpressions[0] = subexpressions[1]


def p_term_times(subexpressions):
	'term : term TIMES factor'
	exprType = checkType(subexpressions[1],subexpressions[3])
	subexpressions[0] =  {"value": subexpressions[1]["value"] + "-" + subexpressions[3]["value"], "type":exprType}


def p_term_factor(subexpressions):
	'term : factor'
	subexpressions[0] = subexpressions[1]


def p_factor_number(subexpressions):
	'factor : NUMBER'
	subexpressions[0] = {"value": subexpressions[1]["value"], "type":subexpressions[1]["type"]}


def p_factor_expression(subexpressions):
	'factor : LPAREN expression RPAREN'
	subexpressions[0]["value"] = "(" + subexpressions[2]["value"] + ")"
	subexpressions[0]["type"] = subexpressions[2]["type"]

def p_block_block(subExpr):
	'block : LBRACE sent RBRACE'
	subExpr[0] = "{\n" + subExpr[2] + "}\n"

def p_block_sent(subExpr):
	'block : sent'
	subExpr[0] = subExpr[1]

def p_sent(subExpr):
	'sent : expr SEMICOLON'
	subExpr[0] = subExpr[1]["value"] + ";\n"
"""

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

def otherError(msg, line):
        message = msg
        message += "\nline:" + str(line)
        raise Exception(message)
