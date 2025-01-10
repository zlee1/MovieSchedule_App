from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import urllib
from bs4 import BeautifulSoup
from .forms import TheaterSearchForm

def home(request):
    return render(request, 'subscriptions/home.html')

def login(request):
    return render(request, 'subscriptions/login.html', context={'title': 'Login'})

@login_required
def manage(request):
    current_user = User.objects.first()

    if(request.method == 'POST'):
        form = TheaterSearchForm(request.POST)
        if(form.is_valid()):
            zip_code = form.cleaned_data.get('zip_code')

            return redirect('subscriptions-search', zip_code=zip_code)
    else:
        form = TheaterSearchForm()
    
    return render(request, 'subscriptions/manage.html', context={'title': 'Manage', 'form': form, 'subscriptions':current_user.subscription_set.all()})

def theater_search(request, zip_code):

    theater_list = []

    url = f'https://www.fandango.com/{zip_code}_movietimes'

    zip_search = urllib.request.urlopen(url)
    zip_search_page = BeautifulSoup(zip_search.read().decode('utf8'), 'html.parser')

    zip_search.close()

    theaters = zip_search_page.find(id='nearby-theaters-select-list').find_all('option') # list of all theaters on page

    for theater in theaters[1:]:
        theater_dict = {}
        theater_dict['id'] = theater["value"].replace('/', '').replace('theater-page', '')[-5:] # end of url is theater id
        theater_dict['name'] = theater.text.strip()
        theater_dict['url'] = f'https://www.fandango.com{theater["value"]}'

        if(theater_dict not in theater_list):
            theater_list.append(theater_dict)

    context = {'title': 'Search', 'zip_code': zip_code, 'theaters': theater_list}

    return render(request, 'subscriptions/theater_search.html', context=context)