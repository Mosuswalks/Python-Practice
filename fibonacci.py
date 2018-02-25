"""
Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.

(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the 
sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""




def Fibonacci(fibNum):
    
    print("Enter the amount of Fibonacci numbers you'd like.")
    fiboNum = int(input())

    i = 1

    if fiboNum == 0
        fib = []
    elif fiboNum == 1
        fib = [1,1]
    elif fiboNum == 2
        fib = [1,1]
    elif fiboNum > 2:
        while i < (fiboNum - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    
    return fib

print(Fibonacci(fiboNum))

