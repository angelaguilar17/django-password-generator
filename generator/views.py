from django.shortcuts import render
#from django.http import HttpResponse
import random

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


    for x in range(length):
        generate_password += random.choice(characters) #selecciona aleatoriamente un elemento de la lista

    return render(request,'generator/password.html',{'password':generate_password})

