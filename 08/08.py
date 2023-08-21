def square(x):
	return x * x



# # print(square(5))
# # result = square(5)
# # print(result)

# result = square
# print(result(5))

def cube(x):
	return x * x * x

nums = [1,2,3,4]

def my_map(my_lst, func):
	result = []
	for i in my_lst:
		result.append(func(i))
	return result


print(my_map(nums, cube))


