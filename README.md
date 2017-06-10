Two-Bit!

This language is still in the developmental stages!  This means that things can change quickly.  Whenever changes happen, all old compilers will be left alone, but a new folder will be added with the new compiler.  If code from somewhere else isn't working, make sure you have the correct version of the compiler!

This language has three types of of variable.  The first one is pushed, which is automatically recieved by each commands as input.  If the command does nothing with pushed, it typically simply pushes what was pushed to it.  The second is Array, an array which can be accessed by index.  The third is Output, which is also an array accessed by index.  At the end of the program, if Output is empty, pushed will automatically be outputted, otherwise the contents of Output will be.  

Commands:

0-Seperates commands

1-Adds pushed to its argument.  Not providing any argument results in pushed being doubled

2-Subtracts its argument from pushed.  Not providing any argument results in 0 being pushed

3-Multiplies its argument and pushed.  Not providing any argument results in pushed being squared



11-Divides pushed by its argument.  Not providing any argument results in 1 being pushed

12-Replaces the index of Array equal to its argument with its second argument.  

13-Checks if pushed is prime, pushes 1 if it is, and 0 if it isn't

21-Checks if its two arguments, or pushed and its argument, are equal, returning 1 for true, and 0 for false

22-Checks if its two arguments, or pushed and its argument, are not equal, returning 1 for true, and 0 for false

23-Checks if its first argument is greater than its second argument, or pushed if there is no second argument, returning 1 for true, and 0 for false

31-Checks if its first argument is less than its second argument, or pushed if there is no second argument, returning 1 for true, and 0 for false

32-Pushes the value at the indice of Array equal to its argument.  Can also be used as an arugment, to give the value at the index of Array equal to its argument.  

33-Prepends numbers for arguments.  

111-If pushed is not 0, the next command will be performed, otherwise, the next command will be skipped

112-Pushes the cube of pushed

113-Pushes pushed to the power of its argument

121-Pushes the argumentth root of pushed

122-Pushes the square root of pushed

123-Pushes the cubed root of pushed

133-Pushes its argument

211-Empties Array

212-Pushes the sine of pushed

213-Pushes the cosine of pushed

221-Pushes the tangent of pushed

222-Push pushed plus 1

223-Apppends its argument to Output

231-Push pushed minus 1

232-Appends pushed to Output

233-Empties Output

311-Pushes a really big number that I am currently calculating

312-Randomly pushes either 0 or 1

313-Pushes the number at the pushed index of the Fibonacci Sequence

321-Push the number at index 0 of Array

322-Sets index 0 of Array to pushed

323-Pushes the prime factors of pushed to Array starting at index 0 and going up
