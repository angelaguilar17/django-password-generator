from django.shortcuts import render
#from django.http import HttpResponse
import random
import datetime
from django.contrib.auth.models import User
from .models import Task
import xlsxwriter


def about(request):
    return render(request,'generator/about.html')
    
def home(request):
    return render(request,'generator/home.html')

def password(request): 
    
    characters =list('abcdefghijklmnopqrstuvwxyz')
    generate_password=''

    length= int(request.GET.get('length')) #Se tiene la variable length y se convierte a int

    if request.GET.get('uppercase'): #Si se seleciona mayúsculas
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) #EXTEND se agregan los valores en mayusculas a la lista.
    if request.GET.get('special'):
        characters.extend(list('!#%&/¿¡._-!?*+,@'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    name = request.GET.get('username')
    dates = datetime.datetime.now()
    print(dates)
     

    for x in range(length):
        generate_password += random.choice(characters) #selecciona aleatoriamente un elemento de la lista
    
    p1 = Task(username=name, password=generate_password, date=dates)
    p1.save()
    tasks = Task.objects.all()
    
    archivo = xlsxwriter.Workbook('registers.xlsx')
    hoja = archivo.add_worksheet()
    hoja.write(0,0,"ID")
    hoja.write(0,1,"Name")
    hoja.write(0,2,"Password")
    hoja.write(0,3,"Date")
    for task in tasks:
        format2 = archivo.add_format({'num_format': 'dd/mm/yy    hh:mm'})
        hoja.write(task.id,0,task.id)
        hoja.write(task.id,1,task.username)
        hoja.write(task.id,2,task.password)
        hoja.write(task.id,3,task.date,format2)
    archivo.close()

    
    return render(request,'generator/password.html',{'password':generate_password, 'names':name, 'date':dates})


def names(request):
    tasks = Task.objects.all()
    return render(request,'generator/names.html',{'tasks':tasks})

