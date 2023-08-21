import unittest
from emps import Employee



class TestEmployee(unittest.TestCase):

	def test_fullname(self):
		
		emp_1 = Employee('John', 'K', 60000)
		emp_2 = Employee('Tom', 'G', 80000)

		self.assertEqual(emp_1.fullname(), 'John K')
		self.assertEqual(emp_2.fullname(), 'Tom G')

		emp_1.first = 'Jane'
		emp_2.first = 'Kate'

		self.assertEqual(emp_1.fullname(), 'Jane K')
		self.assertEqual(emp_2.fullname(), 'Kate G')


if __name__ == '__main__':
	unittest.main()