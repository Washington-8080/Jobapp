from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Job  # Import your Job model
import requests
import threading

def home(request):
    return render(request, 'Jobapp1/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Jobapp1/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'Jobapp1/login.html', {'form': form})

@login_required
def update_user(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'Jobapp1/update_user.html', {'form': form})

@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'Jobapp1/delete_user.html')

@login_required
def dashboard(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'Jobapp1/dashboard.html', context)

def job_search(request):
    search_query = request.GET.get('query')
    if search_query:
        endpoint = "https://jsearch.p.rapidapi.com/search"
        search_params = {
            "query": search_query,
            "country": "malawi"
        }
        headers = {
            'x-rapidapi-key': "eabda60bafmsh524608e76d10b6ap1f19cdjsn1261d937df1b",
            'x-rapidapi-host': "jsearch.p.rapidapi.com"
        }
        response = requests.get(endpoint, params=search_params, headers=headers)
        
        if response.status_code == 200:
            search_results = response.json().get('data', [])
        else:
            search_results = {'error': 'Failed to fetch results'}

        return render(request, 'Jobapp1/search_results.html', {'search_results': search_results})

    return render(request, 'Jobapp1/search_results.html')

def automatic_application():
    # Placeholder function for automatic application
    print("Automatic application running...")

def search(request):
    query = request.GET.get('q')
    results = Job.objects.filter(title__icontains=query)
    return render(request, 'Jobapp1/search_results.html', {'results': results})

# Other views...
