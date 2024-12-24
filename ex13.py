# from sys import argv
# # read the WYSS section for how to run this
# script, first, second, third = argv

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

from sys import argv

script, name, height = argv

weight = input("what is your weight?")

print(f"This srcipt named {script}, and you are {name}, {height} tall, {weight} heavy.")