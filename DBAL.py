##DBAL.py
import pyodbc
def getConnection():
    cnxn = pyodbc.connect(r'Driver=SQL Server;Server=LAPTOP-EHUO75F9\SQLEXPRESS;Database=company;')
    cursor = cnxn.cursor()
    return cursor

def FetchAllEmployees():
    cursor = getConnection()
    cursor.execute("SELECT * from Employee")
    rows = cursor.fetchall()
    return rows
##FetchAllEmployees()
#print(FetchAllEmployees())

## this is for dbal direct insert
##def InsertEmployee(id,name,address):
##    cursor = getConnection()
##    s=cursor.execute("Insert into Employee values(1,'AAMNA','vip')")
##    flag = cursor.commit()
 ##   return flag

def InsertEmployee(objEmp):
    cursor = getConnection()
    s=cursor.execute(f"Insert into Employee values({objEmp.id},'{objEmp.name}','{objEmp.address}')")
    flag = cursor.commit()
    return flag
def getEmployeeById(id):
    cursor = getConnection()
    cursor.execute(f"SELECT * from EMployee where id={id}")
    row = cursor.fetchone()
    return row
def updateEmployee(objEmp):
    cursor = getConnection()
    s=cursor.execute(f"update employee set name ='{objEmp.name}', address='{objEmp.address}' where id={objEmp.id}")
    flag = cursor.commit()
    return flag

def deleteEmployee(id):
    cursor=getConnection()
    cursor.execute(f"delete from employee where id={id}" )
    flag=cursor.commit()
    return flag


