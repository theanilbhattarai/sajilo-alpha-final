import ply.yacc as yacc
from sajilo.lexer import *
from sajilo.exceptions import *

disable_warnings = False

precedence = (
    ('left', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'EXP', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS'),
)


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    else:
        p[1].children.append(p[2])
        p[0] = p[1]


def p_statement(p):
    '''
    statement : identifier
              | expression
              | if_statement
    '''
    p[0] = p[1]


def p_identifier(p):
    '''
    identifier : IDENTIFIER
    '''
    p[0] = ast.Identifier(p[1])


def p_exit_stmt(p):
    '''
    statement : EXIT STMT_END
    '''
    p[0] = ast.ExitStatement()


def p_primitive(p):
    '''
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
    '''
    if isinstance(p[1], ast.BaseExpression):
        p[0] = p[1]
    else:
        p[0] = ast.Primitive(p[1])


def p_binary_op(p):
    '''
    expression : expression PLUS expression %prec PLUS
            | expression MINUS expression %prec MINUS
            | expression MUL expression %prec MUL
            | expression DIV expression %prec DIV
            | expression EXP expression %prec EXP
            | expression MOD expression %prec MOD

            | expression BIT_AND expression
            | expression BIT_OR expression
            | expression BIT_XOR expression
            | expression LSHIFT expression
            | expression RSHIFT expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])

def p_boolean_operators(p):
    '''
    boolean : expression EQ expression
            | expression NEQ expression
            | expression GT expression
            | expression GTE expression
            | expression LT expression
            | expression LTE expression
            | expression AND expression
            | expression OR expression
    '''
    p[0] = ast.BinaryOperation(p[1], p[3], p[2])


def p_unary_operation(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | BIT_NEG expression
               | NOT expression
    '''
    p[0] = ast.UnaryOperation(p[1], p[2])


def p_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2] if isinstance(p[2], ast.BaseExpression) else ast.Primitive(p[2])


# Parse the boolean expression
def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = ast.Primitive(p[1])


def p_assignable(p):
    '''
    assignable : primitive
               | expression
    '''
    p[0] = p[1]


def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | expression
              |
    '''
    if len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
    elif len(p) == 1:
        p[0] = ast.InstructionList()
    else:
        p[1].children.append(p[3])
        p[0] = p[1]


def p_ternary_op(p):
    '''
    expression : expression QUESTION_MARK expression COLON expression
    '''
    p[0] = ast.TernaryOperator(p[1], p[3], p[5])

def p_arrays(p):
    '''
    expression : LSQBRACK arguments RSQBRACK
    '''
    p[0] = ast.Array(p[2])


def p_array_access(p):
    '''
    expression : identifier LSQBRACK expression RSQBRACK
    '''
    p[0] = ast.ArrayAccess(p[1], p[3])
