things = ['a', 'b', 'c', 'd']
# print(things[1])
things[1] = 'z'
# print(things[1])
# print(things


stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
# print(stuff['name'])
# print(stuff['age'])
# print(stuff['height'])
stuff['city'] = 'SF'
# print(stuff['city'])

stuff[1] = "wow"
stuff[2] = "Neato"
# print(stuff)

stuff.pop('city')
stuff.pop(1)
stuff.pop(2)

# print(stuff)

##########################

#create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California':'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of state and some cities in them
cities = {
	'CA': 'San Fancisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'*10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

#print out some states
print('-'*10)
print("Michigan's abbreviation is : ", states['Michigan'])
print("Florida's abbreviation is : ", states['Florida'])

#do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-'*10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-'*10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' *10)
#safely get a abbreviation by state that might not be here
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")
