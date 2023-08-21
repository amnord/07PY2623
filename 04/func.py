
# def hello_func(message):
# 	return message

# def hi_func(message):
# 	return message


# hello_func('Hello')
# print(hi_func('Hi'))




def emp_details(*args, **kwargs):
	print(args)
	print(kwargs)

emp_details('Java', 'Python', name='John', email='J@company.com')
# emp_details('Python')