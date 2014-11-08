def nth_fib(n):
        if n == 1 or n == 2:
                return 1

        x = 1 
        y = 1 

        for i in range(3, n+1):
                fib_i = x + y 
                x = y 
                y = fib_i

        return y 

def fib_len(length):
    
        i = 3 

        while True:
                fib = nth_fib(i)
                if len(str(fib)) == length:
                        return i    
                i += 1

#fib_seq
