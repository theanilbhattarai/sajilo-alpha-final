 ### Notes from the book - Building your own lisp.

Running C code :
`cc -std=c99 -Wall 'file_name' -o 'output_binary_name'`

Here in the code, -std=c99 means that we are using the standard version of c.
To run the code, just run ./output_binary_name 

#### Errors
1. Debugging C programs is hard.
2. If you are a beginner use a lot of print statements.
3. If you are somewhat confident you can use a program called `gdb` 
4. ON mac we can use `valgrind` for memory leakds or lldb.

5. Documentation of the standard library.

#### C Programs
A C program only consists of functions and structure defintions. Therefore source file is simply a list of functions and types. These functions can call each other or themselves, and can use any data types that have been declared or are built into the language.

It is possible to call functions in other libraries, or to use their data types. This is how layers of complexity are accumulated in C programming. 

A C program always starts with the main and from here it can call more and more functions to perform all the action it requires.

#### Variables.
C functions are all about manipulating variables. these are items of data which we give a name to.
Every varaiable in C has an explicit type. 
- These types can be declared by user 
- Some types are built into the language.

To create a a new `int` called `count` we could write:
`int count;`
Or we can also initialize the variable when we declare it.
`int count = 10`

##### Some built in types in C.
1. `void` : Empty Data type
2. `char` : Single Character/Byte `char last_ini = 'H'`
3. `int` : Integer `int age = 23`
4. `long` : integer that can hold large values. `long age_of_universe = 13798000000;`
5. `float` : Decimal number `float age = 22.0568f;`
6. `double` : Float value with double precision. `double age = 22.9039230`

### Declaring Functions

A function is a computation that manipulates variables, and optionally changes the state of the program. If the function only manipulates variables that is a function without a side effect.

To declare a function in c we write the type of the variable it returns, the name of the function, and then the parenthesis a list of variables it takes as input, separted by commas. the contents of the function are put inside curly brackets `{}`, and lists all of the statements the function executes, terminated by semicolors`;`. A `return` statement is used to let the function finish and output a variable.

1. A simple function in C:
<!-- So this is how you do multi line codes-->
```
int add_nums(int x, int y) {

    int result = x + y;
    return result;
}
```

Here the function takes in x and y as integer and add them together. When function ends, it outputs a integer result.

We can call functions by writing their name and putting the arguments to the function in parenthesis, separated by commas. For example to call the above function and store result in variable `result` we would do something like below:

`int result = add_nums(10,10)`

###### Note: We need to declare functions before main if we declare them below main and want to use them on the main and the main is on top.

`int add_nums(int x, int y);`


### Declaring structures or structs
###### Structs are user defined types.
Structures are used to declare new types. Structures are several variables bundled together into a single package.
1. We can use structure to represent more complex data types. For instance : a point in 2D space we could create a struct called point that packs together two `float` values `x` and `y`. 
We can declare structures by using keywords `typedef` and `struct` in conjuction.

###### Syntax :
```
typedef struct {
    float x;
    float y;
}point;
```
###### Use
If we want to use the structures we defined. We need to do it above the functions where we want to use it. 

This type is not different from built in types, and we can use it in all the same ways. To access an individual field we use a dot `.` operator, followed by the name of the field, `x` in this example.

```
point p;
p.x = 0.1;
p.y = 10.0;

//formula, l = sqrt(sqr(x) + sqr(y))
float length = sqrt(p.x * p.x + p.y * p.y)

```
###### Remember to initialize the structs before you use them.


### Pointers -- very important and misunderstood.

A pointer is a variation on a normal type where the type name is suffixed with an asterisk. For instance we can declare a pointer to an integer by writing
`int*`. We already saw the pointer type `char** argv`. This is a pointer to pointers to characters, and is used to input to `main` function.

1. Pointers are used as reference to the value of the variables.
2. They can also be used other different things such as strings or lists.
3. These are ont of the most difficult part of C

###### There is separarte file for pointers to look for.

### Strings
In C strings are represented by the pointer type char*. Under the hood they are stored as a list of chars, where the final char is called the null terminator. 

String processing is tiny bit complicated in C. We can also declare strings with "" likee `"My name is Anthony"`.

### Conditional :IFFF
Conditional statments let the program execute an action only when certain conditions aree met.

To preform code under some conditions we use the `if` statement. This is writteen as `if` followed by some condition in parentheses, followed by the code to executee in curly braces. An `if` stament can be followed by an optional `else` statment, followed by other statements in curly braces. The else block only executes if the condition is false.

We can test for multiple conditons as well. 
1. `||` for OR
2. `&&` for AND

Inside a conditional statement's parentheses any value that is not `0` will evaluate to true. 
>> This is important to rem as many conditions use this to check things implicitly.

If we wished to check if `int` in `x` was greater than `10` and less than `100`, we would write:

```
if ( x > 10 && x< 100) {
    puts("x is greater than 10 and less than 100");
}
else {
    puts("X is less than 11 or greater than 99");
}
```

### Loops 

Loops allow for some code to be repeateed until some condition becomes false, or some counter elapses.

There are two main loops in C. The first is a `while` loop. this loop repeatedly executees a block of code until some condition is false. It is written as:

```
int count = 0;
while(count > 10){
    printf(count);
    count = count + 1;
}
```

The second kind of loop is a `for` loop. Rather than a condition, this loop requires three expressions separated by semicolos `;`.
These are:
1. The initialiser
2. Condition
3. Incrementer/Decrementer

for example:

```
for (int i = 0; i < 10; i++) {
    puts("Loop Iteration");
}
```
