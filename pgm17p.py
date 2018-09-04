import sys

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y







a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]
j=0
i=1

for j in range(0,4,2):
	
	{

		for i in range(1,4,2):
			if (argv[i]=='+'):
			{
				d= add(num1,num2)
				i=i+2;
			}
			elif (argv[i] == '-'):
			{
				d= subtract(argv[j],argv[j+2])
				i=i+2;
			}

			elif (argv[i] == '*'):
			{
				d = multiply(argv[j],argv[j+2])
				i=i+2;
			}
			elif(argv[i] == '/'):
			{
				d = divide(argv[j],argv[j+2])
				i=i+2
			}
			else :
				print("Invalid input")

		j=j+2
	}

print(d)



