class Employee():

	raise_amt = 1.06
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee('John', 'K', 60000)
emp_2 = Employee('Tom', 'G', 80000)


import datetime

my_date = datetime.date(2023, 8,19)

print(Employee.is_workday(my_date))






# emp_data = 'John-K-60000'
# emp_1 = Employee.from_str(emp_data)

# print(emp_1.first)

# # first, last, pay = emp_data.split('-')
# # new_emp = Employee(first, last, pay)

# # Employee.set_raise_amt(1.09)
# # print(emp_1.raise_amt)
# # print(new_emp.raise_amt)


# import datetime

# print(datetime.__file__)