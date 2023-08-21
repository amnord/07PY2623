message = 'Hi, Hey, Hello'

# # ['item1', 'item2', 'item3']
# message = ["Hi" ,"Hey", "Hello"]


# # print(message[0:2])
# # print(message[-2])

# # print(f'{message[0]} {message[2]}')

# message = ["Hi" ,"Hey", "Hello"]

# # message.remove(0)
# removed = message.pop(1)

# print(removed)
# print(message)

# # print('hi' in message)

# for index, value in enumerate(message):
# 	print(index, value)




# # new_msg = ['Bye', 'Goodbye']

# # message.append('Bye')
# # message.insert(2,new_msg)
# # message.extend(new_msg)

# # print(message)
# # print(message)


# nums = [45,12,45,1,9]

# # nums.sort(reverse=True)

# print(sorted(nums))
# print(nums)
# # print(new_nums)

message = 'Hi, Hey, Hello'

new_list = message.split(', ')

print(new_list)

new_msg = ' - '.join(new_list)

print(type(new_msg))