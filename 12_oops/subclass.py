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

class Developer(Employee):
	raise_amt = 1.09

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):

	def __init__(self, first, last, pay, emps=None):
		super().__init__(first, last, pay)
		if emps is None:
			self.emps = []
		else:
			self.emps = emps

	def add_emp(self, emp):
		if emp not in self.emps:
			self.emps.append(emp)

	def remove_emp(self, emp):
		if emp in self.emps:
			self.emps.remove(emp)

	def disp_emps(self):
		for emp in self.emps:
			print(emp.fullname())


emp = Employee('John', 'M', 60000)
dev = Developer('Tom', 'K', 60000, 'Python')
mgr = Manager('Ravi', 'M', 90000, [emp])

mgr.add_emp(dev)
mgr.remove_emp(emp)
mgr.disp_emps()
