## Grammar for the sajilo language syntax


### Parsing Method : LR Parsing

#### Precedence
```
precedence = (

    ('left', 'NOT'),

    ('left', 'PLUS', 'MINUS'),

    ('left', 'MUL', 'DIV'),

    ('left', 'EXP', 'MOD'),

    ('right', 'UMINUS'),

    ('right', 'UPLUS'),

)
```

#### Expression
```
    expression : primitive
               | STRING
               | identifier
```

#### Statement
```
    statement : identifier
              | expression
              | if_statement
```

#### Statement List

```
    statement_list : statement
                   | statement_list statement
```

#### Identifer
```
    identifier : IDENTIFIER
```

#### Primitives
```
    primitive : NUM_INT
              | NUM_FLOAT
              | STRING
              | boolean
```

#### Exit Statement
```
    statement : EXIT STMT_END
```

### Ops

#### Binary Operation expression
```
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
```

#### Boolean Operators
```
    boolean : expression EQ expression
            | expression NEQ expression
            | expression GT expression
            | expression GTE expression
            | expression LT expression
            | expression LTE expression
            | expression AND expression
            | expression OR expression
```

#### Unary Operations
```
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
               | BIT_NEG expression
               | NOT expression
```

## Ternary Operations
```
    expression : expression QUESTION_MARK expression COLON expression
```

#### Parenthesis
```
    expression : LPAREN expression RPAREN
```

#### Boolean
```
    boolean : TRUE
            | FALSE
```

#### Assignment
```
    assignable : primitive
               | expression
```
#### Comma Separated expressions
```
    arguments : arguments COMMA expression
              | expression
              |
```

#### Accessing array
```
    expression : identifier LSQBRACK expression RSQBRACK
```

#### Array Slice

```
    expression : identifier LSQBRACK expression COLON expression RSQBRACK
               | identifier LSQBRACK COLON expression RSQBRACK
               | identifier LSQBRACK expression COLON RSQBRACK
               | identifier LSQBRACK COLON RSQBRACK
```

#### Array Access Assignments
```
    statement : identifier LSQBRACK expression RSQBRACK EQUALS expression STMT_END
```

#### Assignment
```
    expression : identifier EQUALS assignable STMT_END
```

#### IF Statement
```
    if_statement : IF expression LBRACK statement_list RBRACK
```

#### IF/ ELSE Statement
```
    if_statement : IF expression LBRACK statement_list RBRACK ELSE LBRACK statement_list RBRACK
```

#### IF / ELSE / ELSE IF 
```
    if_statement : IF expression LBRACK statement_list RBRACK ELSE if_statement
```

#### IN/LAI Expression
```
    expression : expression IN expression
               | expression NOT IN expression
```

#### Print statement
```
    statement : PRINT arguments STMT_END
```

#### Compound Operations
```
    statement : identifier PLUS_EQ expression STMT_END
               | identifier MINUS_EQ expression STMT_END
               | identifier MUL_EQ expression STMT_END
               | identifier DIV_EQ expression STMT_END
               | identifier EXP_EQ expression STMT_END
               | identifier MOD_EQ expression STMT_END
``` 

#### Increment and Decrement 
```
    expression : identifier DOUBLE_PLUS
               | identifier DOUBLE_MINUS
```

#### Expression
```
    expression : primitive
               | STRING
               | identifier
```

#### For loop
```
    statement : FOR identifier IN expression ARROW_LTR expression LBRACK statement_list RBRACK
              | FOR identifier IN expression ARROW_RTL expression LBRACK statement_list RBRACK
```

#### For loop with in
```
    statement : FOR identifier IN expression LBRACK statement_list RBRACK
```
#### While loop
```
    statement : WHILE expression LBRACK statement_list RBRACK
```

#### Infinite for loop
```
    statement : FOR LBRACK statement_list RBRACK
```

#### Function Declartions
```
    statement : FUNCTION identifier LPAREN arguments RPAREN LBRACK statement_list RBRACK
              | FUNCTION identifier LBRACK statement_list RBRACK
```

#### Returns statement
```
    statement : RETURN expression STMT_END
```

#### Function call

```
    expression : identifier LPAREN arguments RPAREN
    statement : identifier LPAREN arguments RPAREN STMT_END

```

