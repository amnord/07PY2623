result = 'Hello'

def find_index(args_lst, target):
	for index, item in enumerate(args_lst):
		if item == target:
			print(f"The index of '{item}' is {index}")
