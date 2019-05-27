import sqlite3

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

def insert_emp(emp):
	with conn:
		cur.execute("INSERT INTO employees VALUES (:first, :last, :pay)",\
			{'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
	cur.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
	return cur.fetchall()

def update_emp(emp, pay):
	with conn:
		cur.execute("""UPDATE employees SET pay=:pay 
			WHERE first=:first AND last=:last""", 
			{ 'pay':pay, 'first':emp.first, 'last':emp.last})

def remove_emp(emp):
	with conn:
		cur.execute("""DELETE FROM employees 
			WHERE first=:first AND last=:last""",
			{'first':emp.first, 'last':emp.last})


conn = sqlite3.connect('emp.db') # create memory space/link to space(file) if exist
cur = conn.cursor() # create cursor, like open() when dealing files

cur.execute("""DROP TABLE IF EXISTS employees""") 

# create table contents: 3"" can deal with multi lines, any punctuations 
cur.execute("""CREATE TABLE employees (
				first TEXT,
				last TEXT,
				pay INTEGER
			)""") 

emp_1 = Employee('John', 'Dow', 80000)
emp_2 = Employee('Jane', 'Dow', 90000)

insert_emp(emp_1)
insert_emp(emp_2)
emps = get_emps_by_name('Dow')
print(emps)

update_emp(emp_2, 70000)
remove_emp(emp_1)

emps = get_emps_by_name('Dow')
print(emps)

conn.close()
