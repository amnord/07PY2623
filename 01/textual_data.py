"""
Anything in between ' ', " ", """ 
""", ''' ''' is Textual Data --> Strings
"""

# name = z
# greeting = 'Hello'

# message = greeting + ',' + ' ' + name +'!'
# message = "{}, {}!".format(greeting, name)
# message = f"{greeting}, {name}!"

#[start:stop]
# print(name[11:15])


# Numbers: Whole Number ---> integers , Decimals --> floats

num_1 = '2000'
num_2 = '3000'

result = float(num_1) + float(num_2)
print(f"The sum of '{num_1}' and '{num_2}' is '{result}'")