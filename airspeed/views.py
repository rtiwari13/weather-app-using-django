from django.shortcuts import render
import requests 

# Create your views here.
def home(request):
   if request.method == 'POST':
       city = request.POST['cityName']
       print(city)
       url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b27fabff98a95a8751f76b52b6cfe0ad'
       res = requests.get(url)
       data = res.json()
       print(data)
       return render(request,'home.html',{'data':data})
   else:
       data = ''
       return render(request,'home.html',{'weather_data':data})