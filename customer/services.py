from django.conf import settings
from django.core.mail import send_mail
from .models import Customer, Tasks
import datetime

def sending_mail(email,name):
    subject='Welcome to ToDoPY'
    message=f'Hi {name} happy to have you on board. Have a great organized Life!'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)

def entToDto(data,customer):
    for attr,value in data.dict().items():
        setattr(customer,attr,value)
    return customer

def taskEntToDto(data,task):
    for attr,value in data.dict().items():
        setattr(task,attr,value)
    return task

def setDate(task: Tasks):
    if(task.status==1):
        task.completedOn=datetime.date.today()
    elif( task.status==2):
        task.removedOn=datetime.date.today()

def getAllTasks(task):
    if(task['status']!=2):
        return True
    else:
        return False

def getPending(task):
    if task['status']==0:
        return True
    else:
        return False

def getCompleted(task):
    if task['status']==1:
        return True
    else:
        return False






