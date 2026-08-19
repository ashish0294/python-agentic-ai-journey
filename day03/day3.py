name="Ashu"
city="Mumbai"
message="I am learning Python"

user_input="Remember that I like short explanations"

print(name[0])
print(city[3])
print(message[-2])
print(user_input[0:8]) #start is included, end in not included
print(user_input[:8])
print(message[5:])
print(name.upper())
print(name.lower())

text_with_space="       this is a text with space        "
print(text_with_space.strip())
print(user_input.replace("short","long"))
print(len(name))

words=text_with_space.split()
print(words)

sentence="$$".join(words)
print(sentence)

sentence.upper()
print(sentence)
sentence=sentence.upper()
print(sentence)

#task

name="Ashu"
city="Mumbai"
profession="IT Engineer"
description="I am learning Python to keep up with AI"

print(name)
print(city)
print(profession)
print(description)

print(name[0])
print(name[len(name)-1])
print(name[:3])

why_learn="I am learning Python for AI"
print(why_learn)
why_learn=why_learn.upper()
print(why_learn)
why_learn=why_learn.lower()
print(why_learn)
print(len(why_learn))
words=why_learn.split()
print(words)

name="Ashu"
age=40
city="Mumbai"

message1=f"My name is {name}, I am {age} years old, and I live in {city}"
print(message1)
message2=message1.upper()
print(message2)














