branches = ['EWT', 'ESI', 'AES', 'VLSI', 'ES']

branches.append('BIG DATA')

# to Appended List
print('Appended List is: ', branches)

branches.insert(3, 'IOT')

# to Inserted List
print('Inserted List is: ',branches)

branches.sort()

# to get Ascending Order(Sort)
print('Sorted list: ', branches)

branches.sort(reverse = True)

# to  get Descending Order(Reverse Sort)
print('Sorted list(Descending Order): ', branches)
