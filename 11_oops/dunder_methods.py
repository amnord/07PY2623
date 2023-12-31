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


	def __repr__(self):
		return f"Employee('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname()} - {self.pay}"

emp_1 = Employee('John', 'K', 60000)
emp_2 = Employee('Tom', 'G', 80000)


print(emp_1)