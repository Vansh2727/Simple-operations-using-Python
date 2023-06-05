'''Write a program that gets an integer N > 1 from the user and computes the average 
of all integers I = 1, … , N. The computation should be done in a function that takes 
N as input parameter. Print the result to the screen with an appropriate text. Run the 
program with N=5 and confirm that you get the correct answer.
'''
def average(N): #creating a function with parameter 'N'.
    a=0
    for i in range(N+1):
        a+=i
    avg=(a/N) #Calculation for average.
    print("tThe Average is: {}".format(avg))
N=int(input("Enter The Integer To Calculate Average (greater than 1): "))

if N>1: #if else stament if the number entered is less than 1.
    average(N)
else:
    print("Please Enter Number Greater Than 1.")