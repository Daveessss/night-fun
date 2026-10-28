number = (10,20,30,40)
print("original Tuple: ", number)
number = number + (50,)
print("New Tuple: ", number)

number_list = (1,2,[3,4],5)
number_list[2][1] = 99
print(number_list)

fruits = ('apple', 'banana', 'cherry')
fruits_list = []
for index in fruits:
	fruits_list.append(index)
print(fruits_list)
fruits_list.append('mango')
print("converted list: ",fruits_list)
fruits_tuple = tuple(fruits_list)
print("converted tuple: ",fruits_tuple)

new_numbers = (10,20,30,40)
new_list = []
for index in new_numbers:
	new_list.append(index)
#print(new_list)
a = new_list[0]
b = new_list[1]
the_rest = new_list[2],new_list[3]	
print("A: ", a, "\n" "B: ", b,"\n" "Rest: ", the_rest )

numbers = [[2,3,4],[1,5,7],[4,6,8]]
result = []
for index in numbers:
	sums = 0
	for count in index:
		sums += count
	result.append(sums)
		
print(sums)

numbers = [[2,3,4],[1,5,7],[4,6,8]]
result = []
for index in range(len(numbers[0])):
	sums = 0
	for count in numbers:
		sums = sums + count[index]
	result.append(sum)
	

	
def get_even(number):
		if number % 2 == 0:
			return number

numbers = list(range(1, 21))
	
list_range = filter(get_even,numbers)
print(list_range)
