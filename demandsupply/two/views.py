from django.shortcuts import render
import requests
import pandas as pd
from  .models import *

# Create your views here.

    
def home(request):
    return render(request, 'home.html')

   
def demand(request):
    
    DemandURL='http://10.11.52.113:9000/demand_1'
    response = requests.get(DemandURL)
    r2 = response.json()
    demand_df = pd.DataFrame.from_dict(r2)
    print(demand_df)
    context = {
        'df' : demand_df.to_html()
    }
    return render(request,'demand.html', context)


def supply(request):
   
    DemandURL='http://10.11.52.113:9000/demand_1'
    SupplyURL='http://10.11.52.113:7000/supply_13'
    response = requests.get(DemandURL)
    r2 = response.json()
    demand_df = pd.DataFrame.from_dict(r2)
    print(demand_df)

    num1 = int(request.GET["num1"])
    demand1 = {"demand" : num1}    
    response = requests.get(SupplyURL, json = demand1)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context1 = {
        'demand' : num1,
         'df' : demand_df.to_html(),
         'df1' : supply_df.to_html()
        }
    return render(request, 'supply.html', context1)

def one(request):
    params = {"demand" : 20}
    response = requests.get('http://10.11.52.113:7000/supply_13',json = params)
    r3 = response.json()
    dict = pd.json_normalize(response)
    print(dict)
    supply_df = pd.DataFrame.from_dict(r3)
    print(supply_df)
    context = {
         'df' : supply_df.to_html()
        }
    return render(request,'one.html',context)