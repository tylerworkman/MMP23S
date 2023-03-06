from time import process_time
from sys import exit

def fib():
    def getFib(n_int,total_time=None):
        if n_int > 1:
            fib = getFib(n_int-1)[0] + getFib(n_int-2)[0];
        elif n_int == 1:
            fib = 1
        else:
            fib = 0
        if total_time is None:
            total_time=float(process_time())
        else:
            total_time=total_time+float(process_time())
        return fib,total_time

    n = input('Please enter a non-negative integer or type stop: ')
    if n=="stop":
        return None
    else:
        n = int(n);
        result,runtime=getFib(n)
        print( "fib({}) = {}".format(n,result) );
        print("average runtime: ",str(runtime)," seconds")
        fib()
        return None
fib()
