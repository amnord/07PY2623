# def outer_func(message):
# 	def inner_func():
# 		print(message)
# 	return inner_func

# my_func = outer_func('Hello')
# my_func()


def dec_func(func):
	def wrapper_func(*args, **kwargs):
		print('Hello world')
		return func(*args, **kwargs)
	return wrapper_func

@dec_func
def display():
	print('This is the display function')

@dec_func
def emp_info(name, age):
	print(f"emp_info ran with args '{name}' '{age}'")

# my_disp = dec_func(display)
# my_disp()

emp_info('John', 30)