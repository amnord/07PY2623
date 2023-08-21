# class, instance variables, Class Variable, methods


class Employee():

	raise_amt = 1.05
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

# emp_1 = Employee('John', 'K', 60000)

# print(emp_1.fullname())