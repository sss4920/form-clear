from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import CreateForm
import urllib.parse,urllib.request
import pandas
import requests
from django.http import JsonResponse


# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'crudpra/home.html',{'post':post})

def create(request, post = None):
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')
    else:
        form = CreateForm(instance=post)
        return render(request, 'crudpra/new.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return create(request,post)

def delete(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('home')

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1acc16a96aa8764e33997f3c2ac1a09c'
    city = 'Gwangju'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    weather = {
        'city' : city,
        'temperature' : (city_weather['main']['temp'] - 32)/1.8000,
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    context = {'weather' : weather}
    return render(request, 'crudpra/weather.html',context)
    
    
