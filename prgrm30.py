'''to print pyramid'''
def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*",end="")
        print("\r")
 
# Driver Code
n = 6
pypart(n)