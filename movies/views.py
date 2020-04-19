from django.shortcuts import render,redirect
from django.contrib import messages
from airtable import Airtable
import os

AIRTABLE_API_KEY="key8V0J3ads6eJy12"
AIRTABLE_MOVIESTABLE_BASE_ID="appaWB8itTCLS2B8M"

AT = Airtable(os.environ.get('AIRTABLE_MOVIESTABLE_BASE_ID',AIRTABLE_MOVIESTABLE_BASE_ID),#'Movies',
                  'Movies',api_key=os.environ.get('AIRTABLE_API_KEY',AIRTABLE_API_KEY))

# Create your views here.
def home_page(request):
    ##print(str(request.GET.get('query','')))

    user_query=str(request.GET.get('query',''))
    search_result=AT.get_all(formula="FIND('"+user_query.lower()+"',LOWER({Name}))")
    stuff_for_frontend={'search_result':search_result}
    return render(request,'movies/movies_stuff.html',stuff_for_frontend)

def create(request):
    if request.method =='POST':
        data={
            'Name':request.POST.get('name'),
            'Pictures':[{'url':request.POST.get('url')}],
            'Rating':int(request.POST.get('rating')),
            'Notes':request.POST.get('notes')
        }
        AT.insert(data)
    return redirect('/')