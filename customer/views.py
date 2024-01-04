import datetime
from collections import namedtuple
from typing import List

from django.shortcuts import render
from ninja import NinjaAPI
from .schemas import CustomerOut, CustomerIn, CustomerLogin, CustomerLogOut, TaskIn, TaskOut, TaskUpdIn
from .models import Customer, Tasks
from .services import sending_mail, entToDto, taskEntToDto, setDate, getPending, getCompleted, getAllTasks

# Create your views here.
api=NinjaAPI()

"""
Adding A new Customer to the data base
params: CustomerIn
Author: Santhosh Kumar
Date Created: 20/12/2023
"""
@api.post("newCus",response=CustomerOut)
def newCustomer(request,data: CustomerIn):
    customer=Customer()
    # Changing the customer schema into customer
    result=entToDto(data,customer)
    #Saving the Customer
    result.save()
    #sending_mail(data.email,data.name)
    return result
"""
Getting all the customers
Author:Santhosh Kumar
Date Created: 20/12 2023
"""
@api.get("getAll",response=List[CustomerOut])
def getAll(request):
    customers=Customer.objects.all()
    return customers

"""
Getting Customer by Id
Params : Customer Id
Author: Santhosh Kumar
Date Created: 20/12/2023
"""
@api.get("getById/{cusId}",response=CustomerOut)
def getById(request,cusId: int):
    customer=Customer.objects.get(id=cusId)
    return customer

"""
Get Customer By Email
Params: Email
Author: Santhosh Kumar
Date Created: 21/12/2023
"""

@api.get("getByEmail/{email}",response=CustomerLogOut)
def getByEmail(request,email:str):
    customer=Customer.objects.filter(email=email).values()
    return customer[0]



"""
Updating Customer Object
Params: CusId, New Customer Details
Author: Santhosh Kumar
Date Created: 20/12/2023
"""
@api.post("update/{cusId}",response=CustomerOut)
def updateCustomer(request, cusId: int, data: CustomerIn):
    customer=Customer.objects.get(id=cusId)
    result=entToDto(data,customer)
    result.id=cusId
    result.save()
    return result

"""
Deleting the Customer 
Params: customer id
Author: Santhosh Kumar
Date Created: 20/12 2023
"""
@api.delete("delete/{cusId}")
def deleteCustomer(request, cusId: int):
    customer=Customer.objects.get(id=cusId)
    customer.delete()
    return {"Deleted Successfully":True}

"""
Customer Login  Function
Params: CustomerLogIn
Author: Santhosh Kumar
Date Created: 20/12 2023
"""
@api.post('login',response= CustomerLogOut)
def cusLogIn(request,customerLogin:CustomerLogin):
    result=Customer()
    customer=Customer.objects.filter(email=customerLogin.email).values()
    if len(customer)!=0 and customer[0]['password'] ==customerLogin.password:
        result=customer[0]
    return result

"""
Task adding function
Param: TaskIn 
Author: Santhosh Kumar
Created on : 26/12/2023
Modified on:
"""
@api.post("newTask",response=TaskOut)
def newTas(request,data: TaskIn):
    task= Tasks()
    result=taskEntToDto(data,task)
    result.addedOn = datetime.date.today()
    result.status = 0
    result.save()
    return result

"""
Task Updating Function
Params: taskId, Task
Author: Santhosh kumar
Date Created: 26/12/2023
Date Modified: 
"""
@api.post("updateTask/{taskId}",response=TaskOut)
def updateTask(request, taskId: int, data: TaskUpdIn):
    task=Tasks.objects.get(id=taskId)
    #print(type(task))
    result=taskEntToDto(data,task)
    setDate(result)
    result.save()
    return result

"""
Getting all the tasks of an user
params: Email
author: Santhosh kumar
Date Created: 26/12 2023
Date Modified: 
"""

@api.get("getTasks/{email}/{status}",response=List[TaskOut])
def getHistory(request, email:str,status:int):
    if( status>1):
        result=Tasks.objects.filter(email=email).values()
    elif( status ==0):
        tasks=Tasks.objects.filter(email=email).values()
        result=filter(getPending,tasks)
    elif( status==1):
        tasks=Tasks.objects.filter(email=email).values()
        result=filter(getCompleted,tasks)
    return result


"""
Getting tasks for home page
Params: email
Author:Santhosh Kumar
Date Created: 27/12/2023
Date Modified:
"""
@api.get("getAll/{email}",response=List[TaskOut])
def getAll(request,email:str):
    print(email)
    tasks=Tasks.objects.filter(email=email).values()
    #tasks2=filter(lambda x: x.email=="\""+email+"\"")
    result=filter(getAllTasks,tasks)
    return result


"""
Getting pending tasks
param: Email
Author: Santhosh Kumar
Date Created: 02/01/2023
Date Modified:
"""
@api.get("pending/{email}",response=List[TaskOut])
def getPendingTasks(request,email:str):
    print(email)
    tasks = Tasks.objects.filter(email=email).values()
    # tasks2=filter(lambda x: x.email=="\""+email+"\"")
    result = filter(getPending, tasks)
    return result


"""
Getting Completed tasks
param: Email
Author: Santhosh Kumar
Date Created: 02/01/2023
Date Modified:
"""
@api.get("completed/{email}",response=List[TaskOut])
def getCompletedTasks(request,email:str):
    print(email)
    tasks = Tasks.objects.filter(email=email).values()
    # tasks2=filter(lambda x: x.email=="\""+email+"\"")
    result = filter(getCompleted, tasks)
    return result


"""
Getting History tasks
param: Email
Author: Santhosh Kumar
Date Created: 02/01/2023
Date Modified:
"""
@api.get("history/{email}",response=List[TaskOut])
def getHistoryOfTasks(request,email:str):
    print(email)
    tasks = Tasks.objects.filter(email=email).values()
    # tasks2=filter(lambda x: x.email=="\""+email+"\"")
    result = tasks
    return result
















