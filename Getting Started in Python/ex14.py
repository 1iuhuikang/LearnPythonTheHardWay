from sys import argv

script, user_name, user_nickname = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"{user_nickname}, I'd like to ask you a few question.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")