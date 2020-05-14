# Handwritter Lexer and Parser for the Sajilo Programming Language Prototype.

#### Project Details
>> 1. PR no : 2
>> 2. Completion : 40% 
>> 3. Date

## Things done
1. Handwritten lexer implmented with the text comparison with IFs.
2. Token identified and Implmentented to some aspect.
3. Implmented an error class and identified the way I will show errors.
4. Lexer can perfectly tokenize the chars as PLY would do.

## Left to do
1. Try and implment Handwritten parser for the AST
2. Implment an interpreter for the simple expressions.

## Why do it?
1. Understand how Lexers are implemented before using PLY for the final prototype to be implmented.
2. Research and experiment with few keywords for the syntax.
3. Research and experiment with writing BNF grammar.
4. It is fun to experiment with REPL/Shell

## Why left it?
1. It became execedingly difficult to parse the tokens and resolve the grammar issues.
2. It is not a good idea to use classes in Python

## Screenshots/Demo
### 1. Working Lexer
!["Working Lexer"](Results.png "Working Lexer")

### 2. REPL
!["Working Lexer"](shell.png "Working Lexer")

### 3. Debugging the Lexer
!["Working Lexer"](Debug.png "Working Lexer")

### 4. Reserved Keywords 
>> Everything will be subjected to change down the line.
!["Keywords"](keywords.png "Reserved Keywords")

### 5. Example Program
>> Syntax will be subjected to change
!["Example Program"](eg2.png "Example Program")

### 6. Example Program Output
!["Output"](eg1.png "Output")

### 7. Example Program 2
!["Area of Rect"](synt.png "Area of Rectangle")

## Ressources
1. https://repl.it/talk/learn/Making-your-own-programming-language-with-Python/45767
2. https://www.youtube.com/watch?v=Eythq9848Fg&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD 
>> The Youtube Tutorial is very intuitive to follow along but it promotes very bad programming practices.

## Lessons learned
1. It is really difficult to parse text with handwritten lexer even in Python,
I can hardly imagine how much code would I have to write for C/CPP
2. Working with REPL and infinite loops.
3. Language Syntax
4. Semicolor `;` doesn't look as awesome or intuitive as I thought.
5. I may not be able to implment while loop in the time specified.
6. I may not able to implment wait
