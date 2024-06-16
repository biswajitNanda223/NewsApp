from django.shortcuts import render
from .utils import *
# Create your views here.
def home(request):
    # url='https://newsapi.org/v2/top-headlines?country=us&apiKey=743b90189d3b4a2e8aa079c053a0ab3f'
    # get_news_form_api(url)
    return render(request, 'home.html',context={'articles':Articles.objects.all()})