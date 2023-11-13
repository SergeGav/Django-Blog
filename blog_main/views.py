from django.shortcuts import render, redirect
from blogs.models import Blog, Category, About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request): 
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
        # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)

# Registration view 
def register(request):
    if request.method == 'POST':
        # passing the data to the registration form
        form = RegistrationForm(request.POST)
        # if the form is valid 
        if form.is_valid():
            #save the form 
            form.save()
            #return back to register
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

#Login 
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] # name atributes of form username and password 
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form':form

    }
    return render (request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
