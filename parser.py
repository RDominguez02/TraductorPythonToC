# parser.py
import ply.yacc as yacc
from lexer import tokens

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POW'),
    ('left', 'MOD'),
    ('nonassoc', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'),  # Operadores de comparación
)

# Reglas de producción
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression_statement
                | if_statement
                | while_statement
                | for_statement
                | print_statement
                | assignment_statement'''
    p[0] = p[1]

def p_expression_statement(p):
    '''expression_statement : expression'''
    p[0] = ('EXPR', p[1])

def p_if_statement(p):
    '''if_statement : IF expression COLON block ELSE COLON block
                   | IF expression COLON block'''
    if len(p) == 5:
        p[0] = ('IF', p[2], p[4])
    else:
        p[0] = ('IF_ELSE', p[2], p[4], p[7])

def p_while_statement(p):
    '''while_statement : WHILE expression COLON block'''
    p[0] = ('WHILE', p[2], p[4])

def p_for_statement(p):
    '''for_statement : FOR ID IN expression COLON block'''
    p[0] = ('FOR', p[2], p[4], p[6])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('PRINT', p[3])

def p_assignment_statement(p):
    '''assignment_statement : ID EQUALS expression'''
    p[0] = ('ASSIGN', p[1], p[3])

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = p[2]

def p_expression(p):
    '''expression : expression PLUS expression
                 | expression MINUS expression
                 | expression TIMES expression
                 | expression DIVIDE expression
                 | expression POW expression
                 | expression MOD expression
                 | expression GT expression
                 | expression LT expression
                 | expression GE expression
                 | expression LE expression
                 | expression EQ expression
                 | expression NE expression
                 | LPAREN expression RPAREN
                 | LBRACKET expression_list RBRACKET
                 | NUMBER
                 | ID'''
    if len(p) == 2:
        p[0] = ('NUM', p[1]) if isinstance(p[1], int) else ('ID', p[1])
    elif p[1] == '[' and p[3] == ']':
        p[0] = ('LIST', p[2])
    else:
        p[0] = (p[2], p[1], p[3])

def p_expression_list(p):
    '''expression_list : expression
                      | expression_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    raise SyntaxError(f"Error de sintaxis en '{p.value}'")

# Construir el parser
parser = yacc.yacc()