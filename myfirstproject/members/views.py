from django.shortcuts import render, get_object_or_404
from .models import Member, Meta

def athlete(request):
    return render(request, 'members/athlete.html')

def first(request):
    mymembers = Member.objects.all().values()
    return render(request, 'members/first.html', {'mymembers': mymembers})

def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    return render(request, 'members/details.html', {'mymember': mymember})

def main(request):
    return render(request, 'members/main.html')

def testing(request):
    text = ['Apple', 'Banana', 'Cherry']
    return render(request, 'members/template.html', {'text': text})
# Create your views here.