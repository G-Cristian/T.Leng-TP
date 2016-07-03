import pdb
tokens = [
    # aritmeticos
    'AO',
    # ++/--
    'DOUBLE_AO',
    # asignacion
    'EQUAL',
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
t_DOUBLE_AO = r"\+\+|\-\-"
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

t_MULTIPLICACIONESCALAR = "multiplicacionEscalar"
t_CAPITALIZAR = "capitalizar"
t_COLINEALES = "colineales"
t_PRINT = "print"
t_LENGTH = "length"
t_IF = "if"
t_ELSE = "else"
t_FOR = "for"
t_WHILE = "while"
t_DO = "do"

t_BOOL_OP = r"AND|OR"
t_NOT = 'NOT'


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
    r"\".*\""
    token.value = token.value[1:-1]


def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

def t_COMMENT(token):
    r"\#.*"
    # token.value = token.value.strip()
    # token.line = token.lexer.lineno
    token.value = {"value":token.value.strip(), "line":token.lexer.lineno }
    return token

# t_VAR = r"[_a-zA-Z][_a-zA-Z0-9]*"
t_ignore = " \t"

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)
