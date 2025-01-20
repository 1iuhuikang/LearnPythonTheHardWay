# i = 0
# numbers = []

# while i < 6:
# 	print(f"At the top i is {i}")
# 	numbers.append(i)

# 	i += 1
# 	print("Now number is ", numbers)
# 	print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
# 	print(num)

def while_loop(i,j):
	numbers = []

	while i < 6:
		print(f"At the top i is {i}")
		numbers.append(i)

		i += j
		print("Now number is ", numbers)
		print(f"At the bottom i is {i}")

	print("The numbers: ")
	
	for num in numbers:
		print(num)

while_loop(1,2)

def for_lop(i,j):
	numbers = []

	for k in range(i,6,j):
		numbers.append(k)

	print("The numbers: ")
	for num in numbers:
		print(num)

for_lop(1,2)
