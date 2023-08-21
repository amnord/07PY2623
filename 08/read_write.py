# f = open('new_file.txt', 'r')

# print(f.closed)
# print(f.read())


# f.close()


# with open('new_file.txt', 'r') as f:
	
# 	for i in f:
# 		print(i, end='')


# with open('demo.txt', 'w') as f:
# 	f.write('Demo')
# 	f.seek(0)
# 	f.write('Hello world!')


with open('new_file.txt', 'r') as rf:
	with open('file_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)