# import pdb
tokens = [
    # aritmeticos
    'AO',
    # ++/--
    'DOUBLE_AO',
    # asignacion
    'EQUAL',
    'PEQUAL',
    'MEQUAL',
    # comparacion
    'COMP',
    # parentesis
    'LPAREN',
    'RPAREN',
    # corchetes
    'LBRACKET',
    'RBRACKET',
    # llaves
    'LBRACE',
    'RBRACE',
    # puntuacion
    'COMMA',
    'DOT',
    'COLON',
    'SEMICOLON',
    'QUESTION',
    # Comentario
    'COMMENT',
    # Number,
    'NUMBER',
    # Cadenas
    'STRING',
    # funciones
    'MULTIPLICACIONESCALAR',
    'CAPITALIZAR',
    'COLINEALES',
    'PRINT',
    'LENGTH',
    # condicional
    'IF',
    'ELSE',
    # bucles
    'FOR',
    'WHILE',
    'DO',
    # booleans
    'TRUE',
    'FALSE',
    'BOOL_OP',
    'NOT',
    # variables
    'VAR'
]

t_AO = r"[\+\-\*/\^%]"
t_DOUBLE_AO = r"(\+\+)|(\-\-)"
t_EQUAL = "="
t_COMP = r"<|>|==|!="
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"]"
t_LBRACE = r"\{"
t_RBRACE = r"}"
t_COMMA = ","
t_DOT = r"\."
t_COLON = ":"
t_SEMICOLON = ";"
t_QUESTION = "\?"

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'do' : 'DO',
    'multiplicacionEscalar' : 'MULTIPLICACIONESCALAR',
    'capitalizar' : 'CAPITALIZAR',
    'colineales' : 'COLINEALES',
    'print' : 'PRINT',
    'length' : 'LENGTH',
    'OR' : 'BOOL_OP',
    'AND' : 'BOOL_OP',
    'NOT' : 'NOT'
}

types = set(['int', 'float'])

def t_TRUE(token):
    "true"
    token.value = {"value": token.value, "line": token.lexer.lineno}
    return token

def t_FALSE(token):
    "false"
    token.value = {"value": token.value, "line": token.lexer.lineno}
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

def t_STRING(token):
    r"\"[^\"]*\""
    token.value = {"value": token.value[1:-1], "line": token.lexer.lineno}
    return token

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VAR')    # Check for reserved words

    if t.type == 'VAR':
        t.value = {"value": t.value, "type": t.type, "line":t.lexer.lineno}

    return t

def t_MEQUAL(token):
    r"\-="
    return token

def t_PEQUAL(token):
    r"\+="
    return token


def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

def t_COMMENT(token):
    r"\#.*"
    token.value = {"value":token.value.strip(), "line":token.lexer.lineno }
    return token

t_ignore = " \t"

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
