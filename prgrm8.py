tuple_a = ('Apple', 'Banana', 'pineapple', 'Pomagrenat')
tuple_b = ('Potato', 'Brinjal', 'tomato', 'onion')
my_list = list(zip(tuple_a,tuple_b))

for val in range(len(my_list)):
	print (my_list[val])


