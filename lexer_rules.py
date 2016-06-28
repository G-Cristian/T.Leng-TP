tokens = [
  'TYPE',
  'ID',
  'NUMBER',
  'COMMENT',
  'NEWLINE',
  'COMMA',
  'SEMICOLON',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIV',
  'LPAREN',
  'RPAREN',
  'LBRACKET',
  'RBRACKET',
  'LBRACE',
  'RBRACE',

  'BEGIN',
  'END',
  'WHILE',
  'FOR',
  'IF',
  'ELSE',
  'DO',
  'RES',
  'RETURN',
  'TRUE',
  'FALSE',
  'AND',
  'OR',
  'NOT',

  'EQUALS',
  'NOTEQUALS',
  'LEQUALS',
  'GEQUALS',
  'LESS',
  'GREATER'
]

types = set(['int', 'float'])

def t_ID(token):
    r"[_a-zA-Z][_a-zA-Z0-9]*"
    if token.value in types:
        token.type = 'TYPE'
    return token


def t_NUMBER(token):
    r"[0-9]+(\.[0-9]+)?"
    if token.value.find(".") >= 0:
        number_type = "float"
        number_value = float(token.value)
    else:
        number_type = "int"
        number_value = int(token.value)
    token.value = {"value": number_value, "type": number_type}
    return token

def t_NEWLINE(token):
	r"\n+"
	token.lexer.lineno += len(token.value)

def t_COMMENT(token):
	r"\#.*\n"
	token.value = token.value.strip()
	token.lexer.lineno += 1
	return token

t_COMMA = r","
t_SEMICOLON = r";"
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIV = r"\/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_BEGIN = r"begin"
t_END = r"end"
t_WHILE = r"while"
t_FOR = r"for"
t_IF = r"if"
t_ELSE = r"else"
t_DO = r"do"
t_RES = r"res"
t_RETURN = r"return"
t_TRUE = r"true"
t_FALSE = r"false"
t_AND = r"AND"
t_OR = r"OR"
t_NOT = r"NOT"

t_EQUALS = r"="
t_NOTEQUALS = r"!="
t_LEQUALS = r"<="
t_GEQUALS = r">="
t_LESS = r"<"
t_GREATER = r">"

t_ignore = " \t"


def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
