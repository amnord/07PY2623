class Employee():
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname(self):
		return f"{self.first} {self.last}"

	@property
	def email(self):
		return f'{self.first}.{self.last}@company.com'


emp = Employee('John', 'M', 60000)

emp.first = 'Tom'

print(emp.first)
print(emp.email)
print(emp.fullname())
print(emp.email)
print(emp.email)
