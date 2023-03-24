from django.shortcuts import render,redirect

from user.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

#--------------------------------
#----- Index ------------------
#--------------------------------

def index(request):
    

    return render(request,  'exterior/index.html',{})

#--------------------------------
#----- Registro ------------------
#--------------------------------

def registro(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST )
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            messages.success(request, 'Se ha registrado correctamente')
           # return redirect(to='index') 

        else:
            data['form'] = formulario  

    return render(request,  'registration/registro.html', data)