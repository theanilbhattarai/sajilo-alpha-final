"""
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x -y
    elif operator == 'mul':
        reutnr x * y 
    elif operator == 'div':
        return x /y
    else:
        return None

dispatch_if('mul',2,8)
"""

# An example of implementation of the switch statment in the possible way.
# I could do this instead of doing the grand if or regex for the 
def dispatch_dict(operator, x, y):
    return {
        'add' : lambda: x + y,
        'sub' : lambda: x -y,
        'mul' : lambda : x * y,
        'div' : lambda: x / y,
    }.get(operator,lambda : None)()