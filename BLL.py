import DBAL

class Employee():
    def __init__(self, id=1, name="iqra", address="kamla park"):
        self.id = id
        self.name = name
        self.address = address
        
####    we make this as a static method so we
####dont have to make an object to call   
    @staticmethod
    def GetAllEmployees():
        employees = DBAL.FetchAllEmployees()
        return employees
    ## to print the object str is used
##    def __str__(self):
##        return (f"id={self.id},name={self.name},address={self.address}")
#### str is string representation of the object 
####
    def InsertEmployee(self):
        flag = DBAL.InsertEmployee(self)
        return flag

##    def __str__(self):
##        return (f"id={self.id},name={self.name},address={self.address}")
####
####
    @staticmethod
    def getEmployeeId(id):
        row=DBAL.getEmployeeById(id)
        return row

    def updateEmployee(self):
        flag = DBAL.updateEmployee(self)
        return flag
##    def __str__(self):
##        return (f"id={self.id},name={self.name},address={self.address}")
    @staticmethod
    def deleteEmployee(self):
        flag=DBAL.deleteEmployee(self)
        return flag
