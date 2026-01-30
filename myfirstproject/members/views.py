from django.shortcuts import render, get_object_or_404
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
    return render(request, 'template.html', {'text': text})
# Create your views here.