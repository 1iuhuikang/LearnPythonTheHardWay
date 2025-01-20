# class MyStuff(object):

# 	def __init__(self):
# 		self.tangerine = "And now a thousand years between"

# 	def apples(self):
# 		print("I AM CLASSY APPLES!")

# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)


# #dict style
# MyStuff['apples']

# #module style
# MyStuff.apples()
# print(MyStuff.tangerine)

# #class style
# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()