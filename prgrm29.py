
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)


def get_even_odd_sum(N):
    sum_even, sum_odd = (0, 0)
    for i in range(1, N+1):
        if i%2:
            sum_odd += i
        else:
            sum_even += i
    return (sum_even, sum_odd)

(X, Z) = get_even_odd_sum(b)
c = float(X/n)
d = float(Z/n)
print ("Sum of even=",X)
print ("Sum of odd=",Z)
print("average of even=", c)
print("average of odd=", d)