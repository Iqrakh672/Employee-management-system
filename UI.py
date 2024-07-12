##UI.py

import BLL
for i in range(0,3):
        action = input("enter command :")
        if(action=='f'):
                rows= BLL.Employee().GetAllEmployees()
                for row in rows:
                  employee = BLL.Employee(row[0],row[1],row[2])
##                employee is an object 
                    
                  print(row )
                break
       
        elif(action=='i'):
                id,name,address=input("enter id,name, address ").split(",")
                objEmp= BLL.Employee(id,name,address)
                flag=objEmp.InsertEmployee()
                break
         
        elif(action=="u"):
                id=input("enter id")
                row=BLL.Employee().getEmployeeId(id)
                #obj=BLL.Employee(row[0],row[1],row[2])
                print(row)
                id,name,address=input("enter update").split(",")
                objEmp= BLL.Employee(id,name,address)
                flag=objEmp.updateEmployee()
                break

        elif(action=="d"):
                id=input("enter id")
                y_n=input(f"are you sure you want to delete {id}  (y,n):")
                if(y_n=="y"):
                        row=BLL.Employee().getEmployeeId(id)
                        BLL.Employee().deleteEmployee(id)
                        print("query executed successfully ")
                else:
                        print("thanks for visiting")
                break
        else:
                print("enter right key" )
                print(" enter f for fetchall details, i for insert , u for update and d for delete")

else:
        print("sorry you entered wrong  command ")

 
        



