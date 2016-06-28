tokens = [
    #aritmeticos
    'AO',
    #++/--
    'DOUBLE_AO',
    #parentesis
    'LPAREN',
    'RPAREN',
    #puntuacion
    'SEMICOLON',
    'COMMA',
    'DOT',
    #Comentario
    'COMMENT',
    #Number,
    'NUMBER'
]

t_AO = r"[\+\-\*/]"
t_DOUBLE_AO = r"\+\+ | \-\-"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SEMICOLON = r";"
t_COMMA = r","
t_DOT = r"\."

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
    token.value = {"value": number_value, "type": number_type, "line":token.lexer.lineno}
    return token

def t_NEWLINE(token):
	r"\n+"
	token.lexer.lineno += len(token.value)

def t_COMMENT(token):
	r"\#.*"
	token.value = token.value.strip()
	return token

t_ignore = " \t"


def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
