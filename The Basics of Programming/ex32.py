the_count = [1,2,3,4,5]
fruits = ['apple','orange','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#the fisrt kind of for-loopgoes through a list
for number in the_count:
	print(f"This is count {number}")

#also we can go through mixed lists too
for i in change:
	print(f"I got {i}")

#we can also build lists, first start with an empty one.
elments = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print(f"Adding {i} to the list.")
	#append is a function that lists understand
	elments.append(i)

#now we can print them out too
for i in elments:
	print(f"Elments was: {i}")