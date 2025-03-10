# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'POW',
    'MOD',
    'EQUALS',
    'ID',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'PRINT',
    'COLON',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'GT',       # >
    'LT',       # <
    'GE',       # >=
    'LE',       # <=
    'EQ',       # ==
    'NE',       # !=
    'IN',       # in
)

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT',  # Asegúrate de que 'print' esté asociado al token 'PRINT'
    'in': 'IN',
}

# Reglas para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\^'
t_MOD = r'%'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='
t_IN = r'in'

# Regla para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para identificadores (variables)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es una palabra reservada
    return t

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    raise SyntaxError(f"Carácter ilegal '{t.value[0]}' en la posición {t.lexpos}")

# Construir el lexer
lexer = lex.lex()