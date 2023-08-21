# def hi_func(message='Hi'):
# 	return message


# print(hi_func('Hello'))

# nums = ['Hi', 'Hello', 'hey']

# for i in nums:
# 	if i == 'Hello':
# 		print('Found!')
# 		continue
# 	print(i)

# print(list(range(100)))

# for i in range(100):
# 	print('Hello')

# x = 0

# while x < 10:
# 	print(x)
# 	x+=1



# LEGB : Local --> Enclosing --> Global --> Builtins

# x = 'global x'

# def outer_func(arg):
# 	# x = 'local x'
# 	# print(x)
# 	print(arg)

# outer_func('hi')
# print(arg)

# nums = [100,2,91,1]

# # def min():
# # 	pass

# print(min(nums))


# import builtins

# # print(dir(builtins))
# print(help(min))

x = 'global x'
def outer_func():
	x = 'outer x'

	def inner_func():
		x = 'inner x'
		print(x)
	inner_func()

	print(x)

outer_func()