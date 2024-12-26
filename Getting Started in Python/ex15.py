from sys import argv
#import argv

script, filename = argv
#get input from user

txt = open(filename)
#open the file, get back a "file" object

print(f"Here's your file {filename}:")
#nosense
print(txt.read())
#print file.read()

print("Type the filename again:")
file_again = input("> ")
#another way to get input from user

txt_again = open(file_again)
#open file again

print(txt_again.read())
#print

txt.close()
txt_again.close()
#close the io stream