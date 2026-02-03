from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Member, Meta

def athlete(request):
    return render(request, 'athlete.html')

def first(request):
    mymembers = Member.objects.all().values()
    return render(request, 'first.html', {'mymembers': mymembers})

def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    return render(request, 'details.html', {'mymember': mymember})

def main(request):
    return render(request, 'main.html')

def testing(request):
    text = {'firstname': 'Linus'}
    return render(request, 'templates.html', {'text': text})

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')  # Changed from 'home' to 'main'
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})  # Fixed template path
# Create your views here.