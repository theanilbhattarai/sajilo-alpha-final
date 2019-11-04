import lexer

while True:
    text = input(
        'Namaste!!\n'
        'Sajilo Shell >>'
    )
    if text == "exit()": exit()
    result, error = sajilo.run('Shell',text)
    if error: print(error.as_string())
    print(result) 
