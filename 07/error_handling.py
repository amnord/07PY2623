# '''

# try:
# 	pass
# except:
# 	pass
# else:
# 	pass
# finally:
# 	pass


# NameError, FileNotFoundError

# '''
old_var = 'Hello'

# open('demofile.txt')

try:
	f = open('demo_file.txt')
	message = old_var

except NameError as e:
	print(e)

except FileNotFoundError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(message)
	print(f.read())
	f.close()

finally:
	print('Executing...')
