from django.shortcuts import render
from .models import service,whyus,Pricing,TextOffPricing,Team,Question,Portfolio




def home(request):
    services=service.objects.all()
    whyuses=whyus.objects.all()
    Pricings=Pricing.objects.all()
    team=Team.objects.all()
    TextOffPricings=TextOffPricing.objects.all
    question=Question.objects.all()
    portfolio=Portfolio.objects.all()
    context={
        'services':services,
        'whyuses':whyuses,  
        'pricing':Pricings,
        'TextoffPricing':TextOffPricings,
        'teams':team,
        'questions':question,
        #portfolioni tuzitish
        'portfolio':portfolio
    }
    return render(request,'index.html',context)
