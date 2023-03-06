This folder contains the answers and code for the assigned tasks from HW2, as well as brief descriptions. </line>
  
**IEEE-Storage Convention for Real Numbers:** 404 Error, webpage of this task was either mis-linked or doesn't exist </line>
  
**Integer Overflow:** Trying to increase an integer value above the storage limit of its variable causes an overflow error, sometimes referred </line>
to as a "roll-over", where trying to increase by 1 instead ends up rolling the value back to the variable's minimum stored value. (127+1= -128). </line>
This roll-over happens in the opposite direction: trying to subtract from the minimum value rolls over to the maximum. Int8 has max/min values of 127/-128, </line>
Int16 has max/min values of 32767/-32768, and Int32 has max/min values of 2147483647/-2147483648. </line>
  
**Python Aliasing vs Copying Variables:** For Part A, when declaring a variable as another variable, it appears to assign the original variable's </line>
ID to the new one. However, redeclaring the variable with a new value appears to reassign it a new ID. For Part B, there are some functions in </line>
Python which edit an original value rather than overriding the original (such as the append function). These functions do not reassign an ID. </line>
Part C shows one of two things, though which it is I'm unsure of. Either modifying a variable's type reassigns the ID, or pulling values from </line>
a variable to assign them doesn't copy the original's ID. Part D indicates that assigning a variable as the entire range of values of an array </line>
copies the ID of that array. </line>
  
**Python script call from the Bash command line:** See attached file "script_call.py"
  
**Python Modifying the index of a for-loop:** From the output of the code snippet, it appears that modifying the contents of a list (which the for </line>
loop used as its point of reference) can change the current index in that loop. In this case, the loop skipped the indeces 4-7 because those had been deleted by the program.
  
**Impact of machine precision on numerical computation:** The code snippet is halfing the value of eps at each iteration. Mathematically, eps will </line>
never reach 0 (you'll always be able to divide it by 2 to a nonzero number again), but the computer can only store so small a number for computing. </line>
Once the eps variable gets below this precision, the computation treats it as though it were 0. </line>
  
**Impact of round-off errors on numerical computations:** The code snippet takes the number 2, then square roots that number multiple times before </line>
squaring the remaining number that many times. In theory, the math should cancel out and return to the original 2, but since the computer can only </line>
store so many digits, it must round to a certain number of digits, which leads to a decrease in accuracy. As the number of times we root/square </line>
increases, this inaccuracy becomes worse and worse until eventually the computer thinks the original is 1 instead of 2. </line>
  
**String concatenation using for-loop:** Included is my code snippet "String-Concatenation.ipynb", where I solve this problem manually. There are, </line>
however, some ways to solve this problem using libraries that have a dedicated concatenate function. </line>
  
**Computing the Fibonacci sequence via for-loop:** Ran into an issue with attempting to get the whole runtime, which meant leaving variable undeclared, </line>
hence the weird parameter on getFib(). Changed how results are displayed to prevent doubling of runtime,
