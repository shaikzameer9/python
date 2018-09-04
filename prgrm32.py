fname = input("Enter file name: ")
num_students = 0
with open(fname, 'r') as f:
    for line in f:
        num_students += 1
print("Total Number of students:")
print(num_students)





