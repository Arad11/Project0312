import pyodbc
conn = pyodbc.connect('DSN=ONN;database=NORTHWIND;autocommit=True;')
cursor = conn.cursor()
sql = "select EmployeeID,FirstName,LastName from Employees where EmployeeID = 1"
res = cursor.execute(sql)
