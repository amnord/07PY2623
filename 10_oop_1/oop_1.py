# class, instance variables, Class Variable, methods


class Employee():

	raise_amt = 1.05
	num_of_emps = 0
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay
		Employee.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

print(Employee.num_of_emps)
emp_1 = Employee('John', 'K', 60000)
emp_2 = Employee('Tom', 'G', 80000)

print(Employee.num_of_emps)