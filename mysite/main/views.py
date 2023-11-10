from django.shortcuts import render
from products.cosine import cos_recommendation
from .models import Coffee, Roastery


# Create your views here.

favor = {}

def test(request):
   template_name = "index2.html"
   global favor
   caf = request.GET.get('caf')
   blend = request.GET.get('blend')
   notes = request.GET.getlist('notes[]')
   sour = request.GET.get('sour')
   sweet = request.GET.get('sweet')
   bitter = request.GET.get('bitter')
   body = request.GET.get('body')
   
   favor = {'caf':caf,'blend':blend,'notes':notes,'sour':sour,'sweet':sweet,'bitter':bitter,'body':body}
   
   
   return render(request,template_name)

def result(request):
   template_name = "result.html"
   global favor
   print('아으아으',favor)
   similarity_ids = cos_recommendation(favor, 4)
   similarity = Coffee.objects.filter(CoffeeID__in=similarity_ids)

   context = {'main_coffee':similarity[0],'sub_coffee':similarity[1:]}
   
   return render(request,template_name,context)

def index(request):
    return render(request, 'main/mainpage.html')

def mypage(request):
    return render(request, 'main/mypage_privateinfo.html')

def servicePopup(request):
    return render(request, 'main/popup.html')

def basket(request):
    return render(request, 'main/basket.html')


def purchase(request):

    return render(request, 'main/mypage_purchase.html')
